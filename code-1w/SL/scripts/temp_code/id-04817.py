from collections import defaultdict, Counter
from itertools import zip_longest

# Simulated telemetry data from a distributed sensor network
telemetry_stream = [
    (1001, [23.4, 25.1, 24.8, 0.0, 26.3]),
    (1002, [18.9, 19.5, 0.0, 20.1, 18.7]),
    (1003, [30.2, 0.0, 31.5, 32.0, 30.8]),
    (1004, [15.6, 16.0, 15.8, 0.0, 16.2])
]

# System state flags
system_state = {
    'active_nodes': 12,
    'core_temperature': 67.3,
    'voltage_stability': 0.94,
    'last_reboot': '2023-07-15',
    'firmware_version': '2.1.8'
}

# Irrelevant calibration table (distractor)
calibration_map = {
    'gain': [1.02, 0.98, 1.01, 0.99],
    'offset': [0.1, -0.05, 0.08, 0.12],
    'thresholds': [22.0, 25.5, 28.0, 31.5]
}

# Dead code path - unused function (red herring)
def legacy_recalibrate(data):
    adjusted = []
    for val in data:
        if val > 0:
            adjusted.append(val * 1.05 - 0.2)
        else:
            adjusted.append(0.0)
    return adjusted

# Unused transformation (misleading intermediate)
shadow_buffer = []
for node_id, readings in telemetry_stream:
    filtered = [r for r in readings if r > 0]
    avg = sum(filtered) / len(filtered) if filtered else 0
    shadow_buffer.append((node_id, avg * 0.98))  # Not used later

# Simulated event log with decoy content
event_log = defaultdict(list)
event_log['errors'].append('CRC mismatch on node 1005')
event_log['warnings'].append('High temp alert (cleared)')
event_log['info'].extend(['Startup OK', 'Sync complete'])

# Primary data structure for processing
log_data = []
for node_id, sensor_readings in telemetry_stream:
    reading_stats = {}
    valid_readings = [r for r in sensor_readings if r > 0]
    
    # Compute various metrics (some irrelevant)
    reading_stats['node'] = node_id
    reading_stats['raw_count'] = len(sensor_readings)
    reading_stats['valid_count'] = len(valid_readings)
    reading_stats['missing_count'] = sensor_readings.count(0.0)
    reading_stats['mean_raw'] = sum(sensor_readings) / len(sensor_readings)
    reading_stats['mean_valid'] = sum(valid_readings) / len(valid_readings) if valid_readings else 0
    reading_stats['variance_proxy'] = sum((x - reading_stats['mean_valid']) ** 2 for x in valid_readings) / len(valid_readings) if valid_readings else 0
    reading_stats['stability_index'] = reading_stats['valid_count'] / reading_stats['raw_count']
    
    # Introduce decoy derived values
    reading_stats['deprecated_flag'] = reading_stats['mean_raw'] < 20.0
    reading_stats['legacy_codepath'] = False
    
    log_data.append(reading_stats)

# Decoy aggregation (not used in final result)
total_nodes = len(log_data)
avg_completion = sum(entry['stability_index'] for entry in log_data) / total_nodes if total_nodes else 0

# Auxiliary function with early returns and conditional complexity
def assess_node_health(metrics):
    if metrics['valid_count'] == 0:
        return 0
    if metrics['stability_index'] < 0.6:
        return 1
    if metrics['mean_valid'] > 30.0:
        return 3
    if metrics['variance_proxy'] > 4.0:
        return 2
    return 2  # default medium risk

# Another distraction: frequency counter of meaningless categories
category_counter = Counter()
for entry in log_data:
    if entry['mean_valid'] < 20.0:
        category_counter['cold'] += 1
    elif entry['mean_valid'] > 30.0:
        category_counter['hot'] += 1
    else:
        category_counter['normal'] += 1

# Core processing function with nested logic and distractors
def process_metrics(log_entries, sys_state):
    # Irrelevant pre-computation (distractor)
    baseline_reference = sys_state['core_temperature'] / sys_state['voltage_stability']
    scaling_factor = 1.0 + (sys_state['active_nodes'] % 7) * 0.01
    
    health_scores = []
    for entry in log_entries:
        # Multi-step health assessment
        base_score = assess_node_health(entry)
        
        # Conditional modifiers (some misleading)
        modifier = 0
        if entry['node'] % 2 == 0:
            modifier += 0.5
        if sys_state['firmware_version'] > '2.0.0':
            modifier += 0.3  # Always true
        if entry['mean_valid'] > baseline_reference:  # Misleading comparison
            modifier += 0.2
        
        final_score = base_score + modifier
        health_scores.append(final_score)
    
    # Real computation path
    raw_sum = sum(h * 10 for h in health_scores)  # Scale health scores
    adjustment = len([h for h in health_scores if h >= 3.0]) * 5  # penalty for high risk
    compensation = int(sys_state['voltage_stability'] * 100) // 10  # 9 -> fixed
    
    # Critical calculation buried among distractions
    diagnostic_value = raw_sum - adjustment + compensation
    
    # Dead branches with decoy outputs
    if diagnostic_value > 100:
        return diagnostic_value * 0.95
    elif diagnostic_value < 20:
        return diagnostic_value * 1.2
    else:
        # This is the actual execution path
        return int(diagnostic_value) + 7  # Final deterministic transformation

# Execute main processing step
intermediate_probe = [entry['mean_raw'] for entry in log_data]  # Red herring usage
baseline_diagnostic = process_metrics(log_data[:2], system_state)  # Partial test (unused)

# Key statement
final_diagnostic = process_metrics(log_data, system_state)

# Output target result
print(f"Target result: {final_diagnostic}")