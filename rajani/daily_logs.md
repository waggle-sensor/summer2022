## Week 1

### Monday, June 6

- Attended new employee orientation
- Completed quadchart
- Read three recent papers on self-supervised learning:
  - Chen et al. (2020) on constrastive learning of visual representations
  - Caron et al. (2021) on self-supervised vision transformers
  - Bardes et al. (2022) on variance-invariance-covariance regularization

### Tuesday, June 7

- Met with Dario to discuss papers from Monday and applications to my project
- Learned about artificial neural networks from 3Blue1Brown series on deep learning
- Skimmed He et al. (2021) on federated self-supervised learning
- Started learning PyTorch, including the following material:
  - Tensor manipulation and operations
  - Using PyTorch's built-in autograd for gradient computation
  - Details of gradient descent and the backpropagation algorithm

### Wednesday, June 8

- Attended Sage software team meeting
- Practiced PyTorch training pipeline by training a linear regression model across several epochs
- Learned to implement logistic regression in PyTorch
- Learned about several PyTorch features, including:
  - Using the built-in Dataset and Dataloader classes
  - Using Dataset transforms
  - Using the softmax function with cross-entropy loss
  - Using several activation functions, such as the sigmoid function, tanh, ReLU, and leaky ReLU

### Thursday, June 9

- Attended required workplace violence training
- Attended LANS seminar on neuromorphic computing
- Implemented a basic feedforward neural network for MNIST digit classification and a basic convolutional neural network for image classification in PyTorch
- Learned how to save and load PyTorch models
- Started reading through through GitHub repository associated with VICReg paper

### Friday, June 10

- Downloaded and processed ImageNet data subset
- Made slight modifications to VICReg codebase to train a linear classifier on top of the pretrained backbone for 200 image classes from ImageNet subset
- Evaluated linear classifier and compared results to paper

## Week 2

### Monday, June 13

- Learned how to use Python's os module
- Wrote a script to split labelled data from Tiny ImageNet dataset into training, validation, and test data using os module
- Trained VICReg model on Tiny ImageNet; evaluated top-1 and top-5 accuracy and compared to pretrained model

### Tuesday, June 14

- Met with Dario to discuss vision transformers and some prerequisite concepts
- Learned about recurrent neural networks, backpropagation through time, LSTM, and GRUs

### Wednesday, June 15

- Planned use of VICReg for anomaly detection by monitoring variance, invariance, and covariance terms in loss function
- Learned how to use Tensorboard, and tested its features on MNIST dataset
- Started learning how to use TorchAudio, including creating a custom audio dataset in PyTorch and extracting Mel spectrograms

### Thursday, June 16

- Tested VICReg with default augmentations, using Tensorboard to plot the invariance term in the loss and display images
- Found that default augmentations created a model that was likely too robust to detect anomalies due to a lack of noticeable upticks in the invariance term when fed anomalous images
- Used different augmentations in the evaluation stage to see if the fluctuations in the invariance changed

### Friday, June 17

- Learned many more features of torchaudio, including how to pre-process audio to make the dataset more uniform in length, number of channels, etc.
- Implemented a CNN for sound classification using torchaudio
- Planned modified augmentations to training stage of VICReg that would make the model less robust to anomalous images
