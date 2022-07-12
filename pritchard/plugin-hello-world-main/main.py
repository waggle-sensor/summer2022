from waggle.plugin import Plugin
import time

with Plugin() as plugin:
    for i in range(10):
        print("publishing value", i)
        plugin.publish("hello.world.value", i)
        time.sleep(1)
