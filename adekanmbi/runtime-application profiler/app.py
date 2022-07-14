from cProfile import run
from runtime_metrics import profiler
import logging
import threading
import time
import os
import psutil
import sys, getopt
import sched, schedule, time

s = sched.scheduler(time.time, time.sleep)
stack = []


def is_proccess_found(name):
    is_running = False
    for p in psutil.process_iter(attrs=["name", "exe", "cmdline"]):
        l = ","
        running_command = l.join(p.info["cmdline"])
        app_command_list = ["python", "-m", "tau_python_wrapper", "firstprime.py"]
        app_command = l.join(app_command_list)
        if app_command in running_command:
            is_running = True
    return is_running


def find_proccess(stack,metric_service):
    logging.info("Finding Application")
    if is_proccess_found("firstprime.py") == True:
        if len(stack) == 0:
            stack.append(time.time())
            logging.info("Profiling Application Started")
        else:
            logging.info("Profiling ... ")
        metric_service.runSystemProfile()
    else:
        if len(stack) == 1:
            stack.append(time.time())
        logging.info("No Application to profile")

def runtime(stack,metric_service):

    job = schedule.every(2).seconds.do(lambda: find_proccess(stack,metric_service))

    while True:
        schedule.run_pending()
        if len(stack) == 2:
            schedule.cancel_job(job)
            logging.info("Profiling completed")
            break
        time.sleep(1)
    

def main(argv):
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    metric_service = profiler("firstprime.py")

    # parse command line options:
    try:
       opts, args = getopt.getopt(argv,"hr:l",["runtime","live"])
    except getopt.GetoptError:
       print("Error")
       sys.exit(2)

    for opt, arg in opts:
       if opt == "-h":
         print('app.py -r runtime -l live')
         sys.exit()
       elif opt in ("-l", "--live"):
         print("live")
       elif opt in ("-r", "--runtime"):
          runtime(stack,metric_service)
          

   

if __name__ == "__main__":
    main(sys.argv[1:])

    
    # print(metric_service.metric)
