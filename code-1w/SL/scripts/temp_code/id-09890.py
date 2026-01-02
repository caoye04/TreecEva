import math

# Sensor calibration data (partially irrelevant)
def calibrate_sensor(raw_value, offset=0.15):
    return raw_value * 0.98 + offset

# Irrelevant transformation for alternate sensor type
def legacy_normalize(x):
    if x > 100:
        return x / 1.75
    else:
        return x + math.log(abs(x) + 1)

# Core signal processing
def filter_spike(sequence):
    cleaned = []
    for i in range(len(sequence)):
        left = sequence[i-1] if i > 0 else sequence[i]
        right = sequence[i+1] if i < len(sequence)-1 else sequence[i]
        avg_neighbor = (left + right) / 2
        if abs(sequence[i] - avg_neighbor) > 30:
            cleaned.append(avg_neighbor)
        else:
            cleaned.append(sequence[i])
    return cleaned

# Red herring function - never called
def compute_entropy(data):
    total = sum(data)
    probs = [x/total for x in data if x > 0]
    return -sum(p * math.log2(p) for p in probs)

# Data alignment via tuple-based mapping
def align_channels(primary, secondary, shift=2):
    padded_primary = [0]*shift + primary
    truncated_secondary = secondary[:len(primary)]
    aligned = [(p, s) for p, s in zip(padded_primary, [0]*shift + truncated_secondary)]
    return aligned

# Threshold classification map (used later)
threshold_map = {
    'low': 45,
    'caution': 75,
    'high': 90
}

# Simulated raw readings from multiple sensors
raw_readings_a = [68, 72, 95, 43, 87, 77, 65, 91, 88, 76]
raw_readings_b = [54, 88, 40, 92, 67, 75, 83, 44, 90, 70]

# Apply calibration (some relevant, some red herring)
calibrated_a = [calibrate_sensor(x) for x in raw_readings_a]
calibrated_b = [calibrate_sensor(x, 0.10) for x in raw_readings_b]

# Introduce misleading intermediate values
drift_correction = sum([0.05 * i for i in range(len(calibrated_a))])
baseline_offset = max(calibrated_a) - min(calibrated_b)  # unused but plausible

# Filter spikes in primary channel
filtered_a = filter_spike(calibrated_a)

# Align two channels (only first element used later)
aligned_data = align_channels(filtered_a, calibrated_b, shift=1)

# Extract and transform relevant portion
extracted_signal = [item[0] for item in aligned_data][1:-1]  # remove edges

# Apply nonlinear transformation
transformed_data = [
    x ** 0.5 * 1.1 if x < 70 else
    x * 0.95 if x < 85 else
    math.sin(x * math.pi / 180) * 100
    for x in extracted_signal
]

# Dead code path - unreachable due to logic
if sum(transformed_data) < 0:
    transformed_data = [abs(x) for x in transformed_data]

# Decoy variables that look important
aggregation_weight = 0.88
normalization_factor = len(transformed_data) or 1
composite_score = sum(transformed_data) * 0.9 / normalization_factor

# Actual analysis function using threshold logic
def analyze_readings(data, thresholds):
    high_count = 0
    caution_count = 0
    for val in data:
        if val > thresholds['high']:
            high_count += 1
        elif val > thresholds['caution']:
            caution_count += 1
    
    # Complex weighting formula
    severity_index = (high_count * 3.5) + (caution_count * 1.2)
    
    # Secondary check: count consecutive high-risk values
    consecutive_risk = 0
    max_consecutive = 0
    for val in data:
        if val > thresholds['caution']:
            consecutive_risk += 1
            max_consecutive = max(max_consecutive, consecutive_risk)
        else:
            consecutive_risk = 0
    
    # Final diagnostic calculation
    base_score = severity_index * 10
    penalty = max_consecutive * 2.5 if max_consecutive >= 3 else 0
    final_score = base_score - penalty
    
    # Normalize to diagnostic range
    return int(round(final_score / 2))

# Execute critical statement
final_diagnostic = analyze_readings(transformed_data, threshold_map)
print(f"Result: {final_diagnostic}")