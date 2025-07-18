from emulator import generate_sensor_data
from edge_processing import EdgeProcessor
from mqtt_client import MQTTClient
import time

edge = EdgeProcessor(voltage_threshold=5, current_threshold=1)
mqtt = MQTTClient()
mqtt.connect()

try:
    while True:
        data = generate_sensor_data()

        anomaly_data = edge.process(data)
        power_data = edge.process_power_metrics(data)

        data.update(anomaly_data)
        data.update(power_data)

        mqtt.publish(data)
        print("Published:", data)

        time.sleep(1)

except KeyboardInterrupt:
    print("\nStopped by user.")

finally:
    mqtt.disconnect()
    print("MQTT disconnected.")