from collections import Counter

# Simulate sensor data with noise and valid readings
data_stream = [101, 104, 102, 103, 101, 115, 102, 104, 98, 103, 101, 105, 116, 100, 102]
noise_filter_threshold = 10
min_valid_reading = 95
max_valid_reading = 110

# Extract a rolling window of recent data
start_idx = 2
end_idx = 12
data_window = data_stream[start_idx:end_idx]  # Slice operation

# Track frequency of readings
reading_freq = Counter(data_window)

# Identify most stable reading (highest frequency)
most_common_reading, count = reading_freq.most_common(1)[0]

# Apply smoothing: adjust toward median if outlier spike detected
sorted_window = sorted(data_window)
median_val = sorted_window[len(sorted_window) // 2]
adjusted_median = median_val + 2 if count >= 3 else median_val - 1

# Secondary buffer for unused diagnostic info (distractor)
diagnostic_buffer = [x * 1.05 for x in data_stream if x > 105]
spike_count = sum(1 for x in data_stream if abs(x - adjusted_median) > 15)

# Weighted contribution calculation (only some weights matter)
weights = [0.1, 0.2, 0.3, 0.4, 0.5, 0.4, 0.3, 0.2, 0.1, 0.05]
valid_weights = weights[:len(data_window)]
weighted_sum = sum(w * v for w, v in zip(valid_weights, data_window))

# Auxiliary computation: normalize using lambda (not directly used)
normalize = lambda x, mi, ma: (x - mi) / (ma - mi) if ma > mi else 0
norm_values = [normalize(x, min(data_window), max(data_window)) for x in data_window]

# Heuristic adjustment based on stability
stability_bonus = 5 if count >= 4 else 0
variance_estimate = sum((x - adjusted_median) ** 2 for x in data_window) / len(data_window)
penalty_factor = int(variance_estimate // 2)

# Dummy state tracker (misleading complexity)
class StateTracker:
    def __init__(self):
        self.log = []
        self.active = True

tracker = StateTracker()
if tracker.active:
    tracker.log.append(f"Processing {len(data_window)} samples")

# Final scoring logic
def calculate_final_score(window):
    base_score = sum(window) // len(window)
    peak = max(window)
    trough = min(window)
    spread_bonus = (peak - trough) // 4
    return base_score + stability_bonus - penalty_factor + spread_bonus

final_score = calculate_final_score(data_window)

# Irrelevant transformation chain (dead-end computation)
temp_result = [x ** 0.5 for x in diagnostic_buffer]
aggregated_diagnostics = sum(temp_result) / len(temp_result) if temp_result else 0

# Output result
print(f"Result: {final_score}")