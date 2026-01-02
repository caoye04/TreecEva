import itertools

# Simulated system metrics from a distributed network node
temp_readings = [23.5, 24.1, 22.9, 25.0, 23.8, 24.4, 26.1, 23.2]
packet_loss = [0.02, 0.05, 0.01, 0.03, 0.04, 0.02, 0.06, 0.01]
latency_ms = [120, 110, 135, 118, 125, 112, 140, 115]

# Irrelevant historical data (distractor)
historical_max_temp = max(temp_readings) * 1.05
baseline_packet_loss_avg = sum(packet_loss) / len(packet_loss)
theoretical_min_latency = min(latency_ms) * 0.95

# Distractor function – never called
def calculate_theoretical_capacity(nodes, bandwidth):
    return nodes * bandwidth * 0.85

# Misleading transformation chain (dead path)
transformed_metrics = []
for i in range(len(temp_readings)):
    transformed = (temp_readings[i] * 2.1) + (latency_ms[i] * 0.01) - (packet_loss[i] * 100)
    transformed_metrics.append(round(transformed, 2))

# Unused intermediate structure (red herring)
node_data_map = {f'node_{i}': {
    'temp': temp_readings[i],
    'loss': packet_loss[i],
    'latency': latency_ms[i],
    'score': transformed_metrics[i]
} for i in range(len(temp_readings))}

# Decoy statistical computation
aggregate_variance = 0
if len(temp_readings) > 5:
    mean_temp = sum(temp_readings) / len(temp_readings)
    aggregate_variance = sum((x - mean_temp) ** 2 for x in temp_readings) / len(temp_readings)

# Real processing begins — actual relevant logic
filtered_indices = [i for i in range(len(packet_loss)) if packet_loss[i] < 0.04]
filtered_latency = [latency_ms[i] for i in filtered_indices]
filtered_temp = [temp_readings[i] for i in filtered_indices]

# Weight configuration (critical)
weights = {'latency': 0.5, 'stability': 0.3, 'thermal': 0.2}

# Simulate multiple scenario slices using itertools
combinations = list(itertools.combinations(filtered_indices, 2))
penalty_factor = 0
for combo in combinations:
    diff = abs(latency_ms[combo[0]] - latency_ms[combo[1]])
    if diff > 20:
        penalty_factor += 0.01

# Auxiliary decoy dictionary (irrelevant)
system_flags = {
    'overheat': any(t > 25.5 for t in temp_readings),
    'high_loss_burst': any(p > 0.05 for p in packet_loss),
    'latency_spike': any(l > 130 for l in latency_ms)
}

# Actual metric calculation (core logic)
avg_filtered_latency = sum(filtered_latency) / len(filtered_latency) if filtered_latency else 0
thermal_stability = 100 - (max(filtered_temp) - min(filtered_temp)) * 2
raw_latency_score = max(0, 100 - (avg_filtered_latency / 1.5))

# Secondary distractor: unused transformation
normalization_factor = 1 / (1 + penalty_factor) if penalty_factor < 1 else 1

# Critical state tracking (misleading)
current_state_vector = []
for i in filtered_indices:
    score = (100 - packet_loss[i] * 1000) * 0.7 + (100 - abs(temp_readings[i] - 24) * 5) * 0.3
    current_state_vector.append(score)

# Core evaluation function
metrics = {
    'latency': raw_latency_score,
    'stability': thermal_stability,
    'thermal': 100 - (max(filtered_temp) - 20)
}

# Final computation — this is where the answer comes from
def evaluate_performance(met, w):
    total = 0
    for key in w:
        if key == 'latency':
            # Invert because lower latency is better
            total += (100 - met[key]) * w[key]
        else:
            total += met[key] * w[key]
    # Apply combination-based penalty
    global penalty_factor
    adjusted = total - (penalty_factor * 10)
    return round(adjusted, 4)

# Execution point of interest
final_score = evaluate_performance(metrics, weights)

# Output result as required
print(f"Result: {final_score}")