# Maggie Zoerner - Daily Logs

### Overall Project Goals

- [x] Establish documentation in the Waggle GitHub Repository
- [ ] Radar image processing using OpenCV and determine which parameters give the best insight
- [ ] Utilize k-means clustering to place the radar images into distinct categories
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

- [ ] Use scipy ndimage.label to extract the largest region of reflectivity in the radar images
- [ ] Use OpenCV to perform image processing analysis on the labeled images and export as text files

---

#### Monday June 27, 2022

- Assisted with TRACER forecasting and attended briefing (verification)
- Worked with ndimage.label to remove the largest object from the radar images

