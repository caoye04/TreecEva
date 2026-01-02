from itertools import combinations

# Simulate hourly resource utilization across a distributed system
base_load = 42
fluctuation_factors = [0.8, 1.1, 0.9, 1.3, 1.05, 0.75, 1.2, 1.15]
penalty_threshold = 100
dummy_counter = 0

# Irrelevant pre-processing: generate unused pairs of hours
unused_pairs = list(combinations(range(8), 2))
for i in range(len(unused_pairs)):
    dummy_counter += 1  # Dead computation

# Real data processing begins
hourly_adjustments = []
for factor in fluctuation_factors:
    adjusted = int(base_load * factor)
    if adjusted > penalty_threshold:
        adjusted -= 10
    hourly_adjustments.append(max(adjusted, 0))

# Introduce misleading secondary calculation
shadow_buffer = [x * 0.95 for x in hourly_adjustments if x > 45]
buffer_sum = sum(shadow_buffer)  # Semi-relevant but not used in final answer

# Core logic: detect usage peaks under dynamic scaling
scaling_multipliers = [1.0, 1.0, 1.1, 1.2, 1.0, 0.9, 1.3, 1.1]
usage_levels = []
for i in range(len(hourly_adjustments)):
    applied_load = hourly_adjustments[i] * scaling_multipliers[i]
    rounded_load = round(applied_load)
    usage_levels.append(rounded_load)

# Add noise: some condition that looks important but isn't
if len(usage_levels) % 2 == 0:
    _temp = [x + 1 for x in usage_levels]  # Unused transformed version

# Key statement
peak_capacity = max(usage_levels)

# Print result as required
print(f"Target result: {peak_capacity}")