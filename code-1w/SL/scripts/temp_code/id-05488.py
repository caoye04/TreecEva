from collections import defaultdict, Counter

# Simulate sensor data analysis for system health monitoring
def analyze_sensor_readings(readings):
    counts = defaultdict(int)
    anomalies = []
    total = 0
    valid_count = 0

    for reading in readings:
        category = reading['type']
        value = reading['value']
        counts[category] += 1
        total += value

        # Irrelevant filtering (distractor)
        if value < 0:
            anomalies.append(value)

        # Actual logic: count only valid high-frequency signals
        if category == 'HF' and value > 50:
            valid_count += 1

    avg = total / len(readings) if readings else 0
    return counts, avg, valid_count

# Process performance with redundant steps
def compute_efficiency(data_map):
    efficiency = 1.0
    debug_log = []
    temp_vals = []

    for key, values in data_map.items():
        mean = sum(values) / len(values)
        adjusted = mean * 0.9 + 10
        temp_vals.append(adjusted)

        # Dead code path - never used later
        if adjusted < 20:
            debug_log.append(f'Low efficiency in {key}')

    # Complex but irrelevant aggregation
    hist = Counter(temp_vals)
    peak = max(hist.keys()) if hist else 0

    # Real computation buried here
    efficiency = round(sum(temp_vals) / len(temp_vals), 2) if temp_vals else 1.0
    return efficiency

# Main processing with mixed concepts
def process_performance(metrics, threshold):
    raw_data = metrics['readings']
    config = metrics['config']
    
    # Step 1: Analyze sensor readings (returns multiple values)
    type_counts, average_val, hf_valid = analyze_sensor_readings(raw_data)
    
    # Step 2: Prepare grouped data for efficiency calculation
    grouped = defaultdict(list)
    for item in raw_data:
        grouped[item['source']].append(item['value'])
    
    # Step 3: Compute base efficiency
    base_eff = compute_efficiency(grouped)
    
    # Step 4: Apply calibration (intermediate distractor variables)
    calibration_factor = 0.0
    if config['mode'] == 'calibrated':
        spread = max(type_counts.values()) - min(type_counts.values()) if type_counts else 0
        adjustment = spread * 0.05
        calibration_factor = adjustment  # Not actually impactful
    
    # Step 5: Determine multiplier based on HF signal validity
    multiplier = 1.0
    if hf_valid > threshold:
        multiplier = 1.25
    else:
        multiplier = 0.85
    
    # Step 6: Combine results (core answer logic)
    preliminary = int(base_eff * 100)  # Convert to integer scale
    scaled = preliminary * multiplier
    
    # Step 7: Final adjustment using average (only part influences result)
    final_score = int(scaled + (average_val // 10))
    
    # Irrelevant trailing operations
    outlier_report = [v for v in grouped['sensor_a'] if v > 100]
    summary_stats = {'size': len(outlier_report), 'flagged': False}
    
    return final_score

# Input data construction
sensor_inputs = [
    {'type': 'HF', 'value': 65, 'source': 'sensor_a'},
    {'type': 'LF', 'value': 30, 'source': 'sensor_b'},
    {'type': 'HF', 'value': 70, 'source': 'sensor_a'},
    {'type': 'MF', 'value': 45, 'source': 'sensor_c'},
    {'type': 'HF', 'value': 55, 'source': 'sensor_b'},
    {'type': 'HF', 'value': 80, 'source': 'sensor_a'},
    {'type': 'LF', 'value': 25, 'source': 'sensor_c'},
]

params = {
    'readings': sensor_inputs,
    'config': {'mode': 'calibrated'}
}

threshold = 2
final_score = process_performance(params, threshold)
print(f"Target result: {final_score}")