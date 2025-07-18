from collections import deque

class SMAProcessor:
    def __init__(self, window_size):
        self.buffer = deque(maxlen=window_size)

    def process(self, value):
        self.buffer.append(value)
        if len(self.buffer) < self.buffer.maxlen:
            return None
        return sum(self.buffer) / len(self.buffer)

class EdgeProcessor:
    def __init__(self, window_size=3, voltage_threshold=None, current_threshold=None):
        self.voltage_sma = SMAProcessor(window_size)
        self.current_sma = SMAProcessor(window_size)
        self.voltage_threshold = voltage_threshold
        self.current_threshold = current_threshold

        self.energy_total = 0
        self.pf_buffer = deque(maxlen=window_size)

    def process(self, data):
        voltage = data.get("V_rms")
        current = data.get("I_rms")

        sma_voltage = self.voltage_sma.process(voltage)
        sma_current = self.current_sma.process(current)
        anomaly = False
        reason = ""

        if sma_voltage and self.voltage_threshold:
            if abs(sma_voltage - voltage) > self.voltage_threshold:
                anomaly = True
                reason += "Voltage anomaly (Delta = " + str(abs(sma_voltage - voltage)) + "); "

        if sma_current and self.current_threshold:
            if abs(sma_current - current) > self.current_threshold:
                anomaly = True
                reason += "Current anomaly (Delta = " + str(abs(sma_current - current)) + ")"

        result = {
            "SMA_Voltage": round(sma_voltage, 2) if sma_voltage else None,
            "SMA_Current": round(sma_current, 2) if sma_current else None,
            "Anomaly": anomaly,
            "Anomaly_Reason": reason.strip()
        }

        return result

    def process_power_metrics(self, data):
        active_power = data.get("Active_Power")
        power_factor = data.get("Power_Factor")
        energy = data.get("Energy_kWh")

        self.energy_total += energy
        self.pf_buffer.append(power_factor)

        avg_pf = None
        if len(self.pf_buffer) == self.pf_buffer.maxlen:
            avg_pf = sum(self.pf_buffer) / len(self.pf_buffer)

        result = {
            "Total_Energy_kWh": round(self.energy_total, 3),
            "Avg_Power_Factor": round(avg_pf, 3) if avg_pf else None
        }

        return result