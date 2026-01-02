import itertools

# Simulated system performance metrics (some are decoys)
raw_data = [0.85, 0.92, 0.78, 0.96, 0.88]
device_ids = ['D1', 'D2', 'D3', 'D4', 'D5']
threshold_map = {'critical': 0.90, 'warning': 0.80, 'normal': 0.70}

# Irrelevant preprocessing - red herring
filtered_devices = [d for d in device_ids if d.startswith('D')]
sorted_pairs = sorted(zip(raw_data, device_ids), key=lambda x: x[0], reverse=True)
ranked_devices = [item[1] for item in sorted_pairs]

# Decoy transformation using slicing and lambda
transform_fn = lambda x: (x * 1.05) % 1.0
boosted_values = [transform_fn(val) for val in raw_data]
decoy_snapshot = boosted_values[1:4:2]  # Unused slice

# Real metric components (subset of raw_data)
basic_accuracy = raw_data[0]
consistency_ratio = raw_data[2]
stability_index = raw_data[4]

# Fake derived metrics - misleading intermediate values
aggregated_fidelity = sum(boosted_values) / len(boosted_values)
phantom_baseline = max(boosted_values) - min(boosted_values)

# Benchmark weight configuration (critical)
benchmark_weights = {
    'accuracy': 0.4,
    'consistency': 0.35,
    'stability': 0.25
}

# Additional distraction: combinatorics on irrelevant data
permutations = list(itertools.permutations([1, 2, 3], 2))
combo_count = len(permutations)  # unused

# Auxiliary function that looks important but is never called
def calculate_robustness_score(data, factor=1.1):
    return sum(d * factor for d in data if d > 0.8)

# Core evaluation logic
metrics = {
    'accuracy': basic_accuracy,
    'consistency': consistency_ratio,
    'stability': stability_index
}

# Weighted scoring with distractor terms
weighted_sum = 0.0
total_weight = 0.0
for key, weight in benchmark_weights.items():
    if key in metrics:
        weighted_sum += metrics[key] * weight
        total_weight += weight

# Normalize (redundant since weights sum to 1, but included for confusion)
efficiency_bonus = 0.02 if total_weight == 1.0 else 0.01
final_score = weighted_sum + efficiency_bonus

# Output result
print(f"Result: {final_score}")