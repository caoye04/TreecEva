import math

# Simulated sensor array data with calibration offsets
data_stream = [14, 19, 24, 31, 36, 40, 45, 50, 55, 60]
calibration_map = {14: 1.1, 19: 0.95, 24: 1.05, 31: 0.9, 36: 1.15, 40: 1.0, 45: 0.85, 50: 1.2, 55: 0.75, 60: 1.3}

# Irrelevant transformation function (dead code path)
def transform_legacy(val):
    return (val ** 2 + 3) // 7

# Decoy statistical analysis
mean_value = sum(data_stream) / len(data_stream)
median_value = sorted(data_stream)[len(data_stream)//2]
mode_approx = max(set(data_stream), key=data_stream.count)

# Bit manipulation for noise filtering (partially relevant)
def apply_noise_mask(value, level=3):
    masked = value ^ (level * 7)
    if masked < 0:
        return abs(masked)
    return masked

# Complex preprocessing pipeline
preprocessed = []
for raw in data_stream:
    calibrated = raw * calibration_map[raw]
    adjusted = int(calibrated + 0.5)
    noise_filtered = apply_noise_mask(adjusted)
    preprocessed.append(noise_filtered)

# Secondary irrelevant computation: entropy approximation
total_bits = 0
for x in preprocessed:
    if x > 0:
        total_bits += x * math.log2(x)
entropy_estimate = total_bits / sum(preprocessed) if total_bits else 0

# Core efficiency calculation engine
efficiency_scores = []
for i, val in enumerate(preprocessed):
    # Use of enumerate and lambda in functional mapping
    offset_fn = lambda idx, v: (v * (idx + 1)) % 17
    shifted = offset_fn(i, val)
    
    # Conditional branching with logical complexity
    if shifted > 20:
        score = shifted / 3.7
    elif shifted > 10:
        score = shifted * 0.8 + 2
    else:
        score = shifted * 1.3
    
    # Early termination logic (not triggered but affects control flow understanding)
    if score < 0:
        break
    
    efficiency_scores.append(score)

# Aggregation using zip and set operations
duplicate_guard = list(set(efficiency_scores))  # Remove duplicates (minimal effect)
score_pairs = list(zip(duplicate_guard[:-1], duplicate_guard[1:]))

# Accumulation with distraction variables
aggregated_shift = 0
for a, b in score_pairs:
    diff = abs(a - b)
    if diff > 1.0:
        aggregated_shift += diff * 0.5

baseline_anchor = sum(duplicate_guard) / len(duplicate_guard)
fluctuation_penalty = aggregated_shift * 0.3

# Final optimization step (key logic)
raw_efficiency = baseline_anchor * 2.1
penalized_efficiency = raw_efficiency - fluctuation_penalty

# Distractor: unused alternative model
alt_model = sum([x**0.5 for x in efficiency_scores]) * 1.1

# Critical assignment: this is the target variable
optimized_efficiency = int(penalized_efficiency + 0.5)

# Red herring output
print(f"Legacy Transform (unused): {transform_legacy(10)}")
print(f"Entropy Estimate: {entropy_estimate:.4f}")

# Only relevant print for result
final_results = []
final_results.append(optimized_efficiency)
print(f"Target result: {optimized_efficiency}")