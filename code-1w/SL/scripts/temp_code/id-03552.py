import math

# System parameters for a microgrid energy management simulation
temperature = 25
base_capacity = 1200
load_profile = [105, 200, 150, 0, 300, 250]

# Environmental efficiency degradation factor
temp_factor = 1 - 0.005 * (temperature - 20)

# Calculate effective capacity under temperature stress
effective_capacity = base_capacity * temp_factor

# Lambda function to filter active loads above threshold
is_active = lambda x: x > 0
active_loads = list(filter(is_active, load_profile))

total_load = sum(active_loads)
utilization_ratio = total_load / effective_capacity

# Efficiency drops non-linearly with high utilization
if utilization_ratio > 0.8:
    efficiency_factor = 0.7 + (1 - utilization_ratio) * 0.2
else:
    efficiency_factor = 0.9

# Apply safety margin and compute final available output
filtered_load = total_load * 0.95
final_adjustment = efficiency_factor * filtered_load
energy_output = int(final_adjustment)

print(f"Result: {energy_output}")