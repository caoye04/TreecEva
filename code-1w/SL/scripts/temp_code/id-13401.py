from collections import defaultdict, Counter

# Simulated sensor array data with noise and calibration offsets
sensor_readings = [107, 214, 198, 205, 107, 312, 198, 409, 214, 501]
calibration_map = {'offset_a': 13, 'offset_b': -7, 'gain': 1.05}

# Irrelevant auxiliary processing: frequency analysis (distractor)
frequency_count = Counter(sensor_readings)
dominant_reading = frequency_count.most_common(1)[0][1]

# Noise filter simulation using sliding window (partially relevant)
filtered_values = []
for i in range(2, len(sensor_readings)):
    window_avg = (sensor_readings[i-2] + sensor_readings[i-1] + sensor_readings[i]) / 3
    filtered_values.append(int(window_avg))

# Secondary derived metrics (distractors)
rolling_deltas = [filtered_values[i] - filtered_values[i-1] for i in range(1, len(filtered_values))]
spike_count = sum(1 for d in rolling_deltas if d > 50)

# Core diagnostic computation chain (target logic)
base_aggregate = sum(r % 100 for r in sensor_readings)  # Focus on last two digits

# Apply gain from calibration map (relevant)
scaled_base = base_aggregate * calibration_map['gain']

# Conditional adjustment based on pattern detection
even_cluster = [r for r in sensor_readings if r % 2 == 0]
if len(even_cluster) > 4:
    scaling_modifier = 0.9
else:
    scaling_modifier = 1.1

adjusted_total = int(scaled_base * scaling_modifier)

# Decoy complex transformation using slicing and case conversion (irrelevant)
status_flags = ['OK', 'ERR', 'WARN', 'OK', 'OK']
flag_summary = ''.join(status_flags).lower().replace('err', 'FATAL')
summary_length = len(flag_summary)  # Red herring

# Hidden correction factor derived from duplicate analysis
dup_stats = defaultdict(int)
for val in sensor_readings:
    dup_stats[val] += 1
duplicate_classes = [k for k, v in dup_stats.items() if v > 1]
correction_factor = sum(d % 10 for d in duplicate_classes)  # Units digit sum of duplicates

# Primary aggregation
aggregate_score = adjusted_total // 3

# Key assignment statement
final_diagnostic = aggregate_score + correction_factor

# Dead code path (decoy function)
def compute_resilience_index(data):
    return sum(d.bit_length() for d in data) % 100

# Unused intermediate
redundant_metric = compute_resilience_index(sensor_readings)

# Output target result
print(f"Result: {final_diagnostic}")