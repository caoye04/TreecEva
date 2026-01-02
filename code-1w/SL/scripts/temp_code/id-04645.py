import itertools

# Simulated sensor array diagnostics with noise filtering and redundancy checks
def analyze_sensor_node(nodes):
    base_weights = [0.85, 0.91, 0.77, 0.95, 0.88]
    noise_floor = 0.12
    temp_offset = 0.03
    adjustment_factor = 1.04

    # Irrelevant temperature calibration (distractor)
    calibrated_temps = [(t * adjustment_factor + temp_offset) for t in [22.1, 23.5, 21.8, 24.0, 22.7]]
    avg_temp = sum(calibrated_temps) / len(calibrated_temps)

    # Redundant node scoring with bit manipulation (mixed paradigm)
    raw_scores = []
    for i, node in enumerate(nodes):
        signal = node['signal']
        redundancy = node['redundancy']
        age = node['age']

        # Primary metric: weighted signal adjusted by redundancy and decay
        weight = base_weights[i]
        decay = max(0.5, 1.0 - (age * 0.02))
        boosted_signal = signal * (1 + bin(redundancy).count('1'))  # Bit count as boost

        score = (boosted_signal * weight * decay)
        raw_scores.append(score)

    return raw_scores


def compute_stability_index(raw_scores):
    # Advanced stability analysis with misleading intermediate transforms
    squared_devs = [(x - sum(raw_scores)/len(raw_scores))**2 for x in raw_scores]
    stability_proxy = 100 / (1 + sum(squared_devs))  # Inverse relationship

    # Dead path: unused transformation chain
    normalized = [x / max(raw_scores) for x in raw_scores]
    inverted_norm = [1 - x for x in normalized if x < 1]
    entropy_shadow = -sum([x * __import__('math').log(x) for x in normalized if x > 0])

    # Actual relevant logic buried here
    if stability_proxy > 85:
        return stability_proxy * 1.15
    elif stability_proxy > 70:
        return stability_proxy * 1.05
    else:
        return stability_proxy * 0.93


def aggregate_metrics(scores, thresholds):
    # Complex aggregation using lambda and itertools
    filtered = list(itertools.dropwhile(lambda x: x < thresholds[0], sorted(scores)))
    if not filtered:
        filtered = [min(scores)]

    # Mean of top 3 (or all if fewer)
    top_k = sorted(filtered, reverse=True)[:3]
    mean_top = sum(top_k) / len(top_k)

    # Irrelevant geometric transform (distractor)
    product_all = 1
    for x in scores:
        product_all *= (x / 100)
    geo_mean_shadow = product_all ** (1/len(scores))

    # Apply threshold multipliers based on modular pattern
    modifier = 1.0
    score_sum_mod = int(sum(scores)) % 7
    if score_sum_mod in [0, 1, 2]:
        modifier = 0.98
    elif score_sum_mod in [3, 4]:
        modifier = 1.02
    else:
        modifier = 1.08

    # Final computation
    adjusted_mean = mean_top * modifier
    penalty = 0
    for s in scores:
        if s < thresholds[1]:
            penalty += (thresholds[1] - s) * 0.1
    final_score = max(0, adjusted_mean - penalty)

    return final_score

# Main execution with decoy data structures
decoys = {
    'config': {'version': '2.1', 'mode': 'diagnostic'},
    'history': [(2021, 0.88), (2022, 0.91), (2023, 0.89)],
    'unused_metric': list(map(lambda x: x**2, range(5)))
}

sensor_nodes = [
    {'signal': 89.3, 'redundancy': 7, 'age': 18},
    {'signal': 92.1, 'redundancy': 11, 'age': 12},
    {'signal': 85.7, 'redundancy': 14, 'age': 25},
    {'signal': 94.2, 'redundancy': 13, 'age': 8},
    {'signal': 87.9, 'redundancy': 6, 'age': 21}
]

thresholds = [80.0, 82.5]

# Execute pipeline
reliability_scores = analyze_sensor_node(sensor_nodes)
stability_index = compute_stability_index(reliability_scores)
final_diagnostic = aggregate_metrics(reliability_scores, thresholds)

# Print result
print(f"Result: {final_diagnostic}")