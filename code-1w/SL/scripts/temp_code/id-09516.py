from collections import defaultdict, Counter

# Simulated sensor data: (timestamp, heart_rate, movement_index)
sensor_readings = [
    (1001, 72, 3), (1002, 68, 1), (1003, 88, 7), (1004, 75, 2), (1005, 63, 0),
    (1006, 95, 9), (1007, 77, 4), (1008, 83, 6), (1009, 70, 1), (1010, 80, 5)
]

# Irrelevant baseline data (distractor)
baseline_temperatures = [36.1, 36.5, 37.0, 35.9, 36.8, 37.2, 36.4, 36.9, 36.0, 37.1]

# Misleading preprocessing
offset_map = {t: t % 1000 for t, _, _ in sensor_readings}
temp_offset = sum(offset_map.values()) // len(offset_map)  # Red herring computation

# Data transformation with distractors
duplicate_flags = [False] * len(sensor_readings)
for i, (t, hr, mi) in enumerate(sensor_readings):
    if i > 0 and hr == sensor_readings[i-1][1]:
        duplicate_flags[i] = True

# Unused function (dead code path)
def analyze_temperature(data):
    avg = sum(data) / len(data)
    return {'mean': avg, 'deviations': [abs(x - avg) for x in data]}

# Another decoy function doing nothing relevant
def calculate_entropy(values):
    freq = Counter(values)
    total = len(values)
    entropy = 0
    for count in freq.values():
        p = count / total
        entropy -= p * (p ** 0.5)  # Not actual entropy, just looks plausible
    return round(entropy, 3)

# Real processing begins here — buried among noise
def extract_peaks(data, min_intensity=70):
    peaks = []
    for i, (_, hr, mi) in enumerate(data):
        if hr >= min_intensity:
            peaks.append((i, hr, mi))
    return peaks

# Secondary filter based on movement correlation
def filter_by_correlation(peaks, raw_data, movement_threshold=5):
    correlated = []
    index_set = {p[0] for p in peaks}
    for idx, _, mi in raw_data:
        pos = idx - 1001
        if pos in index_set and mi >= movement_threshold:
            correlated.append(pos)
    return correlated

# Main aggregation logic
def compute_stress_index(peaks, correlated_indices, base=1.5):
    index_val = len(peaks) * base
    for i, (_, hr, mi) in enumerate(peaks):
        if i in correlated_indices:
            index_val += (hr - 70) * 0.3 + mi * 0.7
    return round(index_val, 4)

# Auxiliary mapping (partially used)
severity_map = defaultdict(lambda: 'normal')
for level in range(5, 8):
    severity_map[level] = 'elevated'
for level in range(8, 10):
    severity_map[level] = 'high'

# Distractor list comprehension
snapshot_momenta = [mi ** 2 for _, _, mi in sensor_readings if mi > 4]
snapshot_total = sum(snapshot_momenta)  # Looks important but unused later

# Actual pipeline
health_data = extract_peaks(sensor_readings)
correlated_positions = filter_by_correlation(health_data, sensor_readings)
stress_level = compute_stress_index(health_data, correlated_positions)

# Complex conditional assignment with red herrings
threshold = 6.5
if stress_level > threshold:
    category = 'alert'
    multiplier = 2.1
elif stress_level > threshold - 1.5:
    category = 'watch'
    multiplier = 1.6
else:
    category = 'normal'
    multiplier = 1.0

# Decoy dictionary construction
summary_snapshot = {
    'readings_count': len(sensor_readings),
    'peak_count': len(health_data),
    'correlated_count': len(correlated_positions),
    'stress_raw': stress_level,
    'multiplier_applied': multiplier,
    'temp_baseline': round(sum(baseline_temperatures) / len(baseline_temperatures), 2),
    'offset_magic': temp_offset,
    'phantom_metric': calculate_entropy([hr for _, hr, _ in sensor_readings])
}

# Final computation chain — this is where answer comes from
adjustment_factor = 0.85 if summary_snapshot['correlated_count'] > 2 else 1.15
effective_multiplier = multiplier * adjustment_factor

# Bit manipulation distraction
encoded_flag = 0
for pos in correlated_positions:
    encoded_flag ^= (pos << 2) | 1
encoded_flag &= 0xFF  # Limit to 8 bits

# Critical statement: this determines the final answer
final_score = int((stress_level * effective_multiplier + encoded_flag) * 10)

# Output result as required
print(f"Target result: {final_score}")