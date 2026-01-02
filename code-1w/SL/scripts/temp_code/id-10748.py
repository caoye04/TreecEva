def sensor_calibration(sequence):
    calibrated = []
    for i, val in enumerate(sequence):
        if i % 3 == 0:
            calibrated.append(val * 1.05)
        elif i % 4 == 0:
            calibrated.append(val * 0.95)
        else:
            calibrated.append(val * 1.01)
    return [round(x, 2) for x in calibrated]

# Irrelevant helper (dead function - red herring)
def compute_flux_capacitance(values):
    total = 0
    for v in values:
        total += (v ** 2) * 0.001
    return total  # Never used

# Another decoy transformation
def transform_coordinates(data):
    result = []
    for item in data:
        x = item * 0.7 + 2
        y = item * 1.3 - 1
        result.append((x, y))
    return result  # Computed but unused

# Real processing chain
def preprocess_signal(raw):
    filtered = [x for x in raw if x > 50 and x < 950]  # Filter noise
    normalized = [x / 10 for x in filtered]
    shifted = [x - 25 for x in normalized]
    return shifted

# Distractor: fake aggregation
def aggregate_patterns(samples):
    stats = {}
    stats['peak'] = max(samples)
    stats['trough'] = min(samples)
    stats['midpoint'] = (stats['peak'] + stats['trough']) / 2
    stats['range'] = stats['peak'] - stats['trough']
    return stats  # Used only for distraction

# Core logic disguised among noise
def generate_threshold_map(config):
    base_map = {i: (i * 0.75) for i in range(1, 11)}
    adjustment = config.get('adj', 1.2)
    offset = config.get('offset', -0.5)
    return {k: v * adjustment + offset for k, v in base_map.items()}

# Real analysis function
def analyze_readings(data, thresholds):
    count_breaches = 0
    for idx, reading in enumerate(data):
        key = (idx % 10) + 1
        if key not in thresholds:
            continue
        ref = thresholds[key]
        if reading > ref:
            count_breaches += 1
    temp_result = count_breaches * 117
    extra_offset = 0
    for i in range(1, 6):
        if i % 2 == 0:
            extra_offset += i * 3
        else:
            extra_offset -= i * 2
    # extra_offset = (-2) + 6 + (-6) + 12 + (-10) = 0
    final_score = temp_result + extra_offset
    return final_score

# Unused diagnostic
baseline_samples = [88, 102, 95, 110, 100, 90, 85, 98]
sample_flux = compute_flux_capacitance(baseline_samples)  # Dead computation

# Main data pipeline
raw_input_stream = [
    100, 850, 700, 920, 150, 960, 400, 880, 650, 770,
    500, 910, 300, 870, 730, 940, 600, 890, 550, 930
]

processed_signal = preprocess_signal(raw_input_stream)
# Apply calibration (relevant but indirect)
calibrated_readings = sensor_calibration(processed_signal)

# Fake pattern analysis (distractor)
pattern_stats = aggregate_patterns(calibrated_readings)

# Generate actual threshold map
config_settings = {'adj': 1.6, 'offset': -3.0}
threshold_map = generate_threshold_map(config_settings)

# Transform to dummy coordinates (red herring)
dummy_coords = transform_coordinates(calibrated_readings)  # Not used

# Critical statement
final_diagnostic = analyze_readings(processed_signal, threshold_map)

print(f"Result: {final_diagnostic}")