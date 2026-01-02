import itertools

# Simulate environmental sensor readings over time with noise filtering
temperature_readings = [22.3, 23.1, 21.8, 24.0, 22.9, 23.5, 21.5]
humidity_readings = [45, 47, 50, 44, 52, 48, 51]

# Misleading auxiliary calculation (distractor)
avg_humidity = sum(humidity_readings) / len(humidity_readings)
humidity_variance = sum((h - avg_humidity) ** 2 for h in humidity_readings) / len(humidity_readings)

# Filter out unstable initial readings using itertools.dropwhile
clean_temps = list(itertools.dropwhile(lambda t: t < 22.0, sorted(temperature_readings)))

# Base pressure derived from average of clean temperature data
base_temperature = sum(clean_temps) / len(clean_temps)
base_pressure = (base_temperature * 1.82) + 10.5  # Hypothetical physical model

# Secondary adjustment path (semi-relevant but not used directly)
raw_pressure_estimate = (sum(temperature_readings[:4]) * 1.75) + 12.1
temp_correction = abs(base_pressure - raw_pressure_estimate) * 0.1  # Dead-end computation

# Compute wind effect index (distractor)
wind_speeds = [3.2, 4.1, 2.8, 3.9, 4.5]
winds_above_threshold = [w for w in wind_speeds if w > 3.5]
wind_effect_index = len(winds_above_threshold) * 0.25

# Determine correction factor based on combinatorial interaction of conditions
combinations = list(itertools.combinations([22.3, 23.1, 24.0], 2))
effective_pairs = [pair for pair in combinations if abs(pair[0] - pair[1]) < 1.0]
pair_count = len(effective_pairs)

if pair_count >= 2:
    correction_factor = 1.15
else:
    correction_factor = 1.05

# Final pressure calibration step
final_pressure = base_pressure * correction_factor

# Extraneous post-calculation (irrelevant to final_pressure)
adjusted_final = final_pressure + (wind_effect_index * 0.85)
normalized_value = round(adjusted_final, 2)

print(f"Result: {final_pressure}")