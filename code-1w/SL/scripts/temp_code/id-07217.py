from itertools import compress

# System configuration for distributed energy units
unit_outputs = [120, 150, 130, 160, 140, 170, 110]
efficiency_flags = [True, False, True, True, False, True, True]
base_threshold = 125

# Identify grids operating above base efficiency threshold
efficient_grids = [output > base_threshold for output in unit_outputs]

# Apply additional runtime filter: only include units with efficiency flag enabled
optimized_grids = list(compress(unit_outputs, compress(efficient_grids, efficiency_flags)))

# Final aggregation after optimization pass
total_capacity = sum(optimized_grids)

print(f"Result: {total_capacity}")