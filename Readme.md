#  IoT Edge Emulator with Anomaly Detection & MQTT Streaming

A Python-based project that simulates electrical sensor data, performs edge-level processing (like anomaly detection and power tracking), and publishes results over MQTT.

Designed for testing IoT pipelines, dashboards, and cloud integrations.

---

##  Features

-  **Sensor Emulator**: Simulates real-time voltage, current, power, energy, and power factor readings
-  **Edge Processing**:
  - Simple Moving Average (SMA)
  - Voltage & Current Anomaly Detection
  - Energy consumption tracking
  - Rolling average of Power Factor
-  **MQTT Publishing**: Publishes all processed data to a local MQTT broker
-  **CSV Data Logger**: MQTT subscriber that logs incoming data to `data/mqtt_data_log.csv`
-  **Modular Design**: Each component (emulator, edge processor, MQTT client) is cleanly separated

---

##  Folder Structure
iot-edge-emulator/
├── src/
│ ├── emulator.py # Simulates sensor readings
│ ├── edge_processing.py # SMA + anomaly detection + metrics tracking
│ ├── mqtt_client.py # MQTT client class for publishing
│ └── main.py # Main program: integrates all modules
├── data/
│ └── subscriber_logger.py # MQTT subscriber logger (CSV)
├── requirements.txt
├── .gitignore
└── README.md

🔹 Step 1: Make sure Mosquitto broker is running
In PowerShell or a new terminal, run:
mosquitto -v
This starts the local MQTT broker on port 1883.

🔹 Step 2: Run the Main Generator and Publisher
In a second terminal:

cd "C:\Users\Abhinav\Documents\PROGRAMMING\iot-edge-emulator"
python src/main.py
This runs:
generate_sensor_data() from emulator.py 

Edge processing using EdgeProcessor

Publishes to iot/sensor/data using MQTTClient

You'll see output like:
Published: {'V_rms': ..., 'SMA_Current': ..., 'Anomaly': False, ...}
🔹 Step 3: Run the Logger (Subscriber)
In a third terminal:
python data/subscriber_logger.py

 This will:
Subscribe to iot/sensor/data

Print incoming messages

Log them to data/mqtt_data_log.csv

###Requirements
Install dependencies:

pip install -r requirements.txt

Author
Abhinav Singh
B.Tech EEE + IoT @ BPIT
Passionate about Embedded Systems, IoT, and Edge Intelligence
