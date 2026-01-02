from collections import defaultdict

# Simulate hourly resource utilization across data centers
capacity_log = [
    (1, 45), (2, 67), (3, 52), (4, 89), (5, 76),
    (6, 94), (7, 88), (8, 70), (9, 65), (10, 90)
]

baseline_threshold = 50
efficiency_factor = 0.85
scaling_buffer = 12
adjustment_count = 0

# Track peak usage per region
region_peaks = defaultdict(int)
validation_scores = []

initial_estimate = sum(load for _, load in capacity_log[:3]) // 3
projected_growth = initial_estimate * 1.2

peak_capacity = 0
current_load = 0

for hour, load in capacity_log:
    # Irrelevant validation check
    score = (load * 0.95) + (hour * 0.5)
    validation_scores.append(score)

    # Core logic with distractors
    if load > baseline_threshold:
        adjusted_load = int(load * efficiency_factor) + scaling_buffer
        current_load = adjusted_load

        # Critical update point
        peak_capacity = max(peak_capacity, current_load)

        # Tracking region-specific peaks (semi-relevant)
        region_id = hour % 3 + 1
        region_peaks[region_id] = max(region_peaks[region_id], current_load)

        # Misleading adjustment counter
        if adjusted_load > 85:
            temp_flag = True
            adjustment_count += 1  # Distractor: not used in final result

    else:
        current_load = load  # Less efficient path

    # Spurious computation
    residual = (current_load * 0.1) % 10

# Additional irrelevant aggregation
total_validations = sum(1 for s in validation_scores if s > 60)
final_projection = projected_growth * (1 + adjustment_count * 0.05)

print(f"Result: {peak_capacity}")