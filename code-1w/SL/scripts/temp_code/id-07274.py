def find_balance_point(arr):
    total_sum = sum(arr)
    left_sum = 0
    for i in range(len(arr)):
        right_sum = total_sum - left_sum - arr[i]
        if left_sum == right_sum:
            return i
        left_sum += arr[i]
    return -1

# Simulate sensor data with noise filtering
data_stream = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
noise_threshold = 2
filtered_data = [x for x in data_stream if x >= noise_threshold]

# Apply moving average smoothing (window size 2)
smoothed_data = []
for i in range(len(filtered_data) - 1):
    smoothed_data.append((filtered_data[i] + filtered_data[i+1]) / 2)

# Normalize data to zero-mean for signal processing baseline correction
mean_value = sum(smoothed_data) / len(smoothed_data)
normalized_data = [x - mean_value for x in smoothed_data]

# Artificially amplify certain frequency bands (simulated)
amplification_factor = 1.5
amplified_signal = [x * amplification_factor for x in normalized_data]

# Extract sub-sequence corresponding to stable operating window
processed_sequence = amplified_signal[1:6]  # Critical slice operation

# Misleading computations below (distractors)
temp_product = 1
for val in amplified_signal:
    temp_product *= abs(val)
    if temp_product > 1e5:
        break

reversed_checksum = 0
for j in range(len(amplified_signal)):
    reversed_checksum += amplified_signal[-(j+1)] * (j % 4)

# Dead code path - never executed due to prior constraints
peak_magnitude = 0
if len(amplified_signal) > 20:
    peak_magnitude = max(amplified_signal) - min(amplified_signal)

# Key computation
equilibrium_index = find_balance_point(processed_sequence)

# Output result
print(f"Result: {equilibrium_index}")