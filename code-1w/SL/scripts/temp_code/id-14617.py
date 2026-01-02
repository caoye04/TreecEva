from collections import defaultdict, Counter

# Simulated sensor data stream with noise and redundant readings
timestamps = [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008]
sensor_a = [23.5, 24.1, 23.9, 24.0, 24.2, 24.5, 25.0, 25.1]
sensor_b = [22.8, 24.3, 23.7, 24.2, 24.1, 24.6, 24.9, 25.3]

# Irrelevant auxiliary data (distractor)
legacy_codes = ['A7', 'B2', 'C9', 'D4', 'E1', 'F8', 'G5', 'H6']
lookup_table = {k: v for k, v in zip(legacy_codes, timestamps)}

# Data alignment using zip and enumerate (relevant)
aligned_data = []
for i, (ts, a, b) in enumerate(zip(timestamps, sensor_a, sensor_b)):
    diff = abs(a - b)
    avg = (a + b) / 2
    aligned_data.append((ts, avg, diff))

# Noise filtering threshold (misleading intermediate computation)
excessive_noise_count = sum(1 for _, _, d in aligned_data if d > 0.5)  # Only 1 pair exceeds this

# Compute time-weighted trend (dead code path - not used later)
time_weighted_sum = 0.0
for idx, (ts, avg_val, _) in enumerate(aligned_data):
    time_weighted_sum += avg_val * (idx + 1)

total_weights = sum(range(1, len(aligned_data) + 1))
trend_estimate = time_weighted_sum / total_weights if total_weights else 0

# Focus on stable readings only (diff < 0.4) - actual relevant filter
stable_readings = [avg for _, avg, diff in aligned_data if diff < 0.4]

# Compute base aggregate score using list comprehension
aggregate_score = sum([round(x, 1) * 1.05 for x in stable_readings])

# Decoy statistical analysis (irrelevant)
reading_frequencies = Counter([round(x, 0) for x in sensor_a + sensor_b])
mode_estimate = reading_frequencies.most_common(1)[0][0]

# Simulate calibration offset from multiple sources (mixed relevance)
calibration_offsets = defaultdict(float)
calibration_offsets['temp_drift'] = -0.3
calibration_offsets['humidity_comp'] = 0.15
calibration_offsets['aging_factor'] = -0.08

offset_total = sum(calibration_offsets.values())

# Secondary adjustment based on environmental heuristics (partially misleading)
environment_flags = [True, False, True, True, False]
heuristic_penalty = 0
for flag in environment_flags:
    if not flag:
        heuristic_penalty += 0.05

# Correction factor derived from offset and penalty
correction_factor = round(offset_total - heuristic_penalty, 2)

# Dead recursive function (decoy)
def calculate_residual(n):
    if n <= 1:
        return 1
    return n * calculate_residual(n - 2)

# Unused recursive call (distractor)
_ = calculate_residual(5)

# Final diagnostic fusion (key statement)
final_diagnostic = aggregate_score + correction_factor

print(f"Result: {final_diagnostic}")