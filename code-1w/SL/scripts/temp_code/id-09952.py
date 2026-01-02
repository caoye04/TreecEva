import math

# Simulated sensor data processing with diagnostic analysis
def collect_samples():
    raw_signals = [0.88, -1.22, 3.14, -2.71, 0.0, 1.41, -1.73]
    timestamped = {i: val for i, val in enumerate(raw_signals)}
    return timestamped

# Irrelevant helper - distractor
def smooth_noise(data):
    smoothed = []
    for i in range(len(data)):
        if i == 0 or i == len(data)-1:
            smoothed.append(data[i])
        else:
            smoothed.append((data[i-1] + data[i] + data[i+1]) / 3)
    return smoothed

# Data normalization - relevant but indirect
def normalize_values(signal_dict):
    values = list(signal_dict.values())
    mean_val = sum(values) / len(values)
    stdev = (sum((x - mean_val)**2 for x in values) / len(values))**0.5
    normalized = {k: (v - mean_val) / stdev for k, v in signal_dict.items()}
    return normalized

# Decoy function - never used
def compute_entropy(seq):
    from collections import Counter
    counts = Counter(seq)
    total = len(seq)
    entropy = -sum((count/total) * math.log2(count/total) for count in counts.values())
    return entropy

# Complex transformation with string-based key mapping
def encode_features(normalized):
    code_map = {}
    for idx, val in normalized.items():
        prefix = "SIG"
        quality = "H" if abs(val) > 1.0 else "L"
        flag = "P" if val >= 0 else "N"
        label = f"{prefix}_{quality}{flag}_{idx:02d}"
        # Use string manipulation to derive a numeric code
        char_sum = sum(ord(c) for c in label if c.isalpha())
        position_factor = int(label[-2:])
        code_map[label] = (char_sum % 17) + position_factor - (len(prefix) * (idx % 3))
    return code_map

# Real processing path
processed_cache = []
def process_segment(segment_data):
    result = []
    for k, v in segment_data.items():
        transformed = round(math.sin(v * math.pi / 4) * 100, 2)
        result.append(transformed)
    processed_cache.extend(result)
    return result

# Another red herring - uses zip but irrelevant
def correlate_streams(stream_a, stream_b):
    if len(stream_a) != len(stream_b):
        return 0.0
    mean_a = sum(stream_a) / len(stream_a)
    mean_b = sum(stream_b) / len(stream_b)
    cov = sum((a - mean_a) * (b - mean_b) for a, b in zip(stream_a, stream_b))
    var_a = sum((a - mean_a)**2 for a in stream_a)
    var_b = sum((b - mean_b)**2 for b in stream_b)
    if var_a == 0 or var_b == 0:
        return 0.0
    return round(cov / ((var_a * var_b)**0.5), 4)

# Core analysis function
# Uses dictionary operations and conditional logic
def analyze_signal(data_list, calib):
    base_score = 0
    for i, val in enumerate(data_list):
        key_name = f"SIG_LN_{i:02d}"
        if key_name in calib:
            adjustment = calib[key_name]
            if val > 50:
                base_score += adjustment * 2
            elif val < -50:
                base_score -= adjustment
            else:
                base_score += abs(val) // 10
    # Additional logic with nested conditions
    magnitude = sum(1 for v in data_list if abs(v) > 75)
    if magnitude > 2:
        base_score = int(base_score * 1.3)
    elif magnitude == 0:
        base_score = int(base_score * 0.85)
    return base_score

# --- Execution Flow ---
raw_data = collect_samples()
normalized_data = normalize_values(raw_data)

# Encode features (generates map but only some values are used)
feature_codes = encode_features(normalized_data)

# Process main data path
processed_data = process_segment(normalized_data)

# Create calibration map using string methods and filtering
calibration_keys = [k for k in feature_codes.keys() if 'H' in k]
calibration_map = {}
for key in calibration_keys:
    digits = ''.join(filter(str.isdigit, key))
    if digits:
        num = int(digits) % 9
        calibration_map[key] = num + 1

# Unused intermediate - dead code path
redundant_analysis = [
    (k, v) for k, v in feature_codes.items() 
    if 'P' in k and v % 2 == 0
]

# Key statement
final_diagnostic = analyze_signal(processed_data, calibration_map)

# Print final result
print(f"Target result: {final_diagnostic}")