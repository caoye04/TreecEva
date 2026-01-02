def analyze_signal(samples, threshold=0.75):
    """ Analyze sensor signal with noise filtering and pattern detection """
    filtered = [s for s in samples if abs(s) > threshold]
    if not filtered:
        return 0
    
    # Irrelevant transformation (distractor)
    inverted = list(map(lambda x: 1/(x + 1e-5), filtered))
    smoothed = [filtered[i] for i in range(len(filtered)) if i == 0 or abs(filtered[i] - filtered[i-1]) < 2.0]

    # Real computation path
    magnitude = sum(abs(x) for x in filtered)
    peaks = len([i for i in range(1, len(smoothed)-1) if smoothed[i] > smoothed[i-1] and smoothed[i] > smoothed[i+1]])
    return magnitude * (peaks + 1)

# Simulated sensor data (real input)
sensor_data = [0.1, -0.3, 1.2, -1.5, 0.9, 2.3, -0.4, 1.8, -2.1, 0.6]

# Irrelevant data structures (distractors)
baseline_profiles = {
    'A': [0.2, 0.4, 0.6],
    'B': [0.1, -0.1, 0.3],
    'C': []
}

# Unused helper function (dead code path)
def deprecated_normalize(vec):
    norm = sum(x**2 for x in vec) ** 0.5
    return [x/norm for x in vec] if norm else vec

# Another distractor: irrelevant bit manipulation
decoys = []
for i in range(5):
    temp_val = (i << 3) ^ 0xAA
    decoys.append(temp_val % 10)

# Configuration with misleading fields
config = {
    'sampling_rate': 44100,
    'calibration_offset': -0.05,
    'active_filters': ['low_pass', 'notch'],
    'debug_mode': True,
    'weighting': [0.1, 0.2, 0.4, 0.2, 0.1],
    'legacy_flag': False
}

# Transform data using zip and enumerate (required Python features)
transformed_data = []
for idx, (i, val) in enumerate(zip(range(len(sensor_data)), sensor_data)):
    if idx % 2 == 0:
        transformed_data.append(val * 1.5)
    else:
        transformed_data.append(val * 0.8)

# Unused accumulator (red herring)
total_energy = 0.0
for reading in transformed_data:
    total_energy += reading ** 2

# Real processing chain begins here
def process_metrics(data, cfg):
    # Distractor variables
    temp_results = []
    dummy_acc = 0
    for j in range(3):
        dummy_acc += j * 100  # Dead computation
    
    # Actual relevant logic
    valid_readings = [x for x in data if x != 0]
    if len(valid_readings) == 0:
        base_score = 0
    else:
        avg = sum(valid_readings) / len(valid_readings)
        variance = sum((x - avg)**2 for x in valid_readings) / len(valid_readings)
        base_score = abs(avg) * (1 + variance)
    
    # Secondary metric from original signal analysis
    secondary = analyze_signal(sensor_data, threshold=0.5)
    
    # Final combination
    final_weight = cfg['weighting'][2]  # Use only one element from weighting
    return int(round(base_score * secondary * final_weight))

# Execute main logic
intermediate_flag = False
if len(transformed_data) > 5:
    intermediate_flag = True

# Key execution point
final_diagnostic = process_metrics(transformed_data, config)

# Output result as required
print(f"Target result: {final_diagnostic}")