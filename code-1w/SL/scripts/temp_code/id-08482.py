def analyze_signal_strength(signal):
    # Irrelevant signal preprocessing
    if len(signal) == 0:
        return 0
    base_power = sum([x ** 2 for x in signal]) / len(signal)
    normalized = [x / (base_power + 1e-5) for x in signal]
    return sum(normalized[:5])

# Decoy function - never used
def decrypt_sequence(seq):
    return [seq[i] ^ (i * 3) % 17 for i in range(len(seq))]

# System telemetry data (simulated)
sensor_readings = [
    [12, 15, 22, 19, 8, 11, 14],
    [9, 11, 10, 13, 16, 14, 12],
    [18, 20, 23, 25, 21, 19, 17],
    [7, 9, 6, 8, 10, 12, 11]
]

# Dead code path: unused transformation
transformed_readings = []
for idx, reading in enumerate(sensor_readings):
    offset_reading = [r + idx * 2 for r in reading]
    transformed_readings.append(offset_reading)

# Real processing begins here
log_data = {
    'timestamps': [1634567890, 1634567900, 1634567910, 1634567920],
    'errors': [0, 1, 0, 2],
    'throughput': [95, 87, 92, 89],
    'latency_spikes': [3, 6, 4, 7]
}

system_thresholds = {
    'max_latency_spike': 5,
    'min_throughput': 90,
    'critical_errors': 2
}

# Distractor computation - looks important but unused
aggregate_health = 0
for i, t in enumerate(log_data['timestamps']):
    if log_data['errors'][i] > 0:
        aggregate_health -= log_data['errors'][i] * 10
    else:
        aggregate_health += 5

# Another red herring: character counting in fake logs
fake_logs = ["ERR", "INFO", "WARN", "CRIT", "DEBUG"]
count_stats = {}
for log in fake_logs:
    upper_log = log.upper()
    lower_log = log.lower()
    diff_case = sum(1 for a, b in zip(upper_log, lower_log) if a != b)
    count_stats[log] = len(log) + diff_case  # Always just len*2 due to case conversion

# Core logic embedded in distraction
intermediate_scores = []
for i, latency in enumerate(log_data['latency_spikes']):
    score = 0
    if latency <= system_thresholds['max_latency_spike']:
        score += 20
    else:
        score -= 15
    
    if log_data['throughput'][i] >= system_thresholds['min_throughput']:
        score += 25
    else:
        score -= 10
        
    error_count = log_data['errors'][i]
    if error_count >= system_thresholds['critical_errors']:
        score -= 30
    elif error_count > 0:
        score -= 10

    intermediate_scores.append(score)

# Use enumerate and dictionary operation (required features)
adjusted_diagnostics = {}
for idx, s in enumerate(intermediate_scores):
    key_name = f'diag_{idx+1}'
    adjusted_diagnostics[key_name] = s * 1.1  # Apply adjustment factor

# Final aggregation with misleading branching
final_diagnostic = 0
if len(adjusted_diagnostics) >= 3:
    values = list(adjusted_diagnostics.values())
    sorted_vals = sorted(values)
    # Take trimmed mean: exclude highest and lowest
    trimmed = sorted_vals[1:-1]
    final_diagnostic = sum(trimmed) / len(trimmed)
else:
    final_diagnostic = sum(adjusted_diagnostics.values())

# Print required result
print(f"Target result: {final_diagnostic}")