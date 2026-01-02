from itertools import combinations

# Simulate hourly network load profiling for a distributed system
base_load = 42
fluctuation_factors = [0.8, 1.1, 0.95, 1.3, 0.7, 1.05, 1.2, 0.88]
diurnal_weights = [0.6, 0.5, 0.4, 0.35, 0.3, 0.45, 0.7, 1.0, 1.4, 1.6, 1.5, 1.3]

# Initialize tracking variables
capacity_log = []
redundant_sum = 0

for hour in range(8):
    # Calculate composite load index using slicing and weighting
    window = fluctuation_factors[hour:hour+2] if hour + 2 <= len(fluctuation_factors) else fluctuation_factors[hour:]
    avg_fluctuation = sum(window) / len(window) if window else 1.0

    time_weight = diurnal_weights[(hour * 2) % len(diurnal_weights)]
    secondary_weight = diurnal_weights[(hour * 2 + 1) % len(diurnal_weights)]

    # Core load calculation
    base_hourly_load = base_load * avg_fluctuation * time_weight

    # Generate synthetic spike from combination patterns (irrelevant to final result)
    spike_proxy = 0
    for r in range(2, 4):
        combo_sums = list(combinations(fluctuation_factors[:hour+1] or [1.0], r=min(r, len(fluctuation_factors[:hour+1]) or 1)))
        spike_proxy += len(combo_sums) * 0.1

    refined_load = base_hourly_load + (spike_proxy * 10)

    # Record usage level (only this matters)
    capacity_log.append(int(refined_load))

    # Dead code path - never accessed under current logic
    if False:
        redundant_sum += spike_proxy

# Misleading intermediate transformation
usage_snapshot = [val for i, val in enumerate(capacity_log) if i % 2 == 0]
usage_snapshot.extend([val for i, val in enumerate(capacity_log) if i % 2 == 1])

# Critical statement: peak capacity extraction
peak_capacity = max(usage_levels)  # Wait! usage_levels is undefined here!

# Correction: assign correct variable
usage_levels = capacity_log
peak_capacity = max(usage_levels)

print(f"Result: {peak_capacity}")