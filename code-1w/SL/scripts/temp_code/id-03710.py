from itertools import combinations

# Simulate sensor readings from 5 monitoring stations
temperature_readings = [23.4, 25.1, 24.8, 22.9, 26.3]

# Calculate pairwise temperature differences for anomaly detection
diff_pairs = []
for pair in combinations(temperature_readings, 2):
    diff_pairs.append(round(abs(pair[0] - pair[1]), 2))

# System efficiency model based on deviation from optimal (24.0°C)
optimal_temp = 24.0
weight_factors = [0.9, 1.0, 0.95, 0.85, 1.1]  # Calibration weights per station

weighted_deviation = 0.0
for i, temp in enumerate(temperature_readings):
    weighted_deviation += weight_factors[i] * abs(temp - optimal_temp)

# Compute individual station efficiencies (inverted scale)
individual_efficiencies = []
for temp in temperature_readings:
    deviation = abs(temp - optimal_temp)
    efficiency = 100 - (deviation * 4.5)  # 4.5 penalty per degree off
    individual_efficiencies.append(round(efficiency, 2))

# Final system efficiencies include stress factor above 25°C
stressed_efficiencies = []
for temp, eff in zip(temperature_readings, individual_efficiencies):
    if temp > 25.0:
        eff *= 0.9  # 10% efficiency loss due to overheating
    stressed_efficiencies.append(round(eff, 2))

# Apply moving average filter (3-point) to smooth fluctuations
smoothed = []
for i in range(1, len(stressed_efficiencies)-1):
    smoothed.append(round((stressed_efficiencies[i-1] + stressed_efficiencies[i] + stressed_efficiencies[i+1]) / 3, 2))

# Overall system efficiency profile
if len(smoothed) > 0:
    avg_smoothed = sum(smoothed) / len(smoothed)
else:
    avg_smoothed = sum(stressed_efficiencies) / len(stressed_efficiencies)

# Normalize all efficiency values relative to average performance
normalized = [eff / avg_smoothed * 90 for eff in stressed_efficiencies]
efficiencies = [round(eff, 2) for eff in normalized]

# Critical statement
peak_efficiency = max(efficiencies)
print(f"Result: {peak_efficiency}")