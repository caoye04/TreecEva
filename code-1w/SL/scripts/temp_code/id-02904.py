from itertools import accumulate

# System telemetry data over time
base_load = [120, 150, 130, 170, 200, 160, 140]
event_impact = [30, -10, 50, -20, 40, 0, -15]

# Compute dynamic system load using cumulative effects
temporal_adjustments = [b + e for b, e in zip(base_load, event_impact)]
system_loads = list(accumulate(temporal_adjustments, lambda x, y: x + (y - x) * 0.1))

# Critical measurement point
peak_capacity = max(system_loads)

# Final output
print(f"Target result: {peak_capacity}")