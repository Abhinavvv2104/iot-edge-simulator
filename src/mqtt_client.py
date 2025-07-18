import paho.mqtt.client as mqtt
import json


class MQTTClient:
    def __init__(self, broker='localhost', port=1883, topic='iot/sensor/data'):
        self.broker = broker
        self.port = port
        self.topic = topic
        self.client = mqtt.Client()

    def connect(self):
        self.client.connect(self.broker, self.port)
        self.client.loop_start()

    def publish(self, data_dict):
        payload = json.dumps(data_dict)
        self.client.publish(self.topic, payload)

    def disconnect(self):
        self.client.loop_stop()
        self.client.disconnect()
        