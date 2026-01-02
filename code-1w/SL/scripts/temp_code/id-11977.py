from itertools import accumulate

# Simulate hourly network bandwidth adjustments over a day
time_slots = 24
base_load = [30, 25, 40, 60, 80, 95, 110, 125, 120, 115, 100, 90]
base_load += [85, 75, 70, 65, 60, 70, 90, 110, 130, 140, 135, 100, 60, 40]

# Apply dynamic scaling based on congestion thresholds
dynamic_adjustment = []
for load in base_load:
    if load > 100:
        adjustment = load * 0.15
    elif load > 50:
        adjustment = load * 0.05
    else:
        adjustment = load * 0.02
    dynamic_adjustment.append(round(adjustment))

# Compute cumulative buffer allocation
buffer_pool = [x - y for x, y in zip(base_load, dynamic_adjustment)]
buffers_allocated = list(accumulate(buffer_pool, lambda a, b: a + int(b * 0.1)))

# Track usage with recovery cycles every 6 hours
usage_trajectory = []
recovery_points = []
for i, val in enumerate(buffers_allocated):
    if i % 6 == 0 and i > 0:
        recovered_val = int(val * 0.9)
        usage_trajectory.append(recovered_val)
        recovery_points.append(recovered_val)
    else:
        usage_trajectory.append(val)

# Misleading secondary calculation (distractor)
total_surplus = sum(dynamic_adjustment) - sum(recovery_points)
efficiency_ratio = total_surplus / len(base_load) if len(base_load) else 0

# Normalize trajectory for display (irrelevant to peak)
normalized_path = [round(x / 1.5) for x in usage_trajectory]

# Key computation point
peak_capacity = max(usage_trajectory)

# Print final result
print(f"Result: {peak_capacity}")