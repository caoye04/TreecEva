def analyze_pattern(sequence):
    # Irrelevant helper function (dead code path)
    return sum(x ** 2 for x in sequence if x % 3 == 0)

threshold_map = {'t1': 35, 't2': 70, 't3': 90}
sensor_ids = ['S101', 'S102', 'S103', 'S104']
timestamps = [1623456000, 1623456060, 1623456120, 1623456180]

# Distractor: unused sensor calibration data
calibration_matrix = [
    [1.02, 0.98, 1.01],
    [0.99, 1.03, 1.00],
    [1.01, 1.00, 0.99]
]

dummy_stats = {
    'mean_offset': 0.05,
    'variance_floor': 0.001,
    'peak_distortion': 0.12
}

# Real input data
sensor_data = [
    {'id': 'S101', 'values': [20, 38, 45, 68, 72], 'active': True},
    {'id': 'S102', 'values': [10, 75, 88, 62, 95], 'active': True},
    {'id': 'S103', 'values': [5, 40, 55, 60, 58], 'active': False},  # Inactive sensor
    {'id': 'S104', 'values': [30, 42, 50, 71, 80], 'active': True}
]

# Misleading intermediate processing
def apply_filter(data):
    return [x for x in data if x > 25]

# Unused transformation chain
transform_chain = lambda x: x.replace('S', 'X').upper() if 'S' in x else x
mapped_names = [transform_chain(sid) for sid in sensor_ids]

# String distractors
diagnostic_log = "ERROR: Calibration failed on S305|WARN: Low signal on S103|INFO: Normal operation"
log_entries = diagnostic_log.split('|')
filtered_logs = [entry for entry in log_entries if 'S101' in entry or 'CRITICAL' in entry]

# Core logic disguised among noise
def compute_score(vals, thresh):
    count = 0
    for v in vals:
        if v > thresh:
            count += 1
            if count >= 3:
                break
    return count

# Auxiliary function with red herring parameters
def evaluate_stability(readings, min_duration=5, tolerance=0.05):
    return len(readings) >= min_duration and tolerance < 0.1

# Main processing function
def process_readings(sensors, limits):
    results = []
    temp_cache = {}
    
    for idx, sensor in enumerate(sensors):
        if not sensor['active']:
            continue
            
        readings = sensor['values']
        stable = evaluate_stability(readings)
        high_count = compute_score(readings, limits['t2'])  # Use t2 = 70
        
        # Simulate some string-based tagging
        tags = []
        for i, val in enumerate(readings):
            if val > 70:
                tags.append(f"high@{i}")
        tag_summary = ','.join(tags) if tags else 'none'
        
        # Only sensors with at least 3 values above 70 contribute
        if high_count >= 3:
            key_id = sensor['id']
            # Extract position using enumerate and zip (required feature)
            for pos, (sid, ts) in enumerate(zip(sensor_ids, timestamps)):
                if sid == key_id:
                    base_score = pos * 100 + len(tag_summary.split(','))
                    temp_cache[key_id] = base_score
    
    # Final aggregation from cache
    total = 0
    for k, v in temp_cache.items():
        if 'S102' in k:
            total += v * 2
        else:
            total += v
    
    # Decoy calculation with no effect
    avg_timestamp = sum(timestamps) / len(timestamps) if timestamps else 0
    
    return int(total) if temp_cache else -1

# Execution point of interest
final_diagnostic = process_readings(sensor_data, threshold_map)
Result: final_diagnostic