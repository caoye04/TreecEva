from collections import defaultdict, Counter

# Simulated sensor array data with noise and redundant readings
def collect_sensor_data():
    raw_readings = [
        ("temp", 23.5), ("humid", 45.2), ("temp", 24.1), ("pressure", 1013.25),
        ("humid", 46.0), ("co2", 410), ("temp", 22.8), ("pressure", 1012.9),
        ("co2", 395), ("humid", 44.8), ("temp", 23.0), ("co2", 420),
        ("light", 300), ("light", 310), ("motion", 1), ("motion", 0)
    ]
    return raw_readings

# Irrelevant utility: converts units but not used in main logic
def celsius_to_fahrenheit(c):
    return c * 9/5 + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

# Noise filter based on frequency - only keeps values appearing at least twice
def filter_noisy_data(readings):
    counts = Counter([r[0] for r in readings])
    valid_types = {k for k, v in counts.items() if v >= 2}
    return [r for r in readings if r[0] in valid_types]

# Misleading aggregation: computes averages but returns unused stats
def compute_averages(data):
    aggregates = defaultdict(list)
    for sensor_type, value in data:
        aggregates[sensor_type].append(value)
    
    avg_results = {}
    for stype, vals in aggregates.items():
        avg_results[stype] = sum(vals) / len(vals)
    
    # Dead code path: never used later
    if 'o2' in avg_results:
        scale_adjustment = avg_results['o2'] * 0.02
    else:
        scale_adjustment = 0.0  # Unused
    
    return avg_results  # Not actually used in final computation

# Core transformation: maps each sensor type to a threshold band
def build_threshold_map(base_offset=0.5):
    base_map = {
        'temp': (22.0, 25.0),
        'humid': (40.0, 50.0),
        'pressure': (1010.0, 1020.0),
        'co2': (350, 450)
    }
    
    # Distractor modification
    temp_correction = base_offset * 1.5
    base_map['temp'] = (base_map['temp'][0] - temp_correction, base_map['temp'][1] + temp_correction)
    
    # Fake expansion - adds irrelevant key
    base_map['voc'] = (0, 100)  # Not present in data, misleading
    
    return base_map

# Diagnostic engine: counts how many readings fall outside thresholds
def process_readings(data, thresholds):
    outlier_count = defaultdict(int)
    grouped = defaultdict(list)
    
    # Group by sensor type
    for stype, val in data:
        grouped[stype].append(val)
    
    # Evaluate against thresholds
    for stype, values in grouped.items():
        if stype not in thresholds:
            continue
        low, high = thresholds[stype]
        for v in values:
            if v < low or v > high:
                outlier_count[stype] += 1
    
    # Compute total deviation score
    total_score = 0
    weight_map = {'temp': 3, 'humid': 2, 'pressure': 1, 'co2': 2}
    for stype, count in outlier_count.items():
        if stype in weight_map:
            total_score += count * weight_map[stype]
    
    # Secondary adjustment based on pattern clustering
    cluster_flag = False
    if 'temp' in outlier_count and 'humid' in outlier_count:
        if outlier_count['temp'] >= 2 and outlier_count['humid'] >= 2:
            cluster_flag = True
    
    if cluster_flag:
        total_score += 5  # Bonus penalty for correlated anomalies
    
    # Final diagnostic is total_score modulo a prime to compress range
    final_diagnostic = total_score % 97
    
    # Red herring: this variable looks important but isn't used
    diagnostic_hash = hash((tuple(sorted(outlier_count.items())), total_score)) % 1000
    
    return final_diagnostic

# Unused function that looks relevant
def generate_report_snapshot(data, score):
    timestamp = "2023-12-01T10:00:00Z"
    severity = "LOW" if score < 30 else "MEDIUM" if score < 70 else "HIGH"
    return {"timestamp": timestamp, "score": score, "severity": severity}

# Main execution flow
data_stream = collect_sensor_data()
filtered_data = filter_noisy_data(data_stream)
_ = compute_averages(filtered_data)  # Result discarded
treshold_map = build_threshold_map(base_offset=0.8)  # Typo in var name: treshold
final_diagnostic = process_readings(filtered_data, treshold_map)
print(f"Result: {final_diagnostic}")