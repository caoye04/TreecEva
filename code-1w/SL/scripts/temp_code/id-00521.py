from collections import defaultdict

# Simulate hourly resource utilization across data centers
capacity_log = [
    ("east", 85), ("west", 90), ("north", 70), ("east", 95), ("west", 87),
    ("south", 60), ("north", 75), ("east", 92), ("south", 68), ("west", 93),
    ("east", 96), ("north", 74), ("south", 71), ("west", 89), ("east", 94)
]

# Track stats per region
region_counts = defaultdict(int)
region_total_usage = defaultdict(float)
region_peaks = {"east": 0, "west": 0, "north": 0, "south": 0}

# Distractor variables
temp_buffer = []
data_quality_score = 0.0
validation_passes = 0
redundant_sum = 0

# Primary tracking variables
current_load = 0
peak_capacity = 0
baseline_threshold = 85
adjustment_factor = 0.95

for region, usage in capacity_log:
    # Update count and totals
    region_counts[region] += 1
    region_total_usage[region] += usage
    
    # Update region-specific peak (relevant for final logic)
    if usage > region_peaks[region]:
        region_peaks[region] = usage

    # Simulate some load calculation
    if usage >= baseline_threshold:
        current_load += usage * 0.1
    else:
        current_load -= 5 * 0.1  # artificial decay

    # Clamp to avoid negative loads
    if current_load < 0:
        current_load = 0

    # Key update point: track peak system-wide load
    peak_capacity = max(peak_capacity, current_load)

    # Irrelevant validation routine (distractor)
    if len(temp_buffer) < 3:
        temp_buffer.append(usage * adjustment_factor)
    else:
        avg_temp = sum(temp_buffer) / len(temp_buffer)
        if abs(avg_temp - usage) < 10:
            data_quality_score += 0.1
        temp_buffer.clear()

    # Extra bookkeeping not used in final answer
    redundant_sum += region_total_usage[region]
    validation_passes += 1

# Final adjustment based on peaks (not affecting peak_capacity directly)
final_reported_peak = max(region_peaks.values()) * 1.05

# Output the target result
print(f"Target result: {peak_capacity}")