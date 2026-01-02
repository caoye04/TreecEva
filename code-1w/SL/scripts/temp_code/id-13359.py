import itertools

# Simulated sensor array data with noise and calibration offsets
data_stream = [12, 15, 22, 27, 30, 33, 39, 45, 48, 51]
calibration_factor = 0.9
offset_adjustment = 3
noise_floor = [1, -2, 1, 0, -1, 2, -1, 0, 1, -1]

# Irrelevant auxiliary arrays (distractors)
baseline_readings = [10, 14, 20, 25, 29, 32, 38, 44, 47, 50]
dummy_weights = [0.1, 0.3, 0.2, 0.5, 0.7, 0.4, 0.6, 0.8, 0.9, 1.0]
shadow_buffer = [x * 0.5 + 2 for x in data_stream]

# Apply offset and noise (real transformation)
adjusted_signal = [(data_stream[i] + noise_floor[i] + offset_adjustment) * calibration_factor for i in range(len(data_stream))]

# False processing path: looks important but unused (dead code path)
weighted_average = sum(dummy_weights[i] * baseline_readings[i] for i in range(len(baseline_readings))) / sum(dummy_weights)
extrapolated_values = [x * 1.1 for x in baseline_readings if x > 25]

# Signal transformation via windowed differencing
window_size = 3
stride = 2
strided_windows = [adjusted_signal[i:i+window_size] for i in range(0, len(adjusted_signal)-window_size+1, stride)]

differenced_peaks = []
for window in strided_windows:
    if len(window) == window_size:
        peak_change = max(window) - min(window)
        differenced_peaks.append(peak_change)

# Secondary transformation: exponential smoothing on peaks (relevant)
smoothing_factor = 0.3
smoothed_sequence = [differenced_peaks[0]]
for i in range(1, len(differenced_peaks)):
    smoothed_val = smoothing_factor * differenced_peaks[i] + (1 - smoothing_factor) * smoothed_sequence[-1]
    smoothed_sequence.append(smoothed_val)

# Threshold-based filtering using statistical reference (red herring)
mean_peak = sum(differenced_peaks) / len(differenced_peaks)
std_deviation = (sum((x - mean_peak) ** 2 for x in differenced_peaks) / len(differenced_peaks)) ** 0.5
dynamic_threshold = mean_peak + 0.5 * std_deviation  # Looks adaptive, but not used directly

# Real threshold used (misleading naming)
operational_threshold = 8.5

# Transform to binary fluctuation map above operational threshold
binary_fluctuations = [1 if x > operational_threshold else 0 for x in smoothed_sequence]

# Count transitions using itertools (relevant)
transition_pairs = list(itertools.pairwise(binary_fluctuations))
transition_count = sum(1 for a, b in transition_pairs if a != b)

# Simulate diagnostic pattern matching with lambda (core logic)
pattern_matcher = lambda seq: sum(seq[i] * (2 ** i) for i in range(len(seq)))
local_signature = pattern_matcher(binary_fluctuations[:4]) if len(binary_fluctuations) >= 4 else 0

# Dummy fallback system (decoy)
default_fallback_score = sum(noise_floor) * 100
redundant_flag_check = any(x < 0 for x in noise_floor)

# Actual analysis function (uses recursion)
def analyze_pattern(signal_pattern, thresh):
    if not signal_pattern:
        return 0
    if len(signal_pattern) == 1:
        return signal_pattern[0] * 10
    
    mid = len(signal_pattern) // 2
    left_part = signal_pattern[:mid]
    right_part = signal_pattern[mid:]
    
    # Recursive scoring with conditional boost
    left_score = analyze_pattern(left_part, thresh)
    right_score = analyze_pattern(right_part, thresh)
    
    adjustment = 5 if abs(sum(left_part) - sum(right_part)) < thresh else -3
    return left_score + right_score + adjustment

# Transform data into amplitude-normalized form (actual input)
transformed_data = [round(x / operational_threshold, 2) for x in smoothed_sequence]

# Threshold remains constant
threshold = operational_threshold

# Key assignment statement
final_diagnostic = analyze_pattern(transformed_data, threshold)

# Print result as required
print(f"Result: {final_diagnostic}")