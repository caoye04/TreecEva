from itertools import accumulate
import math

# Simulate a complex but deterministic resource utilization model
base_loads = [12, -5, 8, 14, -22, 19, -11, 6, 9, -3]
fluctuation_mask = [i % 3 + 1 for i in range(len(base_loads))]

# Irrelevant transformation (distractor)
decay_curve = [math.exp(-i * 0.1) for i in range(len(base_loads))]
weighted_decay = [a * b for a, b in zip(base_loads, decay_curve)]  # unused

# Relevant processing with slicing and lambda
adjusted_loads = [abs(x) * y for x, y in zip(base_loads, fluctuation_mask)]
spike_filter = list(map(lambda val: val + 1 if val > 10 else val, adjusted_loads))

# Introduce dead computation (distractor)
squared_pairs = [(a**2, b**2) for a, b in zip(spike_filter, base_loads) if a > b]  # not used

# Core accumulation logic
raw_jumps = [x - 5 for x in spike_filter]  # shift baseline
usage_trajectory = list(accumulate(raw_jumps))

# Early termination check (never triggers due to deterministic input)
critical_threshold = 1000
for idx, val in enumerate(usage_trajectory):
    if val > critical_threshold:
        usage_trajectory = usage_trajectory[:idx+1]
        break

# Key assignment point
peak_capacity = max(usage_trajectory)

# Additional red herring variables
average_load = sum(usage_trajectory) / len(usage_trajectory)
variance_proxy = sum((x - average_load)**2 for x in usage_trajectory)  # distractor
normalization_factor = math.sqrt(variance_proxy) if variance_proxy > 0 else 1  # unused
final_normalized = [x / normalization_factor for x in usage_trajectory]  # irrelevant to peak

print(f"Result: {peak_capacity}")