from collections import defaultdict, Counter
import itertools

# Simulated system performance metrics over time (irrelevant padding)
timestamps = list(range(1000, 2000, 37))
raw_data = [((t * 2) % 199) + ((t % 13) ** 2) for t in timestamps]

# Irrelevant preprocessing: frequency analysis of meaningless values
freq_map = Counter(raw_data)
decoy_stats = {k: v ** 0.5 for k, v in freq_map.items() if v > 1}
spurious_total = sum(decoy_stats.values()) * 0.3

# Real data initialization
base_metrics = [85, 92, 78, 96, 88]
weights = [0.1, 0.2, 0.3, 0.25, 0.15]

# Decoy transformation chain (dead path)
def transform_series(data, factor=1.5):
    return [int(x * factor) % 100 for x in data]

decoy_metrics = transform_series(base_metrics, 2.1)
decoy_metrics = [x for x in decoy_metrics if x > 50]

# Unused recursive function (red herring)
def calculate_depth(n):
    if n <= 1:
        return 1
    return n + calculate_depth(n // 2)

recursion_trace = [calculate_depth(i) for i in range(1, 6)]

# Distractor: fake normalization using itertools
cumulative_offsets = list(itertools.accumulate([3, -1, 2, -2, 1]))
normalized_decoy = [dm + co for dm, co in zip(decoy_metrics, cumulative_offsets)]

# Real weighting logic obscured by structure
def adjust_for_bias(value, index):
    bias_factor = (index + 1) * 0.05
    return value * (1 + bias_factor)

corrected_metrics = [adjust_for_bias(m, i) for i, m in enumerate(base_metrics)]

# Intermediate distraction: dictionary-based mapping with unused entries
metric_labels = ['response', 'throughput', 'latency', 'accuracy', 'stability']
metric_dict = defaultdict(float)
for label, value in zip(metric_labels, corrected_metrics):
    metric_dict[label] = value

# Add irrelevant aggregations
total_spread = sum(abs(a - b) for a, b in itertools.pairwise(sorted(corrected_metrics)))
avg_correction = sum(corrected_metrics) / len(corrected_metrics)

# Real evaluation function buried in logic
def evaluate_performance(metrics, weights):
    # Apply exponential scaling to emphasize top performers
    scaled = [m ** 1.1 for m in metrics]
    
    # Introduce conditional boost for high scorers (real logic)
    boosted = []
    for s in scaled:
        if s > 90:
            boosted.append(s * 1.08)
        elif s < 80:
            boosted.append(s * 0.95)
        else:
            boosted.append(s * 1.02)
    
    # Final weighted combination
    weighted_sum = sum(b * w for b, w in zip(boosted, weights))
    
    # Final adjustment based on pattern presence (triggers on specific sequence)
    if any(boosted[i] > boosted[i+1] for i in range(len(boosted)-1)):
        weighted_sum *= 1.03
    
    return round(weighted_sum, 6)

# Critical execution point
final_score = evaluate_performance(metrics=corrected_metrics, weights=weights)

# Output requirement
print(f"Target result: {final_score}")