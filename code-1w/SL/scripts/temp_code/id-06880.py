import math

# Simulated sensor fusion system for environmental monitoring
def analyze_readings(readings):
    filtered = [x for x in readings if x > -50 and x < 100]
    offset = sum(1 for x in readings if x < 0)
    baseline = sum(filtered) / len(filtered) if filtered else 0
    adjusted = [math.log(abs(x) + 1) * (-1 if x < 0 else 1) for x in filtered]
    return baseline, adjusted, offset

# Irrelevant auxiliary function - dead code path
# def deprecated_normalization(vec):
#     magnitude = sum(x**2 for x in vec) ** 0.5
#     return [x/magnitude for x in vec] if magnitude else vec

# Data calibration logic with red herring variables
def calibrate_sensor_data(raw_data):
    calibrated = {}
    temp_offset = 0
    pressure_factor = 1.0
    
    for key, values in raw_data.items():
        if 'temp' in key:
            avg = sum(values) / len(values)
            # Distractor computation
            variance = sum((x - avg) ** 2 for x in values) / len(values)
            temp_offset = math.sqrt(variance + 1e-9)
            calibrated[key] = [x - avg + temp_offset for x in values]
        elif 'pressure' in key:
            peak = max(values)
            # Misleading normalization
            normalized = [x / (peak + 1e-5) for x in values]
            pressure_factor = sum(normalized) / len(normalized)
            calibrated[key] = [x * pressure_factor for x in values]
        else:
            calibrated[key] = values  # Pass through
    
    # Decoy derived metrics
    dummy_metric_1 = temp_offset * pressure_factor
    dummy_metric_2 = sum(calibrated.get('temp_internal', []))
    
    return calibrated

# Core performance aggregation with bitwise weighting
weights = {
    'precision': 0b1010,  # Weight: 10
    'recall': 0b0110,      # Weight: 6
    'latency': 0b0001,     # Weight: 1
    'stability': lambda x: int(x * 100) & 0b1111  # Dynamic weight via lambda
}

# Conditional expression for adaptive thresholding
adaptive_threshold = lambda x: x > 0.7 if x < 1.0 else x > 0.95

metrics = {
    'precision': 0.85,
    'recall': 0.72,
    'latency': 0.33,
    'stability': 0.91
}

# Simulated raw data with irrelevant fields
raw_sensor_data = {
    'temp_internal': [23.5, 24.1, 22.8, 25.0, 23.9],
    'temp_external': [-2.1, -1.5, -3.0, -1.8, -2.5],
    'pressure_chamber_a': [980, 985, 978, 990, 982],
    'pressure_chamber_b': [1010, 1015, 1005, 1020, 1012],
    'humidity': [45, 47, 44, 46, 48]
}

# Step 1: Analyze external temperature readings
baseline_temp, processed_readings, negative_count = analyze_readings(raw_sensor_data['temp_external'])

# Step 2: Calibrate all sensor data (includes irrelevant transformations)
calibrated_data = calibrate_sensor_data(raw_sensor_data)

# Step 3: Extract relevant features for scoring
feature_set = {
    'baseline_deviation': abs(baseline_temp + 2.18),
    'reading_complexity': len(processed_readings) ^ negative_count,  # XOR operation
    'calibration_shift': sum(calibrated_data['temp_internal']) - sum(raw_sensor_data['temp_internal'])
}

# Step 4: Compute derived scores with conditional logic
derived_scores = {}
for k in ['precision', 'recall', 'latency']:
    if k in metrics:
        # Apply min/max clamping as distractor
        capped = min(max(metrics[k], 0.0), 1.0)
        weight_val = weights[k]
        derived_scores[k] = capped * weight_val

# Special handling for stability using lambda-based weight
dynamic_weight = weights['stability'](metrics['stability'])
derived_scores['stability'] = metrics['stability'] * dynamic_weight

# Red herring: unused dictionary transformation
tainted_scores = {k: v * 0.95 + 0.1 for k, v in derived_scores.items() if k != 'latency'}

# Step 5: Aggregate performance with weighted average and bit masking
mask = 0b1101  # Ignore one dimension via bitmask
valid_weights = 0
weighted_sum = 0.0

for idx, (metric, score) in enumerate(derived_scores.items()):
    weight_val = weights[metric] if not callable(weights[metric]) else dynamic_weight
    bit_check = (mask >> idx) & 1
    if bit_check:
        weighted_sum += score * weight_val
        valid_weights += weight_val

aggregate_performance = lambda scores, w_map: weighted_sum / valid_weights if valid_weights else 0

# Critical statement
final_score = aggregate_performance(metrics, weights)

# Additional decoy operations to mislead
checksum = 0
for c in str(final_score):
    if c.isdigit():
        checksum ^= int(c)

# Output result
Result: {final_score}