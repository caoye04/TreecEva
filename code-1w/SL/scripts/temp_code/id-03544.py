import math

# Simulated telemetry data from a distributed sensor network
timestamps = [1623456000 + i*60 for i in range(100)]
sensor_a_readings = [(i * 0.7 + (i % 15)**0.8) for i in range(100)]
sensor_b_readings = [(i * 0.3 + math.sin(i / 10)) for i in range(100)]

# Irrelevant auxiliary data - red herring
aux_data = [math.cos(x) * math.exp(-x/100) for x in range(50)]
dummy_matrix = [[i*j % 7 for j in range(8)] for i in range(8)]
scaling_factor = 0.987
offset_correction = sum(aux_data) / len(aux_data)  # Unused distraction

# System state flags
system_state = {
    'active_nodes': 12,
    'last_reset': 1623450000,
    'mode': 'diagnostic',
    'version': '3.7.1'
}

# Log entries with mixed severity and metadata
log_entries = [
    {'timestamp': 1623456060, 'level': 'ERROR', 'node': 'N7', 'code': 503},
    {'timestamp': 1623456120, 'level': 'WARN', 'node': 'N3', 'code': 206},
    {'timestamp': 1623456180, 'level': 'INFO', 'node': 'N9', 'code': 101},
    {'timestamp': 1623456240, 'level': 'ERROR', 'node': 'N7', 'code': 503},
    {'timestamp': 1623456300, 'level': 'WARN', 'node': 'N1', 'code': 404}
]

# Decoy function - looks important but unused
def analyze_pattern(data):
    n = len(data)
    transformed = [data[i] * (i+1) for i in range(n)]
    return sum(transformed) / (n * (n+1) / 2)

# Real processing begins here
aggregated_readings = []
for i in range(len(sensor_a_readings)):
    combined = sensor_a_readings[i] * 0.6 + sensor_b_readings[i] * 0.4
    aggregated_readings.append(combined)

# Compute moving average as signal baseline
window_size = 5
baseline = []
for i in range(len(aggregated_readings) - window_size + 1):
    window_avg = sum(aggregated_readings[i:i+window_size]) / window_size
    baseline.append(window_avg)

# Calculate anomaly score using deviation from baseline
anomaly_scores = []
for i in range(len(baseline)):
    raw_value = aggregated_readings[i + window_size // 2]
    deviation = abs(raw_value - baseline[i])
    score = min(deviation * 10, 100)
    anomaly_scores.append(score)

# Bit manipulation decoy - irrelevant calculation
obfuscation_key = 0b110101
masked_scores = [int(s) ^ obfuscation_key for s in anomaly_scores[:10]]
bit_analysis = sum([(s >> 2) & 0b111 for s in masked_scores])  # Distractor

# Error frequency analysis - relevant to final result
error_count = 0
recent_errors = []
for log in log_entries:
    if log['level'] == 'ERROR':
        error_count += 1
        recent_errors.append(log['code'])

# Hash-like transformation of error pattern (relevant)
error_signature = 0
for code in recent_errors:
    error_signature ^= (code * 7919)  # Large prime multiplier

# Summation accumulator with lambda filter - core logic
valid_anomalies = list(filter(lambda x: x > 25.0, anomaly_scores))
anomaly_sum = sum(valid_anomalies)
effective_error_weight = error_signature % 1000

# Secondary distraction: complex unused formula
theoretical_limit = math.gamma(6) * math.pi / math.log(1000 + len(dummy_matrix))
projected_risk = theoretical_limit * 0.7 + 2*len(aux_data)  # Dead end

# Key diagnostic computation
base_score = len(valid_anomalies) * 17
adjusted_errors = max(effective_error_weight - 200, 0)
penalty_factor = adjusted_errors / 25.0

# Final integration using system mode logic
if system_state['mode'] == 'diagnostic':
    raw_diagnostic = base_score + penalty_factor
    
    # Apply non-linear correction based on active nodes
    node_mod = system_state['active_nodes']
    if node_mod > 10:
        raw_diagnostic *= (1.1 + (node_mod - 10) * 0.05)
    
    # Hidden rounding behavior - critical detail
    final_diagnostic = round(raw_diagnostic * 10) / 10
else:
    # This branch is unreachable but present as distractor
    temp = [math.tanh(x/50) for x in valid_anomalies]
    final_diagnostic = sum(temp) * 100

# Additional red herring: string manipulation unrelated to result
status_str = "System Health: {grade}"
grades = ['A', 'B', 'C', 'D', 'F']
health_index = int(5 - (final_diagnostic / 20))
health_index = max(0, min(4, health_index))
formatted_status = status_str.format(grade=grades[health_index])  # Unused

# Output the required result
print(f"Result: {final_diagnostic}")