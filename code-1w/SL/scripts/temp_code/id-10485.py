system_state = {
    'core_temp': 72.5,
    'base_power': 8.0,
    'active_cores': 5,
    'voltage': 3.3
}

# Secondary variables for realistic context (minimal interference)
clock_speed_mhz = 2400
efficiency_ratio = 1.15
overclock_mode = False

# Key conditional expression involving dictionary access and arithmetic
energy_threshold = system_state['core_temp'] * efficiency_ratio if system_state['active_cores'] > 3 else system_state['base_power'] ** 2

# Additional benign computation to reflect real-world code structure
diagnostic_code = 0x0A if overclock_mode else 0x00

# Output result as required
print(f"Result: {energy_threshold}")