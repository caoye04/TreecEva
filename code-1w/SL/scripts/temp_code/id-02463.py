from itertools import combinations

# Simulate sensor array data for environmental monitoring station
temperature_readings = [22.3, 24.1, 25.6, 23.8, 26.0, 24.9, 23.2]
humidity_readings = [55, 60, 62, 58, 65, 63, 57]
pressure_readings = [1013, 1011, 1009, 1012, 1008, 1010, 1014]

# Derived metrics
temp_humidity_index = [(t + h / 10) for t, h in zip(temperature_readings, humidity_readings)]
adjusted_pressure = [(p - 1000) * 0.9 for p in pressure_readings]

# Efficiency simulation based on multi-factor thresholds
efficiencies = []
fluctuation_score = 0
baseline_drift = 0

for i in range(len(temp_humidity_index)):
    base_eff = temp_humidity_index[i] * 0.8 + adjusted_pressure[i]
    if temperature_readings[i] > 24:
        base_eff *= 1.1
    if humidity_readings[i] > 60:
        base_eff *= 0.95
    # Noise filtering factor
    noise_factor = abs(temperature_readings[i] - temperature_readings[(i-1)%len(temperature_readings)])
    filtered_eff = base_eff - noise_factor * 0.3
    efficiencies.append(round(filtered_eff, 3))

    # Accumulate fluctuation (irrelevant to final result)
    fluctuation_score += noise_factor

# Compute peak efficiency from filtered values
peak_efficiency = max(efficiencies)

# Dead code path: diagnostic check for rare edge case (never triggered in this data)
if any(e < 20 for e in efficiencies):
    baseline_drift = sum(e - 20 for e in efficiencies if e < 20)

# Irrelevant combinatorial analysis of temperature pairs above threshold
count_high_temp_pairs = 0
for pair in combinations([t for t in temperature_readings if t > 24], 2):
    if abs(pair[0] - pair[1]) < 1.5:
        count_high_temp_pairs += 1

# Spurious transformation of humidity (not used later)
normalized_humidity = [h / max(humidity_readings) for h in humidity_readings]
scaled_humidity_product = 1
for nh in normalized_humidity:
    scaled_humidity_product *= nh

# Final output
print(f"Result: {peak_efficiency}")