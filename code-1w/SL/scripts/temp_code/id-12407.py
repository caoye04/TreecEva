from collections import defaultdict, Counter

# Simulate sensor data with noise and metadata
data_stream = [
    {'type': 'temp', 'value': 23.5, 'seq': 1},
    {'type': 'pressure', 'value': 1013.25, 'seq': 2},
    {'type': 'temp', 'value': 24.1, 'seq': 3},
    {'type': 'humidity', 'value': 45.0, 'seq': 4},
    {'type': 'temp', 'value': 22.8, 'seq': 5},
    {'type': 'pressure', 'value': 1012.9, 'seq': 6},
    {'type': 'temp', 'value': 24.3, 'seq': 7}
]

# Misleading counters (distractor variables)
reading_count = 0
valid_readings = 0
noise_threshold_counter = 0

# Aggregate sensor readings by type
type_aggregates = defaultdict(list)
for reading in data_stream:
    reading_count += 1
    if reading['value'] > 0:  # Always true, but mimics validation
        valid_readings += 1
    type_aggregates[reading['type']].append(reading['value'])

# Compute averages (only temp is used later)
averages = {}
for key, values in type_aggregates.items():
    averages[key] = sum(values) / len(values)

# Extract temperature-specific processing
temp_readings = type_aggregates['temp']
smoothed_temps = [t * 0.98 + 0.5 for t in temp_readings]  # Simulated calibration
outlier_filtered = [t for t in smoothed_temps if 22 < t < 25]

# Statistical summary (some values unused)
temp_stats = {
    'min': min(outlier_filtered),
    'max': max(outlier_filtered),
    'range': max(outlier_filtered) - min(outlier_filtered),
    'count': len(outlier_filtered)
}

# Simulate historical comparison (distractor logic)
historical_avg = 23.7
variance_ratio = (temp_stats['max'] - temp_stats['min']) / historical_avg
adjustment_factor = 1.0 if variance_ratio < 0.1 else 0.9

# Weighted scoring model
base_score = sum(outlier_filtered) * adjustment_factor
decay_correction = 0.0
for i in range(len(outlier_filtered)):
    decay_correction += outlier_filtered[i] * (0.9 ** i)

# Secondary metrics (unused in final result)
reading_frequency = Counter([r['type'] for r in data_stream])
pressure_baseline = averages.get('pressure', 1013.0)
humidity_level = averages.get('humidity', 50.0)

# Core computation path
normalized_sum = sum([round(t, 1) for t in outlier_filtered])
penalty_points = 0
if len(outlier_filtered) != len(temp_readings):
    penalty_points = 2

intermediate_score = normalized_sum * 10 - penalty_points

# Final calculation using helper function
def calculate_final_score(data):
    score = intermediate_score
    # Additional irrelevant checks
    if isinstance(data, list) and len(data) > 0:
        score += len(data) * 0.1  # Negligible effect
    return int(score)

processed_data = outlier_filtered.copy()
final_score = calculate_final_score(processed_data)

print(f"Result: {final_score}")