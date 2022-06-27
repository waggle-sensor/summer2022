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
| 🟩 | Train model | High | <ul><li>Train:</li><ul><li>Number of stacked LSTM models</li><li>epochs, batch size, number folds</li><li>Discuss initial findings with mentors</li></ul>
| 🟩 | Write separate function to load data and set up into time series format | High | <ul><li>Takes a long time to run</li><li>Write out to some file</li><li>Needs to be re-run for different inputs and step sizes</li></ul> |
| 🟩 | Research variations in LSTM models | Med | <ul><li>Some nice elementary explanations [x]</li></ul> |
| 🟩 | Meet with Seongha | Low | <ul><li>Update on work accomplished thus far</li><li>Discuss future communication</li><li>Consider next steps</li></ul>|

✅ Completed, 🟩 In-Progress, ❎ Uncompleted (by end of week)

## Monday, June 27

- Setup goals for week

**Primary Project:**
LSTM to predict solar irradiance based on cloud coverage in July