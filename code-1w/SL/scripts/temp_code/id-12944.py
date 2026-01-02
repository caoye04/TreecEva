from collections import defaultdict, Counter

# Simulate sensor data with noise and valid readings
def generate_sensor_data():
    raw_data = [101, 105, 102, 110, 98, 100, 103, 120, 95, 107, 108, 104]
    timestamps = list(range(len(raw_data)))
    labeled_data = {ts: val for ts, val in zip(timestamps, raw_data)}
    return labeled_data

# Filter out anomalous spikes using simple moving average
def smooth_data(data, window=2):
    smoothed = []
    temp_vals = list(data.values())
    for i in range(len(temp_vals)):
        start = max(0, i - window)
        end = i + 1
        window_avg = sum(temp_vals[start:end]) / (end - start)
        smoothed.append(round(window_avg))
    return {k: smoothed[i] for i, k in enumerate(data.keys())}

# Determine which readings exceed dynamic thresholds
def count_exceedances(data, base_threshold=102):
    counts = defaultdict(int)
    sorted_values = sorted(data.values(), reverse=True)
    median_val = sorted_values[len(sorted_values) // 2]
    adaptive_threshold = base_threshold if median_val < 105 else base_threshold + 3
    
    # Irrelevant computation: simulate log
    log_entries = []
    for k, v in data.items():
        if v > adaptive_threshold:
            counts['high'] += 1
        elif v < adaptive_threshold - 10:
            counts['low'] += 1
        else:
            counts['normal'] += 1
        log_entries.append(f"Time {k}: {v} -> threshold check")
    
    # Dead code - never used again
    summary_stats = Counter(log_entries)
    
    return dict(counts), adaptive_threshold

# Main scoring logic
def calculate_final_score(data, thresholds):
    # Unrelated preprocessing step (distractor)
    squared_map = {k: v**2 for k, v in data.items()}
    total_energy = sum(squared_map.values()) // 1000  # Fake energy metric
    
    # Core logic
    status_count, adj_thresh = count_exceedances(data)
    base_score = status_count.get('high', 0) * 10
    penalty = status_count.get('low', 0) * 3
    adjustment = 5 if adj_thresh > 102 else 0
    
    # Extra distraction: unused conditional sort
    if total_energy > 50:
        sorted_items = sorted(data.items(), key=lambda x: x[1], reverse=True)
        mid_point = len(sorted_items) // 2
        top_half_avg = sum(v for _, v in sorted_items[:mid_point]) / mid_point
        bottom_half_avg = sum(v for _, v in sorted_items[mid_point:]) / (len(sorted_items) - mid_point)
        stability_index = top_half_avg - bottom_half_avg  # Not used
    
    final_score = base_score - penalty + adjustment
    return final_score

# Execution flow
data_raw = generate_sensor_data()
data_smooth = smooth_data(data_raw)
thresholds = {'base': 102, 'window': 2}
final_score = calculate_final_score(data_smooth, thresholds)
print(f"Result: {final_score}")