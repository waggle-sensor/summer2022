# Daily Progress Report

### Project Goals ###

- [ ] Create workflow and documentation (in the waggle github) to run instrumented AI@Edge in a docker.  Demo how to do it for the whole team.
- [ ] Decide on 5 simple measurements, by default, for all computational tasks.  For example: GPU RAM max, CPU RAM max, average, etc.
- [ ] Add into workflow pywaggle hooks to report summary measurements for each job to beehive.
- [ ] Add in pywaggle bits to publish internally, periodically, to scoreboard, so resource managers running locally could decide how to tune or tweak a running container that was misbehaving or exceeding resources.

### Week 1 ###

----------------------------------------------

#### Monday May 16, 2022 ####

- Completed new student orientation day 1
- Completed new student tile

#### Tuesday May 17, 2022 ####

- Completed new student orientation day 2
- Started JHQ training (3/8)
- Followed up with email with Sameer on TAU.

#### Wednesday May 18, 2022 ####

- Filled Dayforce time log
- Completed JHQ training (8/8)

#### Thursday May 19, 2022 ####

- Worked on creating a local docker container locally.

#### Friday May 20, 2022 ####

- Completed run Tau on docker image provided my Sameer.

    ``` docker pull ecpe4s/waggle-plugin-base:1.1.1-ml-cuda11.0-amd64
        docker run -it ecpe4s/waggle-plugin-base:1.1.1-ml-cuda11.0-amd64```

     ```root@b25e65e95994:/tau-2.31/examples/python# pprof -f profile.0.0.0 
        Reading Profile files in profile.0.0.0.*

        profile.0.0.0
        ---------------------------------------------------------------------------------------
        %Time    Exclusive    Inclusive       #Call      #Subrs  Inclusive Name
                    msec   total msec                          usec/call 
        ---------------------------------------------------------------------------------------
        100.0            0           90           3           0      30005 .TAU application => [CONTEXT] .TAU application
        100.0            0           90           3           0      30005 [CONTEXT] .TAU application
        85.5           74           76           1           5      76941 .TAU application
        66.2           59           59           2           0      29812 .TAU application => [CONTEXT] .TAU application => [SAMPLE] UNRESOLVED /lib/x86_64-linux-gnu/libc-2.27.so
        66.2           59           59           2           0      29812 [SAMPLE] UNRESOLVED /lib/x86_64-linux-gnu/libc-2.27.so
        33.8           30           30           1           0      30391 .TAU application => [CONTEXT] .TAU application => [SAMPLE] UNRESOLVED /usr/bin/python3.6
        33.8           30           30           1           0      30391 [SAMPLE] UNRESOLVED /usr/bin/python3.6
        1.4            1            1           1           0       1280 compile
        0.9        0.008        0.854           1           1        854 exec
        0.9        0.004        0.846           1           1        846 <module> 
        0.9        0.531        0.842           1           4        842 firstPrimeAfter 
        0.4        0.073        0.347           1          21        347 find_module 
        0.3        0.029        0.287           1           6        287 _find_and_load 
        0.2        0.009        0.206           1           3        206 _find_and_load_unlocked 
        0.2        0.033        0.137           1           6        137 _load_unlocked 
        0.1        0.022        0.081           6           7         14 isfile 
        0.1        0.009        0.076           1           3         76 module_from_spec 
        0.1        0.058        0.064           2           1         32 open
        0.1        0.016         0.06           1           6         60 detect_encoding 
        0.1        0.027        0.059           1           3         59 _find_spec 
        0.1        0.059        0.059           6           0         10 stat
        0.1        0.016         0.05           2           2         25 _call_with_frames_removed 
        0.1        0.032         0.05           7          23          7 join 
        0.1        0.005        0.047           1           1         47 create_module 
        0.0        0.008         0.04           3           3         13 __enter__ 
        0.0        0.034        0.034           1           0         34 create_builtin
        0.0        0.003         0.03           1           2         30 find_spec 
        0.0        0.012        0.027           2           4         14 find_cookie 
        0.0        0.018        0.026           1           1         26 read
        0.0        0.016        0.026           1           4         26 spec_from_loader 
        0.0        0.013        0.025           3           4          8 __exit__ 
        0.0        0.018        0.024           1           3         24 _get_module_lock 
        0.0        0.021        0.021           1           0         21 print
        0.0        0.016        0.019           6           3          3 __init__ 
        0.0        0.013        0.019           1           6         19 _init_module_attrs 
        0.0        0.013        0.015           1           3         15 get_suffixes 
        0.0        0.015        0.015           3           0          5 match
        0.0        0.006        0.014           2           2          7 read_or_stop 
        0.0        0.005        0.009           7           7          1 _get_sep 
        0.0        0.001        0.009           1           1          9 exec_module 
        0.0        0.007        0.008           1           1          8 decode 
        0.0        0.008        0.008           2           0          4 readline
        0.0        0.007        0.007           1           1          7 acquire 
        0.0        0.006        0.006           1           1          6 _requires_builtin_wrapper 
        0.0        0.006        0.006           9           0          1 isinstance
        0.0        0.006        0.006           8           0          1 startswith
        0.0        0.004        0.005           1           4          5 any
        0.0        0.004        0.005           1           1          5 release 
        0.0        0.002        0.004           1           3          4 cb 
        0.0        0.004        0.004           7           0          1 fspath
        0.0        0.004        0.004           4           0          1 hasattr
        0.0        0.003        0.003           4           0          1 getattr
        0.0        0.002        0.002           3           0          1 <listcomp> 
        0.0        0.002        0.002           1           0          2 format
        0.0        0.002        0.002           2           0          1 is_builtin
        0.0        0.002        0.002           1           0          2 new_module 
        0.0        0.001        0.002           1           1          2 parent 
        0.0        0.002        0.002           3           0          1 release_lock
        0.0        0.002        0.002           2           0          1 rpartition
        0.0        0.001        0.001           4           0          0 <genexpr> 
        0.0        0.001        0.001           1           0          1 _verbose_message 
        0.0        0.001        0.001           3           0          0 acquire_lock
        0.0        0.001        0.001           2           0          0 allocate_lock
        0.0        0.001        0.001           2           0          0 decode
        0.0        0.001        0.001           2           0          0 endswith
        0.0        0.001        0.001           2           0          0 get
        0.0        0.001        0.001           2           0          0 get_ident
        0.0        0.001        0.001           1           0          1 has_location 
        0.0        0.001        0.001           1           0          1 is_frozen
        0.0        0.001        0.001           1           0          1 sqrt
        0.0        0.001        0.001           1           0          1 utf_8_decode
        0.0            0            0           1           0          0 S_ISREG
        0.0            0            0           1           0          0 exec_builtin
        0.0            0            0           1           0          0 is_package 
        root@b25e65e95994:/tau-2.31/examples/python# ```

### Week 2 ###

------------------------------------------------

#### Monday May 23, 2022 ####

- Worked on running TAU with [plugin-surface-water-detection](https://github.com/waggle-sensor/plugin-surface-water-detection) locally.

#### Tuesday May 24, 2022 ####

- Worked on running TAU with [plugin-surface-water-detection](https://github.com/waggle-sensor/plugin-surface-water-detection) locally.

#### Wednesday May 25, 2022 ####

- Completed running the [plugin-surface-water-detection](https://github.com/waggle-sensor/plugin-surface-water-detection) locally got some errors need to debug.

#### Thursday May 26, 2022 ####

- Read some documentation on [TAU](https://sea.ucar.edu/sites/default/files/tau-seaconf18.pdf) and [Prometheus](https://prometheus.io/docs/concepts/metric_types/) documentations.

#### Friday May 27, 2022 ####

- Replicating the results of the [live monitoring app example](https://github.com/waggle-sensor/application-profiling).
- Modified the docker file to install pycuda.

Things to added to dockerfile.

``` export PATH="/usr/local/cuda-11.0/bin:$PATH" ```
``` export LD_LIBRARY_PATH="/usr/local/cuda-11.0/lib64:$LD_LIBRARY_PATH" ```
``` apt-get install nvidia-cuda-toolkit ```
``` pip install pycuda ```

### Week 3 ###

------------------------------------------------

#### Monday May 30, 2022 ####

- Labor Day.

#### Tuesday May 31, 2022 ####

- Read and worked on using socket programing on docker and also using docker-in-docker.

#### Wednesday June 01, 2022 ####

- Set up nvidia nx local for testing application.

#### Thursday June 02, 2022 ####

- Debug errors on running application on running on nx.

#### Friday June 03, 2022 ####

- Completed running running a live-application on nvidia-nx.
- Created a docker container with tau and example app [app-example:latest](https://hub.docker.com/layers/227035774/odunayo/waggle-plugin-base/1.1.1-ml-cuda10.2-l4t/images/sha256-8ced3a3e95d45dad0135ef14338891c8730a540ca78b175b0d048cbefd7e02e8?context=repo)

### Week 4 ###

------------------------------------------------

#### Monday June 6, 2022 ####

- Worked on running beehive waggle-plugin example.

#### Tuesday June 7, 2022 ####

- Worked on running beehive waggle-plugin example.

#### Wednesday June 8, 2022 ####

- Worked on code for generating runtime metrics for applications.

#### Thursday June 9, 2022 ####

- Worked on code for generating runtime metrics for applications.

#### Friday June 10, 2022 ####

- Worked on code for generating runtime metrics for applications.
- My code can be found here in runtime-application profiler, for version control changes see my forked branch here [runtime-application profiler](https://github.com/aabayomi/application-profiling.git)

### Week 5 ###

------------------------------------------------

#### Monday June 13, 2022 ####

- Worked on code for generating runtime metrics for applications.

#### Tuesday June 14, 2022 ####

- Worked on code for generating runtime metrics for applications.

#### Wednesday June 15, 2022 ####

- Implemented Tegrastats metric logging for running application. Below are the system and application metrics collected.

    ``` {'container_ram_usage': 233357312, 'tegrastats': {'time': datetime.datetime(2022, 6, 14, 23, 24, 4, 556681),'uptime': datetime.timedelta(1, 34193, 110000), 'jetson_clocks': 'OFF', 'nvp model': 'MODE_15W_4CORE', 'CPU1': 98, 'CPU2': 100, 'CPU3': 96, 'CPU4': 100, 'CPU5': 'OFF', 'CPU6': 'OFF','GPU': 13, 'MTS FG': 4, 'MTS BG': 4, 'RAM': 6189988, 'EMC': 6189988, 'SWAP': 392 'APE': 150, 'NVENC': 'OFF', 'NVDEC': 'OFF', 'NVJPG': 'OFF', 'fan': 100.0, 'Temp AO': 37.0, 'Temp AUX': 37.0, 'Temp CPU': 38.0, 'Temp GPU': 36.5, 'Temp thermal': 37.3, 'power cur': 5417, 'power avg': 3684}} ```

#### Thursday June 16, 2022 ####

- worked on writing a shell helper script to run in docker container. Can be found in runtime-application profiler/start.sh

#### Friday June 17, 2022 ####

- completed a working code for runtime profiler using the tau sample code.

### Week 6 ###

------------------------------------------------

#### Monday June 20, 2022 ####

- Drew the architecture for application profiler
- Worked running real application

#### Tuesday June 21, 2022 ####

- Worked on creating dockerize application on kubernetes

#### Wednesday June 22, 2022 ####

- Tried out the kubernetes tutorials

- Worked on creating dockerize application on kubernetes

#### Thursday June 23, 2022 ####

- Wrote script(tau_parser.py) to parse TAU outputs to JSON.

#### Friday June 24, 2022 ####

- Read paper on ai benchmarks [AI Benchmark: All About Deep Learning on Smartphones in 2019](https://arxiv.org/pdf/1910.06663.pdf)
- Usefull profiling metics

- Serial application - suggested metrics
  - Inclusive calls
  - Exclusive calls
  - Hardware Performance counter (PAPI )
  - Floating Point Instructions executed per second
  - Floating point instructions executed
  - Total instructions issued
  - Total instructions executed
  - Vector/SIMD instructions executed
  - Millions of floating point operations/second (PCL)
- Tau event trace
- Parallel application - suggested metrics
  - Tau MPI 




### Week 7 ###

------------------------------------------------

#### Monday June 27, 2022 ####

- Worked on dockerizing [plugin-surface-water-detection](https://github.com/aabayomi/plugin-surface-water-detection) to work on Jetson NX

#### Tuesday June 28, 2022 ####

- Worked on dockerizing [plugin-surface-water-detection](https://github.com/aabayomi/plugin-surface-water-detection) to work on Jetson NX

- Meet with Yongho,Seongha and Raj and pivoting to modeling a simple app for profile snapshots.

#### Wednesday June 29, 2022 ####

- Career day

#### Thursday June 30, 2022 ####

- Worked on installing PAPI to collect snapshot data

#### Friday July 1, 2022 ####

- Worked on Installing PAPI to collect snapshot on docker container

### Week 8 ###

------------------------------------------------

#### Monday July 4, 2022 ####

- Independence day

#### Tuesday July 5, 2022 ####

- Continued debug to run PAPI on Jetson NX

#### Wednesday July 6, 2022 ####

- Started working on final presentation
- Continued debug to run PAPI on Jetson NX
- Created a docker compose for app profiling example

#### Thursday July 7, 2022 ####

- Worked on presentation and designing experiment.

#### Friday July 8, 2022 ####

- Worked on presentation and designing experiment.

### Week 8 ###

------------------------------------------------

#### Monday July 11, 2022 ####

- Worked on presentation and designing experiment.

#### Tuesday July 12, 2022 ####

- Worked on presentation and designing experiment.
#### Wednesday July 13, 2022 ####

- Completed internship presentation.

#### Thursday July 14, 2022 ####

- Worked on using vector as profiling visualization.

#### Friday July 15, 2022 ####

- Worked on using PCP on Linux
- Started implementing using psutil


### Week 9 ###

------------------------------------------------

#### Monday July 18, 2022 ####

- Worked on shell usable version of CPU,GPU and Memory in docker. Code Changes can be tracked here in the runtime-profiler branch.
[runtime-profiler](https://github.com/waggle-sensor/application-profiling/tree/runtime-profiler)
#### Tuesday July 19, 2022 ####

- Worked on shell usable version of CPU,GPU and Memory in docker.
#### Wednesday July 20, 2022 ####

- Worked on shell usable version of CPU,GPU and Memory in docker.

#### Thursday July 21, 2022 ####

- Worked on shell usable version of CPU,GPU and Memory in docker.

#### Friday July 22, 2022 ####

- Worked on shell usable version of CPU,GPU and Memory in docker.


### Week 10 ###

------------------------------------------------

#### Monday July 25, 2022 ####

- - Worked on plotting visualization of profile data.
#### Tuesday July 26, 2022 ####

- Worked on plotting visualization of profile data.
#### Wednesday July 27, 2022 ####

- Created plot utility for profiler 
- Dry run presentation with Raj and Yongho.