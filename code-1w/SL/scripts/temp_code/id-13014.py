import math

# Simulated system telemetry data
timestamps = [1623456780 + i * 60 for i in range(100)]
raw_sensor_values = [round((i * 0.7) + (10 * math.sin(i / 5)) + 25, 2) for i in range(100)]

# Irrelevant auxiliary data (distractor)
user_sessions = [{'id': f'usr{i}', 'active': (i % 7) != 0} for i in range(50)]
config_params = {f'param_{c}': c * 1.5 for c in range(10)}

# System event log entries with metadata
log_entries = [
    {
        'time': t,
        'value': v,
        'severity': 'high' if abs(v - 25) > 15 else ('medium' if abs(v - 25) > 8 else 'low'),
        'delta': round(abs(v - raw_sensor_values[i-1]) if i > 0 else 0, 2),
        'anomaly_score': round(abs(v - 25) / 5.0, 2)
    }
    for i, (t, v) in enumerate(zip(timestamps, raw_sensor_values))
]

# Threshold configuration for diagnostics
system_thresholds = {
    'critical_level': 40.0,
    'warning_bandwidth': 12.5,
    'hysteresis_window': 3.0,
    'decay_factor': 0.9,
    'min_stability_score': 0.67
}

# Decoy function – looks important but unused (dead code path)
def analyze_user_impact(session_list):
    return sum(1 for s in session_list if s['active']) * 0.3

# Auxiliary transformation (used indirectly)
transform_value = lambda x: math.log(x + 1) if x > 0 else 0

# Secondary metric calculation with red herring variables
baseline_drift = sum(abs(sv - 25) for sv in raw_sensor_values[:20]) / 20
fluctuation_index = sum(1 for le in log_entries if le['delta'] > 2.0)
phantom_metric = fluctuation_index * baseline_drift * 0.01  # Unused distraction

# Core processing pipeline
reliability_weights = [
    1.0 if le['severity'] == 'low' else 0.5 if le['severity'] == 'medium' else 0.1
    for le in log_entries
]

accumulated_risk = 0.0
stability_buffer = []

for i, entry in enumerate(log_entries):
    raw_val = raw_sensor_values[i]
    offset = abs(raw_val - 25)
    
    # Simulated dynamic adjustment (with conditional expression)
    adjustment = system_thresholds['decay_factor'] if offset < system_thresholds['warning_bandwidth'] else 0.4
    accumulated_risk += offset * (0.8 if entry['severity'] == 'high' else adjustment)
    
    # Build stability history
    stability_buffer.append(1.0 if offset < 5.0 else 0.2)

# Compute rolling consistency (misleading intermediate result)
rolling_consistency = round(sum(stability_buffer[-10:]) / 10, 3) if len(stability_buffer) >= 10 else 0.0

# Diagnostic processor combining multiple concepts
process_metrics = lambda logs, thresholds: (
    sum(
        le['anomaly_score'] * reliability_weights[i]
        for i, le in enumerate(logs)
        if le['value'] > thresholds['warning_bandwidth']
    ) * thresholds['decay_factor']
    + math.sqrt(baseline_drift + 1e-5)
)

# Critical execution point
final_diagnostic = process_metrics(log_entries, system_thresholds)

# Print target result
print(f"Result: {final_diagnostic}")