# 🛰️ IoT Edge Emulator with Anomaly Detection & MQTT Streaming

A Python-based project that simulates electrical sensor data, performs edge-level processing (like anomaly detection and power tracking), and publishes results over MQTT.

Designed for testing IoT pipelines, dashboards, and cloud integrations.

---

## 🚀 Features

- 🔌 **Sensor Emulator**: Simulates real-time voltage, current, power, energy, and power factor readings
- 🧠 **Edge Processing**:
  - Simple Moving Average (SMA)
  - Voltage & Current Anomaly Detection
  - Energy consumption tracking
  - Rolling average of Power Factor
- 📡 **MQTT Publishing**: Publishes all processed data to a local MQTT broker
- 🗂️ **CSV Data Logger**: MQTT subscriber that logs incoming data to a `.csv` file
- 💡 **Modular Design**: Each component (emulator, edge processor, MQTT client) is cleanly separated

---

## 🛠️ How to Run

### 1. Start MQTT Broker
(Make sure Mosquitto is installed)
mosquitto -v

2. Run the Publisher
python src/main.py

3. Run the Logger (in another terminal)
python data/subscriber_logger.py

📦 Requirements
Install dependencies:

pip install -r requirements.txt
📊 Example Output
json

{
  "V_rms": 229.5,
  "I_rms": 10.1,
  "SMA_Voltage": 228.9,
  "SMA_Current": 10.05,
  "Anomaly": false,
  "Total_Energy_kWh": 0.032,
  "Avg_Power_Factor": 0.91
}
👨‍💻 Author
Abhinav Singh
B.Tech EEE + IoT @ BPIT
Passionate about Embedded Systems, IoT, and Edge Intelligence

📄 License
MIT License — feel free to use, modify, and share.
