from collections import defaultdict

# Simulate server load across time intervals
intervals = [f't+{i}' for i in range(6)]
base_loads = [120, 150, 135, 160, 142, 158]

# Apply dynamic scaling factor based on interval
scaling_factors = {t: 1.1 if 't+1' in t or 't+4' in t else 1.0 for t in intervals}
scaled_loads = [base_loads[i] * scaling_factors[t] for i, t in enumerate(intervals)]

# Register loads in capacity tracker
capacity_tracker = defaultdict(float)
for t, load in zip(intervals, scaled_loads):
    capacity_tracker[t] = load

# Aggregate peak capacity
load_profiles = list(capacity_tracker.values())
peak_capacity = max(load_profiles)

print(f"Result: {peak_capacity}")