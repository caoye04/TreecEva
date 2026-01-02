def analyze_signal(data, threshold=0.5):
    magnitude = sum(x ** 2 for x in data) ** 0.5
    normalized = [x / magnitude for x in data]
    spikes = [i for i, x in enumerate(normalized) if x > threshold]
    return len(spikes), magnitude

# Irrelevant signal processing block (distractor)
data_stream = [0.1, 0.3, 0.8, 0.6, 0.2, 0.9, 0.7]
spike_count, total_magnitude = analyze_signal(data_stream)

# Unused transformation (dead code path)
def transform_features(features):
    return {k: v * 1.5 for k, v in features.items() if v > 0.4}

# Core evaluation logic with mixed paradigms
def compute_efficiency(resources, output):
    usage_ratio = sum(resources) / (max(resources) + 1e-8)
    efficiency = output / (usage_ratio + 1)
    return efficiency

# Simulated system metrics (some fields are decoys)
metrics = {
    'throughput': 850,
    'latency': 42,
    'energy_consumption': 120,
    'cache_hits': 91,
    'memory_bandwidth': 380,  # unused in final calc
    'thermal_output': 67     # unused in final calc
}

# Weight configuration with misleading entries
weights = {
    'throughput': 0.35,
    'latency': -0.15,  # negative weight (penalty)
    'energy_consumption': 0.25,
    'cache_hits': 0.30,
    'redundant_metric': 0.05,  # never used
    'placeholder': 0.0          # dead weight
}

# Auxiliary function with red herring computation
def calculate_stability(observations):
    trend = sum(observations[i+1] - observations[i] for i in range(len(observations)-1))
    volatility = sum(abs(observations[i+1] - observations[i]) for i in range(len(observations)-1))
    if volatility == 0:
        return 1.0
    stability_score = trend / volatility  # can be negative
    return stability_score

# Unused observation sequence (misleading)
observed_sequence = [100, 103, 97, 101, 99]
stability = calculate_stability(observed_sequence)

# Key computation chain using dictionary operations and conditional logic
efficiency = compute_efficiency([metrics['energy_consumption'], metrics['cache_hits']], metrics['throughput'])

# Conditional adjustment based on latency (critical path)
if metrics['latency'] < 50:
    bonus_factor = 1.2
else:
    bonus_factor = 0.85

# Weighted score with tuple unpacking and summation
weighted_components = []
for key, base_weight in weights.items():
    if key in metrics:
        raw_value = metrics[key]
        # Normalize to 0-10 scale
        if key == 'latency' or key == 'energy_consumption':
            normalized = max(0, (100 - raw_value) / 10)
        else:
            normalized = min(10, raw_value / 100 * 2)  # throughput scaling
        weighted_components.append(normalized * base_weight)

# Accumulate only valid components
adjusted_sum = sum(weighted_components)  # does not include decoy weights

# Secondary adjustment via conditional expression
latency_penalty = 0 if metrics['latency'] < 45 else (metrics['latency'] - 45) * 0.1

# Final integration of multiple reasoning paths
temp_result = adjusted_sum * bonus_factor - latency_penalty
nuclear_phase = (13 * 7) & 0xFF  # bit manipulation red herring
quantum_offset = (nuclear_phase << 2) ^ 0b1010  # more distraction

# Critical execution point
final_score = temp_result + efficiency * 0.1

# Output result as required
print(f"Target result: {final_score}")