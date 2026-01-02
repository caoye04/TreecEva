def calculate_efficiency(base, loss_factor):
    return base * (1 - loss_factor)

# System parameters
turbine_count = 4
base_capacity = 250.0  # MW per turbine
loss_factor = 0.08
maintenance_factor = 0.95

# Calculate total raw capacity
total_capacity = turbine_count * base_capacity

# Apply efficiency calculation using function
net_capacity = calculate_efficiency(total_capacity, loss_factor)

# Lambda for dynamic weather adjustment
weather_adjustment = lambda x, severity: x * (0.92 if severity > 0.6 else 1.0)
severity_level = 0.75
adjusted_capacity = weather_adjustment(net_capacity, severity_level)

# Unrelated tracking variable (minor distraction)
system_uptime_days = 327

# Final adjustment based on grid demand
final_adjustment = lambda cap: cap * maintenance_factor if cap > 800 else cap * 1.01
energy_output = final_adjustment(adjusted_capacity)

print(f"Result: {energy_output}")