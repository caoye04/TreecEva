def analyze_efficiency(record):
    base = record['cycles']
    overhead = record['idle_cycles']
    efficiency = (base - overhead) / base if base > 0 else 0
    penalty = 0.1 if efficiency < 0.7 else 0
    adjusted = efficiency - penalty
    return adjusted

# Simulated system performance log
timestamps = [100, 200, 300, 400]
data_points = [{'cycles': 1000, 'idle_cycles': 300}, {'cycles': 800, 'idle_cycles': 500}, {'cycles': 1200, 'idle_cycles': 200}]

# Irrelevant tracking variables (distractors)
counter_sync = 0
phase_flag = False
buffer_status = {ts: 'active' for ts in timestamps}

# Aggregation map for metric collection
metrics_log = {}
for i, entry in enumerate(data_points):
    key = f"node_{i}"
    metrics_log[key] = analyze_efficiency(entry)

# Secondary processing with red herring computation
aggregate = 0
weight_sum = 0
weights = [0.5, 1.0, 1.5]
for j, w in enumerate(weights):
    temp_key = f"node_{j % 3}"
    if temp_key in metrics_log:
        aggregate += metrics_log[temp_key] * w
        weight_sum += w

weighted_avg = aggregate / weight_sum if weight_sum > 0 else 0

# Bitwise interference - irrelevant to final result
status_code = 0b1101
mask = 0b1010
filtered_status = status_code & mask  # Used nowhere important

# Adjustment logic based on environmental factor
environment_factor = 2
adjustment_factor = (environment_factor ** 2) + (environment_factor % 3)

# Core state-tracking variable (misleading path)
current_state = [0, 0, 0]
for idx in range(len(current_state)):
    current_state[idx] = idx * adjustment_factor

# Actual critical function
def process_performance(log, adj):
    total = 0
    count = 0
    for k, v in log.items():
        if 'node' in k:
            # Apply adjustment and bitwise XOR as obfuscation
            adjusted_value = v * adj
            masked = int(adjusted_value * 100) ^ 15  # XOR with constant
            unmasked = masked ^ 15  # Restore original effect
            total += unmasked / 100.0
            count += 1
    return int((total / count) * 100) if count > 0 else 0

# Final computation step
final_score = process_performance(metrics_log, adjustment_factor)

# Additional dead code path (never executed)
if phase_flag and False:
    sync_value = counter_sync + buffer_status[100]
    final_score -= sync_value

# Print result
print(f"Result: {final_score}")