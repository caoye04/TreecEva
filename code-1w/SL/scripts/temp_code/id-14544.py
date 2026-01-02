def calculate_efficiency(rpm, load):
    base_efficiency = 0.85
    efficiency = base_efficiency * (1 + 0.2 * min(rpm / 3000, 1))
    adjustment = 0.1 if load > 0.9 else (-0.05 if load < 0.3 else 0)
    return round(efficiency + adjustment, 4)

# Sensor readings
temperature = 88.5
vibration_level = 0.12
rpm = 2750
load_factor = 0.88

# Control system computation
energy_output = calculate_efficiency(rpm, load_factor)

# Logging (irrelevant to result)
system_status = "NORMAL" if vibration_level < 0.15 else "WARNING"

# Output result
print(f"Result: {energy_output}")