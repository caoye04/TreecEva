from itertools import accumulate

# Simulate daily system load with incremental user growth and periodic maintenance dips
daily_increments = [120, 135, -50, 140, 160, -30, 180, 190, -40, 200]

# Apply cumulative changes to compute actual loads over time
system_loads = list(accumulate(daily_increments, initial=500))

# Track warning thresholds for operational safety
warning_thresholds = [load * 0.9 for load in system_loads if load > 600]

# Identify peak observed capacity during monitoring period
peak_capacity = max(system_loads)

# Print final result for evaluation
print(f"Target result: {peak_capacity}")