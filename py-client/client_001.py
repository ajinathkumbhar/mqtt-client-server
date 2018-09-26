import paho.mqtt.client as mqtt
import sys
import time

"""
MQTT subscriber 

"""

broker_addr = "127.0.0.1"
broker_port = "9998"
broker_user = "ajinath"
broker_pass = "ajinath"
subcriber_name = "tron1475"
topic = "hihello/pressure"

# Create client instance
mClient = mqtt.Client(subcriber_name)

# connect callback
def on_connect(client, userdata, flags, rc):
    if rc != 0:
        print 'Bad connection return code: ' + str(rc)
        client.bad_connection_flag = True
        return -1

    mClient.subscribe(topic)
    client.connected_flag = True


# message received callback
def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)

def on_log(client, userdata, level, buf):
    print("##log: ",buf)


# setup client
def init():
    mClient.connected_flag = False
    mClient.bad_connection_flag = False
    mClient.on_connect = on_connect
    mClient.on_message = on_message
    mClient.on_log = on_log
    mClient.username_pw_set("ajinath", "ajinath")

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
    #
    # Do not mix the different loop functions
    # Unfortunately I did not notice anywhere in the documentation
    # that both of those functions are not thread safe (might be wise to document this).
    # https://github.com/eclipse/paho.mqtt.python/issues/255
    mClient.loop_forever()

if __name__ == '__main__':
    main()
