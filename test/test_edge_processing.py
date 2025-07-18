from emulator import generate_sensor_data
from edge_processing import EdgeProcessor
import time

edge = EdgeProcessor(voltage_threshold=5, current_threshold=1)

for _ in range(10):
    data = generate_sensor_data()

    anomaly_result = edge.process(data)
    power_result = edge.process_power_metrics(data)

    # Merge both result dictionaries
    result = {}
    result.update(data)
    result.update(anomaly_result)
    result.update(power_result)

    print("------------------------------------------------")
    for key, value in result.items():
        print(key + ": ", value)
    
    time.sleep(1)