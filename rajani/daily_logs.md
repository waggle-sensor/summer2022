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

## Week 3

### Monday, June 20

- Got access to ThetaGPU and learned how to submit jobs, start interactive sessions, forward ports, etc.
- Learned in more detail how to use the Linux command line (piping, etc.)
- Set up pretrained VICReg model on ThetaGPU; assessed performance on ImageNet

### Tuesday, June 21

- Read Hojjati et. al.’s survey paper on self-supervised anomaly detection to come up with alternative ideas for detecting anomalies in the spectrograms
- Trained my own VICReg model on ThetaGPU, assessed performance, and set up anomalous images. The network was unable to distinguish between normal images and anomalous images based on the terms in the loss function
- Set up visualization of terms in loss function and the invariance value of different images using Tensorboard

### Wednesday, June 22

- Since anomaly detection did not work with training on ImageNet, hypothesized that the model was too robust in feature extraction to distinguish between normal and anomalous images in the loss function
- Modified VICReg augmentations to consist solely of a crop, and varied the scale of the crop to attempt to improve contrast between normal and anomalous images, which was unsuccessful
- Devised a more curated task for anomaly detection, in which the network was trained solely on images from two classes of dogs, and then images of beverages were fed to the network as anomalies
- Sped up evaluation by switching from training images to anomalous images (and freezing the network weights) partway through training, logging the terms in the loss function

### Thursday, June 23

- Modified the loss function to consist solely of the covariance term; this was unsuccessful, and the covariance approached zero for all input images as training proceeded
- Presented solid color images to the network in training, and ImageNet images after freezing network weights; this allowed for distinction between normal and anomalous images using any one of the three terms in the loss function
  - Modifying the augmentations to include only the crop (and excluding the normalization) significantly improved performance by increasing the contrast between the loss terms between normal and anomalous images

### Friday, June 24

- Formed a hybrid neural network in which the Resnet50 used in the VICReg paper was replaced by the vision transformer used in DINO
- Assessed performance of the hybrid network on anomaly detection and found that it could distinguish between training images (two classes of dogs) and anomalous images (beverages) using the covariance term, but only for large batch sizes (e.g., 64), and not on the scale of individual images
- Implemented a basic autoencoder for anomaly detection, which I will adapt to audio spectrograms next week

## Week 4

### Monday, June 27

- Wrote a convolutional autoencoder to reconstruct audio spectrograms based on basic last week's basic autoencoder, with the plan to monitor reconstruction error to detect anomalies
- Met with Dario to discuss some alternate approaches for anomaly detection

### Tuesday, June 28

- Debugged and tried out many layer combinations for the autoencoder
- Evaluated performance of different network architectures based on training loss, monitored by viewing plot in Tensorboard

### Wednesday, June 29

- Career Day!

### Thursday, June 30

- Wrote an evaluation script to reconstruct audio from spectrograms and to display original and reconstructed spectrograms
- Evaluated chosen network architecture to assess whether reconstruction performance increased as training proceeded

### Friday, July 1

- Tested out several hyperparameters of model (batch size, learning rate, etc.)
- Learned how to use Singularity, and created an image to prepare convolutional autoencoder for ThetaGPU training

## Week 5

### Monday, July 4

- Holiday!
