from collections import defaultdict

# Simulate sensor benchmark results across multiple test phases
test_phases = ['startup', 'stabilization', 'operation', 'recovery']
benchmark_results = [
    [0.85, 0.91, 0.76, 0.88],
    [0.90, 0.82, 0.84, 0.79],
    [0.78, 0.88, 0.93, 0.81],
    [0.83, 0.77, 0.80, 0.90]
]

# Irrelevant auxiliary data (distractor)
system_logs = defaultdict(lambda: 'OK')
system_logs['sensor_array'] = 'DEGRADED'
system_logs['power_supply'] = 'STABLE'

# Weight configuration for performance calculation
weights = [0.2, 0.3, 0.3, 0.2]

# Misleading intermediate computation (dead path)
average_per_phase = []
for i in range(len(benchmark_results)):
    total = 0
    for j in range(len(benchmark_results[i])):
        total += benchmark_results[i][j]
    avg = total / len(benchmark_results[i])
    average_per_phase.append(avg)

# Unused transformation function (distractor)
transform_data = lambda x: [[val ** 0.5 for val in row] for row in x]
sqrt_transformed = transform_data(benchmark_results)

# Calculate phase-wise efficiency scores (semi-relevant)
efficiency_scores = []
for idx, readings in enumerate(benchmark_results):
    weighted_sum = sum(readings[i] * weights[i] for i in range(len(readings)))
    efficiency_scores.append(weighted_sum)

# Compute overall stability deviation (irrelevant)
stability_deviation = 0
for scores in benchmark_results:
    mean = sum(scores) / len(scores)
    variance = sum((x - mean) ** 2 for x in scores) / len(scores)
    stability_deviation += variance ** 0.5

# Core calculation: aggregate performance with weighting
def calculate_performance(results, w):
    cumulative = 0
    for i in range(len(results)):
        phase_total = 0
        for j in range(len(results[i])):
            phase_total += results[i][j] * w[j]
        normalized = phase_total / sum(w)
        if i % 2 == 0:
            normalized *= 1.05  # Boost even-indexed phases slightly
        cumulative += normalized
    return int(cumulative * 10)  # Discretized final score

# Final performance metric
temp_bias_correction = sum(weights) ** 2
final_score = calculate_performance(benchmark_results, weights)

# Print result as required
print(f"Result: {final_score}")