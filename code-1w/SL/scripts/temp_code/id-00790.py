temperature_readings = [23.5, 24.1, 22.9, 25.0, 23.8]
pressure_values = (101.3, 102.1, 100.7, 103.2)
power_levels = (120, 145, 130, 140, 135)

total_samples = len(temperature_readings) + len(pressure_values)
avg_pressure = sum(pressure_values) / len(pressure_values)
system_active = avg_pressure > 101.5 and total_samples >= 9

energy_baseline = sum(power_levels) / len(power_levels)
energy_threshold = min(power_levels) * (1.5 if system_active else 0.5)

Result: energy_threshold