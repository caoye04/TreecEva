from collections import defaultdict
from itertools import cycle

# Simulated sensor data with multiple channels
def get_sensor_data():
    return [
        {'temp': 72.5, 'pressure': 30.1, 'humidity': 45, 'vibration': 0.23},
        {'temp': 73.1, 'pressure': 29.9, 'humidity': 47, 'vibration': 0.25},
        {'temp': 71.8, 'pressure': 30.2, 'humidity': 44, 'vibration': 0.21},
        {'temp': 74.0, 'pressure': 29.8, 'humidity': 48, 'vibration': 0.27},
        {'temp': 72.9, 'pressure': 30.0, 'humidity': 46, 'vibration': 0.24}
    ]

# Irrelevant helper - used to mislead about data source
def generate_mock_labels(n):
    labels = []
    for i in range(n):
        if i % 3 == 0:
            labels.append(f"SYS_ERR_{i}")
        else:
            labels.append(f"OK_{i}")
    return labels

# Unused but plausible transformation (dead code path)
def transform_coordinates(data_list):
    transformed = []
    for entry in data_list:
        x = entry['temp'] * 0.5 + entry['pressure'] * 2
        y = entry['humidity'] * 1.5 - entry['vibration'] * 100
        z = (x + y) / 2
        transformed.append({'x': x, 'y': y, 'z': z})
    return transformed  # Never actually used

# Decoy function that looks important but isn't called in main logic
def compute_reliability_score(records):
    score = 0
    for r in records:
        if r['temp'] > 72:
            score += 10
        if r['pressure'] < 30.0:
            score -= 5
        score = max(0, min(score, 100))
    return score

# Real processing function with distractors embedded
def analyze_variance(readings, key='temp'):
    values = [r[key] for r in readings]
    mean = sum(values) / len(values)
    variance = sum((x - mean) ** 2 for x in values) / len(values)
    return variance

# Main logic disguised among distractions
def detect_anomalies(data, threshold_map):
    anomalies = defaultdict(int)
    temp_vals = [d['temp'] for d in data]
    pressure_vals = [d['pressure'] for d in data]
    
    # Real logic: count how many exceed dynamic thresholds
    for reading in data:
        if reading['temp'] > threshold_map['temp_hi']:
            anomalies['overheat'] += 1
        if reading['temp'] < threshold_map['temp_lo']:
            anomalies['chill'] += 1
        if reading['pressure'] < threshold_map['pressure_lo']:
            anomalies['low_pressure'] += 1
        # This condition is never true due to data range - red herring
        if reading['vibration'] > threshold_map.get('vibe_fail', 0.99):
            anomalies['vibration_fault'] += 1
    
    return dict(anomalies)

# Central processing with misleading intermediate steps
def process_readings(sensor_data, thresholds):
    # Step 1: Extract baseline stats (some used, some not)
    temp_mean = sum(d['temp'] for d in sensor_data) / len(sensor_data)
    pressure_mean = sum(d['pressure'] for d in sensor_data) / len(sensor_data)
    humidity_vals = [d['humidity'] for d in sensor_data]
    
    # Irrelevant sorting - looks like it matters
    sorted_humidity = sorted(humidity_vals, reverse=True)
    
    # Compute variance (only temp variance is later used)
    temp_variance = analyze_variance(sensor_data, 'temp')
    pressure_variance = analyze_variance(sensor_data, 'pressure')  # Computed but unused
    
    # Detect anomalies - this contributes to final result
    anomaly_report = detect_anomalies(sensor_data, thresholds)
    overheat_count = anomaly_report.get('overheat', 0)
    low_pressure_count = anomaly_report.get('low_pressure', 0)
    
    # Fake normalization attempt (distractor)
    normalization_factor = max(temp_mean, 1.0)
    normalized_temp = temp_mean / normalization_factor  # Always ~1.0, irrelevant
    
    # Core calculation chain (8+ logic steps)
    base_score = 100
    base_score -= overheat_count * 8
    base_score -= low_pressure_count * 12
    
    # Only significant variance impacts score
    if temp_variance > 0.4:
        base_score -= 15
    
    # Additional penalty based on pattern cycling (itertools usage)
    pattern_cycle = cycle([1, -1, 0])
    adjustment = 0
    for i, val in enumerate(humidity_vals):
        if i >= 3: break
        adjustment += next(pattern_cycle) * (val % 5)
    
    base_score += adjustment  # Small influence
    
    # Final mapping through dictionary lookup (dict op)
    rating_map = {k: v for k, v in enumerate(['FATAL', 'CRIT', 'LOW', 'MOD', 'HIGH', 'OPTIMAL'])}
    diagnostic_code = max(0, min(base_score // 20, 5))
    final_diagnostic = base_score + (50 if rating_map[diagnostic_code] == 'OPTIMAL' else -10)
    
    # Dead assignment - looks like it does something
    final_diagnostic = final_diagnostic or -999
    
    return final_diagnostic

# Main execution block
if __name__ == "__main__":
    # Initialize real parameters
    sensor_data = get_sensor_data()
    thresholds = {
        'temp_hi': 72.7,
        'temp_lo': 71.0,
        'pressure_lo': 30.0,
        'vibe_fail': 0.99  # Deliberately unreachable
    }
    
    # Generate unused labels (distraction)
    labels = generate_mock_labels(len(sensor_data))
    
    # Transform unused coordinates (red herring computation)
    ghost_data = transform_coordinates(sensor_data)
    
    # Compute decoy reliability (never used)
    fake_score = compute_reliability_score(sensor_data)
    
    # Actual critical statement
    final_diagnostic = process_readings(sensor_data, thresholds)
    
    # Output result as required
    print(f"Result: {final_diagnostic}")