from itertools import accumulate

# System node efficiency ratings (unitless)
efficiencies = [0.85, 0.92, 0.78, 0.96, 0.88]

# Base power capacities in MW
base_powers = [120, 150, 100, 200, 180]

# Calculate effective capacities
effective_caps = [b * e for b, e in zip(base_powers, efficiencies)]

# Apply maintenance adjustment factor (simulated as cumulative decay)
maintenance_factor = 0.97
adjusted_caps = [cap * (maintenance_factor ** i) for i, cap in enumerate(effective_caps)]

# Final capacity aggregation
capacities = list(accumulate(adjusted_caps, lambda acc, x: acc + x * 0.95))

total_capacity = sum(capacities)

# Irrelevant diagnostic variable (minor distraction)
diag_status = "OK"

print(f"Result: {total_capacity}")