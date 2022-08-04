import paho.mqtt.client as mqtt
from queue import Queue
import json
import base64

q = Queue()

def mess(client, userdata, message):
    data = "Message received: " + message.payload.decode('utf-8') + " with topic " + str(message.topic)
    # q.put()
    tmp_dict = json.loads(message.payload.decode('utf-8'))
    print(tmp_dict)
    bytes_b64 = tmp_dict["data"].encode('utf-8')
    bytes = base64.b64decode(bytes_b64)
    q.put(bytes.decode('utf-8'))
    print(data)
    print(list(q.queue))

def mqtt_start():
    
    client  = mqtt.Client("Andre's Computer")
    print("connecting...")
    client.connect("10.31.81.21")
    print("subscribing...")
    client.subscribe("application/2/device/#")
    print("waiting for callback...")
    client.on_message = mess
    # q.put(data)
    client.loop_forever()



if __name__ == "__main__":
    mqtt_start()
