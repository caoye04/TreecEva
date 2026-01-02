from collections import defaultdict, Counter
import math

# Simulated sensor network data with metadata
def fetch_sensor_network():
    return [
        {'id': 'S1', 'type': 'temp', 'values': [23.5, 24.1, 22.9, 25.0, 23.8], 'active': True},
        {'id': 'S2', 'type': 'humid', 'values': [45.2, 47.8, 46.1, 44.9], 'active': True},
        {'id': 'S3', 'type': 'temp', 'values': [19.3, 20.1, 18.9, 21.2], 'active': False},
        {'id': 'S4', 'type': 'pressure', 'values': [1013, 1015, 1012, 1014], 'active': True},
        {'id': 'S5', 'type': 'temp', 'values': [26.7, 27.3, 25.9, 28.1], 'active': True}
    ]

# Legacy function - unused but looks important
def legacy_calibrate(data):
    adjusted = []
    for d in data:
        if d['type'] == 'temp':
            adjusted.append([v * 0.98 + 0.5 for v in d['values']])
    return adjusted

# Irrelevant transformation chain
def transform_sequence(seq):
    if not seq:
        return []
    result = [seq[0]]
    for i in range(1, len(seq)):
        result.append(result[-1] + seq[i] * 0.1)
    smoothed = list(map(lambda x: round(x, 2), result))
    return smoothed[::-1]

# Decoy statistical function
def compute_skewness(data):
    n = len(data)
    if n < 3: return 0.0
    mean_val = sum(data) / n
    variance = sum((x - mean_val) ** 2 for x in data) / n
    std_dev = math.sqrt(variance)
    if std_dev == 0: return 0.0
    skew = sum(((x - mean_val) / std_dev) ** 3 for x in data) / n
    return round(skew, 4)

# Real processing begins here
def extract_readings(sensors):
    readings = defaultdict(list)
    for sensor in sensors:
        if sensor['active'] and sensor['type'] == 'temp':
            readings[sensor['id']].extend(sensor['values'])
    return readings

# Secondary filter based on operational thresholds
def apply_threshold_filter(raw_readings):
    limits = {'low': 20.0, 'high': 27.0}
    filtered = {}
    stats_summary = {}  # distractor: collected but unused later
    
    for sid, values in raw_readings.items():
        valid = [v for v in values if limits['low'] <= v <= limits['high']]
        if valid:
            filtered[sid] = valid
            # Dead computation - looks diagnostic but unused
            avg = sum(valid) / len(valid)
            deviance = sum(abs(v - avg) for v in valid)
            stats_summary[sid] = {'mean': avg, 'deviance': deviance}
    
    # More red herring: transform unrelated data
    dummy_seq = [1, 2, 3, 5, 8, 13]
    transformed = transform_sequence(dummy_seq)
    if len(transformed) > 3:
        offset = transformed[0] * 0.05
        # This block does nothing meaningful
        for k in stats_summary:
            stats_summary[k]['mean'] += offset

    return filtered

# Core logic masked by abstraction
def generate_threshold_map(readings_dict):
    base_map = defaultdict(lambda: 0.5)
    total_sensors = len(readings_dict)
    total_points = sum(len(vals) for vals in readings_dict.values())
    
    # Complex-looking but actually simple derivation
    if total_points > 0:
        ratio = total_sensors / (total_points * 0.01 + 1e-8)
        adjustment = math.log(1 + ratio * 100)
        base_map['adjustment_factor'] = round(adjustment, 3)
    
    # Add decoy entries that look functional
    base_map['calibration_needed'] = False
    base_map['legacy_mode'] = None
    
    return base_map

# Actual critical processing function
def process_readings(data, config):
    aggregate = []
    for values in data.values():
        # Only this computation matters
        cleaned = [v for v in values if v >= 22.0]  # additional filter
        if cleaned:
            product = 1
            for val in cleaned:
                product *= int(val)  # truncate to int and multiply
            aggregate.append(product)
    
    # Final result derived from multiplicative chain
    final_diagnostic = sum(aggregate)
    
    # Distractor: complex set operation that doesn't affect output
    all_keys = set(data.keys())
    reference_set = {'S1', 'S5', 'S9'}
    intersection_size = len(all_keys & reference_set)
    dummy_correction = intersection_size * 1000
    
    # This would mislead if used, but it's not
    # final_diagnostic += dummy_correction  # commented out dead path
    
    return final_diagnostic

# --- Execution Sequence ---
if __name__ == "__main__":
    network_data = fetch_sensor_network()
    
    # Step 1: Extract temperature sensors
    raw_temp_data = extract_readings(network_data)
    
    # Step 2: Apply operational range filter
    filtered_data = apply_threshold_filter(raw_temp_data)
    
    # Step 3: Generate configuration map (contains red herrings)
    threshold_map = generate_threshold_map(filtered_data)
    
    # Step 4: Critical computation point
    final_diagnostic = process_readings(filtered_data, threshold_map)
    
    # Output the target result
    print(f"Result: {final_diagnostic}")