    return {
        "V_rms": round(float(V_rms), 2),
        "I_rms": round(float(I_rms), 2),
        "Active_Power": round(float(active_power), 2),
        "Apparent_Power": round(float(apparent_power), 2),
        "Power_Factor": round(float(power_factor), 3),
        "Energy_kWh": round(float(Energy), 3),
        "Timestamp": datetime.datetime.now().isoformat()
    }
        
