import math

# Simulated sensor fusion system for environmental monitoring

def collect_samples():
    raw = [14.7, 18.3, 15.1, 19.8, 13.6, 16.9, 17.2, 15.5]
    offset = 0.3
    calibrated = [x + offset for x in raw]
    return calibrated

# Irrelevant helper - distractor
def smooth_signal(data):
    smoothed = [data[0]]
    for i in range(1, len(data) - 1):
        avg = (data[i-1] + data[i] + data[i+1]) / 3
        smoothed.append(avg)
    smoothed.append(data[-1])
    return smoothed

# Unused transformation - red herring
def frequency_transform(seq):
    transformed = []
    for i, val in enumerate(seq):
        transformed.append(val * math.sin(i * 0.5))
    return transformed

# Decoy analysis function - dead path
def legacy_evaluation(stream):
    total_power = sum([x**2 for x in stream])
    return total_power > 1000

# Real processing pipeline

def filter_outliers(data, limit=1.5):
    mean_val = sum(data) / len(data)
    variance = sum((x - mean_val) ** 2 for x in data) / len(data)
    std_dev = math.sqrt(variance)
    return [x for x in data if abs(x - mean_val) <= limit * std_dev], mean_val

def categorize_level(value, thresholds):
    if value < thresholds['low']:
        return 'LOW'
    elif value < thresholds['moderate']:
        return 'MODERATE'
    elif value < thresholds['high']:
        return 'HIGH'
    else:
        return 'CRITICAL'

# String-based status mapping - uses string methods
status_codes = {
    'LOW': 'OK'.lower(),
    'MODERATE': 'watch'.upper(),
    'HIGH': 'alert'.strip(),
    'CRITICAL': 'ALERT'.casefold()
}

# Set operations to track active zones - relevant use
active_zones = {'north', 'south', 'east'}
deprecated_zones = {'west', 'south'}
current_monitoring = active_zones - deprecated_zones  # Only north, east

# Threshold configuration map - critical dictionary
threshold_map = {
    'low': 14.0,
    'moderate': 16.0,
    'high': 18.0,
    'critical': 19.5
}

# Secondary derived map - partially irrelevant
risk_weights = {
    'LOW': 1,
    'MODERATE': 2,
    'HIGH': 3,
    'CRITICAL': 4
}

# Data processor with tuple unpacking and conditional expression

def process_entry(value, base_ref):
    deviation = abs(value - base_ref)
    severity = 'HIGH' if deviation > 2.0 else ('MODERATE' if deviation > 1.0 else 'LOW')
    code = status_codes.get(severity, 'UNKNOWN')
    return (value, severity, code)  # returns tuple

def analyze_readings(data_list, config):
    results = []
    base_estimate = sum(data_list) / len(data_list)
    
    for val in data_list:
        entry = process_entry(val, base_estimate)
        results.append(entry)
    
    # Extract only severity levels using list comprehension
    severities = [r[1] for r in results]
    
    # Count occurrences using dictionary
    counts = {}
    for s in severities:
        counts[s] = counts.get(s, 0) + 1
    
    # Determine dominant category
    max_count = 0
    dominant = 'LOW'
    for cat, cnt in counts.items():
        if cnt > max_count:
            max_count = cnt
            dominant = cat
    
    # Compute composite risk score - actual answer source
    score_components = []
    for reading in data_list:
        if reading >= config['moderate']:
            penalty = (reading - config['low']) ** 1.8
            score_components.append(penalty)
    
    raw_score = sum(score_components)
    adjustment_factor = len(current_monitoring)  # depends on set operation result
    final_score = raw_score * (adjustment_factor / 2.0) if adjustment_factor > 0 else raw_score
    
    # Final diagnostic is floor of adjusted score
    final_diagnostic = int(math.floor(final_score))
    
    # Dead code branch - misleading
    if final_diagnostic < 0:
        fallback = 0
        for z in deprecated_zones:
            fallback += ord(z[0])
        final_diagnostic = fallback
    
    return final_diagnostic

# --- Execution Flow ---
raw_sensor_data = collect_samples()
filtered_data, center_ref = filter_outliers(raw_sensor_data)
processed_data = [x for x in filtered_data if x > 12.0]  # trivial filter

# Unused variables - distractions
transformed_stream = frequency_transform(filtered_data)
dummy_analysis = legacy_evaluation(transformed_stream)
smudged = smooth_signal(processed_data)

# Critical execution point
final_diagnostic = analyze_readings(processed_data, threshold_map)

# Irrelevant aggregation
summary_tuple = (len(processed_data), center_ref, final_diagnostic)
extra_flag = 'north' in current_monitoring and 'CRITICAL' in status_codes.values()

# Output required result
print(f"Result: {final_diagnostic}")