from collections import defaultdict, Counter

# Simulated sensor data from multiple environmental monitoring stations
temperature_readings = [23.5, 24.1, 19.8, 25.6, 22.3, 20.9, 26.1, 24.7, 23.0, 21.4]
humidity_readings = [45, 52, 58, 43, 60, 55, 48, 50, 53, 47]
pressure_readings = [1013, 1015, 1012, 1018, 1010, 1014, 1016, 1011, 1017, 1013]

# Irrelevant auxiliary data (distractor)
legacy_codes = ['A7', 'B2', 'C9', 'D4', 'E1', 'F8', 'G3', 'H6', 'I5', 'J0']
station_metadata = {code: {'calibration': idx * 0.03, 'version': 'v2.1'} for idx, code in enumerate(legacy_codes)}

# Misleading transformation (dead path)
def apply_legacy_correction(data, codes):
    result = []
    for i, val in enumerate(data):
        if codes[i][0] in 'CEG':
            result.append(val * 1.02)
        else:
            result.append(val * 0.99)
    return result

corrected_temps = apply_legacy_correction(temperature_readings, legacy_codes)  # Unused

# Core processing pipeline
sorted_indices = sorted(range(len(temperature_readings)), key=lambda i: temperature_readings[i], reverse=True)
sorted_temps = [temperature_readings[i] for i in sorted_indices]
sorted_humidity = [humidity_readings[i] for i in sorted_indices]
sorted_pressure = [pressure_readings[i] for i in sorted_indices]

# Zipping related sensor streams
sensor_bundle = list(zip(sorted_temps, sorted_humidity, sorted_pressure))

# Data aggregation with defaultdict (relevant)
aggregated_by_temp = defaultdict(list)
for temp, hum, pres in sensor_bundle:
    temp_bin = int(temp // 1) * 1
    aggregated_by_temp[temp_bin].append((temp, hum, pres))

# Decoy statistical analysis (irrelevant)
mean_humidity = sum(humidity_readings) / len(humidity_readings)
median_pressure = sorted(pressure_readings)[len(pressure_readings)//2]
mode_temperature = Counter(round(t) for t in temperature_readings).most_common(1)[0]

# Another red herring: spurious correlation check
correlation_proxy = 0
for i in range(len(temperature_readings) - 1):
    if (temperature_readings[i] > temperature_readings[i+1]) == (pressure_readings[i] < pressure_readings[i+1]):
        correlation_proxy += 1

# Real preprocessing: normalize and detect anomalies
def preprocess_sensors(temps, hums, press):
    normalized = []
    for i, t in enumerate(temps):
        norm_val = (t - 20) / 5
        humidity_factor = (hums[i] - 40) / 10
        stability_index = abs(press[i] - 1013) / 5
        score = norm_val * 1.2 - humidity_factor * 0.8 + stability_index * 0.3
        normalized.append(score)
    return normalized

processed_data = preprocess_sensors(sorted_temps, sorted_humidity, sorted_pressure)

# Threshold configuration map (critical)
threshold_map = {
    'warning': 1.5,
    'alert': 2.8,
    'critical': 4.0
}

# False alarm system (distractor)
alarm_patterns = []
for i, val in enumerate(processed_data):
    context_window = processed_data[max(0,i-2):i+3]
    if len(context_window) >= 3 and context_window[0] < val > context_window[-1]:
        alarm_patterns.append(i)

# Actual diagnostic engine with recursion (core logic)
def count_critical_nodes(scores, thresholds, index=0):
    if index >= len(scores):
        return 0
    
    current = scores[index]
    level = 0
    if current >= thresholds['critical']:
        level = 2
    elif current >= thresholds['alert']:
        level = 1
    
    recursive_contribution = count_critical_nodes(scores, thresholds, index + 1)
    
    if level == 2 and index > 0 and scores[index-1] >= thresholds['warning']:
        return recursive_contribution + 3
    elif level == 1:
        return recursive_contribution + 1
    else:
        return recursive_contribution + level

# Secondary analysis (misleading)
event_density = defaultdict(int)
for score in processed_data:
    if score > 1.0:
        event_density[int(score)] += 1

# Final analysis function
def analyze_readings(processed, config):
    base_count = count_critical_nodes(processed, config)
    
    # Spurious adjustment based on empty condition (distractor)
    adjustment = 0
    for k, v in station_metadata.items():  # Uses unrelated metadata
        if 'v3' in v['version']:
            adjustment += 1
    
    # Real adjustment: check consecutive high values
    consecutive_bonus = 0
    streak = 0
    for val in processed:
        if val >= config['warning']:
            streak += 1
            if streak == 3:
                consecutive_bonus += 2
                streak = 0  # Reset after bonus
        else:
            streak = 0
    
    # Another decoy calculation
    entropy_proxy = 0
    for i in range(len(processed)-1):
        diff = abs(processed[i] - processed[i+1])
        if diff > 0.5:
            entropy_proxy += 1

    final_score = base_count * 7 + consecutive_bonus - adjustment
    return final_score

# Execute critical statement
final_diagnostic = analyze_readings(processed_data, threshold_map)
print(f"Target result: {final_diagnostic}")