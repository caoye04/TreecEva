from collections import defaultdict, Counter

# Simulate sensor node cluster state and diagnostic tracking
def monitor_cluster_health(node_data, threshold=0.75):
    active_nodes = []
    instability_flags = defaultdict(int)
    diagnostic_trace = []

    for node_id, readings in node_data.items():
        avg_load = sum(readings) / len(readings)
        peak_spikes = sum(1 for r in readings if r > 0.9)
        
        # Irrelevant smoothing filter (distractor)
        smoothed = [readings[0]]
        for i in range(1, len(readings)):
            smoothed.append(0.7 * readings[i] + 0.3 * smoothed[i-1])
        
        if avg_load > threshold and peak_spikes > 2:
            instability_flags[node_id] = peak_spikes
            active_nodes.append(node_id)
            diagnostic_trace.append(f"Node {node_id}: High load")
        elif avg_load > threshold * 0.8:
            diagnostic_trace.append(f"Node {node_id}: Moderate stress")

    return active_nodes, instability_flags, diagnostic_trace


def calculate_thermal_metric(state, log_entries):
    base_heat = 0.0
    penalty_factor = 1.0
    
    # Misleading entropy-like computation (not used in final result)
    entry_counter = Counter(log_entries)
    total_entries = len(log_entries)
    entropy = 0.0
    for count in entry_counter.values():
        p = count / total_entries
        entropy -= p * (p ** 0.5)  # Non-standard, irrelevant calculation
    
    for entry in log_entries:
        if "High" in entry:
            base_heat += 3.2
        elif "Moderate" in entry:
            base_heat += 1.1

    # Artificial dampening based on state length (semi-relevant)
    state_size = len(state)
    if state_size > 4:
        penalty_factor = 0.85
    elif state_size == 0:
        penalty_factor = 1.5

    # Final metric computation
    thermal_index = base_heat * penalty_factor
    
    # Dead code path (distractor)
    if False:
        fallback = 0
        for k in entry_counter:
            fallback += ord(k[5]) % 3
        thermal_index = fallback

    return round(thermal_index, 4)

# System initialization and data ingestion
sensor_network = {
    'N01': [0.6, 0.7, 0.92, 0.95, 0.81],
    'N02': [0.5, 0.65, 0.71, 0.73, 0.77],
    'N03': [0.82, 0.87, 0.93, 0.96, 0.88],
    'N04': [0.4, 0.55, 0.61, 0.67, 0.59],
    'N05': [0.79, 0.81, 0.94, 0.93, 0.83],
    'N06': [0.3, 0.45, 0.51, 0.49, 0.42]
}

# Diagnostic phase with distraction variables
active_list, anomalies, logs = monitor_cluster_health(sensor_network)

# Auxiliary analysis (semi-redundant)
stable_ratio = (len(sensor_network) - len(active_list)) / len(sensor_network)
baseline_reference = sum(len(v) for v in sensor_network.values()) / len(sensor_network)

# Core calculation point — target intervention statement
thermal_capacity = calculate_thermal_metric(cluster_state=active_list, efficiency_log=logs)

# Print final result as required
print(f"Result: {thermal_capacity}")