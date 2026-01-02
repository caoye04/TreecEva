import math

# Sensor calibration constants (irrelevant to final result)
CALIBRATION_OFFSET = 0.023
NOISE_FLOOR = 0.001
TEMP_CORRECTION = [0.1, -0.05, 0.2, 0.0]

# Irrelevant sensor types and dummy processing functions
def preprocess_flow_rate(x):
    return x * 1.05 + 0.002
def adjust_humidity_level(h):
    return min(100, max(0, h + 5))

def transform_signal(data_list):
    """Irrelevant signal transformation for non-used pathway"""
    transformed = []
    for val in data_list:
        if val > 50:
            transformed.append(val * 0.9)
        else:
            transformed.append(val * 1.1)
    return transformed

def compute_entropy(sequence):
    """Dead function: not used in main logic"""
    freq_map = {}
    for item in sequence:
        freq_map[item] = freq_map.get(item, 0) + 1
    total = len(sequence)
    entropy = 0
    for count in freq_map.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 4)

# Core data structures
sensor_ids = ['S101', 'S102', 'S103', 'S104']
base_thresholds = {'S101': 45, 'S102': 60, 'S103': 40, 'S104': 70}

# Decoy configuration map (partially misleading)
config_matrix = {
    'S101': {'gain': 2.1, 'active': True, 'mode': 'A'},
    'S102': {'gain': 1.8, 'active': False, 'mode': 'B'},
    'S103': {'gain': 2.0, 'active': True, 'mode': 'A'},
    'S104': {'gain': 1.9, 'active': True, 'mode': 'C'}
}

# Raw input data (simulated readings)
raw_readings = {
    'S101': [40, 42, 46, 44],
    'S102': [58, 63, 59, 61],
    'S103': [38, 36, 41, 39],
    'S104': [72, 70, 68, 71]
}

# Secondary derived values (some irrelevant)
rolling_averages = {}
for sid, readings in raw_readings.items():
    rolling_averages[sid] = sum(readings) / len(readings)

# Unused diagnostic flag (red herring)
stable_performance = all(rolling_averages[s] > 40 for s in sensor_ids)

# Actual processing begins here
status_flags = {}
processed_data = {}

for sensor in sensor_ids:
    # Only sensors with active=True in config_matrix are processed further
    if config_matrix[sensor]['active']:
        latest = raw_readings[sensor][-1]
        base = base_thresholds[sensor]
        # Critical condition: XOR-based activation logic
        above_base = latest > base
        is_high_gain = config_matrix[sensor]['gain'] > 1.95
        triggered = bool(above_base ^ is_high_gain)  # XOR logic gate
        status_flags[sensor] = triggered
        processed_data[sensor] = {
            'value': latest,
            'threshold': base,
            'alert': triggered
        }
    else:
        # Inactive sensors get dummy placeholder
        processed_data[sensor] = {'value': 0, 'threshold': 0, 'alert': False}

# Build threshold map for analysis function
threshold_map = {}
for k, v in base_thresholds.items():
    if k in ['S101', 'S103', 'S104']:
        # Artificial offset based on ID length (only S104 affected)
        adj = v + (len(k) - 3) * 2 if 'S104' in k else v
        threshold_map[k] = adj

# Misleading intermediate aggregation
critical_count = sum(1 for v in status_flags.values() if v)
emergency_mode = critical_count >= 3

# Main analysis function with dictionary operations and filtering
def analyze_readings(data_dict, limits):
    score = 0
    penalty = 0
    
    # Iterate only over relevant sensors
    for key, entry in data_dict.items():
        if entry['alert']:
            actual = entry['value']
            limit = limits.get(key, 50)
            if actual > limit:
                score += (actual - limit) * 10
            else:
                penalty += 5
    
    # Complex adjustment using bitwise and logical ops
    adjustment_factor = 1
    if score > 0:
        bits = score ^ 255  # Bitwise XOR with constant
        bits = bits & 127   # Mask upper bit
        adjustment_factor = (bits % 7) + 1
    
    final_score = (score - penalty) * adjustment_factor
    
    # Additional trap: unused correction branch
    if final_score < 0:
        corrected = abs(final_score) // 2
        return corrected  # Never reached in this case
    
    return int(final_score)

# Execute critical statement
final_diagnostic = analyze_readings(processed_data, threshold_map)

# Print result as required
print(f"Result: {final_diagnostic}")