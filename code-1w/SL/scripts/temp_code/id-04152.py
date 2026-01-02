def analyze_efficiency(data, threshold=0.75):
    # Irrelevant helper function with dead-end logic
    temp_results = []
    for item in data:
        temp_results.append(item * 0.95 if item > threshold else item * 0.3)
    return sum(temp_results) / len(temp_results)

# Misleading data structure that looks important but isn't used in final result
diagnostic_log = {
    'errors': [],
    'warnings': ["Low threshold", "High variance"],
    'debug_mode': True
}

# Core metrics and weight configuration
metrics = {
    'latency': 88,
    'throughput': 92,
    'reliability': 85,
    'scalability': 90
}

weights = [0.2, 0.3, 0.25, 0.25]

# Auxiliary transformation - partially relevant
adjusted_metrics = list(map(lambda x: x + 2 if x < 90 else x, metrics.values()))

# Dummy accumulator for distraction
running_total = 0
for val in adjusted_metrics:
    running_total += val * 0.1  # Not used later

# Secondary computation with red herring variables
baseline = sum(metrics.values()) / len(metrics)
effective_base = baseline * 0.88 if baseline > 80 else baseline * 1.1

# Key evaluation logic
conversion_factor = 1.05

# Weighted scoring using modular arithmetic to obscure logic slightly
weighted_sum = 0
for i, key in enumerate(metrics.keys()):
    metric_val = list(metrics.values())[i]
    weight = weights[i]
    # Apply modular adjustment based on index for subtle interference
    mod_adjustment = (i + 1) % 3 / 100
    weighted_sum += metric_val * weight * (1 + mod_adjustment)

# Final transformation with intermediate distractors
temp_score = weighted_sum * conversion_factor
decay_correction = 0.99 ** len(weights)  # Looks sophisticated but has minimal effect

# Add fake normalization step
normalized_interim = temp_score * decay_correction

# Introduce tuple unpacking that simulates complexity
aux_data = (normalized_interim, effective_base, running_total)
interim_score, _, _ = aux_data

# Final performance evaluation - depends only on weighted_sum and conversion
final_score = int(interim_score * 1.01)  # Minor boost

# Print final result as required
print(f"Result: {final_score}")