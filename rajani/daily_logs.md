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

### Tuesday, July 5

- Librosa was not working properly with the Singularity container, which I needed to reconstruct audio files from the spectrograms. After many failed attempts, I resorted to training the model on ThetaGPU and evaluating on my local machine
- Used argparse to add arguments to training code to streamline training the model

### Wednesday, July 6

- Attended one seminar on poster presentations and the LANS seminar on the use of AI in mathematics.
- Learned in depth how parallelization works in PyTorch, and implemented a basic version in my training code (DataParallel), with plans to use DistributedDataParallel to decrease the overhead time cost and allow for training across multiple nodes

### Thursday, July 7

- Added more command line arguments to my code and set up model checkpoints in the manner done on the VICReg GitHub
- Created `anomaly_usd` GitHub repository to track progress on training on the Urban Sound Dataset
- Created separate `anomaly_bird` workspace for working with the BirdAudio dataset, and wrote a script that splits up a long (~6 hr.) audio clip into one-second samples and uses these samples as training data
  - Audio preprocessing occurs before the `__getitem__` method in order to speed up multiple-epoch training
- Performed a long (~3 hr.) training on BirdAudio dataset, for which the loss seemed to decrease very slowly, suggesting that the hyperparameter analysis would need to be re-done for this dataset

### Friday, July 8

- Wrote a script to scan through several combinations of hyperparameters for the new dataset, and found that a learning rate of 0.0001, a weight decay of 1e-7, and a batch size of 256 worked best
- Reformatted evaluation script as a `.ipynb` file to avoid having to re-load the dataset each time a different section of the data is to be analyzed
- Re-trained the model on daytime, rather than nighttime sounds and realized that the loss decreased much more smoothly (this dataset actually contained bird sounds, and wasn't just noise)
- Wrote code to report the timestamp of the largest reconstruction error, and found that it corresponded precisely with a very loud plane flying directly overhead, indeed an anomaly! It seems the autoencoder is working :)

## Week 6

### Monday, July 11

- Cleaned up and added new functionality to the evaluation component of the autoencoder, including:
  - Using `torch.utils.data.Subset` to allow for evaluation on a smaller portion of the dataset
  - Splitting evaluation into three functions:
    - `plot_recons()`: plots the original and reconstructed spectrograms of a specified set of frames
    - `save_audio()`: converts the original and reconstructed spectrograms to `.wav` files and saves them, for a specified set of frames
    - `get_max_loss()`: gives the timestamp of the maximum reconstruction error, as well as its value, and the average reconstruction error across the dataset
  - Added functionality to stitch together original audio and reconstructed audio from multiple training samples. The elevated noise level in the audio derived from the spectrograms suggests using more mels would be beneficial.

### Tuesday, July 12

- Implemented spectrogram cropping, whereby 128 mels are allocated for the entire spectogram, and only the frequencies corresponding with the highest 64 mels are used in training.
  - Met with Dario to discuss in which situations it makes sense to crop the spectrograms (e.g. clustering embeddings) and in which situations it doens't (e.g. anomaly detection based on monitoring the loss function)
- Modified the VICReg and resnet50 code to work with the custom BirdAudio dataset, implementing time-cropping of spectrogram clips as the joint embedding augmentations.

### Wednesday, July 13

- Trained VICReg on the spectrograms from a BirdAudio file, and found that anomalies generally occur when a bird sound appears in one half of a spectrogram, but does not appear in the other. Moreover, anomalies don't spike the invariance term in the loss, indicating that there are likely distinct embeddings corresponding with the anomalies (e.g. a plane).
- Attempted several variations on training, such as training on data known to contain no major anomalies and testing on data with anomalies, but found no spikes in the loss function corresponding with anomalous data points.

### Thursday, July 14

- Tested the effect of the autoencoder dimensionality on training speed and reconstruction quality.
- Implemented appropriate scaling for reconstructed spectrograms.
- Devised an alternate method of anomaly detection using attentional maps and met with Dario to discuss.

### Friday, July 15

- Modified the autoencoder architecture to output the embeddings at the bottleneck for analysis.
- Implemented PCA to reduce the dimensionality of autoencoder embeddings.
- Plotted the dimension-reduced embeddings in interactive 2D and 3D plots, along with their timestamps and losses, to visualize anomaly embeddings.

## Week 7

### Monday, July 18

- Re-trained autoencoder with higher embedding dimensionality (10-dimensional), both on cropped and uncropped spectrograms
- Implemented the ability to draw samples from a list containing multiple audio files (which required coming up with a means of indexing audio samples in well-defined way)
- Devised potential jigsaw puzzle pretext task for self-supervised representation learning; met with Dario to discuss this strategy and a few other ideas

### Tuesday, July 19

- Trained autoencoder with 5-dimensional embeddings on ThetaGPU, plotted embeddings, and analyzed clusters
  - Audio samples within the same cluster tended to have similar timestamps, suggesting that the noise in audio samples from different times of the day was informing the autoencoder's embeddings
- Modified VICReg code to save the embeddings during inference, with the idea that monitoring embeddings in addition to the reconstruction error might be a fruitful way of detecting anomalies

### Wednesday, July 20

- Further adjusted VICReg code to add functionality for saving embeddings both from the backbone alone and from the projections
- Trained VICReg with both the original augmentations from the paper, and the left/right cropping augmentation I implemented
- Wrote an script to load the backbone and projection embeddings from the saved file, perform PCA, and visualize them
  - Found that embeddings outside of the distribution did not correspond with anomalies

### Thursday, July 21

- Implemented the functionality to pull all audio files from a specified directory, rather than requiring specifying the path of each audio file
- Implemented a "tight cropping" mode that uses only the precise frequencies at which bird songs occur when cropping the Mel spectrogram
- Submitted a three-hour training to ThetaGPU that would use 0.2 second tight-cropped clips, with the hope that this would result in better clustering of birds
- Read Noroozi et. al (2016), a paper on jigsaw puzzle pretext tasks for self-supervised learning
