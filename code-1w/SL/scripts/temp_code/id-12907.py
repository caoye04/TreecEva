def calculate_storage(state):
    base = state[0] * 2 + state[1]
    bonus = 10 if state[2] else 5
    return base * bonus // 3

# System calibration parameters (used in other modules)
calibration_factor = 0.95
reference_voltage = 3.3

grid_state = (7, 4, True)
activation_threshold = 8

# Determine storage capacity based on grid configuration
energy_capacity = calculate_storage(grid_state)

# Peripheral system check (irrelevant to main calculation)
status_flag = "OK" if activation_threshold <= 8 else "WARNING"

print(f"Result: {energy_capacity}")