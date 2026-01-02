import itertools

def analyze_component(data, threshold=0.5):
    # Irrelevant helper that computes unused metrics
    above_threshold = [x for x in data if x > threshold]
    below_threshold = [x for x in data if x <= threshold]
    avg_above = sum(above_threshold) / len(above_threshold) if above_threshold else 0
    spurious_metric = sum(itertools.chain([0.1 * x for x in below_threshold]))
    return len(above_threshold)


def validate_integrity(seq):
    # Distractor function with dead-end logic
    if not seq:
        return False
    checksum = 0
    for i, val in enumerate(seq):
        checksum += val * (i + 1)
    normalized = checksum / sum(seq) if sum(seq) != 0 else 0
    return normalized > 0.7

# Simulated benchmark phase outputs across 4 subsystems
subsystem_a = [0.82, 0.91, 0.75, 0.88]
subsystem_b = [0.64, 0.71, 0.69, 0.73]
subsystem_c = [0.90, 0.86, 0.94, 0.89]
subsystem_d = [0.55, 0.60, 0.58, 0.62]

# Weights for final aggregation (deliberately uneven)
weights = [0.4, 0.3, 0.2, 0.1]

# Spurious data structures to increase cognitive load
benchmark_metadata = {
    'version': '2.1',
    'mode': 'stress_test',
    'reliability': 0.98,
    'latency_penalty': 0.05
}

# Misleading intermediate calculations
raw_averages = [
    sum(subsystem_a) / len(subsystem_a),
    sum(subsystem_b) / len(subsystem_b),
    sum(subsystem_c) / len(subsystem_c),
    sum(subsystem_d) / len(subsystem_d)
]

adjusted_scores = []
for i, avg in enumerate(raw_averages):
    adjustment_factor = 1.05 if avg > 0.7 else 0.95
    adjusted_scores.append(avg * adjustment_factor)

# Unused normalization chain
normalized_adjusted = [score / max(adjusted_scores) for score in adjusted_scores]

# Real computation begins here — only this part contributes to final result
def calculate_performance(results, w):
    # results: list of lists, w: list of weights
    means = [sum(r) / len(r) for r in results]  # mean of each subsystem
    
    # Apply non-linear boost to high performers
    boosted = [m**1.1 if m > 0.8 else m for m in means]
    
    # Weighted sum using zip and list comprehension
    weighted_sum = sum([b * wt for b, wt in zip(boosted, w)])
    
    # Secondary adjustment based on system balance (min/max ratio)
    balance_factor = min(boosted) / max(boosted) if max(boosted) != 0 else 0
    balanced_score = weighted_sum * (0.8 + 0.2 * balance_factor)
    
    return round(balanced_score * 100, 2)  # Scale to percentage-like score

# Execute main calculation
final_score = calculate_performance([subsystem_a, subsystem_b, subsystem_c, subsystem_d], weights)

# Validate unrelated integrity (distractor call)
dummy_check = validate_integrity([1, 2, 3])

# Print final answer as required
print(f"Target result: {final_score}")