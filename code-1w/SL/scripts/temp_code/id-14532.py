def analyze_readings(readings):
    # Irrelevant transformation: normalize values (not used in final path)
    normalized = [round((x - min(readings)) / (max(readings) - min(readings)) * 100) for x in readings]
    
    # Distractor: statistical decoy
    mean_val = sum(readings) / len(readings)
    variance = sum((x - mean_val) ** 2 for x in readings) / len(readings)
    z_scores = [abs((x - mean_val) / (variance ** 0.5)) for x in readings]

    # Relevant logic: count outliers beyond 30
    outliers = [x for x in readings if x > 30]
    return len(outliers)


def encode_state(device_id, status_flags):
    # Complex bit manipulation red herring
    encoded = device_id << 4
    for i, flag in enumerate(status_flags):
        if flag:
            encoded |= (1 << i)
    # This function is never called; dead code path
    return encoded

# Unused data structures for distraction
system_logs = {
    'errors': [101, 203, 404],
    'timestamps': [1718923400, 1718923460, 1718923520],
    'resolved': [False, True, False]
}

# Decoy function with misleading name
def compute_stability_index(data):
    sorted_data = sorted(data, reverse=True)
    index = 0
    for i in range(len(sorted_data) - 1):
        if sorted_data[i] - sorted_data[i+1] > 5:
            index += 10
    return index * 1.5  # Never used

# Real processing chain begins
sensor_input = [12, 15, 33, 45, 8, 22, 51]

# Conditional expression distractor
mode_flag = 'high_res' if len(sensor_input) > 5 else 'low_res'
buffer_size = 256 if mode_flag == 'high_res' else 128

# Dictionary of thresholds (partially relevant)
threshold_map = {
    'critical': 50,
    'warning': 30,
    'info': 10,
    'debug': 0
}

# Health data contains multiple fields, only one is used
health_data = {
    'readings': sensor_input,
    'location_id': 4056,
    'version': '2.3.1',
    'calibration': [0.98, 1.02, 1.01],
    'anomalies_detected': analyze_readings(sensor_input),  # Calls function but result not directly used
    'timestamp_valid': True
}

# Sorting decoy
sorted_keys = sorted(threshold_map.keys(), key=lambda x: len(x))

# Multi-step data transformation with irrelevant branches
intermediate_scores = {}
for k, v in threshold_map.items():
    if v > 0:  # Skip debug
        count_above = len([x for x in health_data['readings'] if x > v])
        intermediate_scores[k] = count_above * v

# Dead code block — looks important but unused
if intermediate_scores.get('warning') > 10:
    adjustment_factor = 0.85
else:
    adjustment_factor = 1.15

# Core logic hidden among distractions
def process_metrics(data, thresholds):
    raw_readings = data['readings']
    warn_level = thresholds['warning']
    crit_level = thresholds['critical']
    
    # Real computation buried here
    above_warning = [x for x in raw_readings if x > warn_level]
    above_critical = [x for x in raw_readings if x > crit_level]
    
    # Key calculation step
    base_score = len(above_warning) * 17
    penalty = len(above_critical) * 5
    
    # Final diagnostic uses only this value
    result = base_score - penalty + 2  # +2 offset for calibration
    
    # More distractions inside function
    diagnostics_log = {
        'entries': [],
        'status': 'processed'
    }
    for val in raw_readings:
        severity = 'crit' if val > crit_level else 'warn' if val > warn_level else 'normal'
        diagnostics_log['entries'].append(severity)
    
    return result

# Execution point of interest
final_diagnostic = process_metrics(health_data, threshold_map)

# Print required output
print(f"Result: {final_diagnostic}")