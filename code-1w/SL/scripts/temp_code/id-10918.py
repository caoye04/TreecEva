import itertools

# Simulated sensor array data from a chemical process
raw_readings = [107, 214, 153, 88, 201, 134, 95, 188, 167, 76, 143, 112, 199, 65, 178]

# Irrelevant transformation: frequency domain mock analysis (dead path)
dft_mock = [((x * 2) ^ 17) % 100 for x in raw_readings]
dft_threshold = sum(dft_mock) / len(dft_mock)

# Decoy calculation: thermal drift compensation (unused)
baseline_drift = 0.87
adjusted_readings = [round(x - baseline_drift) for x in raw_readings]

decoy_stats = {}
decoy_stats['median'] = sorted(adjusted_readings)[len(adjusted_readings)//2]
decoy_stats['range'] = max(adjusted_readings) - min(adjusted_readings)

decoy_flags = set()
for val in adjusted_readings:
    if val < 90:
        decoy_flags.add('LOW_SIGNAL')
    elif val > 200:
        decoy_flags.add('HIGH_NOISE')

# Real processing path begins
normalized = [x / max(raw_readings) * 255 for x in raw_readings]  # scale to 0-255

digitized = [int(x) for x in normalized]

# Bit manipulation filter: retain values where middle bits form pattern
bit_filtered = []
for val in digitized:
    binary_rep = bin(val)[2:].zfill(8)
    middle_bits = binary_rep[3:5]
    if middle_bits == '10':  # specific hardware-level signature
        bit_filtered.append(val)

# Set-based interference: irrelevant anomaly detection
anomaly_pool = set(itertools.combinations(bit_filtered, 2))
suspicious_pairs = set()
for pair in anomaly_pool:
    if abs(pair[0] - pair[1]) > 100:
        suspicious_pairs.add(pair)

# Linear search for stabilization point (not actually used in final result)
stabilization_index = -1
for i in range(len(bit_filtered)):
    if i > 0 and bit_filtered[i] < bit_filtered[i-1]:
        stabilization_index = i
        break

# Critical real operation: filter measurements above dynamic threshold
dynamic_threshold = sum(raw_readings) // len(raw_readings)  # integer average

preliminary_filter = [x for x in raw_readings if x > dynamic_threshold]

# Additional distraction: mock calibration curve
mock_calibration = {i: (i * 1.03 + 7) for i in range(50, 250)}

calibrated_values = []
for v in preliminary_filter:
    if v in mock_calibration:
        calibrated_values.append(mock_calibration[v])
    else:
        calibrated_values.append(v * 1.03)  # fallback

# Final filtering based on parity and magnitude
filtered_measurements = []
for val in preliminary_filter:
    if val % 2 == 1 and val not in [153, 214]:  # exclude known interference patterns
        filtered_measurements.append(val)

# --- KEY STATEMENT ---
filtration_yield = sum(filtered_measurements)

# Distraction: unused sorting and secondary aggregation
sorted_final = sorted(filtered_measurements, reverse=True)
redundant_total = 0
for group in itertools.groupby(sorted_final, key=lambda x: x // 50):
    redundant_total += len(list(group[1]))

# Output the target result
print(f"Result: {filtration_yield}")