import math

# Simulated system telemetry data with mixed signal types
def generate_telemetry():
    raw_signals = [i * 0.5 + math.sin(i) for i in range(10)]
    return {f'node_{i}': {'status': raw_signals[i], 'flagged': raw_signals[i] > 0.75} for i in range(10)}

telemetry_grid = generate_telemetry()

# Irrelevant diagnostic: network latency simulation (red herring)
network_latency_ms = [round(50 + 10 * math.cos(j), 2) for j in range(8)]
latency_outliers = list(filter(lambda x: x > 55, network_latency_ms))

# Data transformation pipeline
log_entries = []
for idx, (node, data) in enumerate(telemetry_grid.items()):
    if data['flagged']:
        transformed = math.log(1 + data['status']) * 100
        normalized = round(transformed, 3)
        log_entries.append({'id': idx, 'value': normalized, 'weight': idx % 3 + 1})

# Unused backup processor (dead code path)
def backup_process(entries):
    return sum(e['value'] * 0.9 for e in entries if e['weight'] == 2)

# Primary metric processor with conditional logic and recursion
def recursive_weight_sum(weights, index=0):
    if index >= len(weights):
        return 0
    current_contribution = weights[index] * (index % 4 + 1)
    return current_contribution + recursive_weight_sum(weights, index + 1)


def evaluate_stability(risk_profile):
    base = 100
    adjustments = 0
    for entry in risk_profile:
        if entry['weight'] == 1:
            adjustments -= 5
        elif entry['weight'] == 2:
            adjustments += 3
        else:
            adjustments += 1
    return base + adjustments

# Decoy function using dictionary operations (misleading)
system_flags = {k: v['status'] > 0.5 for k, v in telemetry_grid.items()}
flag_summary = {state: list(system_flags.values()).count(state) for state in [True, False]}

# Conditional expression chain with distractor variables
critical_count = sum(1 for d in telemetry_grid.values() if d['status'] > 0.8)
threshold_adjustment = 1.5 if critical_count > 2 else 0.8
system_baseline = 75 if any(d['status'] < 0 for d in telemetry_grid.values()) else 80

# Real processing begins here — hidden among distractions
active_weights = [entry['weight'] for entry in log_entries]
weighted_total = recursive_weight_sum(active_weights)
stability_score = evaluate_stability(log_entries)

# System threshold computed via indirect path
system_threshold = math.floor(stability_score / 10) + int(sum(network_latency_ms[:3]) // 10)  # Uses red herring

# Key computation block
aggregated_value = 0
for entry in log_entries:
    contribution = entry['value']
    if entry['weight'] == 1:
        contribution *= 0.7
    elif entry['weight'] == 2:
        contribution *= 1.2
    else:
        contribution *= 1.5
    aggregated_value += contribution

# Final diagnostic calculation
intermediate_result = aggregated_value / (weighted_total or 1)
scaling_factor = 1 + (system_threshold / 100)

# This is the actual answer point
final_diagnostic = int(intermediate_result * scaling_factor)

# Print required result
print(f"Result: {final_diagnostic}")