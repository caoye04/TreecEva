def calculate_efficiency(temp, press):
    base_efficiency = 85.0
    temp_factor = 1.0 - abs(temp - 25) / 100
    press_factor = 0.9 + (press - 1.0) * 0.1 if press >= 1.0 else 0.9 - (1.0 - press) * 0.15
    return base_efficiency * temp_factor * press_factor

# Environmental conditions
temperature = 35
pressure = 1.2

# Irrelevant sensor calibration offset (distractor)
sensor_bias = 0.05

# Compute energy output based on environmental efficiency
energy_output = calculate_efficiency(temperature, pressure)

# Additional unrelated diagnostic flag (minimal interference)
diagnostic_mode = False

print(f"Result: {energy_output}")