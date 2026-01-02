def calculate_critical_level(data_map):
    base_levels = [val for val in data_map.values() if val > 0]
    adjusted = sum(base_levels) / len(base_levels) if base_levels else 0
    return max(adjusted, 10.5)


def monitor_system_health():
    sensory_data = {'sensor_a': 12.3, 'sensor_b': 8.7, 'sensor_c': 15.1, 'sensor_d': 0.0, 'sensor_e': 9.6}
    
    # Preliminary diagnostic (irrelevant to final result)
    status_codes = {k: 1 if v > 10 else 0 for k, v in sensory_data.items()}
    active_sensors = sum(status_codes.values())
    
    energy_threshold = calculate_critical_level(sensory_data)
    return energy_threshold

result = monitor_system_health()
print(f"Result: {result}")