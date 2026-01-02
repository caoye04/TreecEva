import itertools

# Sensor array diagnostics with noise filtering and calibration
raw_readings = [18, -5, 22, 47, 33, 12, 99, 4, 29, 38, 51, 3]
calibration_map = {i: val % 7 for i, val in enumerate([14, 21, 8, 15, 22, 9, 16, 23, 30, 37, 44, 51])}
offset_table = [x ** 2 % 11 for x in range(12)]
baseline_shift = sum(offset_table) // len(offset_table)

# Irrelevant statistical summary (distractor)
deviation_report = []
for i in range(len(raw_readings)):
    deviation_report.append((raw_readings[i] - baseline_shift) ** 2)
mean_squared = sum(deviation_report) / len(deviation_report)
rms_noise = mean_squared ** 0.5

# Noise threshold calculated via modular arithmetic
noise_threshold = (sum(calibration_map.values()) * 2) % 25

# Primary filtering logic: exclude outliers and apply positional mask
filtered_data = []
for idx, reading in enumerate(raw_readings):
    if abs(reading - baseline_shift) <= noise_threshold:
        if idx % 3 != 0:  # Skip every third sensor (valid design constraint)
            filtered_data.append(reading + offset_table[idx % 12])

# Decoy transformation chain (dead path)
shadow_buffer = raw_readings.copy()
for _ in range(3):
    shadow_buffer = [b ^ 17 for b in shadow_buffer if b % 4 != 2]
compression_flag = len(shadow_buffer) < 5

# Real processing begins: group by magnitude using string-based categorization
magnitude_labels = []
for val in filtered_data:
    label = ''
    if val < 20:
        label = 'low'
    elif val < 40:
        label = 'med'
    else:
        label = 'high'
    magnitude_labels.append(label)

# Use itertools to generate rolling consistency check (distractor)
pairwise_consistency = []
for a, b in itertools.pairwise(magnitude_labels):
    pairwise_consistency.append(1 if a == b else 0)
stability_score = sum(pairwise_consistency)

# Calibration factor derived from map and string analysis
key_sequence = ''.join([str(calibration_map[i]) for i in range(7)])
rotation_index = int(key_sequence[2]) * int(key_sequence[5]) % 7
calibration_factor = rotation_index + sum(int(d) for d in key_sequence if d in '345')

# Core data transformation: apply decay model and aggregate
processed_chain = []
decay_rate = 0.85
for i, val in enumerate(filtered_data):
    adjusted = val * (decay_rate ** i)
    processed_chain.append(round(adjusted, 3))

# Final diagnostic computation (target execution point)
def process_readings(data_list, calib):
    total = 0
    for x in data_list:
        total += (x * calib) % 19
    return total + (calib * 2)

final_diagnostic = process_readings(filtered_data, calibration_factor)

# Output required format
print(f"Result: {final_diagnostic}")