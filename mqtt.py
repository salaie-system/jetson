import paho.mqtt.client as mqtt
import camera
import request

HOST = "192.168.1.213"
PORT = 31727
KEEP_ALIVE = 60
TOPIC_SUB = "/jetson/sub"
TOPIC_PUB = "/jetson/pub"

def on_connect(client, userdata, flags, respons_code):
    print("client.on_connect start")
    print("status {0}".format(respons_code))
    client.subscribe(client.topic)

def on_message(client, userdata, message):

    print("mqtt.py > on_message start")
    cap = camera.setting()
    path = camera.shoot(cap)
    r = request.getPredict(path)

    client.publish(TOPIC_PUB, r.text, 1)

    print(r.text)
    print("mqtt.py > on_message end")

if __name__ == '__main__':
    print("client start")
    client = mqtt.Client(protocol=mqtt.MQTTv311)
    print("client.topic start")
    client.topic = TOPIC_SUB
    
    client.on_connect = on_connect
   
    client.on_message = on_message
    
    client.connect(HOST, port=PORT, keepalive=KEEP_ALIVE)

    client.loop_forever()
