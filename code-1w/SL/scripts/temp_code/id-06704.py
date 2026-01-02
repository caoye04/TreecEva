from collections import defaultdict

# Simulate hourly resource utilization across multiple server clusters
current_load = [18, 23, 15, 40, 38, 42, 35, 39, 45, 44, 41, 43]
threshold = 40
grace_period_hours = 2

# Track scaling events and capacity adjustments
scaling_log = []
baseline_capacity = 30
expansion_factor = 1.5
penalty_rate = 0.9

# Distractor: irrelevant network latency simulation
delay_buffer = []
for i in range(len(current_load)):
    delay = (current_load[i] * 0.02) % 0.5
    delay_buffer.append(round(delay, 3))

# Real logic: model adaptive capacity based on sustained over-threshold usage
usage_tracker = defaultdict(int)
consecutive_high = 0
projected_growth = 0

for hour, load in enumerate(current_load):
    if load > threshold:
        consecutive_high += 1
    else:
        if consecutive_high >= grace_period_hours:
            # Sustained high load triggers capacity expansion
            projected_growth += baseline_capacity * expansion_factor
            scaling_log.append((hour, projected_growth))
        consecutive_high = 0

    # Update usage with decayed historical weight
    for prev_hour in range(max(0, hour - 4), hour):
        usage_tracker[hour] += current_load[prev_hour] * 0.25

    # Add current load contribution
    usage_tracker[hour] += load * 0.5

    # Distractor: unused penalty adjustment
    temp_penalty = baseline_capacity * (penalty_rate ** consecutive_high)

# Reset consecutive counter one final time (irrelevant to result)
if consecutive_high >= grace_period_hours:
    projected_growth += baseline_capacity * 0.1

# Key statement
peak_capacity = max(usage_tracker.values()) if usage_tracker else 0

# Print result for evaluation
print(f"Result: {peak_capacity}")