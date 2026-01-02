def normalize(data):
    mean = sum(data) / len(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    std_dev = variance ** 0.5
    return [(x - mean) / (std_dev + 1e-8) for x in data]


def apply_filter(signal):
    filtered = []
    for i in range(1, len(signal) - 1):
        smoothed = (signal[i-1] + 2*signal[i] + signal[i+1]) / 4
        filtered.append(smoothed)
    return filtered

raw_inputs = [12, 7, 15, 3, 9, 14, 6, 11]
depth_map = [i * 0.7 + 2 for i in range(len(raw_inputs))]

# Irrelevant transformation chain
offsets = [abs(x - 10) for x in raw_inputs]
adjusted_offsets = [o * 1.5 for o in offsets if o > 3]
buffer_zone = sum([o // 2 for o in adjusted_offsets])

# Core processing path
normalized = normalize(raw_inputs)
significance_weights = [0.8 if x > 0 else 0.3 for x in normalized]

# Simulate spatial weighting using slicing and shifting
shifted_weights = significance_weights[1:] + [significance_weights[0]]
blended_weights = [(significance_weights[i] + shifted_weights[i]) / 2 for i in range(len(significance_weights))]

filtered_norm = apply_filter(normalized)
trimmed_norm = normalized[1:-1]  # align lengths

# Secondary distraction: geometric sequence approximation
growth_factor = 1.1
projected_values = [trimmed_norm[0] * (growth_factor ** i) for i in range(len(trimmed_norm))]
residual_error = sum([(trimmed_norm[i] - projected_values[i]) ** 2 for i in range(len(trimmed_norm))])

# Final computation with distractor variables
scaling_factor = 100 / (sum(blended_weights) or 1)
scaled_weights = [w * scaling_factor for w in blended_weights]
scaled_values = [v * 10 for v in trimmed_norm]

# Red herring: unused accumulation
running_total = 0
for val in scaled_values:
    if val > 5:
        running_total += val * 0.3

# Key function call
def compute_aggregate(values, weights):
    weighted_sum = sum(values[i] * weights[i] for i in range(len(values)))
    total_weight = sum(weights)
    return weighted_sum / total_weight if total_weight != 0 else 0

intermediate_product = [scaled_values[i] * scaled_weights[i] for i in range(len(scaled_values))]
validation_check = sum(intermediate_product) % 7

final_score = compute_aggregate(scaled_values, scaled_weights)

print(f"Target result: {final_score}")