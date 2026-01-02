import itertools

# Sensor array diagnostic system with noise filtering and calibration
raw_readings = [145, 128, 139, 152, 130, 141, 133, 144, 137, 136, 143, 132, 147, 135]
calibration_factor = 0.92
noise_threshold = 10
baseline_offset = 125
dummy_counter = 0

# Irrelevant pre-processing: dummy transformations (red herring)
temp_buffer = []
for val in raw_readings:
    temp_buffer.append((val + 7) * 3 % 256)

# Real preprocessing: filter out noise deviations from moving window average
smoothed_readings = []
window_size = 3
for i in range(len(raw_readings)):
    start = max(0, i - window_size // 2)
    end = min(len(raw_readings), i + window_size // 2 + 1)
    window_avg = sum(raw_readings[start:end]) / (end - start)
    if abs(raw_readings[i] - window_avg) <= noise_threshold:
        smoothed_readings.append(raw_readings[i])

# Decoy statistical analysis (dead path)
outlier_report = []
for x in raw_readings:
    deviation = abs(x - sum(raw_readings)/len(raw_readings))
    if deviation > 15:
        outlier_report.append((x, deviation))

# Distractor: unused function simulating alternate processing path
def legacy_process(data):
    result = 0
    for d in data:
        result ^= d
        result = (result * 7) % 100
    return result

# Distractor: fake aggregation chain
aggregation_key = 0
for chunk in itertools.batched(smoothed_readings, 2):
    if len(chunk) == 2:
        aggregation_key += chunk[0] * chunk[1] % 19

# Real signal: identify stable phase readings using grouping
stable_groups = []
for k, g in itertools.groupby(smoothed_readings, key=lambda x: x // 10):
    group_list = list(g)
    if len(group_list) >= 3:
        stable_groups.append(group_list)

# Extract primary stable sequence (only first qualifying group used)
primary_sequence = stable_groups[0] if stable_groups else [130, 133, 132]

# Distractor: unused bit manipulation pyramid
pyramid_sum = 0
for i in range(len(primary_sequence)):
    for j in range(i + 1):
        pyramid_sum += primary_sequence[j] & (i + 1)

# Secondary filter: exclude values deviating from local median
sorted_seq = sorted(primary_sequence)
median_val = sorted_seq[len(sorted_seq)//2]
filtered_data = [x for x in primary_sequence if abs(x - median_val) <= 3]

# Fake checksum chain (misleading intermediate)
checksum = 0
for idx, num in enumerate(filtered_data):
    checksum += (num ^ idx) * (idx + 1)
checksum = checksum % 997

# Critical transformation: apply calibration and compute diagnostic mean
weighted_sum = 0
weight_total = 0
for i, reading in enumerate(filtered_data):
    weight = 1 + (len(filtered_data) - i)  # Emphasize later readings
    weighted_sum += reading * weight * calibration_factor
    weight_total += weight

final_diagnostic = int(weighted_sum / weight_total) if weight_total > 0 else 0

# Distractor: unused combinatorial sweep
combo_score = 0
for combo in itertools.combinations_with_replacement(filtered_data, 2):
    combo_score += abs(combo[0] - combo[1]) * 2

# Output the target result
print(f"Result: {final_diagnostic}")