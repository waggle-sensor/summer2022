import logging
import threading
import time

class thread:
    def __init__(self,jobs):
        self.jobs = jobs

    # def thread_function(name):
    #     logging.info("Thread %s: starting", name)
    #     time.sleep(2)
    #     logging.info("Thread %s: finishing", name)

    def run_job(self):
        threads = list()
        for index in range(len(self.jobs)):
            logging.info("Main    : create and start thread %d.", index)
            x = threading.Thread(target=self.jobs[index])
            threads.append(x)
            x.start()

        for index, thread in enumerate(threads):
            logging.info("Main    : before joining thread %d.", index)
            thread.join()
            logging.info("Main    : thread %d done", index)