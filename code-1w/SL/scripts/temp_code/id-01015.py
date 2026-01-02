def calculate_efficiency(rate, press, temp):
    base_efficiency = rate * (press ** 0.5)
    adjusted = base_efficiency * (1.0 + temp / 100.0) if temp > 0 else base_efficiency * 0.9
    return int(adjusted)

# System parameters
temperature = 25
calibration_factor = 1.05
flow_rate = 120
pressure = 9

# Irrelevant sensor offset (minimal distraction)
sensor_offset = 0.02

energy_output = calculate_efficiency(flow_rate, pressure, temperature)
print(f"Target result: {energy_output}")