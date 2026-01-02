import math

# Simulated sensor array diagnostics with interference
raw_readings = [14.7, 18.3, 15.2, 19.1, 13.4, 20.0, 16.8, 17.5]
offset_calibration = 1.05
temp_buffer = [x * offset_calibration for x in raw_readings]

# Irrelevant preprocessing: frequency harmonics (dead path)
frequency_spectrum = []
for i in range(len(temp_buffer)):
    harmonic = math.sin(temp_buffer[i]) * math.cos(i * 0.5)
    frequency_spectrum.append(round(harmonic, 3))

# Signal filtering with slicing distraction
filtered_signal = temp_buffer[1:-1:2]  # Every other element, excluding edges
smoothed = [round((a + b) / 2, 2) for a, b in zip(filtered_signal, filtered_signal[1:])] + [filtered_signal[-1]]

# Decoy statistical analysis (no impact on final result)
mean_val = sum(smoothed) / len(smoothed)
variance = sum((x - mean_val) ** 2 for x in smoothed) / len(smoothed)
std_deviation = math.sqrt(variance)

# Real processing begins: trend detection via slope analysis
slope_pairs = [(b - a) for a, b in zip(temp_buffer, temp_buffer[1:])]
drift_flags = [1 if abs(slope) > 2.0 else 0 for slope in slope_pairs]

# Bitwise flag encoding (actual use)
encoded_flag = 0
for bit in drift_flags[:8]:
    encoded_flag = (encoded_flag << 1) | bit

# Set operations to compute anomaly overlap (distractor with partial relevance)
historical_spikes = {14.7, 15.2, 13.4, 20.0}
current_outliers = {x for x in temp_buffer if x > 19.5}
anomaly_intersection = historical_spikes & current_outliers
intersection_size = len(anomaly_intersection)

# Dummy machine learning mimicry (red herring)
predictions = []
for x in temp_buffer:
    pred = (0.3 * x + 0.7 * math.log(x + 1)) % 1
    predictions.append(round(pred, 4))
confidence_score = sum(1 for p in predictions if p > 0.5)

# Core diagnostic logic (buried in noise)
def detect_trend_type(data):
    increasing = sum(1 for x in slope_pairs if x > 0)
    decreasing = sum(1 for x in slope_pairs if x < 0)
    if increasing > decreasing * 2:
        return 3
    elif decreasing > increasing * 2:
        return -3
    else:
        return 1

def aggregate_metrics(data, flags):
    base = sum(data[:4])  # Only first four readings matter
    trend_type = detect_trend_type(data)
    flag_influence = bin(flags).count('1') * 10
    # Critical calculation
    return int(base + trend_type * 5 + flag_influence - 17)

# Unused recursive decoy function
def recursive_denoise(signal, depth=0):
    if depth >= 3 or len(signal) < 2:
        return signal
    half = len(signal) // 2
    return recursive_denoise(signal[:half], depth + 1) + recursive_denoise(signal[half:], depth + 1)

# Unused data structure transformation
transform_map = {i: val for i, val in enumerate(temp_buffer)}
inverted_index = {v: k for k, v in transform_map.items()}

# Key execution point
final_diagnostic = aggregate_metrics(temp_buffer, encoded_flag)

# Additional misleading intermediate
normalization_factor = max(temp_buffer)
adjusted_diagnostic = round(final_diagnostic / normalization_factor, 6)

# Print required output
print(f"Result: {final_diagnostic}")