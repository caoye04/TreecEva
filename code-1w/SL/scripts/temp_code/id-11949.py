def calculate_efficiency(load, reserve):
    base_efficiency = 90
    overload_penalty = 15 if load > 80 else 0
    reserve_bonus = 10 if reserve >= 20 else 5
    return base_efficiency - overload_penalty + reserve_bonus

grid_load = 85
capacity_reserve = 25
maintenance_mode = False
system_status = 'online' if not maintenance_mode else 'offline'

# List comprehension to simulate sensor readings (irrelevant but realistic)
sensor_readings = [load * 1.02 for load in [grid_load]]

energy_threshold = calculate_efficiency(grid_load, capacity_reserve)

# Conditional expression for display message (distractor)
display_message = 'Normal' if energy_threshold > 80 else 'Warning'

print(f'Result: {energy_threshold}')