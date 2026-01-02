from collections import defaultdict, Counter
from itertools import combinations

# Simulated sensor network data with diagnostic flags
def collect_sensor_data():
    raw_readings = [
        (101, 23.5, 'OK'), (102, 24.1, 'OK'), (103, -999, 'ERR'),
        (104, 25.3, 'OK'), (105, 22.8, 'OK'), (106, -999, 'ERR'),
        (107, 26.0, 'OK'), (108, 24.7, 'OK')
    ]
    # Irrelevant transformation: group by status (not used in final path)
    grouped = defaultdict(list)
    for sid, val, stat in raw_readings:
        grouped[stat].append((sid, val))
    
    # Critical data structure: map sensor ID to value
    sensor_map = {sid: val for sid, val, _ in raw_readings}
    return sensor_map

# Legacy function – dead code path (not actually called)
def legacy_calibrate(x):
    return x * 0.98 + 2.1

# Unused helper for potential future expansion
def compute_variance(data_list):
    mean = sum(data_list) / len(data_list)
    return sum((x - mean) ** 2 for x in data_list) / len(data_list)

# Misleading intermediate processing with decoy logic
def enhance_readings(data_dict):
    enhanced = {}
    shift_key = 0
    for sensor_id, value in data_dict.items():
        if value < 0:
            # Placeholder for error correction (never triggered due to prior filtering)
            enhanced[sensor_id] = 0
        else:
            # Apply arbitrary bit manipulation (XOR with fixed pattern)
            noise_offset = (sensor_id ^ 255) & 7  # Red herring
            enhanced[sensor_id] = value + (noise_offset * 0.01)
            shift_key ^= int(value)
    # shift_key returned but not used anywhere
    return enhanced

# Core filtering logic: remove invalid readings
def filter_anomalies(raw_values):
    valid_readings = []
    anomaly_log = []  # Collected but unused
    for vid, vval in raw_values.items():
        if vval > 0:  # Only valid physical measurements
            valid_readings.append(vval)
        else:
            anomaly_log.append(vid)
    # Sort for deterministic processing
    valid_readings.sort()
    return valid_readings

# Primary processing with multiple concepts
def process_readings(readings_list):
    # Use of Counter to count binned values (partially relevant)
    bins = Counter(int(r // 1) for r in readings_list)
    
    # Detect repeating magnitude classes
    mode_bin = bins.most_common(1)[0][0]
    
    # Compute weighted influence using adjacent bin interactions
    influence_score = 0
    for b, cnt in bins.items():
        if abs(b - mode_bin) <= 1:
            influence_score += cnt * (1.0 - 0.1 * abs(b - mode_bin))
    
    # Real computation path: use itertools to find critical pair
    critical_pair = None
    for a, b in combinations(readings_list, 2):
        if abs(a - b) > 2.0:  # Significant deviation
            critical_pair = (a, b)
            break
    
    # Final diagnostic based on first significant deviation
    if critical_pair:
        base_metric = critical_pair[0] * 0.7 + critical_pair[1] * 0.3
    else:
        base_metric = readings_list[0]
    
    # Incorporate set operations for overlap analysis (distractor)
    high_set = {x for x in readings_list if x > 25.0}
    low_set = {x for x in readings_list if x < 24.0}
    overlap = high_set & low_set  # Always empty - misleading
    set_penalty = len(overlap) * 100  # Always zero
    
    # Final result influenced only by base_metric and mode_bin
    final_score = base_metric * 10 + mode_bin
    return int(final_score)

# Main execution flow
collected_data = collect_sensor_data()

# Dead code assignment - no effect
enhanced_data = enhance_readings(collected_data)

# Key statement where answer is determined
final_diagnostic = process_readings(filter_anomalies(collected_data))

print(f"Result: {final_diagnostic}")