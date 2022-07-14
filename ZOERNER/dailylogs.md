# Maggie Zoerner - Daily Logs

### Overall Project Goals

- [x] Establish documentation in the Waggle GitHub Repository
- [x] Radar image processing using OpenCV to perform morphology computations
- [x] Utilize k-means clustering to place the radar images into distinct categories
- [ ] Apply algorithm to a season of radar data
- [ ] Complete deliverables (presentation, poster, paper)

### Week 1

##### Goals for this week:

- [x] Get set up with work station
- [x] Meet mentors
- [x] Complete orientation
- [x] Get familiar with Anaconda
- [x] Start working through example code

---

#### Tuesday May 31, 2022

- Completed new student orientation day 1
- Met with Bhupendra to discuss project roadmap

#### Wednesday June 1, 2022

- Completed new student orientation day 2
- Started TMS training
- Met with Bobby, Dario, Bhupendra to discuss additional project details
- Got access to data sets

#### Thursday June 2, 2022

- Finished setting up work space
- Began installing packages into new environment
- Attended TRACER briefing

#### Friday June 3, 2022

- Worked through some Python refresher code
- Started tinkering with data
- Troubleshooted Py-Art with Max
- Attended TRACER briefing

#### Week 1 Progress

- Got familiar with using Anaconda and installing Python packages
- Removed colorbar/title/axes from radar images to have accurate analyses in OpenCV.

---

### Week 2

##### Goals for this week:

- [x] Work through example code in Py-ART
- [x] Continue with required trainings
- [x] Remove some radar noise from images

---

#### Monday June 6, 2022

- Continued troubleshooting Py-ART with Max
- Worked through some example code to help with learning Py-ART
- Attended TRACER briefing

#### Tuesday June 7, 2022

- Attended TRACER briefing
- Did some TRACER training with Max to prepare for presentation of verification
- Finished working through example code for Py-ART

#### Wednesday June 8, 2022

- Attended weekly seminar (Informational Interviewing)
- Assisted with TRACER forecasting and attended briefing (Verification)
- Worked with data set in Py-ART

#### Thursday June 9, 2022

- Attended SEC160 Training
- Assisted with TRACER forecasting and attended briefing (Verification)
- Worked with data set in Py-ART and OpenCV

#### Friday June 10, 2022

- Assisted with TRACER forecasting and attended briefing (Air Quality)
- Worked with data set in OpenCV
- Continued with TMS trainings

#### Week 2 Overview

- Chose data from 5/20/22 because it was a heavy rain event
- Filtered out data < 40dBz as this is a widely accepted value used to use only convective precip. This will help to eliminate radar noise/lower reflectivities to get down to the core shape.
- Began to select radar images that would provide good data for image processing (different shapes)
- Pre-processed images to binary with thresholding with all pixels below 100 are set to 0 (black) and all pixels above 100 are set to 255 (white) to assist further with eliminating radar noise. Unsure if this is a proper method.

---

### Week 3

##### Goals for this week:

- [x] Complete required trainings
- [x] Set up GitHub profile
- [x] Learn more image processing techniques in OpenCV

---

#### Saturday June 11, 2022

- Assisted with TRACER forecasting and attended briefing (assistant)

#### Sunday June 12, 2022

- Assisted with TRACER forecasting (assistant)

#### Monday June 13, 2022

- Assisted with TRACER forecasting and attended briefing (assistant)
- Completed TMS trainings

#### Tuesday June 14, 2022

- Participated in ESH meeting
- Assisted with TRACER forecasting and attended briefing (Air Quality)
- Established folder in Waggle GitHub repository and created this document.
- Completed "About Me" Google Slide

#### Wednesday June 15, 2022

- Assisted with TRACER forecasting and attended briefing (weather forecast)
- Worked through more contour analysis using OpenCV.
- Attended weekly seminar

#### Thursday June 16, 2022

- Weekly Student Connect meeting
- Familiarized myself with Github, cloned the Waggle Github repository to create my own, figured out how to commit changes from my repository to the Waggle repository.
- Writing Coach Introductory Session
- Worked through more contour analysis using OpenCV

#### Friday June 17, 2022

- Assisted with TRACER forecasting and attended briefing (air quality forecast)
- Journaled about this week's project decision-making and progress
- Worked through more contour analysis using OpenCV

#### Week 3 Overview

- Did not make significant progress with the project this week due to heavy involvement with TRACER
- Practiced with more OpenCV techniques

---

### Week 4

##### Goals for this week:

- [x] Remove images from data set that contain little to no data after extracting lower reflectivities
- [x] Outline largest contour using OpenCV
- [x] Learn some image processing techniques in SciPy's ndimage library

---

#### Monday June 20, 2022

- Eliminated radar noise for all KILX 5/20/2022 rain event radar scans via Py-ART by removing reflectivity values less than 40 dBz.
- Saved filtered radar images to /filtered_quicklooks/
- Attended TRACER briefing

#### Tuesday June 21, 2022

- Removed images from data set that have no data after lower reflectivities were filtered out
- Was able to detect and draw largest contour on most images in the data set
- Attended TRACER briefing

#### Wednesday June 22, 2022

- Attended weekly seminar
- Attended TRACER briefing
- Removed images from data set that have little data ( < 1000 pixels) after lower reflectivities were filtered out as these images do not show major convective precip
- Detected and drew largest contour and tweaked the thresholding to only highlight the main convection on all remaining images
- Prepared introduction presentation slides

#### Thursday June 23, 2022

- Met with team to discuss student project progress
- Attended TRACER briefing
- Started working with scipy ndimage package

#### Friday June 24, 2022

- Met with student connect group
- Continued working with scipy ndimage package to practice image analysis

---

#### Week 4 Overview

- Wrote an algorithm that would remove images from the data set that contain little/no data after removing reflectivities less than 40 dBz.
- Drew largest contour on radar echoes using OpenCV
- Started practicing with ndimage.label to pick out the largest shape in the radar images.
- Next steps are to eliminate the smaller echoes to concentrate on the largest echo and calculate shape characteristics.-

---

### Week 5

##### Goals for this week:

- [x] Use scipy ndimage.label to extract the largest region of reflectivity in the radar images
- [x] Use OpenCV to perform image processing analysis on the labeled images and export as text files

---

#### Monday June 27, 2022

- Assisted with TRACER forecasting and attended briefing (verification)
- Worked with ndimage.label to remove the largest object from the radar images

#### Tuesday June 28, 2022

- Assisted with TRACER forecasting and attended briefing (weather forecast)
- Met with Bhupendra for help using the label function to extract the largest echo

#### Wedesday June 29, 2022

- Kayaking day with students and mentors

#### Thursday June 30, 2022

- Introduction meeting with AI group
- Attended TRACER briefing
- Worked on a script that finds the centroid of a shape based on its image moments.

#### Friday July 1, 2022

- Attended TRACER briefing
- Continued working on image analysis with OpenCV
- Created a text file to output to

---

#### Week 5 Overview

---

- Re-wrote first steps using netCDF4 file instead of png images
- Found the image moments
- Began morphology calculations based on image moments

---

### Week 6

##### Goals for this week:

- [x] Use OpenCV to find additional parameters
- [x] Contour new binary image and perform analysis with the contours

---

#### Monday July 4th, 2022

- Holiday, day off.

#### Tuesday July 5th, 2022

- Attended TRACER briefing
- Experimented with collecting more morphological parameters

#### Wednesday July 6th, 2022

- Assisted with TRACER forecasting and attended briefing (weather forecast)
- Continued working with morphological parameters in OpenCV

#### Thursday July 7th, 2022

- Assisted with TRACER forecasting and attended briefing (weather forecast)
- Attended weekly AI meeting
- Met with Bhupendra to discuss project
- Attended weekly Student Connects meeting
- Continued working with morphological parameters in OpenCV

#### Friday July 8th, 2022

- Contoured binary image, collected more parameters based on contour
- Worked on some organization, planning, goal-setting, and writing about progress.

---

#### Week 6 Overview and Reflection

---

I am over halfway through my SULI internship at this point in time, with 4 weeks left. My poster submission is due in 2 weeks, on July 21st.</br>
So far, I have gathered a data set, created a binary image and removed radar noise, and computed some parameters for the radar image.</br>
</br>
My next steps are to export these computations into a text file and format the file, perform k-means clustering on the parameters, and make revisions. Additionally, I need to increase the scale at which my current algorithm operates by looping through a dataset of multiple images and performing the analysis for all of the images in the dataset.  </br>
</br>
If time allows, I can either gather more datasets that I believe would make good cases to analyze, or run this algorithm for an entire season.</br>
</br>
The Learning on the Lawn event is on August 4th, and my final paper is due on August 5th. I will also need to complete a peer review by the end of my internship.</br>
</br>
I have learned so much about the research process throughout my internship at ANL so far. I have met some wonderful people here and have made amazing connections with my collegues. My project has been challenging and enriching for me, as I have had to take a lot of time to learn about new processes and techniques that were previously unfamiliar to me.</br>
</br>
My mentor, Bhupendra, gave me great advice. He told me that research is like learning how to ride a bike, you have to fall down before you can figure it out. I definitely needed to hear that!

---

### Week 7

##### Goals for this week:

- [x] Export data to tabular format
- [x] Perform more morphology computations
- [x] Start using k-means clustering

---

#### Monday July 11th, 2022

- Exported and formatted data into CSV file
- Attended TRACER briefing

#### Tuesday July 12th, 2022

- Performed additional morphology computations and exported to CSV file
- Attended TRACER briefing
- Attended 1:1 student check-in

#### Wednesday July 13th, 2022

- Worked on scaling up script to include 500+ radar files from the May KILX data set
- Troubleshooting and dealing with special cases that came up when I added more files into the script
- Improved contouring methods by performing further thresholding (eliminating radar echoes that contain < 200 pixels).

#### Thursday July 14th, 2022

- Attended weekly AI meeting
- Attended TRACER briefing
- Requested full season of NEXRAD data from Bobby, will be ready Friday evening or by Monday at the latest.
- Started developing poster presentation (due next Thursday July 21st)

#### Friday July 15th, 2022





