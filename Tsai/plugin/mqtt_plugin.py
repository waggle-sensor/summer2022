import paho.mqtt.client as mqtt
import json
import base64
from waggle.plugin import Plugin
import os
os.environ["PYWAGGLE_LOG_DIR"] = "/var/log/pywaggle"

types = {
    "t": "env.temperature",
    "h": "env.humidity",
    "p": "env.pressure",
    "c": "env.coverage.cloud",
    "1": "env.count.bird",
    "2": "env.count.person",
    "3": "env.count.airplane",
    "4": "env.coount.car",
    "5": "env.raingauge.totalacc",
    "6": "env.raingauge.eventacc",
    "7": "env.raingauge.rint",
    "s": "env.smoke.tileprobs",
    "d": "env.detection.sound",
    "m": "message"
}

def mess(client, userdata, message):
    data = "Message received: " + message.payload.decode('utf-8') + " with topic " + str(message.topic)
    tmp_dict = json.loads(message.payload.decode('utf-8'))
    try:
        bytes_b64 = tmp_dict["data"].encode('utf-8')
    except:
        print("Message did not contain data.")
        return
    bytes = base64.b64decode(bytes_b64)
    val = bytes.decode('utf-8')
    type = val[0]

    with Plugin() as plugin:
        try:
            key = types[type]
        except KeyError:
            print("invalid type")
            return
        if type == "m":
            msg = val[1:]
        else:
            try:
                msg = int(val[1:])
            except:
                print("value should be interger:", val)
                msg = val[1:]

        try:
            # plugin.publish(key,msg,meta={"devName":tmp_dict["deviceName"], "devEUI":tmp_dict["devEUI"], "deviceProfile":tmp_dict["deviceProfileName"]})
            plugin.publish(key,msg,meta={"devName":tmp_dict["deviceName"], "devEUI":tmp_dict["devEUI"]})
        except:
            print("something went wrong")
    print(data)

def mqtt_start():
    client  = mqtt.Client("Andre's Computer")
    print("connecting...")
    client.connect("127.0.0.1")
    print("subscribing...")
    client.subscribe("application/2/device/#")
    print("waiting for callback...")
    client.on_message = mess
    client.loop_forever()



if __name__ == "__main__":
    mqtt_start()
