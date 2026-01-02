from collections import defaultdict

# Simulate system performance logs with redundant preprocessing
timestamp_logs = [100, 200, 300, 400, 500]
raw_metrics = [85, 90, 78, 92, 88]

# Irrelevant auxiliary data (distractor)
backup_flags = [False, True, False, True, False]
system_uptime = sum([(t // 100) * 2 for t in timestamp_logs if t > 150])

# Preprocessing: filter and align valid entries
event_window = [i for i in range(len(timestamp_logs)) if raw_metrics[i] > 80]
filtered_metrics = [raw_metrics[i] for i in event_window]

# Misleading transformation (not used in final result)
normalized_data = [round((x - min(filtered_metrics)) / (max(filtered_metrics) - min(filtered_metrics)) * 100) for x in filtered_metrics]

# Core processing: count occurrences by category using defaultdict
category_map = ['A', 'B', 'A', 'B']
processed_data = defaultdict(int)
for idx, val in enumerate(filtered_metrics):
    key = category_map[idx % len(category_map)]
    processed_data[key] += val

# Secondary loop with partial overlap (semi-relevant)
duplicate_tracker = {}
for k, v in processed_data.items():
    temp_val = v * 0.95
    if temp_val > 85:
        duplicate_tracker[k] = int(temp_val)

# Conditional logic affecting final input
adjustment_factor = 1.1 if len(duplicate_tracker) >= 2 else 0.9

# Helper function with red herring parameters
def calculate_efficiency(data, ignore_threshold=80, debug_mode=False):
    base_value = 0
    extra_count = 0  # Dead variable (distractor)
    for key, value in data.items():
        if value > 85:
            base_value += value * 0.75
        else:
            base_value += value * 0.65
    return int(base_value * adjustment_factor)

# Final computation
efficiency_score = calculate_efficiency(processed_data)
print(f"Result: {efficiency_score}")