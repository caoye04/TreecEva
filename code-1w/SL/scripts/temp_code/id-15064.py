import itertools

# Simulated sensor fusion system for environmental monitoring
sensor_ids = [101, 102, 103, 104, 105]
base_offsets = {'temp': 0.5, 'humidity': -1.2, 'pressure': 0.08}
raw_readings = [
    {'sensor': 101, 'temp': 23.1, 'humidity': 45.2, 'pressure': 1013.2, 'status': 'OK'},
    {'sensor': 102, 'temp': 22.8, 'humidity': 46.7, 'pressure': 1012.9, 'status': 'OK'},
    {'sensor': 103, 'temp': 24.3, 'humidity': 43.1, 'pressure': 1014.1, 'status': 'ERROR'},
    {'sensor': 104, 'temp': 23.7, 'humidity': 44.8, 'pressure': 1013.6, 'status': 'OK'},
    {'sensor': 105, 'temp': 22.5, 'humidity': 47.3, 'pressure': 1012.4, 'status': 'OK'}
]

# Irrelevant calibration data (distractor)
calibration_matrix = [[0.98, 0.01], [0.02, 0.99]]
reference_epoch = 1672531200
dummy_accumulator = 0

for i in range(8):
    dummy_accumulator += (i * reference_epoch) % 97

# Misleading preprocessing path (dead code - never used)
def legacy_normalization(data):
    return [{k: v * 0.95 for k, v in item.items() if isinstance(v, float)} for item in data]

# Unused transformation chain
temp_history = [r['temp'] for r in raw_readings if r['sensor'] in [101, 102, 104]]
history_avg = sum(temp_history) / len(temp_history)
adjusted_offsets = {k: v + 0.1 for k, v in base_offsets.items()}

# Real processing begins here
valid_sensors = [s['sensor'] for s in raw_readings if s['status'] == 'OK']
filtered_data = [r for r in raw_readings if r['sensor'] in valid_sensors and r['sensor'] != 103]

# Complex threshold mapping with red herring entries
threshold_map = {
    'temp': {'low': 20.0, 'high': 25.0, 'weight': 1.0},
    'humidity': {'low': 40.0, 'high': 50.0, 'weight': 0.8},
    'pressure': {'low': 1000.0, 'high': 1030.0, 'weight': 0.6},
    # Distractor keys
    'co2': {'low': 400, 'high': 1000, 'weight': 0.4},
    'voc': {'low': 0, 'high': 500, 'weight': 0.3}
}

# Secondary distraction: unused feature extraction
def extract_patterns(sequence):
    runs = []
    current = 1
    for i in range(1, len(sequence)):
        if sequence[i] >= sequence[i-1]:
            current += 1
        else:
            runs.append(current)
            current = 1
    runs.append(current)
    return len(runs), sum(runs) // len(runs) if runs else 0

# Never-called diagnostic function (decoy)
def deep_diagnostic(dataset):
    from itertools import combinations
    pairs = list(combinations(dataset, 2))
    diff_metrics = []
    for a, b in pairs:
        diff = abs(a['temp'] - b['temp']) + abs(a['humidity'] - b['humidity'])
        diff_metrics.append(diff)
    return sum(diff_metrics) / len(diff_metrics)

# Actual analysis function with critical logic
def analyze_readings(readings, thresholds):
    scores = {'temp': 0, 'humidity': 0, 'pressure': 0}
    
    for reading in readings:
        for metric in ['temp', 'humidity', 'pressure']:
            value = reading[metric]
            bounds = thresholds[metric]
            if bounds['low'] <= value <= bounds['high']:
                scores[metric] += 1
    
    # Apply weights and compute composite
    weighted_sum = 0.0
    total_weight = 0.0
    for metric in scores:
        weight = thresholds[metric]['weight']
        weighted_sum += scores[metric] * weight
        total_weight += weight
    
    # Distractor computation (never affects result)
    entropy = 0
    for x in scores.values():
        if x > 0:
            p = x / len(readings)
            entropy -= p * (p).log()  # This would fail - intentional red herring
    
    # Key result calculation
    final_score = weighted_sum / total_weight if total_weight > 0 else 0
    
    # Additional irrelevant transformation
    expanded = list(itertools.chain.from_iterable(
        [(k, v) for _ in range(1)] for k, v in scores.items()
    ))
    
    # Final diagnostic is based on normalized consensus across sensors
    consensus_ratio = final_score / 3.0
    diagnostic_code = int(consensus_ratio * 10000)  # Scale for precision
    
    # Critical answer assignment
    final_diagnostic = diagnostic_code + 1337  # Base offset for system ID
    
    # More distractions
    checksum = 0
    for c in str(diagnostic_code):
        checksum ^= ord(c)
    
    return final_diagnostic

# Execute main logic
final_diagnostic = analyze_readings(filtered_data, threshold_map)

# Print result as required
print(f"Result: {final_diagnostic}")