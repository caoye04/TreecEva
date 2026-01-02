from itertools import combinations

# Sensor data simulation for a distributed energy grid
voltage_readings = [230, 245, 221, 256, 234, 241, 229]
current_readings = [12.3, 14.1, 11.8, 15.2, 13.0, 13.9, 12.7]

temperature_logs = [32.1, 34.5, 31.8, 36.2, 33.0, 35.1, 32.7]  # Unused in final calc (distractor)
humidity_levels = [45, 52, 41, 58, 47, 54, 46]  # Distractor only

# Simulate phase shifts in AC circuit (not used in final answer but looks relevant)
phase_shifts = []
for i in range(len(voltage_readings)):
    shift = (voltage_readings[i] * current_readings[i]) % 360
    phase_shifts.append(shift)

# Calculate power (watts) per sensor node
power_levels = []
for i in range(len(voltage_readings)):
    power = voltage_readings[i] * current_readings[i]
    power_levels.append(round(power, 2))

# Calculate efficiency score: power output relative to temperature-adjusted threshold
efficiencies = []
base_threshold = 2700
for i in range(len(power_levels)):
    temp_factor = 1 + (temperature_logs[i] - 32) / 100  # Minor adjustment
    adjusted_threshold = base_threshold * temp_factor
    efficiency = (power_levels[i] / adjusted_threshold) * 100
    efficiencies.append(round(efficiency, 3))

# Introduce irrelevant pairing analysis using itertools
pairwise_stress = []
for pair in combinations(power_levels, 2):
    stress_score = abs(pair[0] - pair[1]) / min(pair)
    pairwise_stress.append(stress_score)

average_stress = sum(pairwise_stress) / len(pairwise_stress)  # Dead-end computation

# Critical statement: find peak efficiency across nodes
peak_efficiency = max(efficiencies)

# Print result as required
print(f"Result: {peak_efficiency}")