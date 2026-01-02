import math

# Sensor simulation data (irrelevant for final result but adds distraction)
sensor_offsets = {'temp': 0.5, 'pressure': -0.2, 'humidity': 0.1}
baseline_samples = [23.4, 23.6, 23.5, 23.7, 24.0, 23.8]

# Irrelevant calibration function (dead code path)
def calibrate_sensor(data, offset):
    return [x + offset for x in data]

def generate_checksum(tag_list):
    # Unused function – red herring
    return sum([hash(t) % 100 for t in tag_list])

# Real processing begins here
raw_readings = [127, 191, 63, 255, 31]
mask_sequence = [128, 64, 32, 16, 8]

# Bit manipulation and filtering based on bit patterns
filtered_indices = []
for i, val in enumerate(raw_readings):
    if (val & mask_sequence[i]) == 0:  # Check masked bit
        filtered_indices.append(i)

# Distractor: complex-looking but unused transformation
transformed = [((x >> 2) ^ 0b101) * 3 for x in raw_readings if x < 200]

# Actual relevant data preparation
processed_data = []
for idx, val in enumerate(raw_readings):
    if idx not in filtered_indices:
        processed_data.append(val + (idx * 2))

# Threshold configuration with decoy keys
threshold_map = {
    'low': {'limit': 100, 'weight': 0.5},
    'medium': {'limit': 200, 'weight': 0.7},
    'high': {'limit': 300, 'weight': 0.9},
    'debug_mode': True,
    'version': '2.1'
}

# Auxiliary diagnostic function (partially used)
def compute_entropy(values):
    total = sum(values)
    probs = [v / total for v in values if v > 0]
    return -sum(p * math.log(p) for p in probs)

# Main analysis function
def analyze_readings(data, thresholds):
    count_above = 0
    weighted_sum = 0.0

    # Misleading entropy calculation (used but not impactful)
    _ = compute_entropy(data) if len(data) > 1 else 0

    # Actual logic: count how many exceed medium threshold, apply weight
    for val in data:
        if val > thresholds['medium']['limit']:
            count_above += 1
            weighted_sum += val * thresholds['medium']['weight']
        elif val > thresholds['low']['limit']:
            weighted_sum += val * thresholds['low']['weight']

    # Decoy intermediate variables
    avg_val = sum(data) / len(data) if data else 0
    deviation_score = abs(avg_val - 150) / 10

    # Critical computation hidden among distractors
    adjustment_factor = len(data) - len(filtered_indices)  # depends on earlier filter
    raw_total = sum(data)

    # Final diagnostic combines multiple concepts
    result = int(weighted_sum - (raw_total // 10) + (adjustment_factor * 100))

    # This line contains the key assignment
    final_diagnostic = result

    return final_diagnostic

# Execution point of interest
final_diagnostic = analyze_readings(processed_data, threshold_map)

# Output result as required
print(f"Result: {final_diagnostic}")