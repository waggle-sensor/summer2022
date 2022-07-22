# Week 1 (5/31 - 6/3)

## Tuesday, May 31
- Completed new student orientation
- Set up Anaconda
- Registered for ARM Data Discovery
- Worked on TMS
- Read: [Array of things: a scientific research instrument in the public way: platform design and early lessons learned](https://doi.org/10.1145/3063386.3063771)

## Wednesday, June 1
- Completed new student orientation
- Finished TMS
- Met w/ Bobby, discussed immediate steps and internship logistics
- Download and began learning xarray
- Began reading: [Prediction of Solar Irradiance and Photovoltaic Solar Energy Product Based on Cloud Coverage Estimation Using Machine Learning Methods](https://doi.org/10.3390/atmos12030395)

## Thursday, June 2
- Studied xarray
- Obtained badge
- Finished reading: [Prediction of Solar Irradiance and Photovoltaic Solar Energy Product Based on Cloud Coverage Estimation Using Machine Learning Methods](https://doi.org/10.3390/atmos12030395)

## Friday, June 3
- Studied RNN, LSTM, GRU ([x](https://towardsdatascience.com/illustrated-guide-to-lstms-and-gru-s-a-step-by-step-explanation-44e9eb85bf21))
- Practiced xarray (plotting ARM data)

# Week 2 (6/6 - 6/10)

## Monday, June 6 - Friday, June 10

Excused leave for sister’s graduation

# Week 3

## Monday, June 13
- Sorted through some appointment logistics regarding excused leave last week
- Attended writing coach introductory session
- Practiced xarray (plotting ARM data) [practice\220603 xarray, arms data]
- Studied LSTM ([x](https://www.youtube.com/watch?v=S8tpSG6Q2H0))

## Tuesday, June 14

- Set up monitor!
- Practiced LSTM ([x](https://www.youtube.com/watch?v=S8tpSG6Q2H0)) [practice\220614 lstm milk production]
- Met with Bobby (updates, next steps)
- Worked on plotting ARMS data (solar irradiance, cloud coverage) in xarrayd

**Primary Project:** <br>
xarray (plot solar irradiance vs cloud coverage on one graph)

## Wednesday, June 15

- Attended EDU Seminar (When and How Do I go to Graduate School)
- Finished plotting ARMS data (solar irradiance, cloud coverage) in xarrayd
- Obtained prox card and new badge
- Attended Summer Intern Check-In
- Worked on using an LSTM to predict solar irradiance based on cloud coverage in July

**Primary Project:** <br>
LSTM to predict solar irradiance based on cloud coverage in July
# Week 3 (6/13 - 6/17)

## Monday, June 13

- Sorted through some appointment logistics regarding excused leave last week
- Attended writing coach introductory session
- Practiced xarray (plotting ARM data) [practice\220603 xarray, arms data]
- Studied LSTM ([x](https://www.youtube.com/watch?v=S8tpSG6Q2H0))

## Tuesday, June 14

- Set up monitor!
- Practiced LSTM ([x](https://www.youtube.com/watch?v=S8tpSG6Q2H0)) [practice\220614 lstm milk production]
- Met with Bobby (updates, next steps)
- Worked on plotting ARMS data (solar irradiance, cloud coverage) in xarrayd

**Primary Project:**
Deliverable: xarray (plot solar irradiance vs cloud coverage on one graph)

## Wednesday, June 15

- Attended EDU Seminar (When and How Do I go to Graduate School)
- Finished plotting ARMS data (solar irradiance, cloud coverage) in xarray
- Obtained prox card and new badge
- Attended Summer Intern Check-In
- Worked on using an LSTM to predict solar irradiance based on cloud coverage in July

**Primary Project:**
LSTM to predict solar irradiance based on cloud coverage in July

## Thursday, June 16

- Studied LSTM
    - ([1](https://colah.github.io/posts/2015-08-Understanding-LSTMs/)) Impressively clear and thorough explanation of RNN and LSTM. Briefly touches on GRU
    - ([2](http://karpathy.github.io/2015/05/21/rnn-effectiveness/)) Quick explanation of RNN and lots of fun examples of usage
- Worked on using an LSTM to predict solar irradiance based on cloud coverage in July
    - Finished general methods, but model is highly inaccurate

**Primary Project:**
LSTM to predict solar irradiance based on cloud coverage in July

## Friday, June 17

- Heavily refactored code; much cleaner and easier to manipulate now
- Worked on increasing LSTM accuracy

**Primary Project:**
LSTM to predict solar irradiance based on cloud coverage in July

# Week 4 (6/20 - 6/24)

## Monday, June 20

- Attended Principles of Scientific Communication seminar
- Studied time series forecasting to better understand how to improve model ([1](https://machinelearningmastery.com/time-series-forecasting/), [2](https://machinelearningmastery.com/time-series-forecasting/))
- Worked on hyperparameter optimization

**Primary Project:**
LSTM to predict solar irradiance based on cloud coverage in July

## Tuesday, June 21

- Studied k-fold cv ([1](https://machinelearningmastery.com/k-fold-cross-validation/), [2](https://machinelearningmastery.com/how-to-configure-k-fold-cross-validation/), [3](https://towardsdatascience.com/gridsearchcv-for-beginners-db48a90114ee))
- Implemented grid search cross validation (using a time series split)
- Implemented pickle saving/loading

**Primary Project:**
LSTM to predict solar irradiance based on cloud coverage in July

## Wednesday, June 22

- Attended EDU Seminar (Connecting to a Career Through LinkedIn)
- Worked on making model work with multivariate inputs, multistep outputs
- Discussed progress and next steps with Bobby
- Set up SSH, Swing (LCRC)

**Primary Project:**
LSTM to predict solar irradiance based on cloud coverage in July

## Thursday, June 23

- Met with  ML/radar group to discuss progress
- Worked on getting connected to Swing
- Worked on making model work with multivariate inputs, multistep outputs

**Primary Project:**
LSTM to predict solar irradiance based on cloud coverage in July

## Friday, June 24

- Worked on making model work with multivariate inputs, multistep outputs (hyperas)
- Attended student check-in

**Primary Project:**
LSTM to predict solar irradiance based on cloud coverage in July

# Week 5 (6/27 - 7/1)

## Goals

|     | Goal | Priority | Notes |
| --- | --- | --- | --- |
| ❎ | Train model | High | <ul><li>Train:</li><ul><li>Number of stacked LSTM models</li><li>epochs, batch size, number folds</li><li>Discuss initial findings with mentors</li></ul>
| ✅ | Write separate function to load data and set up into time series format | High | <ul><li>Takes a long time to run</li><li>Write out to some file</li><li>Needs to be re-run for different inputs and step sizes</li></ul> |
| 🟩 | Research variations in LSTM models | Med | <ul><li>Some nice elementary explanations [x](https://machinelearningmastery.com/how-to-develop-lstm-models-for-time-series-forecasting/)</li></ul> |
| ✅ | Meet with Seongha | Low | <ul><li>Update on work accomplished thus far</li><li>Discuss future communication</li><li>Consider next steps</li></ul>|

✅ Completed, 🟩 In-Progress, ❎ Uncompleted (by end of week)

## Monday, June 27

- Setup goals for week
- Wrote script to prepare date in time series format
- Debugged misc issues regarding training model
- Worked on hyperparameter opimization
- Studied transformers [[1](https://www.youtube.com/watch?v=EFkbT-1VGTQ), [2](https://arxiv.org/abs/2109.12218)]
    - Interesting, but would be a major change from current methods. Consider if RNN’s perform poorly.
- Set up meeting with Seongha

**Primary Project:**
LSTM to predict solar irradiance based on cloud coverage in July

## Tuesday, June 28

- Debugged multivariate grid search (flatten input and reshape)
- Debugged data loading (improper shape)

**Primary Project:**
LSTM to predict solar irradiance based on cloud coverage in July

## Wednesday, June 29

- Career Day - Kayaking!

## Thursday, June 30

- Debugged data loading
- Met with AI/Algorithm student group
- Met with Seongha
    - Condensed Notes:
        - Key takeaways
            - Completely ignore all faulty data
            - Stick with ARMS data for duration of project
            - Code and model will have to run on NVIDIA Nano; later down the line think about dockerizing for plug-in
        - Todos
            - Check timezone of data: may have to resample to match
            - Resample data to every 15 minutes
            - Switch from just July to all data
            - Normalize variables individually
            - Test for resource usage, accuracy, and speed (in that order of importance)        
- Modified data loading format based on Seongha’s feedback (ignoring faulty data, resampling)
    - Checked time zones: all data is in 0000UTC, but may be split into days differently (i.e., for us, solar irradiance splits at 0000UTC and cloud coverage splits at 0600UTC)

**Primary Project:**
LSTM to predict solar irradiance based on cloud coverage

## Friday, July 1

- Wrote script to delete unnecessary data files (i.e., dates which have data for only one of the two variables)
- Worked on configuring GPU set up
    - Meet with Bobby next week for help

**Primary Project:**
LSTM to predict solar irradiance based on cloud coverage

# Week 6 (7/5 - 7/8)

## Goals

|  | Goal | Priority | Notes |
| --- | --- | --- | --- |
| ✅ | Configure Jupyter to run GPU on Swing | High | <ul><li>Work with Bobby</li></ul> |
| 🟩 | Implement early stopping | High |  |
| ❎ | Train model | High | <ul><li>Train:</li><ul><li>Number of stacked LSTM models</li><li>epochs, batch size, number folds</li><li>Discuss initial findings with mentors</li></ul> |
| 🟩 | Research variations in LSTM models | Low | <ul><li>Some nice elementary explanations [x](https://machinelearningmastery.com/how-to-develop-lstm-models-for-time-series-forecasting/)</li></ul> |

✅ Completed, 🟩 In-Progress, ❎ Uncompleted (by end of week)

## Monday, June 4

- Independence Day Holiday

## Tuesday, June 5

- Setup goals for week
- Worked with Bobby to configure GPU setup
- Debugged using GPU in Jupyter
    - Test Drive: CPU (3:59 CPU / 3:53 wall); GPU (3:54 CPU / 3:46 wall)
    - GPU runs out; issue seems to be in data
- Found issue in data: nan values in solar irradiance (potentially also percent opaque though not yet witnessed)

**Primary Project:**
LSTM to predict solar irradiance based on cloud coverage

## Wednesday, June 6

- Attended EDU Weekly Seminar - Creating Effective Oral and Poster Presentations
- Attended LANS Seminar - AI x Mathematics
- Debugged issues in loading data, refactored code
    - Removed NaN values ⇒ there are now (very, very infrequent) random gaps in data from where the NaN values used to be, in addition to the gaps each night
- Worked on configuring parallel processing (for pre-loading data)
- Rewrote data loading to be much faster (~11.5s vs ~17.3s)

**Primary Project:**
LSTM to predict solar irradiance based on cloud coverage

## Thursday, June 7

- Met with AI/Algorithm student group
    - Notes:
        - Batch by day so gaps between days don’t mess things up
        - When prepping predictions and stuff, be careful you’re cutting in right spot (not including predictive value into input) (i.e. unit test for split step)
- Configured GPU
    - Able to run using Keras, but not with scikit-learn’s GridSearchCV ⇒ switch to some other package for tuning
- Uncovered bug in data loading (overlapping values). Worked on manual opening and concatenation of multiple files to fix

**Primary Project:**
LSTM to predict solar irradiance based on cloud coverage

## Friday, June 8

- Debugged issue in data loading. Finished manual opening and concatenation method.
- Worked on implementing time series cross-validation with early stopping
- Attended Summer Interns Check-In

**Primary Project:**
LSTM to predict solar irradiance based on cloud coverage

# Week 7 (7/11 - 7/15)

## Goals

|  | Goal | Priority | Notes |
| --- | --- | --- | --- |
| ✅ | Wrap up manual implementation (cross validation, early stopping, tuner) | High |  |
| 🟩 | Train model | High | <ul><li>Train:</li><ul><li>Number of stacked LSTM models</li><li>epochs, batch size, number folds</li><li>Discuss initial findings with mentors</li></ul> |
| ✅ | Research variations in LSTM models if model performance unsatisfactory | Low | <ul><li>Some nice elementary explanations [x](https://machinelearningmastery.com/how-to-develop-lstm-models-for-time-series-forecasting/)</li></ul> |

✅ Completed, 🟩 In-Progress, ❎ Uncompleted (by end of week)

## Monday, June 11

- Set up weekly goals
- Implemented manual time series validation, early stopping, hyperparameter tuning
    - Could not use sklearn due to lack of GPU support nor keras due to different training methodologies, so manually implemented
- Researched variations in RNN architectures
- Note: LCRC maintenace day
    - Need to check if all methods still function on GPU tomorrow
    - Need to check if optuna works with environment

**Primary Project:**
LSTM to predict solar irradiance based on cloud coverage and solar irradiance

## Tuesday, June 12

- Checked that new implementations compatible with GPU
- Researched variations in RNN architectures
- Fixed bug in scaling data
- Worked on rewriting data loading to ensure all days have consistent number of timestamps
    - Discovered heavy gaps in data (specifically cloud data, it seems): entire days without data, days missing many data points, etc.
    - For entire days, days missing many data points: remove from dataset, check on resampling without including those days
    - Shorter days (i.e., in the winter): pad with 0’s for night
        - Looks like 900 data points is a safe choice? 850 a slightly tighter bound
        - Figure out how to do this
            - Select times each day to add 0’s to if no existing value (perhaps: 10:30 - 3:00 UTC? Based on graph and Ohio weather data)
            - Remember that times are in UTC which may be funky for indexing (espepecially first day, since there’s data from the previous day’s sunset)

**Primary Project:**
LSTM to predict solar irradiance based on cloud coverage and solar irradiance

## Wednesday, June 13

- Attended EDU Weekly Seminar - Overview of Learning On/Off the Lawn and Open Q&A on Deliverables
- Preprocessing
    - Changed data timezone
    - Removed dates with large amounts of missing data
    - Padded and trimmed data so days have consistent length
    - Rewrote data resampling to avoid creating nonexistant data

**Primary Project:**
LSTM to predict solar irradiance based on cloud coverage and solar irradiance

## Thursday, June 14

- Fixed error with timezone of data
- Met with AI/Algorithm student group
- Fixed bug with missing data values in-between other data values
- Modified train/test split and batch size to be by day
    - Not perfect since time series carries between days
    - Validation is also not by day
    - If wanted to make it perfectly by day would make more sense to have input/output be based on day instead of timestamps. I think for these purposes it makes sense though? Hyperlocal prediction for the next x hours
- Fixed bug with y values being scaled improperly
- Performed preliminary training
    - Long-term: fairly decent. It looks like it tends to follow the days given (e.g. if given 6 sunny days predicts next day sunny as well)
    - Short-term: quite good I think
- Researched energy forecasting for smart grid management

**Primary Project:**
LSTM to predict solar irradiance based on cloud coverage and solar irradiance

## Friday, June 15

- Learned to use slurm to submit jobs (for eventual purpose of running training overnight)
    - Followed [x](https://www.lcrc.anl.gov/for-users/using-lcrc/running-jobs/running-jobs-on-swing/) tutorial from LCRC website
- Pre-loaded variations of dataset (two weeks in, one week out)
    - Not sure if will actually use this since 1) is big and bulky 2) Seongha recommended just one hour and I think the day-ahead search will be sufficient enough to show long-term accuracy 3) haven’t seen ML-focused papers do this, though some energy management papers have listed week or month or even year-ahead forecasting as being valuable

**Primary Project:**
LSTM to predict solar irradiance based on cloud coverage and solar irradiance

# Week 8 (7/18 - 7/22)

## Goals

|  | Goal | Priority | Notes |
| --- | --- | --- | --- |
| ✅ | Wrap up python job for submission to Swing | High |  |
| ✅ | Train model | High | <ul><li>Train:</li><ul><li>Number of stacked cells</li><li>LSTM vs GRU vs SimpleRNN</li><li>Start w/ one-hour ahead, then try one-day ahead</li></ul> |
| ✅ | Create poster for Learning on the Lawn | High | Due **Thursday, 5PM** |

✅ Completed, 🟩 In-Progress, ❎ Uncompleted (by end of week)

## Monday, June 18

- Set up goals for week
- Finished refactoring training/hyperparameter optimization
- Configured slurm file to run training/hyperparameter optimization code
- Scheduled training for overnight
- Worked on poster (additional research on background)

**Primary Project:**
LSTM to predict solar irradiance based on cloud coverage and solar irradiance

## Tuesday, June 19

- Worked on poster (text writing, formatting)
- Fixed a few misc. bugs in code (saving model, saving loss history)
- Visualized results from training
    - Looks exciting!

**Primary Project:**
Poster

## Wednesday, June 20

- Attended EDU Weekly Seminar - Resume Workshop
- Worked on poster (finished first draft)
    - Added additional data visualization
- Attended Summer Interns Check-In

**Primary Project:**
Poster

## Thursday, June 21

- Met with AI/Algorithm student group
- Finished poster! (added conclusions, misc retouches and fixes)

**Primary Project:**
Poster