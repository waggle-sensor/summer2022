from live_metrics import SageAppMetricsServer
from runtime_metrics import profiler
from thread import thread
import logging
import threading
import time
import os
import psutil
import sched,time

s = sched.scheduler(time.time,time.sleep)



def is_proccess_found(name):
    is_running = False
    for p in psutil.process_iter(attrs=["name","exe","cmdline"]):
        if p.info["cmdline"] == ["python","firstprime.py"]:
            is_running = True
    return is_running

if __name__ == '__main__':
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    metric_service = profiler('firstprime.py')
    #print(metric_service.metric)

    # job_list = [metric_service.runTau,metric_service.runSystemProfile]
    # job = thread(job_list)
    # job.run_job()

    def find_proccess(sc):
        logging.info('Finding Application')
        if is_proccess_found("firstprime.py") == True:
            logging.info('Profiling Application')
            metric_service.runSystemProfile
        else:
            logging.info('No Application to profile')
        sc.enter(60,1,find_proccess,(sc,))
    
    s.enter(60,0,find_proccess,(s,))
    s.run()




    # logging.info('')












    # while True:
    #     time.sleep(1)
        # metric_service.


    # Setup custom Prometheus metric exporter
    # metrics_service = SageAppMetricsServer({'latency': SageAppMetricsServer.METRIC_TIMER,
    #                                         'fps': SageAppMetricsServer.METRIC_RATE,
    #                                         'x': SageAppMetricsServer.METRIC_NUMBER})

    # # This would be the app main function below doing some heavy-lifting neural network inferencing
    # while True:
    #     metrics_service.start_timer('latency')  # Start a timer for the metric "latency"

    #     # This could be setup/preprocessing code that is relevant to the latency metric but maybe not the fps metric
    #     print('This whole code block is being timed for latency...')
    #     time.sleep(1)

    #     # This could be a code block where FPS is relevant (I just put a useless for loop in here for example)
    #     metrics_service.start_timer("fps")
    #     x = 1
    #     for i in range(1, 1000):
    #         x = x * i
    #     metrics_service.push_metric('x', x)
    #     metrics_service.stop_timer("fps")

    #     metrics_service.stop_timer('latency')  # Stop the timer for the latency metric and let the server push the metric onto the stack
