pressure_sensor_input = 85
base_offset = 10
pressure_level = pressure_sensor_input * 9 + base_offset

temperature_probe = 320
temperature_calibration = 25
temperature_state = temperature_probe - temperature_calibration

# Evaluate system threshold condition using conditional expression
status_code = 1 if pressure_level > 80 else 0
activation_bit = status_code ^ 1  # Toggle for safety lock

threshold_flag = (pressure_level > 75) and (temperature_state < 300)

Result: threshold_flag