sensor_input = 78.5
is_active = sensor_input > 70
is_peak = sensor_input > 90
min_output = 15
max_output = 95
baseline_offset = 10

efficiency_factor = 1.2 if is_active else 0.8
adjusted_min = min_output * efficiency_factor

energy_threshold = max_output if is_peak else min_output + baseline_offset
print(f"Target result: {energy_threshold}")