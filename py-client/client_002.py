import paho.mqtt.client as mqtt
import sys
import time
import random
"""
MQTT publisher 

"""
broker_addr = "127.0.0.1"
broker_port = "9998"
broker_user = "ajinath"
broker_pass = "ajinath"
subcriber_name = "tron1476"
topic = "hihello/pressure"

# Create client instance
mClient = mqtt.Client(subcriber_name)

# connect callback
def on_connect(client, userdata, flags, rc):
    if rc != 0:
        print 'Bad connection return code: ' + str(rc)
        client.bad_connection_flag = True
        return -1

    client.connected_flag = True
    client.publish(topic, "Sending data")  # publish


def on_log(client, userdata, level, buf):
    print("##log: ",buf)

# setup client
def init():
    mClient.connected_flag = False
    mClient.bad_connection_flag = False
    mClient.on_connect = on_connect
    mClient.on_log = on_log
    mClient.username_pw_set("ajinath", "ajinath")

def publish_msg(msg):
    mClient.publish(topic, str(msg))  # publish
    # publish(self, topic, payload=None, qos=0, retain=False):

def start_send_data():
    loop = 0
    for pressure_val in range(100):
        time.sleep(1)
        loop = loop + 1
        msg = str(loop) + str(" ") + str(random.randint(1,255))
        publish_msg(msg)

# connect to broker
def connect():
    print 'connecting to broker : ' + broker_addr + ":" + broker_port

    # connect with fix addr and port
    mClient.connect(broker_addr, broker_port)

    if mClient.bad_connection_flag:
        sys.exit()

    print 'connected OK'


def main():
    init()
    connect()
    start_send_data()

if __name__ == '__main__':
    main()





















# import paho.mqtt.client as mqtt
# import random
# import time
#
# cli = mqtt.Client()
#
# def on_connect(client, userdata, flags, rc):
#     print 'connected with result code ' + str(rc)
#     client.publish("pressure", "Sending data")  # publish
#
# def on_publish(client, userdata, mid):
#     print 'message published :' + str(mid)
#
# def send_data():
#     loop = 0
#     for pressure_val in range(100):
#         time.sleep(1)
#         loop = loop + 1
#         msg = str(loop) + str(" ") + str(random.randint(1,255))
#         publish_msg(msg)
#
# def publish_msg(msg):
#     cli.publish("pressure", str(msg), qos=1, retain=True)  # publish
#     # publish(self, topic, payload=None, qos=0, retain=False):
#
# def main():
#     cli.on_connect = on_connect
#     cli.on_publish = on_publish
#     cli.username_pw_set("ajinath", "ajinath")
#     cli.connect("127.0.0.1", 1883, 60)
#     send_data()
#
#
# if __name__ == '__main__':
#     main()
#
#

