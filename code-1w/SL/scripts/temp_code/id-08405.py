from itertools import compress

# Simulate sensor readings with noise filtering
temp_readings = [23.5, 24.1, 24.0, 23.9, 25.2, 26.0, 25.8]
valid_mask = [r > 24.0 for r in temp_readings]
filtered_readings = list(compress(temp_readings, valid_mask))

# Compute harmonic mean components only for stable readings above threshold
harmonic_values = []
for val in filtered_readings:
    if val < 26.0:
        harmonic_values.append(1 / val)

# Distractor: unused variable simulating another metric
dummy_rms = sum(x ** 2 for x in temp_readings) / len(temp_readings)

total_harmonic_score = sum(harmonic_values)
print(f"Result: {total_harmonic_score}")