def calculate_efficiency(load):
    base_efficiency = 85.0
    overhead = 0.1 * load if load > 50 else 0
    efficiency = base_efficiency - overhead
    return efficiency if efficiency > 0 else 0

# System monitoring variables (some irrelevant)
temperature = 72.3
cpu_cores_active = 6
disk_usage_percent = 67

network_load = 58
energy_saving_mode = False

# Key computation
energy_threshold = calculate_efficiency(network_load)

# Output result
print(f"Result: {energy_threshold}")