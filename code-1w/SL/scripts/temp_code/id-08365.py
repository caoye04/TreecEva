import math

# Simulated network node diagnostics with embedded computational logic
def analyze_node_health(status_code, latency_ms, packet_loss):
    base_score = 100 - (latency_ms / 10)
    penalty = packet_loss * 25
    if status_code != 200:
        penalty += 40
    return max(base_score - penalty, 0)

# Irrelevant helper function – dead code path (distractor)
def deprecated_checksum(data_str):
    return sum(ord(c) for c in data_str) % 256

# Data transformation pipeline with red herring operations
def transform_logs(raw_logs):
    processed = []
    temp_buffer = []  # unused buffer (misleading)
    for log in raw_logs:
        if 'error' in log['type']:
            continue  # filter out errors
        transformed_entry = {
            'id': log['id'],
            'health': analyze_node_health(log['status'], log['latency'], log['loss'])
        }
        processed.append(transformed_entry)
    return processed

# High-interference computation with multiple irrelevant accumulators
def calculate_system_stress(nodes):
    stress_sum = 0
    dummy_accumulator_1 = 0  # red herring
    dummy_accumulator_2 = []   # misleading list growth
    peak_stress = 0
    for node in nodes:
        load_factor = node['load'] / node['capacity']
        temperature = node['temp']
        stress_metric = (load_factor * 1.5) + (temperature / 100)
        stress_sum += stress_metric
        dummy_accumulator_1 += len(str(node['node_id']))
        dummy_accumulator_2.append(temperature * stress_metric)  # no use
        if stress_metric > peak_stress:
            peak_stress = stress_metric
    avg_stress = stress_sum / len(nodes)
    # Complex but irrelevant normalization
    normalized_peak = (peak_stress - 0.5) * 100 if peak_stress > 0.5 else 0
    return avg_stress  # only this is used downstream

# Core aggregation logic involving lambda and functional constructs
def aggregate_metrics(node_configs, global_load):
    # Real computation begins here
    health_values = [cfg['health'] for cfg in node_configs]
    total_health = sum(health_values)
    count_above_threshold = len([h for h in health_values if h > 75])

    # Critical lambda-based weighting function (key relevance)
    weight_fn = lambda x: 0.8 if x > 80 else (1.2 if x < 60 else 1.0)
    weighted_health = sum(h * weight_fn(h) for h in health_values)

    # Dummy statistical overcomplication (distractor)
    variance_proxy = sum((h - total_health / len(health_values))**2 for h in health_values)
    entropy_distractor = -sum((h/total_health) * math.log(h/total_health) for h in health_values if h > 0)

    # Integration with system-wide load factor
    adjustment_factor = 1 + (global_load / 1000)
    intermediate_result = weighted_health * adjustment_factor

    # Final diagnostic calculation (answer derived here)
    final_diagnostic = int(intermediate_result - 250)  # deterministic result

    # Unused complex structure to mislead (cross-reference decoy)
    diagnostics_summary = {
        'raw_sum': total_health,
        'adjusted_weighted': intermediate_result,
        'stdev_mask': math.sqrt(variance_proxy / len(health_values)),
        'efficiency_ratio': count_above_threshold / len(health_values),
        'entropy': entropy_distractor,  # irrelevant
        'debug_trace': dummy_accumulator_2 if 'dummy_accumulator_2' in globals() else []  # always empty
    }

    return final_diagnostic

# Simulated input data with plausible values
network_nodes = [
    {'id': 1, 'status': 200, 'latency': 45, 'loss': 0.02},
    {'id': 2, 'status': 503, 'latency': 120, 'loss': 0.08},
    {'id': 3, 'status': 200, 'latency': 60, 'loss': 0.01},
    {'id': 4, 'status': 200, 'latency': 30, 'loss': 0.005}
]

system_load = [{'node_id': 'A1', 'load': 750, 'capacity': 1000, 'temp': 68},
                {'node_id': 'B2', 'load': 900, 'capacity': 1000, 'temp': 75},
                {'node_id': 'C3', 'load': 600, 'capacity': 1000, 'temp': 60}]

# Irrelevant pre-processing chain (distraction)
log_entries = [{'id': 'L1', 'type': 'info', 'status': 200, 'latency': 50, 'loss': 0.01},
               {'id': 'L2', 'type': 'error', 'status': 500, 'latency': 0, 'loss': 1.0},
               {'id': 'L3', 'type': 'info', 'status': 200, 'latency': 40, 'loss': 0.005}]

processed_logs = transform_logs(log_entries)
dummy_hash = deprecated_checksum('auxiliary_integrity_check_987')

# Actual execution path
node_health_profiles = [analyze_node_health(n['status'], n['latency'], n['loss']) for n in network_nodes]

enhanced_nodes = []
for i, h in enumerate(node_health_profiles):
    enhanced_nodes.append({
        'index': i,
        'health': h,
        'tier': 'A' if h > 75 else 'B'
    })

system_stress_level = calculate_system_stress(system_load)

# Key statement: this determines the answer
final_diagnostic = aggregate_metrics(enhanced_nodes, system_stress_level * 100)

print(f"Result: {final_diagnostic}")