def preprocess_readings(sensor_data):
    # Irrelevant preprocessing: normalize to z-scores (not used in final logic)
    mean_val = sum(sensor_data) / len(sensor_data)
    variance = sum((x - mean_val) ** 2 for x in sensor_data) / len(sensor_data)
    z_scores = [(x - mean_val) / (variance ** 0.5) for x in sensor_data]
    return z_scores

# Simulated sensor input (distraction)
sensor_inputs = [120, 85, 95, 110, 90, 130, 100]
noise_floor = 80
calibration_offset = 5

# Distractor transformation: FFT-like but unused
def compute_spectral_energy(data):
    energy = 0
    for i in range(len(data)):
        for j in range(len(data)):
            energy += data[i] * data[j] * (i % 2 - j % 2 + 1)
    return energy / len(data)

spectral_diagnostic = compute_spectral_energy(sensor_inputs)  # Dead end

# Core logic disguised among distractions
def apply_correction(x):
    if x < noise_floor + calibration_offset:
        return x + 2
    elif x > 115:
        return x - 3
    else:
        return x

# Real preprocessing path (non-obvious)
raw_metrics = [apply_correction(x) for x in sensor_inputs]

# Bit manipulation red herring
def scramble(value):
    return ((value << 3) & 255) ^ 42 | (value >> 4)

obfuscated_values = [scramble(x) for x in raw_metrics]  # Not used later

# Multiple assignment distraction
baseline, threshold, gain = 90, 105, 1.25
adjustment_factor = 0.9

# Real data path begins here — hard to trace due to noise
filtered_data = [x for x in raw_metrics if noise_floor <= x <= 135]

# Normalize using min-max (actual relevant step)
data_min = min(filtered_data)
data_max = max(filtered_data)
normalized_data = [(x - data_min) / (data_max - data_min) if data_max != data_min else 0 for x in filtered_data]

# Another decoy function — looks important but unused
def rolling_average(series, window=3):
    avgs = []
    for i in range(len(series) - window + 1):
        avgs.append(sum(series[i:i+window]) / window)
    return avgs

# Weight initialization with misleading comments
# Weights correspond to: [response_time, accuracy, stability, throughput]
metric_weights = [0.3, 0.2, 0.4, 0.1]  # Note: only first three are actually used

# Unused tuple unpacking distraction
(_, _, stability_weight), remaining = metric_weights[:3], metric_weights[3:]
dummy_sum = sum(remaining)  # Always 0.1 — irrelevant

# Actual evaluation logic hidden in recursion
def recursive_stability_assessment(seq, index=0, accumulator=0.0):
    if index >= len(seq):
        return accumulator
    # Only every second element contributes (non-obvious rule)
    contribution = seq[index] * (0.5 ** (index % 2)) if index % 2 == 1 else 0
    return recursive_stability_assessment(seq, index + 1, accumulator + contribution)

# Real metric computation chain
accuracy_score = sum(normalized_data) * 10
response_time_metric = len(normalized_data) * 0.75
stability_metric = recursive_stability_assessment(normalized_data)

# Composite score with zip and enumerate (required features)
evaluation_components = [accuracy_score, response_time_metric, stability_metric]
weighted_sum = 0
for weight, (i, comp) in zip(metric_weights, enumerate(evaluation_components)):
    if i < 3:  # Skip last weight (redundant check)
        weighted_sum += weight * comp

# Final assignment — key execution point
temp_debug = weighted_sum * adjustment_factor  # Looks like it might be used
final_score = int(weighted_sum * 100)  # Critical line: answer determined here

# Red herring: conditional that never triggers
debug_mode = False
if debug_mode:
    print("Detailed breakdown:", accuracy_score, response_time_metric, stability_metric)

# Output required result
print(f"Result: {final_score}")