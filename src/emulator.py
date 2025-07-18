import random
import numpy as np
import datetime
def generate_sensor_data():
    f=50
    T=1/f
    duration=0.1
    sampling_rate = 5000
    samples=int(sampling_rate*duration)
    t = np.linspace(0,duration,samples) 

    V_rms_true = 230
    I_rms_true = 10
    V_peak = V_rms_true * np.sqrt(2)
    I_peak = I_rms_true * np.sqrt(2)

    phase_shift_deg = 30
    phase_shift_rad = np.deg2rad(phase_shift_deg)

    voltage_clean = V_peak * np.sin(2 * np.pi * f * t)
    current_clean = I_peak * np.sin(2 * np.pi * f * t - phase_shift_rad)

    voltage_noisy=np.random.normal(0,5,size=samples)
    current_noisy=np.random.normal(0,0.5,size=samples)

    voltage = voltage_clean + voltage_noisy
    current = current_clean + current_noisy

    instant_power=voltage*current
    active_power=np.mean(instant_power)
    V_rms=np.sqrt(np.mean(voltage**2))
    I_rms=np.sqrt(np.mean(current**2))
    apparent_power=V_rms*I_rms
    Energy=(active_power*duration)/3600
    power_factor=active_power/apparent_power
    

    dictionary={
        "V_rms": round(V_rms,2),
        "I_rms": round(I_rms,2),
        "Active_Power": round(active_power,2),
        "Apparent_Power": round(apparent_power,2),
        "Power_Factor": round(power_factor,3),
        "Energy_kWh" : round(Energy,3),
        "Timestamp": datetime.datetime.now().isoformat()
    }
    return dictionary
a=generate_sensor_data()
b=a.get("Timestamp")
print(b)   
    

             
        