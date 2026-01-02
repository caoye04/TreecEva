from itertools import accumulate

# System monitoring simulation: tracking resource utilization over time
base_loads = [120, 180, 90, 200, 140]
scaling_factors = [1.1, 0.9, 1.2, 0.8, 1.3]

# Apply dynamic scaling to base loads
effective_loads = [int(base * factor) for base, factor in zip(base_loads, scaling_factors)]

# Simulate cumulative system load over intervals
system_loads = list(accumulate(effective_loads, lambda x, y: x + int(y * 0.95)))

# Identify peak capacity requirement
trend_analysis = [load * 1.05 for load in system_loads]  # Projected trend (not used in peak)
average_load = sum(system_loads) / len(system_loads)
peak_capacity = max(system_loads)

Result: peak_capacity