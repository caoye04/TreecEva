import math

def sensor_calibrate(raw):
    return [(x * 1.05) + 2.1 for x in raw if x > 0]

def noise_filter(data):
    filtered = []
    for i in range(len(data)):
        if i == 0 or i == len(data)-1:
            continue
        prev, curr, next_val = data[i-1], data[i], data[i+1]
        if (curr - prev) > 5 and (next_val - curr) > 5:
            continue  # spike detected
        filtered.append(curr)
    return filtered

def compute_entropy(values):
    total = sum(values)
    probs = [(v / total) for v in values if v > 0]
    entropy = -sum(p * math.log(p) for p in probs if p > 0)
    return round(entropy, 4)

def rolling_average(series, window=3):
    if len(series) < window:
        return [0]
    avgs = []
    for i in range(len(series) - window + 1):
        avgs.append(sum(series[i:i+window]) / window)
    return avgs

def assess_stability(metric):
    base = metric * 0.87
    adjustment = 1.5 if metric > 10 else 0.7
    return base * adjustment

def analyze_readings(readings, limit):
    valid_readings = [r for r in readings if r < limit]
    if not valid_readings:
        return 0
    
    # Distractor: complex transformation with no impact on final result
    dummy_transform = [math.sin(x) * math.cos(x) for x in valid_readings]
    dummy_score = sum(math.exp(-x) for x in dummy_transform[:3]) if len(dummy_transform) >= 3 else 0.0
    
    # Real logic begins
    squared_devs = [(x - sum(valid_readings)/len(valid_readings))**2 for x in valid_readings]
    variance = sum(squared_devs) / len(squared_devs)
    std_dev = math.sqrt(variance)
    
    # Critical conditional expression
    trend = 'stable' if std_dev < 5 else 'volatile'
    
    # Another distractor function call with side effect that doesn't affect output
    def decoy_maintenance(log_entries):
        count = 0
        for entry in log_entries:
            if 'ERROR' in entry:
                count += 1
        return count * 0.1
    
    logs = ['OK: system nominal', 'WARN: fluctuation', 'OK: normal']
    penalty = decoy_maintenance(logs)
    
    # Key calculation
    magnitude = sum(abs(x) for x in valid_readings)
    weight = 0.3 if trend == 'volatile' else 0.6
    
    # Final diagnostic score
    score_component_1 = magnitude * weight
    score_component_2 = std_dev * 2.1
    final_score = score_component_1 + score_component_2 - penalty  # penalty negligible
    
    # Red herring: unused complex structure
    diagnostics_report = {
        'raw_count': len(readings),
        'filtered_count': len(valid_readings),
        'entropy': compute_entropy(valid_readings),
        'rolling_metrics': rolling_average(valid_readings),
        'stability_index': assess_stability(std_dev),
        'dummy_diagnostic': dummy_score,
        'anomaly_flags': [i for i, x in enumerate(valid_readings) if x > limit * 0.9]
    }
    
    # This is the actual answer variable
    final_diagnostic = int(round(final_score))
    return final_diagnostic

# Simulated sensor input (irrelevant details added)
baseline_readings = [12.1, 8.4, 15.6, 7.2, 9.8, 11.0, 13.4, 6.7, 10.3, 14.2]
dummy_offset = 3.14
offset_applied = [x + dummy_offset for x in baseline_readings]

# Actual processing pipeline
initial_calibration = sensor_calibrate(offset_applied)
processed_data = noise_filter(initial_calibration)

# Threshold used in analysis
threshold = 18.5

# Execution point of interest
final_diagnostic = analyze_readings(processed_data, threshold)

# Output result as required
print(f"Result: {final_diagnostic}")