def analyze_component(reading, threshold=0.7):
    """Irrelevant helper function for sensor analysis (dead code path)."""
    return reading > threshold and reading < 0.9

# Simulated telemetry data stream (distractor list)
telemetry_stream = [0.1, 0.8, 0.65, 0.92, 0.44]

# Unused but plausible-looking configuration map
config_params = {
    'tolerance': 0.05,
    'decay_rate': 0.9,
    'max_iter': 100,
    'activation': lambda x: x ** 2  # Misleading functional element
}

# Core performance metrics (relevant data)
metrics = [
    (85, 'latency', True),
    (72, 'throughput', False),
    (93, 'reliability', True),
    (68, 'scalability', False)
]

# Benchmark weights and baselines (mixed relevant/distractor)
benchmark_data = {
    'weights': [0.3, 0.25, 0.35, 0.1],
    'baseline': 70,
    'penalty_factor': 0.8,
    'bonus_threshold': 90,
    'debug_trace': []  # Dead storage
}

# Red herring: unused transformation chain
def transform_sequence(seq):
    return [x * 1.1 for x in seq if x > 70]

interim_values = transform_sequence([item[0] for item in metrics])

# Real logic begins — conditional weighting with unpacking
adjusted_scores = []
for idx, (value, name, bonus_eligible) in enumerate(metrics):
    weight = benchmark_data['weights'][idx]
    base_contribution = value * weight
    
    # Apply conditional bonus or penalty
    if bonus_eligible and value >= benchmark_data['bonus_threshold']:
        base_contribution *= 1.1
    elif not bonus_eligible and value < benchmark_data['baseline']:
        base_contribution *= benchmark_data['penalty_factor']
    
    adjusted_scores.append(base_contribution)

# Distractor: zip with irrelevant pairing
temp_diagnostic = list(zip(telemetry_stream, [x * 0.1 for x in range(len(telemetry_stream))]))

# Real aggregation step
total = sum(adjusted_scores)

# Decoy normalization function that is never called
def normalize(value, min_val=0, max_val=100):
    return (value - min_val) / (max_val - min_val)

# Conditional expression with fallback (key logic)
baseline_offset = benchmark_data['baseline'] * 0.01 if total > 80 else 0

# Final evaluation using list comprehension and enumerate (core step)
final_components = [
    comp + (0.5 if i % 2 == 0 else 0) 
    for i, comp in enumerate(adjusted_scores)
]

# Critical statement
final_score = evaluate_performance(metrics, benchmark_data)

# Dummy function to simulate external call (overridden below)
def evaluate_performance(data, config):
    """Simulates complex evaluation; actual implementation follows."""
    pass

evaluate_performance = lambda m, c: round(
    sum([
        item[0] * c['weights'][i] * (1.1 if item[2] and item[0] >= c['bonus_threshold'] else 1) * \
        (0.8 if not item[2] and item[0] < c['baseline'] else 1)
        for i, item in enumerate(m)
    ]) + sum([0.5 for i in range(len(m)) if i % 2 == 0]),
    4
)

# Print result as required
Result: {evaluate_performance(metrics, benchmark_data)}
print(f"Target result: {final_score}")