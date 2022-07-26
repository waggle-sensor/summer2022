import numpy as np
import pickle
import xarray as xr

from data_utility import open_data, preprocess_data
from datetime import date
from sklearn.preprocessing import MinMaxScaler

#----------------------------------------------------------------------------------------------------#
# PRE-LOADING DATA                                                                                   #
#----------------------------------------------------------------------------------------------------#
def load_data(date_ranges):
    '''
    Opens x_array data given a list of date ranges. Uses self-written function from open_data.
    

            Parameters:
                    date_ranges (2d np array of datetime.date): Array of start (inclusive) and end
                        (exclusive) date ranges. Of shape (number of date ranges, 2)
                    

            Returns:
                    data (dataset): xr dataset of requested date ranges
    ''' 
    data = open_data(date_ranges)
    print("---------data loaded")
    return data

def format_time_series(data, input_vars, output_var, n_steps_in, n_steps_out):
    '''
    Formats the given data into a time series. Note this only permits one output variable.
    

            Parameters:
                    data (pandas): pandas dataframe of requested date ranges
                    input_vars (array of strs): variables to keep as inputs for model
                    output_var (str): variable for model to predict
                    n_steps_in (int): number of time steps to feed into model
                    n_steps_out (int): number of time steps for model to predict
                    

            Returns:
                    X (np array): data to input to model of requested variables,
                                  of shape (n_samples, n_steps_in, n_features_in)
                    y (np array): data for model to predict, of requested variable,
                                  of shape (n_samples, n_steps_out)
    ''' 
    # set up time series
    n_features = len(input_vars)
    n_time_points = len(data[input_vars[0]])
    n_time_series = n_time_points-(n_steps_in + n_steps_out)+1

    X = np.empty((n_time_series, n_steps_in, n_features))
    y = np.empty((n_time_series, n_steps_out))

    for i in range(n_steps_out):
        y[:,i] = data[output_var][n_steps_in+i : n_time_points-n_steps_out+i+1]
    for i in range(n_time_series):
        X[i] = [[data[input_var][i + step] for input_var in input_vars] for step in range(n_steps_in)]
        print(str(i)+"/"+str(n_time_series), end="\r")
    print("---------time series set up")
    return X,y

def scale_time_series_data(X,y):
    '''
    Scales time series data by individual variable. Inputed variables are directly modified.
    

            Parameters:
                    X (np array): data to input to model of requested variables,
                                  of shape (n_samples, n_steps_in, n_features_in)
                    y (np array): data for model to predict, of requested variable,
                                  of shape (n_samples, n_steps_out)
                    

            Returns:
                    None
    ''' 
    for i in range(X.shape[-1]):
        scaler = MinMaxScaler()
        X_1D = X[:,:,i]
        y_1D = y[:,i]
        X_1D = scaler.fit_transform(X_1D.reshape(-1,1)).reshape(X_1D.shape)
        y_1D = scaler.transform(y_1D.reshape(-1,1)).reshape(y_1D.shape)
        X[:,:,i] = X_1D
        y[:,i] = y_1D
    print("---------data scaled")
    return X,y

def pickle_to_file(X, y, date_ranges, n_steps_in, n_steps_out, resample, scale, prefix):
    '''
    Pickles data to file, with file name of form "YYYYMMDD-YYYYMMDD.n_steps_in.n_steps_out.resample_rate.scaled/unscaled.X/y"
    For example "20160701-20160801.3.2.15min.unscaled.X"
    

            Parameters:
                    date_ranges (2d np array of datetime.date): Array of start (inclusive) and end
                                (exclusive) date ranges. Of shape (number of date ranges, 2)
                    n_steps_in (int): number of time steps to feed into model
                    n_steps_out (int): number of time steps for model to predict
                    (datetime format code as str): time frequency to downsample data. see
                                https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes 
                    scale (bool): whether to scale data or not
                    prefix (str): prefix for filepaths
                    

            Returns:
                    None
    ''' 
    if date_ranges == None:
        date_ranges_str = "all_dates"
    else:
        date_ranges_str = '_'.join([date_range[0].strftime("%Y%m%d") + "-" + date_range[1].strftime("%Y%m%d")
                                 for date_range in date_ranges])
    steps_str = str(n_steps_in) + "." + str(n_steps_out)
    resample_str = "1min" if resample == None else resample
    scale_str = "scaled" if scale else "unscaled"
    filename = prefix + ".".join([date_ranges_str, steps_str, resample_str, scale_str])

    pickle.dump(X, open(filename + ".X", 'wb'))
    pickle.dump(y, open(filename + ".y", 'wb'))
    print("---------written to file, filename: " + filename + "." + " followed by X/y")

def data(n_steps_in, n_steps_out, date_ranges, resample="15Min", scale=False, write_to_file=True,
         prefix="../../!data/pre-loaded/"):
    '''
    Loads data and formats into time series. Scales, resamples, and writes to file as requested.
    

            Parameters:
                    n_steps_in (int): number of time steps to feed into model
                    n_steps_out (int): number of time steps for model to predict
                    date_ranges (2d np array of datetime.date): Array of start (inclusive) and end
                                (exclusive) date ranges. Of shape (number of date ranges, 2)
                    resample (datetime format code as str): time frequency to downsample data. see
                                https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes 
                    scale (bool): whether to scale data or not
                    write_to_file (bool): whether to pickle data to file or not
                    prefix (str): prefix for filepaths
                    

            Returns:
                    None
    ''' 
    data = load_data(date_ranges)
    data = preprocess_data(data, resample)
    
    input_vars = ["downwelling_shortwave", "percent_opaque"]
    output_var = "downwelling_shortwave"
    X,y = format_time_series(data, input_vars, output_var, n_steps_in, n_steps_out)
    
    # scale the data
    if scale:
        scale_time_series_data(X,y)
    
    # write to file
    if write_to_file:
        pickle_to_file(X, y, date_ranges, n_steps_in, n_steps_out, resample, scale, prefix)