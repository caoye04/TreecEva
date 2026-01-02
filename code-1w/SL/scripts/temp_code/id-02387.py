def analyze_signal_strength(signal):
    if not signal:
        return 0
    magnitude = sum(abs(x) for x in signal)
    normalized = magnitude / len(signal) if signal else 0
    return int(normalized * 100)


def extract_features(data_str):
    # Irrelevant string processing (distractor)
    cleaned = data_str.strip().lower()
    tokens = cleaned.split(',')
    feature_vector = []
    for token in tokens:
        if token.isnumeric():
            feature_vector.append(int(token))
    return feature_vector

# Decoy function – never used
def decrypt_sequence(seq):
    result = []
    for val in seq:
        result.append(val ^ 255)  # Bitwise XOR red herring
    return result

# Unused helper with misleading name
def calculate_entropy(arr):
    from math import log
    freq_map = {}
    for item in arr:
        freq_map[item] = freq_map.get(item, 0) + 1
    total = len(arr)
    entropy = 0.0
    for count in freq_map.values():
        p = count / total
        entropy -= p * log(p, 2)
    return entropy

# Simulated sensor readings (mixed types)
sensor_data = [12, -45, 67, 23, -11, 89, 44]

# Distractor variables
baseline_offset = 17.3
calibration_matrix = [[1, 0], [0, 1]]  # Unused
redundant_flag = True
snapshot_time = "2023-12-15T10:30:45Z"

# String-encoded auxiliary info (contains hidden distractors)
aux_info = "Mode:SAFE,Checksum:7F,Version:2.1,DebugLevel:HIGH"

# Extract version for no real purpose (dead logic path)
version_str = aux_info.split('Version:')[1].split(',')[0]  # '2.1'
if version_str.startswith('2'):
    baseline_offset += 5.0  # Misleading adjustment

# Red herring: character counting in debug level
debug_level = aux_info.split('DebugLevel:')[1].split(',')[0]
char_count = len(debug_level)  # 4 ('HIGH'), irrelevant

# Threshold determined via convoluted but deterministic path
threshold_base = sum([len(part) for part in aux_info.split(',')])  # 4 parts
threshold_adjust = char_count % 3  # 1
threshold = (threshold_base * 2) - threshold_adjust + 7  # 4*2 -1 +7 = 14

# Another decoy loop with no effect
intermediate_state = []
for i in range(3):
    temp_val = baseline_offset % (i + 2)
    intermediate_state.append(temp_val)

# Core logic buried among noise
primary_magnitude = analyze_signal_strength(sensor_data)

# Conditional mutation based on parity and threshold (key branching)
if primary_magnitude > threshold * 10:
    adjusted = primary_magnitude // 2
else:
    adjusted = primary_magnitude + (threshold & 7)  # Bitwise AND red herring

# Simulate data transformation chain
transformed = []
for val in sensor_data:
    if val < 0:
        transformed.append(val ** 2)
    else:
        transformed.append(val >> 1)  # Right shift distractor

# Real computation obscured by context
def process_readings(readings, limit):
    # Use string method to simulate configuration parsing
    config_line = "filter:active;mode:aggressive;scale:logarithmic"
    if 'aggressive' in config_line:
        scale_factor = 1.75
    else:
        scale_factor = 1.0
    
    # Actual answer depends on this conditional
    total_valid = 0
    for r in readings:
        if abs(r) > limit:
            total_valid += 1
    
    # Final diagnostic combines multiple concepts
    diagnostic_score = (total_valid * 1000) + (adjusted % 100)
    
    # Case conversion distraction
    mode_type = config_line.split('mode:')[1].split(';')[0]
    mode_upper = mode_type.upper()  # 'AGGRESSIVE'
    
    # Hidden dependency: length of mode affects final offset?
    mode_len = len(mode_upper)
    if mode_len > 8:
        diagnostic_score += 50
    else:
        diagnostic_score -= 10  # Triggered: len('AGGRESSIVE') == 10 -> wait, actually 10?

    # Correction: 'aggressive' is 10 characters → condition true
    # But we already computed before branch — correction needed
    # Recompute final with correct logic
    if len(mode_type) > 8:  # 'aggressive' has 10 chars
        diagnostic_score += 50  # So add 50 instead of subtracting 10
    else:
        diagnostic_score -= 10
    
    return diagnostic_score

# Critical execution point
final_diagnostic = process_readings(sensor_data, threshold)

# Output result as required
print(f"Target result: {final_diagnostic}")