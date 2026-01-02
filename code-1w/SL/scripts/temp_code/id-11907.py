import math

# Simulated sensor data with noise and redundant measurements
data_stream = [3.2, 1.8, 4.5, 2.7, 5.1, 3.6, 2.4, 4.0, 3.8, 5.5, 2.9, 4.3, 3.7, 4.8, 3.9]

# Irrelevant preprocessing: normalize to 0-1 (not used in final computation)
normalized_data = [(x - min(data_stream)) / (max(data_stream) - min(data_stream)) for x in data_stream]

# Redundant transformation: log scaling (distractor)
log_scaled = [math.log(x + 1) for x in data_stream]

# Key data slice: only this subset is actually used
start_idx = len(data_stream) // 3
end_idx = start_idx * 2
data_slice = data_stream[start_idx:end_idx]  # Actual input

# Misleading weight initialization (only one is used)
weights_a = [0.1, 0.3, 0.4, 0.2]
weights_b = [0.25, 0.25, 0.25, 0.25]
weights = [0.4, 0.3, 0.2, 0.1]  # This is the correct one

# Dead function: computes something irrelevant
def analyze_trend(seq):
    return sum(seq[i] < seq[i+1] for i in range(len(seq)-1))

trend_index = analyze_trend(data_stream)  # Distractor result

# Unused recursive helper (red herring)
def binary_weight_sum(seq, idx=0):
    if idx >= len(seq):
        return 0
    return seq[idx] * (0.5 ** idx) + binary_weight_sum(seq, idx + 1)

# Conditional expression based on meaningless threshold
adjustment_factor = 1.1 if sum(log_scaled) > 10 else 0.9

# Decoy calculation with set operations (irrelevant)
unique_logs = set(round(x, 1) for x in log_scaled)
duplicate_count = len(log_scaled) - len(unique_logs)

# Auxiliary function that appears important but is not called in critical path
def compute_ema(values, alpha=0.3):
    ema = values[0]
    for v in values[1:]:
        ema = alpha * v + (1 - alpha) * ema
    return ema

# Another decoy: computes variance but unused
mean_val = sum(data_stream) / len(data_stream)
variance = sum((x - mean_val) ** 2 for x in data_stream) / len(data_stream)

# Real processing begins here — nested logic with slicing and weighting
def apply_filter(values, kernel):
    n = len(values)
    k = len(kernel)
    if n < k:
        return [0]
    # Sliding window dot product
    return [sum(values[i+j] * kernel[j] for j in range(k)) for i in range(n - k + 1)]

# Secondary transformation before scoring
deflated_slice = [x * 0.95 for x in data_slice]

# Multiple layers of conditional logic
if len(deflated_slice) >= 4:
    filtered_output = apply_filter(deflated_slice, weights)
    temp_result = sum(filtered_output)
    if temp_result > 5:
        scaling_factor = adjustment_factor  # Uses earlier conditional
    else:
        scaling_factor = 1.0
else:
    filtered_output = deflated_slice
    scaling_factor = 1.0

# Complex aggregation using slicing and conditional expressions
midpoint = len(filtered_output) // 2
first_half = filtered_output[:midpoint] if midpoint > 0 else [0]
second_half = filtered_output[midpoint:] if midpoint > 0 else filtered_output

# Weighted contribution with ternary-like behavior
primary_contrib = sum(second_half) * 0.7
secondary_contrib = sum(first_half) * 0.3 if first_half else 0.0

# Final score depends only on this line
final_score = process_metrics(data_slice, weights)

# Critical function buried among distractions
def process_metrics(seq, w):
    # Direct weighted sum on original slice
    weighted_sum = sum(seq[i] * w[i] for i in range(len(w)))
    # Correction based on length parity (hidden logic)
    correction = 0.5 if len(seq) % 2 == 0 else -0.5
    # Apply non-linear squashing
    return math.tanh(weighted_sum) * 100 + correction

# Recompute final_score after definition (only this call matters)
final_score = process_metrics(data_slice, weights)

print(f"Target result: {final_score}")