import math

# Simulated sensor data from environmental monitoring stations
temperature_readings = [23.5, 24.1, 22.8, 25.6, 26.7, 23.9, 24.4, 25.1]
humidity_readings = [56, 61, 59, 64, 70, 55, 60, 63]
pressure_readings = [1013, 1015, 1012, 1009, 1007, 1014, 1016, 1011]

# Irrelevant backup data (distractor)
temp_backup = temperature_readings[::-1]
hum_backup = [x * 1.005 for x in humidity_readings]

# Misleading normalization function (dead path)
def normalize_signal(signal):
    mean_val = sum(signal) / len(signal)
    return [(x - mean_val) / mean_val for x in signal]

# Unused transformation chain (red herring)
transformed_humidity = []
for i, val in enumerate(humidity_readings):
    if val > 60:
        transformed_humidity.append(val * 0.95 + i)
    else:
        transformed_humidity.append(val * 1.02)

# Decoy analysis with bit manipulation (irrelevant)
def decoy_integrity_check(data):
    checksum = 0
    for x in data:
        checksum ^= int(x) << 1
        checksum &= 0xFFFF
    return checksum | 0xAAAA

# Spurious frequency simulation (distractor)
frequency_shift = 0
for t in temperature_readings:
    frequency_shift += int(t) ^ 7
    frequency_shift = (frequency_shift >> 2) + 3

# Real processing: detect anomalies in signals
def detect_anomalies(data, threshold=2.0):
    mean_val = sum(data) / len(data)
    variance = sum((x - mean_val) ** 2 for x in data) / len(data)
    std_dev = math.sqrt(variance)
    outliers = [x for x in data if abs(x - mean_val) > threshold * std_dev]
    return len(outliers)

# Signal processor with zip and enumerate (required features)
def process_sensor_signals(temp, hum, pres):
    processed = []
    # Combine multiple sensor readings using zip
    for i, (t, h, p) in enumerate(zip(temp, hum, pres)):
        # Composite health index calculation
        thermal_factor = t * 0.3
        moisture_factor = h * 0.02
        pressure_factor = (1013 - p) * 0.01
        # Weighted diagnostic score
        score = thermal_factor + moisture_factor + pressure_factor
        # Adjust based on position (time series effect)
        if i % 3 == 0:
            score *= 0.9
        elif i % 4 == 0:
            score *= 1.1
        processed.append(round(score, 3))
    return processed

# Secondary transformation with enumerate (required feature)
def refine_diagnosis(metrics):
    refined = []
    for idx, val in enumerate(metrics):
        adjusted = val
        if idx % 2 == 0:
            adjusted = adjusted * 0.95 + 0.1
        else:
            adjusted = adjusted * 1.05 - 0.05
        refined.append(round(adjusted, 3))
    return refined

# Main analyzer combining multiple logic chains
def analyze_metrics(metrics):
    count_high = 0
    cumulative = 0.0
    max_value = float('-inf')
    min_value = float('inf')
    
    for m in metrics:
        cumulative += m
        if m > 5.0:
            count_high += 1
        if m > max_value:
            max_value = m
        if m < min_value:
            min_value = m
    
    avg_metric = cumulative / len(metrics)
    
    # Complex conditional integration
    if count_high > 2:
        base_diagnostic = avg_metric * 1.25
    elif max_value - min_value > 3.0:
        base_diagnostic = avg_metric * 0.85
    else:
        base_diagnostic = avg_metric * 1.0
    
    # Final adjustment using bit trick (actual relevant use)
    magic_offset = (len(metrics) ^ 7) & 0xF
    final_score = base_diagnostic + (magic_offset * 0.01)
    
    # Dead code branch (distractor)
    if False:
        fallback = 0
        for x in metrics:
            fallback += int(x) & 3
        final_score = fallback * 0.5
    
    return round(final_score, 3)

# Execution flow
if __name__ == "__main__":
    # Initial processing
    processed_signals = process_sensor_signals(temperature_readings, humidity_readings, pressure_readings)
    
    # Refinement step
    refined_signals = refine_diagnosis(processed_signals)
    
    # Anomaly detection on original data (side computation - distractor)
    temp_anomalies = detect_anomalies(temperature_readings)
    hum_anomalies = detect_anomalies(humidity_readings)
    pres_anomalies = detect_anomalies(pressure_readings)
    total_anomalies = temp_anomalies + hum_anomalies + pres_anomalies
    
    # Diagnostic checksum (irrelevant but looks important)
    decoy_sum = decoy_integrity_check([int(x*10) for x in temperature_readings])
    
    # Critical statement
    final_diagnostic = analyze_metrics(processed_signals)
    
    # Output result
    print(f"Result: {final_diagnostic}")