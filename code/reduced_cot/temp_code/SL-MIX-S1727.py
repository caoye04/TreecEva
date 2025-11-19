from collections import defaultdict

# Initialize signal data
acoustic_signals = [15, 23, 8, 42, 7, 31, 19, 6]
modulus_base = 13

# Step 1: Apply modular transformation with dictionary comprehension
transformed_signals = {idx: (sig * 3 + 7) % modulus_base for idx, sig in enumerate(acoustic_signals)}

# Step 2: Group indices by their transformed values
signal_groups = defaultdict(list)
for idx, mod_value in transformed_signals.items():
    signal_groups[mod_value].append(idx)

# Step 3: Process groups with nested loops and sorting
processing_metrics = {}
for mod_val, indices in signal_groups.items():
    subgroup_sum = 0
    for i in indices:
        for j in indices:
            if i <= j:
                subgroup_sum += (i * j) % 5
    # Sort indices for consistent processing
    sorted_indices = sorted(indices)
    processing_metrics[mod_val] = subgroup_sum * len(sorted_indices)

# Step 4: Calculate final processing result
processing_result = sum(
    (k * v + 1) % 17
    for k, v in sorted(processing_metrics.items())
)

print(f"Result: {processing_result}")