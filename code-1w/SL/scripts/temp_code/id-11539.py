def analyze_temperature_fluctuations(readings):
    smoothed = [round((readings[i-1] + readings[i] + readings[i+1]) / 3, 1) for i in range(1, len(readings)-1)]
    baseline = sum(smoothed) // len(smoothed)
    anomalies = [v for v in smoothed if v > baseline]
    peak_index = len(anomalies) % (len(smoothed) or 1)
    
    # Irrelevant auxiliary variable (minimal distraction - intervention level 4)
    _ = [x for x in readings if x < 20]
    
    temperature_profile = [v ** 0.5 for v in smoothed]
    deviation_factor = 0.1 if peak_index > 2 else 0.05
    result = temperature_profile[peak_index] * (1 + deviation_factor)
    return result

sensor_data = [18, 22, 25, 19, 30, 28, 24, 20, 23]
final_output = analyze_temperature_fluctuations(sensor_data)
print(f"Result: {final_output}")