# Daniel Zetterberg - Daily Logs

### Project Goals
- [ ] Use Xarray and hvplot to analyze lidar data
- [ ] Use k-means clustering and principal component analysis to find patterns within lidar data
- [ ] Develop machine learning methods to analyze lidar data and predict patterns

### Week 1

---

#### Tuesday May 31, 2022

 - Completed new student orientation day 1
 - Read paper about Lidar, began downloading Python packages

 #### Wednesday June 1, 2022

 - Completed new student orientation day 2
 - Met with Bobby, Dario, Bhupendra, and Max to learn background of project
 - Met with Bobby to gain LCRC access

 #### Thursday June 2, 2022

 - Became familiar with Xarray
 - Used hvplot to look at snr and doppler velocity from lidar data

 #### Friday June 3, 2022

 - Began setting up ANL provided desktop by setting up Python packages and LCRC access
 - Attended Tracer meeting to become familiar with meteorology terminology

 ---

 ### Week 2

 ---

 #### Monday June 6, 2022

 - Worked on employee trainings
 - Continued setting up ANL computer
 - Wrote program to run through Bobby's lidar files to find file with cloud formation.

 #### Tuesday June 7, 2022
 
 - Worked on employee trainings
 - Continued setting up ANL computer
 - Found cloud formation in lidar data

 #### Wednesday June 8, 2022

 - Became familiar with features of hvplot
 - Accessed Jupyter through LCRC
 - Met with Bobby to discuss k-means clustering of lidar data
 - Attended summer seminar
 - Attended student connects group

 #### Thursday June 9, 2022

 - Troubleshooted Jupyter access on Bebop
 - Attended Tracer meeting
 - Worked on employee trainings

 #### Friday June 10, 2022

 - Atteneded Tracer meeting
 - Filtered out background SNR
 - Began analysis and k-means clustering of snr and doppler velocity variable of lidar data

 ---

 ### Week 3

 ---

#### Monday June 13, 2022

- Ran k-means clustering over snr, spectral width, and doppler velocity of the lidar data
- Discussed and interpreted results with Bobby
- Attended Tracer meeting

#### Tuesday June 14, 2022

- Began Dask tutorials
- Attended Tracer meeting
- Ran more k-means clustering over lidar data

#### Wednesday June 15, 2022

- Troubleshooted Jupyter access on Bebop
- Attended summer seminar
- Attended student connect groups
- Began reading over principal component analyis (PCA)

#### Thursday June 16, 2022

- Set up Waggle Github account
- Did PCA with lidar data

#### Friday June 17th, 2022

- Wrote in all of past daily logs
- Used PCA along with kmeans clustering

---

### Week 4

---

#### Monday June 20th, 2022

- Talked with Bobby about plotting
- Continued with Dask tutorial
- Worked on plotting cluster data in time-range domain

#### Tuesday June 21st, 2022

- Plotted cluster data in time-range domain
- Plotted Power Spectra for data points, averaged for each day

#### Wednesday June 22nd, 2022

- Student Seminar on LinkedIn
- Streamlined workflow so that all my data only uses xarray

#### Thursday June 23rd, 2022

- Waggle meeting
- Meeting with Argonne EVS mentors and students
- Moved workflow to a defined function, finished streamlining it

#### Friday June 24th, 2022

- Attended Student Connects Group
- Ran algorithm over 2 whole days
- Improved written functions and general of algorithm
- Looked at structure of clusters after PCA 

---

### Week 5 

### Goals for the week: 
- Expand my algorithm to run over all of the data using dask
- Gain a clearer image at the end goal of my project
- Understand the physical meaning of the improved clusters

---

#### Monday June 27th, 2022

- Worked on Creating an elbow plot of the clusters so that I can see the optimal number of clusters for my data
- Worked on updating dailylogs and using Github

#### Tuesday June 28th, 2022

- Continued working on elbow plot and updating it
- Studied Slurm and bash to begin running jobs directly on Bebop
- Ran a test script for an elbow plot on Bebop

#### Wednesday June 29th, 2022

- Sage Career Day!

#### Thursday June 30th, 2022

- AI Alogrithm Students Group Meeting
- Reran test script for an elbow plot on Bebop
- Began working on heatmap for showing clusters in principal component space
- Developed code for 2D histogram cluster plot
- Plotted clusters in time-range space for every hour of 08/31

#### Friday July 1st, 2022

- Could not do much today because Firefox was not working on my desktop, and I use Firefox to use Jupyter
- Wrote code to make a bar chart that shows label frequency versus time

---

### Week 6

### Goals for the Week:
- Use Bebop to run through all 2 months of data
- Simplify workflow so that I don't need to use Jupyter as much
- Start making conclusions for poster

---

#### Tuesday July 5th, 2022

- Restarted bash jobs
- Converted Jupyter notebook to plotting tools
- Worked on plotting the power spectra

#### Wednesday July 6th, 2022

- Continued working on getting clusters for all 2 months of data
- Student Connects Group
- Weekly Student Seminar

#### Thursday July 7th, 2022

- Created an elbow plot to find ideal number of clusters for all 2 months of data
- Ideal number of clusters is 5
- AI Algorithm student group meeting

#### Friday July 8th, 2022

- Ran bebop job to get cluster labels for all 2 months of data
- Created plots that show clustering of data in principal component space

---

### Week 7

### Goals for the week:
- Create a rough draft of the poster
- Make plots to include in the poster
- Find average power spectra for each cluster

---

#### Monday July 11th, 2022

- Continued working on power spectra job to run in Bebop
- Continued working on heatmap and cluster plots in PCA space
- Compared old clusters to new clusters

#### Tuesday July 12th, 2022

- Begun work on poster
- Coninued working on power spectra job
- Improved appearance of plots

#### Wednesday July 13th, 2022

- Continued working on poster
- Student connects group
- Weekly student seminar
- Begun improving power spectra plot code to use less memory

#### Thursday July 14th, 2022

- Updated daily logs for the past 2 weeks
- AI Student algorhithm group meeting
- Continued improving power spectra plot code to use less memory
- Toured sensors on sight at Argonnne, tour led by Matt
- Continued working on poster presentation



