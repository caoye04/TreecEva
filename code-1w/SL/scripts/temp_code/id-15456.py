def calculate_efficiency(temp, press):
    base_efficiency = 85.0
    temp_effect = 0.5 if temp > 75 else 0.2
    press_effect = 0.3 if press > 100 else 0.1
    adjustment = temp_effect + press_effect
    return base_efficiency - adjustment if adjustment > 0.4 else base_efficiency + 5.0

# Environmental conditions
temperature = 78
pressure = 95

# Irrelevant sensor reading (minimal distraction)
sensor_noise = 0.003

energy_output = calculate_efficiency(temperature, pressure)
print(f"Result: {energy_output}")