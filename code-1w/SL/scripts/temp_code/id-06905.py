def analyze_signal(samples):
    magnitude = sum(abs(s) for s in samples)
    normalized = [s / (magnitude + 1e-9) for s in samples]
    energy = sum(s**2 for s in normalized)
    return energy if energy > 0.1 else 0.0

# Irrelevant helper (dead function - not used)
def deprecated_filter(x):
    return [v for v in x if v % 3 == 0]

# Unused transformation chain
temp_offset = 273.15
scaling_factor = 1.8
calibration_data = {f'node_{i}': (i * 0.7) % 1.0 for i in range(12)}

# Simulated sensor readings (mock data)
sensor_readings = [
    [1.2, -0.8, 3.1, 0.5],
    [2.3, -1.1, 0.9, 4.2],
    [-0.7, 0.6, 1.8, -2.4],
    [3.0, 1.1, -0.3, 0.9]
]

# Misleading precomputation (unused later)
baseline_stats = {
    'avg': sum(sum(row) for row in sensor_readings) / len(sensor_readings),
    'peak': max(max(abs(x) for x in row) for row in sensor_readings)
}

# Distractor: complex-looking but unused mapping
encoding_map = dict(zip(['A','B','C','D'], [2**i for i in range(4)]))

# Real processing begins here
processed_frames = []
for idx, frame in enumerate(sensor_readings):
    if idx % 2 == 0:
        filtered = [x for x in frame if x > 0]
    else:
        filtered = [x for x in frame if x < 0]
    score = analyze_signal(filtered)
    processed_frames.append((idx, score))

# Transform using enumerate and zip (relevant)
indexed_scores = [s for _, s in processed_frames]
ranked = sorted(enumerate(indexed_scores), key=lambda x: x[1], reverse=True)
top_ranks = [i for i, _ in ranked[:2]]

# Create composite structure
transformed_data = list(zip(
    [r[0] for r in ranked],
    [round(r[1] * 100, 2) for r in ranked],
    ['high' if i in top_ranks else 'low' for i in range(len(ranked))]
))

# Threshold logic with decoy conditions
threshold_map = {}
for i, (_, val, _) in enumerate(transformed_data):
    if i == 0:
        threshold_map[i] = 85.0
    elif val > 50.0:
        threshold_map[i] = 70.0  # Unused branch
    else:
        threshold_map[i] = 40.0

# Decoy dictionary update (never used)
threshold_map.update({'legacy_mode': 0.0})

# Critical computation path
status_flags = []
for index, entry in enumerate(transformed_data):
    raw_value = entry[1]
    threshold = threshold_map.get(index, 50.0)
    flag = 'PASS' if raw_value >= threshold else 'FAIL'
    status_flags.append(flag)

# Final diagnostic depends only on count of PASS flags
pass_count = status_flags.count('PASS')

# Secondary influence from ranking position
bonus = sum(1 for i, _ in ranked if i < 2 and i in top_ranks)  # Always true, but convoluted

# Final result calculation
final_diagnostic = (pass_count * 1000) + (bonus * 50)

# Print result as required
print(f"Result: {final_diagnostic}")