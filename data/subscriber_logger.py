import paho.mqtt.client as mqtt
import json
import csv
from datetime import datetime
import os

LOG_FILE = "data/mqtt_data_log.csv"
TOPIC = "iot/sensor/data"

if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            "Timestamp", "V_rms", "I_rms", "Active_Power",
            "Apparent_Power", "Power_Factor", "Energy_kWh",
            "SMA_Voltage", "SMA_Current", "Anomaly", "Anomaly_Reason"
        ])

def on_connect(client, userdata, flags, rc):
    print("Connected to broker with code", rc)
    client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    payload = msg.payload.decode()
    print("Received:", payload)

    try:
        data = json.loads(payload)
        with open(LOG_FILE, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                data.get("Timestamp"),
                data.get("V_rms"),
                data.get("I_rms"),
                data.get("Active_Power"),
                data.get("Apparent_Power"),
                data.get("Power_Factor"),
                data.get("Total_Energy_kWh"),
                data.get("SMA_Voltage"),
                data.get("SMA_Current"),
                data.get("Anomaly"),
            ])
    except Exception as e:
        print("Error logging data:", e)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)
client.loop_forever()