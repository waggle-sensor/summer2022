from waggle.plugin import Plugin
import time
import os

os.environ["PYWAGGLE_LOG_DIR"] = "Tsai/plugin/test-run-logs"

with Plugin() as plugin:
    for i in range(10):
        print("publishing value", i)
        plugin.publish("arduino.msg", i, meta={"Number":"1"})
        time.sleep(1)