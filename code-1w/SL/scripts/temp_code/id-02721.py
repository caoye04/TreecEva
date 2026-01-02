from collections import defaultdict, Counter

# Simulated system telemetry data
timestamps = [1678886400, 1678886460, 1678886520, 1678886580, 1678886640]
raw_sensor_data = [
    {'temp': 72.1, 'load': 0.45, 'errors': 2, 'disk': 88},
    {'temp': 73.5, 'load': 0.67, 'errors': 1, 'disk': 89},
    {'temp': 75.0, 'load': 0.88, 'errors': 4, 'disk': 91},
    {'temp': 76.3, 'load': 0.92, 'errors': 7, 'disk': 93},
    {'temp': 74.8, 'load': 0.76, 'errors': 3, 'disk': 92}
]

# Irrelevant auxiliary mappings (distractor)
status_map = {'idle': 0, 'active': 1, 'critical': 2}
unit_conversions = {'F_to_C': lambda x: (x - 32) * 5/9, 'percent_norm': lambda x: x / 100}

# System configuration (some values are misleading)
system_thresholds = {
    'temp_high': 75.0,
    'load_critical': 0.90,
    'error_burst': 5,
    'disk_warning': 90,
    'grace_period': 30,
    'retry_limit': 3
}

# Historical anomaly registry (red herring - not used in main logic)
anomaly_registry = defaultdict(list)
anomaly_registry['node_42'].append('transient_spike_2023')
anomaly_registry['node_42'].append('recovered')

# Log preprocessing with distractors
device_names = ['server_alpha', 'server_beta', 'server_gamma']
log_entries = []
for idx, entry in enumerate(raw_sensor_data):
    # Misleading timestamp manipulation (unused)
    adjusted_time = timestamps[idx] + 3600  # UTC+1 adjustment (not used later)
    
    # Construct log with metadata
    log_entry = {
        'timestamp': timestamps[idx],
        'device': device_names[idx % len(device_names)],
        'metrics': entry,
        'severity': 0
    }
    
    # Conditional severity tagging (partially relevant)
    if entry['temp'] > system_thresholds['temp_high']:
        log_entry['severity'] += 1
    if entry['load'] > system_thresholds['load_critical']:
        log_entry['severity'] += 2
    if entry['errors'] > system_thresholds['error_burst']:
        log_entry['severity'] += 1
    
    # Distractor: unused network field
    if idx % 2 == 0:
        log_entry['network'] = {'latency': 45 + idx*5, 'loss': 0.01}
    else:
        log_entry['network'] = {'latency': 60 + idx*3, 'loss': 0.03}
    
    log_entries.append(log_entry)

# Auxiliary diagnostic functions (some unused)
def analyze_trend(data_list, key_path):
    """Dummy function to simulate advanced analysis (not used)"""
    return sum([eval(f"d['{key_path}']") for d in data_list]) / len(data_list)

def validate_checksum(entry):
    """Irrelevant security check (dead code path)"""
    checksum = 0
    for char in entry['device']:
        checksum += ord(char)
    return checksum % 17

# Core processing pipeline
def extract_spikes(logs, threshold_key='load'):
    spikes = []
    for record in logs:
        val = record['metrics'][threshold_key]
        ref = system_thresholds[f'{threshold_key}_critical'] if f'{threshold_key}_critical' in system_thresholds else 1.0
        if val > ref:
            spikes.append((record['timestamp'], val))
    return spikes

def compute_stability_score(logs):
    # Complex scoring with multiple factors (partial red herring)
    base_score = 100.0
    penalty_weights = {'temp': 0.3, 'load': 0.4, 'errors': 0.2, 'disk': 0.1}
    
    temp_violations = sum(1 for r in logs if r['metrics']['temp'] > 75.0)
    load_peaks = len(extract_spikes(logs, 'load'))
    error_bursts = sum(1 for r in logs if r['metrics']['errors'] > 5)
    disk_warnings = sum(1 for r in logs if r['metrics']['disk'] > 90)
    
    total_penalties = (
        temp_violations * penalty_weights['temp'] +
        load_peaks * penalty_weights['load'] +
        error_bursts * penalty_weights['errors'] +
        disk_warnings * penalty_weights['disk']
    )
    
    # This score is computed but not used in final result (misleading intermediate)
    stability_score = base_score - (total_penalties * 8.5)
    return round(stability_score, 4)

# Unused historical correlation (decoy)
historical_trends = {
    'seasonal_factor': 1.08,
    'maintenance_cycles': [1678880000, 1678890000]
}

def correlate_anomalies(logs, history):
    """Simulate cross-system analysis (never invoked)"""
    correlations = []
    for entry in logs:
        for cycle in history['maintenance_cycles']:
            if abs(entry['timestamp'] - cycle) < 300:
                correlations.append(entry['device'])
    return list(set(correlations))

# Main diagnostic processor (key logic embedded with noise)
def process_metrics(entries, thresholds):
    # Initialize diagnostic state
    diagnostic_state = defaultdict(int)
    spike_count = 0
    critical_events = 0
    transient_flags = []
    
    # Process each entry with multiple checks
    for i, entry in enumerate(entries):
        metrics = entry['metrics']
        
        # Check for compound conditions
        high_temp = metrics['temp'] > thresholds['temp_high']
        critical_load = metrics['load'] > thresholds['load_critical']
        burst_errors = metrics['errors'] > thresholds['error_burst']
        disk_alert = metrics['disk'] > thresholds['disk_warning']
        
        # Update counters
        if high_temp and critical_load:
            diagnostic_state['thermal_overload'] += 1
        
        if burst_errors and disk_alert:
            diagnostic_state['io_pressure'] += 1
        
        # Sequential spike detection
        if critical_load or burst_errors:
            spike_count += 1
            if spike_count >= 2:
                transient_flags.append(i)
        else:
            spike_count = 0
        
        # Critical event accumulation
        if sum([high_temp, critical_load, burst_errors, disk_alert]) >= 3:
            critical_events += 1
    
    # Compute derived metrics
    flag_duration = len(transient_flags)
    base_diagnostic = diagnostic_state['thermal_overload'] * 17
    base_diagnostic += diagnostic_state['io_pressure'] * 11
    base_diagnostic += flag_duration * 3
    base_diagnostic -= critical_events * 2  # Penalty for severity
    
    # Final computation using zip and enumerate (required features)
    weights = [1, -0.5, 2, -1, 0.5]
    reversals = [entries[j]['metrics']['temp'] for j in range(len(entries)-1, -1, -1)]
    trend_pairs = list(zip(reversals, weights))
    
    temperature_momentum = 0
    for idx, (t_val, w) in enumerate(trend_pairs):
        temperature_momentum += (t_val - 70) * w * (idx + 1)
    
    # Final integration
    final_value = int(base_diagnostic + temperature_momentum)
    
    # Decoy operations (no effect)
    _ = [validate_checksum(e) for e in entries]
    _ = compute_stability_score(entries)
    
    return final_value

# Execute main logic
final_diagnostic = process_metrics(log_entries, system_thresholds)

# Print result as required
print(f"Target result: {final_diagnostic}")