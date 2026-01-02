from itertools import accumulate

# Simulate daily resource consumption over a week
base_load = [120, 135, 140, 95, 180, 210, 170]
daily_fluctuation = [0.9, 1.1, 1.0, 0.95, 1.2, 1.3, 0.8]

# Apply fluctuations to base load
effective_load = [int(base * factor) for base, factor in zip(base_load, daily_fluctuation)]

# Compute cumulative stress on system
system_stress = list(accumulate(effective_load, lambda acc, x: acc + x if x > 150 else acc + 10))

# System states represented as (day, capacity_used)
system_states = [(i+1, effective_load[i] + system_stress[i]) for i in range(7)]

# Identify peak capacity usage
target_day = 4
normalization_factor = 0.95
adjusted_peak = (effective_load[target_day] + system_stress[target_day]) * normalization_factor

# Find state with highest effective capacity
peak_capacity = max(system_states, key=lambda x: x[1])

# Print result for verification
print(f"Result: {peak_capacity[1]}")