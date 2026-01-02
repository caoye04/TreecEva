def compute_equilibrium(data, weights):
    total = 0
    weight_sum = sum(weights)
    for i, value in enumerate(data):
        weighted_val = value * weights[i % len(weights)]
        if i % 2 == 0:
            total += weighted_val ** 0.5
        else:
            total -= weighted_val / 2
    return round(total, 4)

# Simulate environmental sensor data with noise filtering
raw_readings = [144, 169, 196, 225, 256, 289, 324]
dummy_offsets = [5, -3, 7, -10, 12]
adjusted_readings = [x - 10 for x in raw_readings]

# Filter every third reading as outlier removal
filtered_data = adjusted_readings[::3]

# Irrelevant transformation: frequency analysis (not used)
freq_analysis = []
for i in range(len(raw_readings)):
    freq_analysis.append(raw_readings[i] // (i + 1) if i > 0 else raw_readings[0])

# Impact factors from external calibration (used in computation)
impact_factors = [0.8, 1.2, 0.9]

# Misleading intermediate calculation (dead code path)
aggregation_buffer = 0
for val in adjusted_readings:
    aggregation_buffer += val * 0.1  # Not used later

# State tracking variables for debugging (semi-relevant)
processing_log = []
for idx, val in enumerate(filtered_data):
    processing_log.append(f'Step {idx}: {val}')

# Core computation block
equilibrium_score = compute_equilibrium(filtered_data, impact_factors)

# Redundant smoothing pass (does not alter result)
temp_copy = filtered_data[:]
scaled_vals = [v * 0.99 for v in temp_copy]

# Final output
print(f'Target result: {equilibrium_score}')