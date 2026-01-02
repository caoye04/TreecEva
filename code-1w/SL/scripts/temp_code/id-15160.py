import itertools

# Simulated sensor array data (temperature, pressure, humidity)
sensor_readings = [
    (23.5, 101.3, 45.0), (24.1, 102.0, 47.2), (19.8, 99.8, 50.1),
    (22.7, 100.9, 44.3), (25.3, 103.1, 48.7), (18.9, 98.7, 52.0),
    (20.2, 99.1, 46.5), (26.0, 104.2, 43.9), (21.8, 101.7, 49.0),
    (19.5, 97.6, 55.3)
]

# Irrelevant baseline constants for distraction
temperature_baseline = 20.0
pressure_baseline = 100.0
humidity_baseline = 45.0

# Decoy transformation: character counting in sensor labels (irrelevant)
sensor_labels = ['T1', 'P2', 'H3', 'T4', 'P5', 'H6', 'T7', 'P8', 'H9', 'T10']
label_char_count = sum(len(label) for label in sensor_labels)  # Dead-end computation

# Misleading intermediate: case conversion on dummy status tags
status_tags = ['OK', 'ERROR', 'OK', 'WARNING', 'OK', 'ERROR', 'OK', 'OK', 'WARNING', 'OK']
lower_tags = [tag.lower() for tag in status_tags]  # Unused path

# Real processing begins: filter readings where temp > 20 and pressure > 100
filtered_data = [r for r in sensor_readings if r[0] > 20 and r[1] > 100]

# Generate threshold map using itertools.cycle for patterned assignment (relevant)
cycle_pattern = itertools.cycle([1.2, 0.8, 1.0])
threshold_map = {i: next(cycle_pattern) for i in range(len(filtered_data))}

# Spurious summation: accumulate dummy index sums (distractor)
dummy_accumulator = 0
for i in range(len(sensor_readings)):
    if i % 2 == 0:
        dummy_accumulator += i * 2
    else:
        dummy_accumulator -= i

# Decoy function that is never called
def analyze_anomalies(data):
    return sum(1 for x in data if x[0] < 19 or x[1] < 99)

# Auxiliary irrelevant list comprehension with slicing red herring
extended_diagnostics = [abs(x[0] - x[1]) for x in sensor_readings[::2] if x[2] > 45]
truncated_diag = extended_diagnostics[1:3]  # Nowhere used

# Core logic: compute deviation scores adjusted by threshold multiplier
def process_readings(readings, thresholds):
    results = []
    for idx, (temp, press, hum) in enumerate(readings):
        # Composite score: weighted combination
        base_score = temp * 1.1 + press * 0.9 - hum * 0.5
        # Adjustment factor from cycling threshold
        adjustment = thresholds.get(idx, 1.0)
        adjusted_score = base_score * adjustment
        results.append(adjusted_score)
    # Final aggregation: alternating sum pattern
    final_sum = 0
    for i, val in enumerate(results):
        final_sum += val if i % 2 == 0 else -val
    return int(round(final_sum))

# Execute main computation
final_diagnostic = process_readings(filtered_data, threshold_map)

# Print result as required
print(f"Result: {final_diagnostic}")