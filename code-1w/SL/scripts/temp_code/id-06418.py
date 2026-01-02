import math

# Simulated system telemetry data
timestamps = [1623456780, 1623456785, 1623456790, 1623456795, 1623456800]
raw_sensor_data = [23.4, 24.1, 25.6, 26.0, 27.3]
error_flags = [False, False, True, False, False]
packet_sequence = [101, 102, 104, 105, 107]  # Missing packets: 103, 106

# Irrelevant auxiliary variables (distractors)
baseline_correction = 0.987
scaling_factor = 1.02
normalization_offset = 12.5
jitter_buffer = [0.1, 0.3, 0.2]
calibration_matrix = [[1, 0], [0, 1]]

# System health parameters
system_threshold = 25.0
maintenance_window = True
grace_period_active = False

# Derived metrics with mixed relevance
smoothed_readings = [round(x * scaling_factor + normalization_offset, 2) for x in raw_sensor_data]
high_load_periods = [temp > system_threshold for temp in raw_sensor_data]
consecutive_errors = sum(1 for i in range(len(error_flags)) if error_flags[i] and (i == 0 or error_flags[i-1]))

# Packet loss analysis (partially relevant)
expected_packets = list(range(min(packet_sequence), max(packet_sequence) + 1))
lost_packets = [p for p in expected_packets if p not in packet_sequence]
packet_loss_rate = len(lost_packets) / len(expected_packets)

# Decoy function - appears useful but unused in final calculation
def compute_health_score(data, errors):
    score = sum(data) / len(data)
    penalty = sum(errors) * 10
    return max(0, score - penalty)

# Auxiliary transformation (red herring)
transformed_logs = []
for i, ts in enumerate(timestamps):
    log_entry = {
        'time': ts,
        'value': raw_sensor_data[i],
        'flag': error_flags[i],
        'corrected': smoothed_readings[i]
    }
    transformed_logs.append(log_entry)

# Simulated log entries with extraneous fields
log_entries = [
    {"ts": t, "val": v, "err": e, "seq": s, "meta": f"X{t % 100}"} 
    for t, v, e, s in zip(timestamps, raw_sensor_data, error_flags, packet_sequence)
]

# Redundant preprocessing (distraction)
valid_logs = [entry for entry in log_entries if not entry['err']]
avg_value = sum(entry['val'] for entry in valid_logs) / len(valid_logs)

# Core processing function with embedded logic chain
def analyze_trend(values, threshold):
    above_count = 0
    trend_segments = 0
    prev_was_above = False
    for v in values:
        current_above = v > threshold
        if current_above:
            above_count += 1
        if current_above and not prev_was_above:
            trend_segments += 1
        prev_was_above = current_above
    return above_count, trend_segments

# Complex data transformation pipeline
def extract_diagnostics(entries, thresh):
    temperatures = [e['val'] for e in entries]
    
    # Primary signal detection
    peaks = [t for t in temperatures if t > thresh]
    peak_count = len(peaks)
    
    # Secondary pattern recognition
    rising_edges = 0
    for i in range(1, len(temperatures)):
        if temperatures[i] > temperatures[i-1] + 0.5:
            rising_edges += 1
    
    # Tertiary statistical measure
    baseline_avg = sum(temperatures[:3]) / 3
    deviation = abs(temperatures[-1] - baseline_avg)
    
    # Composite score (only peak_count is actually used later)
    return {
        'peak_events': peak_count,
        'instability_index': rising_edges,
        'drift_metric': round(deviation, 3),
        'snapshot': temperatures[-1]
    }

# Another decoy - looks important but unused
system_fingerprint = {
    'version': '2.1.5',
    'uptime': 87432,
    'load_avg': [0.75, 0.82, 0.91]
}

# Main processing function - only this affects final result
def process_metrics(logs, limit):
    # Step 1: Extract all values
    all_values = [record['val'] for record in logs]
    
    # Step 2: Identify critical readings
    critical_readings = [v for v in all_values if v > limit]
    
    # Step 3: Compute base anomaly score
    anomaly_score = len(critical_readings) * 100
    
    # Step 4: Adjust based on temporal clustering
    clustered_penalty = 0
    for i in range(1, len(all_values)):
        if all_values[i] > limit and all_values[i-1] > limit:
            clustered_penalty += 25  # Extra penalty for consecutive highs
    
    # Step 5: Apply non-linear transformation
    adjusted_score = anomaly_score + clustered_penalty
    
    # Step 6: Introduce conditional offset (never triggered due to grace_period_active=False)
    emergency_offset = 0
    if maintenance_window and grace_period_active:
        emergency_offset = -50
    
    # Step 7: Calculate secondary metric (completely ignored in output)
    recovery_potential = 0
    sorted_vals = sorted(all_values)
    for v in sorted_vals:
        if v < limit * 0.9:
            recovery_potential += 10
    
    # Step 8: Final diagnostic is combination of direct anomalies and clustering
    final = adjusted_score  # Only this matters
    
    # Dead code path - misleading
    if recovery_potential > 100:
        final = int(final * 0.8)
    
    return final

# Execute main logic
interim_diagnostics = extract_diagnostics(log_entries, system_threshold)
dummy_health = compute_health_score(raw_sensor_data, error_flags)

# Key execution point
final_diagnostic = process_metrics(log_entries, system_threshold)

print(f"Result: {final_diagnostic}")