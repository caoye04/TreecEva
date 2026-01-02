from itertools import accumulate

# Simulate sensor readings from a solar array over time
voltage_readings = [23, 25, 27, 30, 28, 26, 24, 22]
current_readings = [4.1, 4.3, 4.6, 5.0, 4.8, 4.5, 4.2, 4.0]

temperature_drift = [0.1 * abs(t - 25) for t in voltage_readings]  # drift based on deviation from optimal temp
adjusted_current = [i - d * 0.2 for i, d in zip(current_readings, temperature_drift)]

# Power = V * I, but only during daylight hours (first 6 readings)
daylight_power = [v * i for v, i in zip(voltage_readings[:6], adjusted_current[:6])]

# Simulate energy storage inefficiency with cumulative loss model
storage_loss_rate = 0.98
energy_stored = list(accumulate(daylight_power, lambda acc, p: (acc + p) * storage_loss_rate))

# Calculate efficiency relative to theoretical max power (30V * 5A = 150W)
theoretical_max = 150.0
efficiencies = [(p / theoretical_max) * 100 for p in daylight_power]

# Secondary metric: thermal degradation index (not used in final answer)
thermal_index = [abs(temp - 25) * 1.5 for temp in voltage_readings]
total_degradation = sum(thermal_index)

# Noise threshold filtering (irrelevant to peak efficiency)
valid_efficiencies = [e for e in efficiencies if e > 8.0]
median_efficiency = sorted(valid_efficiencies)[len(valid_efficiencies)//2]

# Final determination of system performance
peak_efficiency = max(efficiencies)

# Print result as required
print(f"Result: {peak_efficiency}")