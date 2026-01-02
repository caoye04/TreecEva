import itertools

# Simulated system metrics from sensor array
temperature_readings = [23.5, 24.1, 22.8, 25.0, 23.9]
humidity_readings = [45, 50, 52, 48, 60]
pressure_readings = [1013, 1015, 1012, 1010, 1014]

# Irrelevant backup data (distractor)
backup_temps = temperature_readings[::-1]
backup_humidity = [x * 1.02 for x in humidity_readings]

# Noise filter function (partially relevant but not used directly)
def apply_noise_filter(data, threshold=0.5):
    return [x for x in data if abs(x - sum(data)/len(data)) < threshold]

# Core processing functions
def normalize(data):
    min_val, max_val = min(data), max(data)
    if max_val == min_val:
        return [0.5 for _ in data]
    return [(x - min_val) / (max_val - min_val) for x in data]

def moving_average(data, window=2):
    if len(data) < window:
        return data
    return [sum(data[i:i+window]) / window for i in range(len(data)-window+1)]

def extract_trends(series):
    return [1 if series[i] > series[i-1] else 0 for i in range(1, len(series))]

# Advanced transformation chain
norm_temp = normalize(temperature_readings)
norm_humid = normalize(humidity_readings)
smoothed_pressure = moving_average(pressure_readings, 2)

temp_trend = extract_trends(norm_temp)
humid_trend = extract_trends(norm_humid)

# Dummy transformations for distraction
decoy_metrics = {"flux": sum(smoothed_pressure) % 7,
                 "drift": len(temp_trend) * 0.33,
                 "bias": (max(norm_temp) - min(norm_temp)) * 100}

# Real-time anomaly detection (unused path - red herring)
def detect_anomalies(data_stream, sensitivity=2):
    avg = sum(data_stream) / len(data_stream)
    std_dev = (sum((x - avg)**2 for x in data_stream) / len(data_stream)) ** 0.5
    return [i for i, x in enumerate(data_stream) if abs(x - avg) > sensitivity * std_dev]

anomalies = detect_anomalies(temperature_readings)  # Dead code path

# Data fusion engine
fusion_map = {}
for i, combo in enumerate(itertools.product([0, 1], repeat=2)):
    key = f"state_{i}"
    fusion_map[key] = {
        'temp_dir': combo[0],
        'humid_dir': combo[1],
        'weight': (combo[0] + 1) * (combo[1] + 2)
    }

# Weight adjustment logic
base_weights = {'thermal': 0.4, 'moisture': 0.35, 'barometric': 0.25}

# Misleading weight modification (not actually applied)
adjusted_weights = {k: v * 1.1 if k != 'barometric' else v * 0.9 for k, v in base_weights.items()}

# Critical performance evaluation
metrics = {
    'thermal_stability': 1 - abs(norm_temp[-1] - norm_temp[0]),
    'humidity_consistency': 1 - (sum(humid_trend) / len(humid_trend) * 0.5),
    'pressure_trend': abs(smoothed_pressure[-1] - smoothed_pressure[0]) / 100
}

# Unused metric manipulation (distractor)
transformed = list(map(lambda x: round(x * 100), metrics.values()))
filtered_items = list(filter(lambda item: item[1] > 0.2, metrics.items()))

weights = base_weights.copy()  # Use original weights, not adjusted

# String-based switch for mode selection (irrelevant but plausible)
system_mode = "performance_audit"
mode_flag = system_mode.split('_')[-1] == 'audit'

# Final scoring with dictionary-based weight mapping
def evaluate_performance(metrs, wts):
    if not mode_flag:
        return -1  # Dead branch
    
    score = 0.0
    # Map string keys to actual values
    mapping = {
        'thermal': metrs['thermal_stability'],
        'moisture': metrs['humidity_consistency'],
        'barometric': metrs['pressure_trend']
    }
    
    for key in wts:
        contribution = mapping[key] * wts[key]
        score += contribution
    
    # Apply trend correction only if trends are stable
    stability_check = all(t == 0 for t in temp_trend[-2:])
    if stability_check:
        score *= 1.1
    else:
        score *= 0.95
    
    # Additional bonus condition (never met due to data)
    if len(anomalies) == 0 and 'critical' in fusion_map['state_0']:
        score += 0.2
    
    return round(score * 1000)  # Scale up for integer output

final_score = evaluate_performance(metrics, weights)
print(f"Result: {final_score}")