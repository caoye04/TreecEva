sensor_id = 'A7'

system_loads = {
    'A7': 14,
    'B3': 9,
    'C5': 23
}

system_status = {
    'active': True,
    'mode': 'monitoring',
    'uptime_hours': 127
}

# Determine energy threshold based on active status and load
temp_factor = 1.5
baseline = system_loads[sensor_id] * temp_factor
energy_threshold = system_loads[sensor_id] ** 2 if system_status['active'] else system_loads[sensor_id] >> 1

# Additional unrelated metric (minimal interference)
performance_score = (baseline + energy_threshold) / 2 if system_status['mode'] == 'monitoring' else 0

Result: energy_threshold