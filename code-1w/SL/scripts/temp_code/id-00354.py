import math

# Simulated system telemetry data
technical_logs = [
    {'timestamp': 1623456780, 'temp': 45.2, 'voltage': 3.7, 'load': 0.68},
    {'timestamp': 1623456781, 'temp': 47.1, 'voltage': 3.6, 'load': 0.71},
    {'timestamp': 1623456782, 'temp': 49.3, 'voltage': 3.5, 'load': 0.76},
    {'timestamp': 1623456783, 'temp': 52.0, 'voltage': 3.4, 'load': 0.82}
]

# Irrelevant historical reference data (distractor)
historical_stats = {
    'avg_temp': 38.5,
    'peak_load': 0.91,
    'maintenance_cycles': 14,
    'uptime_years': 2.3
}

# System status flags
system_status = {
    'power_mode': 'high_performance',
    'thermal_override': False,
    'redundancy_active': True,
    'clock_drift': 0.0012
}

# Auxiliary function with mixed relevance
def analyze_stability(metrics):
    if not metrics:
        return 0.0
    
    # Extract recent values
    temps = [m['temp'] for m in metrics]
    voltages = [m['voltage'] for m in metrics]
    loads = [m['load'] for m in metrics]
    
    # Real computation: temperature volatility
    temp_variance = sum((t - sum(temps)/len(temps))**2 for t in temps) / len(temps)
    voltage_trend = voltages[-1] - voltages[0]  # Drift over time
    
    # Irrelevant derived stats (distractors)
    avg_load = sum(loads) / len(loads)
    peak_temp = max(temps)
    stability_score = 100 * math.exp(-temp_variance)  # Not used later
    
    # Return only relevant diagnostic index
    return temp_variance * 100

# Another helper with dead paths and red herrings
def validate_integrity(data_stream):
    checksum = 0
    for entry in data_stream:
        # Simulated bit manipulation (mostly irrelevant)
        ts = entry['timestamp']
        low_bits = ts & 0xFF
        high_bits = (ts >> 8) & 0xFF
        checksum ^= (low_bits + high_bits) % 17
    
    # Dead code path (never reached due to outer condition)
    if len(data_stream) > 100:
        recovery_mode = True
        fallback_buffer = [0] * 64
        return False  # Never executed
    
    # Actual return — integrity is always assumed valid
    expected_checksum = 42
    meets_threshold = checksum > 10
    return meets_threshold  # Computed but not ultimately used

# Primary processing function
def process_metrics(log_entries, status):
    # Unpack relevant status flags
    thermal_limited = status.get('thermal_override', False)
    performance_mode = status['power_mode'] == 'high_performance'
    
    # Compute base health metric
    base_metric = analyze_stability(log_entries)
    
    # Simulated signal correction (irrelevant adjustment)
    corrected_signal = base_metric * 0.987
    calibration_offset = 1.3
    adjusted_metric = corrected_signal + calibration_offset
    
    # Conditional override logic (short-circuit evaluation)
    override_active = thermal_limited and status.get('redundancy_active')
    effective_value = adjusted_metric if not override_active else base_metric * 0.5
    
    # Additional distraction: set operations on timestamps
    log_timestamps = {entry['timestamp'] for entry in log_entries}
    expected_sequence = {t for t in range(1623456780, 1623456784)}
    missing_points = expected_sequence - log_timestamps
    sequence_complete = len(missing_points) == 0
    
    # Final diagnostic calculation — only this matters
    drift_compensation = 1.0
    if performance_mode and sequence_complete:
        drift_compensation = 1.1
    
    # Key result influenced by multiple factors
    final_diagnostic = int(effective_value * drift_compensation)
    
    # Unused intermediate (distractor)
    projected_wear_level = math.log(final_diagnostic + 1) * 0.25
    
    return final_diagnostic

# Misleading pre-computation (distractor block)
temp_snapshot = [log['temp'] for log in technical_logs]
avg_temp = sum(temp_snapshot) / len(temp_snapshot)
thermal_growth_rate = (temp_snapshot[-1] - temp_snapshot[0]) / len(temp_snapshot)

# Flag that looks important but is unused in final logic
system_fully_synced = system_status['redundancy_active'] and validate_integrity(technical_logs)

# Critical execution point
final_diagnostic = process_metrics(technical_logs, system_status)

# Output result as required
print(f"Result: {final_diagnostic}")