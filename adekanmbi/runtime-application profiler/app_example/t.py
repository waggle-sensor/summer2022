# import logging
# import threading
# import time
# def thread_function(name):
#      logging.info("Thread %s: starting", name)
#      time.sleep(2)
#      logging.info("Thread %s: finishing", name)

# if __name__ == "__main__":
#     format = "%(asctime)s: %(message)s"
#     logging.basicConfig(format=format, level=logging.INFO,
#                        datefmt="%H:%M:%S")

#     logging.info("Main    : before creating thread")
#     x = threading.Thread(target=thread_function, args=(1,))
#     logging.info("Main    : before running thread")
#     x.start()
#     logging.info("Main    : wait for the thread to finish")
#     x.join()
#     logging.info("Main    : all done")

#!/usr/bin/python

# from multiprocessing import Process, current_process
# import time

# def worker():

#     name = current_process().name
#     print(name, 'Starting')
#     time.sleep(2)
#     print(name, 'Exiting')

# def service():

#     name = current_process().name
#     print(name, 'Starting')
#     time.sleep(3)
#     print(name, 'Exiting')

# if __name__ == '__main__':

#      while True:

#           service = Process(name='Service 1', target=service)
#           worker1 = Process(name='Worker 1', target=worker)
#           worker2 = Process(target=worker) # use default name

#           worker1.start()
#           worker2.start()
#           service.start()


# import psutil
# proc_iter = psutil.process_iter(attrs=["pid", "name", "cmdline"])
# # print(list(proc_iter))
# other_script_running = any("loop.py" in p.info["cmdline"] for p in list(proc_iter))

# for p in psutil.process_iter(attrs=["pid", "name", "cmdline"]):
#      print(p)


def find_procs_by_name(name):
    "Return a list of processes matching 'name'."
    is_running = False
    for p in psutil.process_iter(attrs=["name", "exe", "cmdline"]):
         if p.info["cmdline"] == ["python","loop.py"]:
             is_running = True

    return is_running


# print(find_procs_by_name("Music"))

import os
import psutil
import sched, time
s = sched.scheduler(time.time, time.sleep)
def do_something(sc): 
    print("Doing stuff...")
    # do your stuff
    print(find_procs_by_name("Music"))
    sc.enter(2, 1, do_something, (sc,))

s.enter(2, 0, do_something, (s,))
s.run()



# def find_procs_by_name(name):
#     "Return a list of processes matching 'name'."
#     ls = []
#     for p in psutil.process_iter(attrs=["name", "exe", "cmdline"]):
#          if p.info["cmdline"] == ["python","loop.py"]:
#               print(p.info["cmdline"])
         
     #     if 
     #    if (
     #        name == p.info["name"]
     #        or p.info["exe"]
     #        and os.path.basename(p.info["exe"]) == name
     #        or p.info["cmdline"]
     #        and p.info["cmdline"][0] == name
     #    ):
     #        ls.append(p)
#     return ls


# print(find_procs_by_name("Music"))

