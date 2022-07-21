import json
import matplotlib.pyplot as plt
import numpy as np
import optuna
import os
import pickle
import tensorflow as tf

from sklearn.model_selection import train_test_split, TimeSeriesSplit
from sklearn.preprocessing import MinMaxScaler


gpu_devices = tf.config.experimental.list_physical_devices("GPU")
for device in gpu_devices:
    tf.config.experimental.set_memory_growth(device, True)
    

    
from keras.metrics import mean_squared_error
from keras.models import Sequential, load_model, clone_model
from keras.layers import LSTM, GRU, SimpleRNN, Dense

#----------------------------------------------------------------------------------------------------#
# TRAINING                                                                                           #
#----------------------------------------------------------------------------------------------------#
class Architecture(object):
    '''
    Class which holds various variables used throughout model
    '''
    def __init__(self, n_steps_in, n_steps_out, n_features, X_train, X_test, y_train, y_test):
        '''
            n_steps_in (int): The number of timestamps fed into the model
            n_steps_out (int): The number of timestamps predicted by the model
            n_features (int): The number of features fed into the model. Note that one feature is always predicted.        
            X_train, X_test, y_train, y_test (np arrays): Training/testing data
        '''
        self.n_steps_in = n_steps_in
        self.n_steps_out = n_steps_out
        self.n_features = n_features
        self.X_train = X_train
        self.X_test = X_test
        self.y_train = y_train
        self.y_test = y_test

def build_model(trial, arch):
    '''
    Builds a model with varying hyperparameters with optuna.
    
            Parameters:
                    trial (optuna trial): Trial, which stores chosen hyperparamters and performance
                    arch (Architecture): Object containing frequently used vars (e.g. n_steps_in, n_features) and training/testing data
            Returns:
                    model (keras model): Model, trained
                    loss (float): mean squared error, used to measure performance of model
    '''
    n_neurons = trial.suggest_categorical('n_neurons', [32, 64, 128]) # tune
    n_layers = trial.suggest_int('n_layers', 1, 4) # tune
    cell_type = trial.suggest_categorical('cell_type', ["LSTM", "GRU", "SimpleRNN"]) # tune
    
    if cell_type == "LSTM":
        cell = LSTM
    elif cell_type == "GRU":
        cell = GRU
    else:
        cell = SimpleRNN
    
    model = Sequential()
    if n_layers == 1:
        model.add(cell(n_neurons, activation="tanh", input_shape=(arch.n_steps_in,arch.n_features)))
    else:
        model.add(cell(n_neurons, activation="tanh", return_sequences=True, input_shape=(arch.n_steps_in,arch.n_features)))
        for i in range(n_layers-2):
            model.add(LSTM(n_neurons, activation="tanh", return_sequences=True))
        model.add(cell(n_neurons))
        
    model.add(Dense(arch.n_steps_out))
    model.compile(optimizer="adam", loss="mse")
    return model

def model_eval(model, X, y, return_pred=False):
    '''
    Evaluates a model w/ mse
    
            Parameters:
                    model (keras model): Model to be trained
                    X, y (np arrays): Evaluation data
            Returns:
                    model (keras model): Model, trained
                    loss (float): mean squared error, used to measure performance of model
    '''
    pred = model.predict(X)
    loss =  mean_squared_error(pred, y)
    return loss, pred if return_pred else loss

def fit_eval(model, X_train, X_test, y_train, y_test, batch_size=57): # tune
    '''
    Trains a model and evaluates it.
    
            Parameters:
                    model (keras model): Model to be trained
                    X_train, X_test, y_train, y_test (np arrays): Training/evaluation data
                    batch_size (int): batch size
            Returns:
                    model (keras model): Model, trained
                    loss (float): mean squared error, used to measure performance of model
    '''
    model.compile(optimizer="adam", loss="mse")
    model.fit(X_train, y_train, batch_size=batch_size)
    loss = model_eval(model, X_test, y_test)
    return model, loss

def train_epoch(model, X, y, n_splits=5): # tune
    '''
    Trains through an epoch of time series cross validation.
    
            Parameters:
                    model (keras model): Model to be trained. In broader context, this model has been trained
                        from the previous epochs and will be trained more this epoch.
                    X, y (np arrays): Training data, to be split for cross validation
                    n_splits (int): number of splits for cross validation
            Returns:
                    model (keras model): Model, trained
                    loss (float): average mean squared error of all folds, used to measure performance of model
    '''
    tscv = TimeSeriesSplit(n_splits)
    fold_mse = []
    for train_index, val_index in tscv.split(X):
        X_fold_train, X_fold_val = X[train_index], X[val_index]
        y_fold_train, y_fold_val = y[train_index], y[val_index]
        
        fold_model = clone_model(model)
        fold_model.set_weights(model.get_weights())
        trained_model, mse = fit_eval(fold_model, X_fold_train, X_fold_val, y_fold_train, y_fold_val)
        fold_mse.append(mse)
    return trained_model, np.average(fold_mse)

def train_umbrella(trial, arch, n_epochs, min_improvement=-1, patience=0):
    '''
    Primary method for training. Trains for given number of epochs with time series cross validation.
    
            Parameters:
                    trial (optuna trial): Trial, which stores chosen hyperparamters and performance
                    arch (Architecture): Object containing frequently used vars (e.g. n_steps_in, n_features) and training/testing data
                    n_epochs (int): number of epochs to train for
                    min_improvement (int): minimum improvement before early stopping. -1 == do not implement early stopping
                    patience (int): number of iterations to wait for improvement before early stopping
            Returns:
                    model (keras model): Model, trained
                    epoch_loss (float): history of mean squared error, used to measure performance of model
    '''
    print("-----begin training")
    epoch_models = [build_model(trial, arch)]
    epoch_loss = [np.inf]
    best_idx = 0
    for epoch in range(n_epochs):
        # train one epoch and store loss
        print("-----epoch #" + str(epoch+1))
        model, mse = train_epoch(epoch_models[-1], arch.X_train, arch.y_train)
        epoch_models.append(model)
        epoch_loss.append(np.average(mse))
        
        # early stopping:
        if min_improvement >= 0:
            curr_idx = len(epoch_loss) - 1
            if epoch_loss[best_idx] - epoch_loss[-1] >= min_improvement:
                best_idx = curr_idx
                print(f"loss={epoch_loss[-1]}, improvement, best_idx={best_idx}, curr_idx={curr_idx}")
            else:
                print(f"loss={epoch_loss[-1]}, no improvement, best_idx={best_idx}, curr_idx={curr_idx}")
            if curr_idx - best_idx > patience:
                print("-----early stopping. best_idx=" + str(best_idx) + ", curr_idx=" + str(curr_idx))
                break
    
    print(epoch_loss)
    best_idx = np.argmin(epoch_loss)
    return epoch_models[best_idx], epoch_loss

def train_and_evaluate_model(trial, arch):
    '''
    Umbrella method. Trains model and evaluates against test data.
    
            Parameters:
                    trial (optuna trial): Trial, which stores chosen hyperparamters and performance
                    arch (Architecture): Object containing frequently used vars (e.g. n_steps_in, n_features) and training/testing data
            Returns:
                    model (keras model): Model, trained
                    loss (float): mean squared error against test data, used to measure performance of model
    '''
    model, loss_history = train_umbrella(trial, arch, n_epochs=140, min_improvement=0, patience=5) # tune
    loss, pred = model_eval(model, arch.X_test, arch.y_test, return_pred=True)
    loss = np.average(loss)
    trial.set_user_attr("loss_history", loss_history)    
    
    # pickle trial and model in case something happens and interrupts running
    trial.set_user_attr("model", model)  
    filename = f"trial.{trial.params}"
    file = open(filename, 'wb')
    pickle.dump(trial, file)
    file.close()

    print("-----final evaluation")
    return model, loss, pred

#----------------------------------------------------------------------------------------------------#
# HYPERPARAMETER OPTIMIZATION                                                                        #
#----------------------------------------------------------------------------------------------------#
class Objective(object):
    '''
    Objective function to be optimized. Made as a class so we can pass data into the function
    
            Parameters:
                    trial (optuna trial): Trial, which stores chosen hyperparamters and performance
                    arch (Architecture): Object containing frequently used vars (e.g. n_steps_in, n_features) and training/testing data
            Returns:
                    loss (float): mean squared error. Optuna will aim to optimize this metric.
    '''
    def __init__(self, arch):
        self.arch = arch

    def __call__(self, trial):
        model, loss, pred = train_and_evaluate_model(trial, self.arch)
        return loss

def perform_study(n_trials, arch):
    '''
    Study object which optimizes hyperparameters
    
            Parameters:
                    n_trials (int): The number of trials for the study to run.
                    arch (Architecture): Object containing frequently used vars (e.g. n_steps_in, n_features) and training/testing data
            Returns:
                    study (optuna study): A study, which contains a number of trials with different hyperparameters
    '''
    # create an Objective object with function __call__ to optimize. we do it like this so we can pass in the data
    objective = Objective(arch)
    
    study = optuna.create_study(direction='minimize')
    study.optimize(objective, n_trials=n_trials)
    return study

def pickle_study_to_file(study, n_steps_in, n_steps_out, dirname):
    '''
    Pickles study to file, with file name of form "n_steps_in.n_steps_out.best_params". Pickles to the given directory
    For example "3in.2out.{n_layers=4, n_nodes=128}"
    
            Parameters:
                    study (optuna study): Object containing all trials in a particular hyperparamter optimization search
                    n_steps_in (int): The number of timestamps fed into the model
                    n_steps_out (int): The number of timestamps predicted by the model
                    dirname (str): Directory to save file to
            Returns:
                    none
    '''
    filename = f"{dirname}{n_steps_in}in.{n_steps_out}out.study"
    file = open(filename, 'wb')
    pickle.dump(study, file)
    file.close()

def pickle_scalers_to_file(scalers, dirname):
    '''
    Pickles scalers to file, with file name "scalers" Pickles to the given directory
    
            Parameters:
                    scalers (list of sklearn scalers): Scalers used to transform given dataset
                    dirname (str): Directory to save file to
            Returns:
                    none
    '''
    filename = f"{dirname}scalers"
    file = open(filename, 'wb')
    pickle.dump(scalers, file)
    file.close()
    
#----------------------------------------------------------------------------------------------------#
# MASTER                                                                                             #
#----------------------------------------------------------------------------------------------------#
def optimize(dirname, n_steps_in, n_steps_out, n_trials, n_features=2):
    '''
    Master umbrella function. Loads data, performs hyperparameter optimization study, and then pickles both
    studies and scalers used to file.
    
            Parameters:
                    dirname (str): Directory to save file to
                    n_steps_in (int): The number of timestamps fed into the model
                    n_steps_out (int): The number of timestamps predicted by the model
            Returns:
                    none
    '''
    # load data and store frequently-used variables and data in object
    X_train, X_test, y_train, y_test, scalers = get_data(dirname, n_steps_in, n_steps_out)
    arch = Architecture(n_steps_in, n_steps_out, n_features, X_train, X_test, y_train, y_test)
    
    study = perform_study(n_trials, arch)
    pickle_study_to_file(study, n_steps_in, n_steps_out, dirname)
    pickle_scalers_to_file(scalers, dirname)

def load_data_from_file(dirname, n_steps_in, n_steps_out, n_features=2):
    # load the data by iterating through all files
    X = np.empty((0,n_steps_in,n_features))
    y = np.empty((0,n_steps_out))
    for file in os.listdir(dirname):
        filename = dirname + file
        print(filename)
        if file.endswith(".X"):
            to_open = open(filename, 'rb')
            X = np.concatenate((X, pickle.load(to_open)))
            to_open.close()
        if file.endswith(".y"):
            to_open = open(filename, 'rb')
            y = np.concatenate((y, pickle.load(to_open)))
            to_open.close()
    return X, y

def scale_data(X, y):
    scalers = []
    for i in range(X.shape[-1]):
        scaler = MinMaxScaler()
        X[:,:,i] = scaler.fit_transform(X[:,:,i].reshape(-1,1)).reshape(X[:,:,i].shape)
        scalers.append(scaler)
    y = scalers[0].transform(y.reshape(-1,1)).reshape(y.shape)
    return X, y, scalers

def get_data(dirname, n_steps_in, n_steps_out, train_size_percent=0.75, resample_rate_min=15):
    # determine sizes for batches, train/test split
    hours_per_day = 14
    datapoints_per_hour = int(60/resample_rate_min)
    datapoints_per_day = hours_per_day * datapoints_per_hour + 1
    n_days = 1503 # manually defined, taken from looking at data
    train_size = np.floor(n_days * train_size_percent)/n_days

    # load, scale, and split data
    X, y = load_data_from_file(dirname, n_steps_in, n_steps_out)
    X, y, scalers = scale_data(X, y)    
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle=False, train_size=train_size)
    return X_train, X_test, y_train, y_test, scalers
