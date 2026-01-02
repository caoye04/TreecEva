def analyze_node_health(node_id, base_signal, noise_floor):
    # Irrelevant transformation (red herring)
    adjusted_noise = noise_floor ^ 257
    if node_id % 3 == 0:
        return (base_signal * 0.85) + (adjusted_noise * 0.15)
    else:
        return base_signal * (1 - (noise_floor / 100))

# Simulated sensor inputs (decoy data)
sensor_readings = [142, 167, 155, 138, 173]
baseline_offset = 42

# Real input data for processing
def process_network_diagnostic():
    network_nodes = ['N1', 'N2', 'N3', 'N4', 'N5']
    raw_power_levels = [95, 87, 91, 89, 93]
    signal_strengths = [p * 1.05 for p in raw_power_levels]  # Boost calibration

    # Distractor: unused but plausible computation
    power_variance = sum([(p - sum(raw_power_levels)/5)**2 for p in raw_power_levels]) / 5

    # Decoy function call with misleading name
    def compute_stability_score(nodes):
        return len(nodes) * 0.95

    stability_score = compute_stability_score(network_nodes)  # Not used

    # Core logic disguised among distractions
    health_scores = []
    for idx, (node, sig) in enumerate(zip(network_nodes, signal_strengths)):
        noise = 10 + (idx * 2) % 7
        score = analyze_node_health(idx, sig, noise)
        if score > 85:
            health_scores.append(score)

    # Irrelevant set operation (looks important but not part of answer)
    unique_signals = set(signal_strengths)
    dropped_nodes = set(network_nodes[1::2])  # Every other node

    # Actual aggregation logic
    valid_indices = [i for i, s in enumerate(signal_strengths) if s > 90]
    filtered_strengths = [signal_strengths[i] for i in valid_indices]

    # Linear search for threshold breach
    peak_index = 0
    for i in range(1, len(filtered_strengths)):
        if filtered_strengths[i] > filtered_strengths[peak_index]:
            peak_index = i

    # Final calculation buried in abstraction
    reference_value = filtered_strengths[peak_index]
    avg_health = sum(health_scores) / len(health_scores)
    final_diagnostic = int((reference_value * 0.7) + (avg_health * 0.3))

    # Dead code path (never reached)
    if False:
        fallback = sum(sensor_readings) // len(sensor_readings)
        final_diagnostic = fallback

    return final_diagnostic

# Execution entry point
def aggregate_health_index(nodes, signals):
    return process_network_diagnostic()

# Trigger execution
target_result = aggregate_health_index(['A','B','C'], [100, 200, 300])
print(f"Target result: {target_result}")