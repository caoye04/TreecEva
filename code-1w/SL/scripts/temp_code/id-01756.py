from itertools import compress

# System configuration parameters
base_load = [120, 150, 130, 160, 140, 170, 180, 190]
efficiency_flags = [True, False, True, True, False, True, True, False]
upgrade_cycles = 3

dynamic_adjustment = [1.1 if i % 2 == 0 else 0.95 for i in range(len(base_load))]
adjusted_load = [base_load[i] * dynamic_adjustment[i] for i in range(len(base_load))]

# Filtering active units based on efficiency and adjustment threshold
active_units = list(compress(adjusted_load, efficiency_flags))

# Simulate incremental capacity upgrades
for cycle in range(upgrade_cycles):
    active_units = [unit * 1.05 for unit in active_units]

# Final optimization step: cap any unit above 200MW
optimized_units = [min(unit, 200) for unit in active_units]
total_capacity = sum(optimized_units)

print(f"Result: {total_capacity}")