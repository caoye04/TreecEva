import math

# Simulated sensor data and calibration parameters
data_stream = [127, 85, 190, 45, 210, 65, 112, 98, 155, 173]
calibration_factor = 0.88
noise_floor = 40
saturation_limit = 200
baseline_offset = 10

# Irrelevant calibration constants (distractors)
reference_voltage = 3.3
adc_resolution = 1024
scaling_exponent = 1.05
normalization_bias = 0.02

# Signal preprocessing with red herrings
adjusted_values = []
for val in data_stream:
    adjusted = (val - noise_floor) * calibration_factor
    if adjusted > saturation_limit:
        adjusted = saturation_limit
    adjusted_values.append(round(adjusted + baseline_offset))

# Dead code path - never executed due to logic (misleading)
potential_outliers = []
dummy_aggregate = 0
if len(data_stream) > 20:  # Impossible condition
    for i, v in enumerate(adjusted_values):
        if v > 150:
            potential_outliers.append(i)
            dummy_aggregate += v ** 0.5

# Real processing begins here
smoothed_data = []
window_size = 3
for i in range(len(adjusted_values)):
    start = max(0, i - window_size // 2)
    end = min(len(adjusted_values), i + window_size // 2 + 1)
    smoothed_value = sum(adjusted_values[start:end]) / (end - start)
    smoothed_data.append(smoothed_value)

# Filter based on dynamic threshold (actual relevant logic)
mean_val = sum(smoothed_data) / len(smoothed_data)
std_dev = (sum((x - mean_val) ** 2 for x in smoothed_data) / len(smoothed_data)) ** 0.5
threshold = mean_val + 0.5 * std_dev

filtered_data = [x for x in smoothed_data if x > threshold]

# Use of lambda and enumerate (required Python features)
index_weights = list(enumerate(map(lambda w: math.sin(w * math.pi / 8) + 1, filtered_data)))
weighted_sum = sum(weight * val for idx, weight in index_weights for val in [filtered_data[idx]])

# Another layer of irrelevant computation (distractor)
spectral_entropy = 0.0
if len(filtered_data) > 1:
    total_energy = sum(x**2 for x in filtered_data)
    if total_energy > 0:
        probabilities = [x**2 / total_energy for x in filtered_data]
        spectral_entropy = -sum(p * math.log(p) for p in probabilities if p > 0)

# Core logic embedded within distractions
def process_signals(signal_list, limit):
    # Bitwise manipulation mixed with arithmetic (complex reasoning)
    accumulator = 0
    shift_register = 1
    for i, sample in enumerate(signal_list):
        # Mix of bitwise and arithmetic ops
        temp = int(sample) ^ (i << 2)
        temp = (temp + shift_register) % 127
        accumulator += temp * (1 if i % 2 == 0 else -1)
        shift_register = (shift_register * 3) & 0b11111  # Keep in 5 bits
    
    # Final transformation using combinatorics-like weighting
    n = len(signal_list)
    combination_factor = math.factorial(n) // (math.factorial(max(1, n-2)) * math.factorial(min(2, n))) if n > 1 else 1
    
    # Actual answer derived here
    result = (accumulator * combination_factor) // 3
    return result

# Critical execution point
final_output = process_signals(filtered_data, threshold)

# Print required output
print(f"Result: {final_output}")