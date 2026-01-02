def preprocess_segment(segment, config):
    adjusted = []
    scaling_factor = config.get('scale', 1.0)
    offset = config.get('offset', 0)
    noise_floor = config.get('noise_floor', 0.1)  # Unused red herring
    for val in segment:
        if val > 0:
            adjusted.append((val * scaling_factor) + offset)
        else:
            adjusted.append(val)
    return adjusted

# Irrelevant helper (dead code path)
def validate_checksum(data):
    checksum = 0
    for item in data:
        if isinstance(item, int):
            checksum ^= item
    return checksum == 0  # Never used

# Distractor function with misleading intermediate results
def compute_entropy(sequence):
    from math import log
    freq = {}
    for s in sequence:
        freq[s] = freq.get(s, 0) + 1
    entropy = 0
    total = len(sequence)
    for count in freq.values():
        p = count / total
        entropy -= p * log(p)
    return round(entropy, 4)

# Real processing chain
def transform_sequence(seq, operations):
    result = seq.copy()
    for op in operations:
        if op == 'reverse':
            result = result[::-1]
        elif op == 'increment':
            result = [x + 1 for x in result if isinstance(x, int)]
        elif op == 'modulo_wrap':
            result = [x % 7 for x in result]
    return result

# Core analysis logic
def build_threshold_map(keys, base_level):
    # Uses enumerate and string methods as required
    mapping = {}
    for i, key in enumerate(keys):
        clean_key = key.strip().upper()
        if 'ERROR' in clean_key:
            mapping[clean_key] = base_level * (i + 1) * 0.8
        elif 'WARNING' in clean_key:
            mapping[clean_key] = base_level * (i + 1) * 0.9
        else:
            mapping[clean_key] = base_level * (i + 1)
    return mapping

# Signal normalization with distractor logic
def normalize_readings(readings):
    max_val = max(readings)
    min_val = min(readings)
    range_val = max_val - min_val or 1
    # Dead computation: frequency analysis not used later
    freq_analysis = {i: readings.count(i) for i in set(readings)}
    normalized = [(x - min_val) / range_val for x in readings]
    return normalized

# Main signal analyzer
def analyze_signal(data, thresholds):
    score = 0
    categories = ['STATUS_OK', 'WARNING_1', 'ERROR_X']
    
    # Use of zip and list comprehension
    paired = list(zip(data, categories))
    filtered_data = [d for d, c in paired if 'ERROR' not in c]
    
    temp_result = 0
    for i, val in enumerate(filtered_data):
        key = f'WARNING_{i+1}'
        if key in thresholds:
            temp_result += val * thresholds[key]
    
    # Critical decoy: looks important but unused
    anomaly_count = sum(1 for d in data if d > 0.7)
    expected_anomalies = len(data) * 0.3
    deviation_score = abs(anomaly_count - expected_anomalies) * 100
    
    # Actual result calculation
    adjustment = 0
    for t in thresholds.values():
        adjustment += t * 0.1
    final_score = temp_result - adjustment
    
    # Final diagnostic derived from actual logic
    final_diagnostic = int(round(final_score * 100))
    return final_diagnostic

# Initialization data
raw_segments = [0.1, 0.3, 0.6, 0.8, 0.4]
config_params = {'scale': 2.5, 'offset': -0.2}
operation_pipeline = ['modulo_wrap', 'reverse']
alert_keys = ['STATUS_OK', 'WARNING_1', 'ERROR_X', 'INFO_TRACE']

# Step-by-step execution flow
preprocessed = preprocess_segment(raw_segments, config_params)
normalized_signal = normalize_readings(preprocessed)
transformed = transform_sequence(normalized_signal, operation_pipeline)
threshold_map = build_threshold_map(alert_keys, base_level=0.5)
processed_data = [x + 0.1 for x in transformed if x < 0.75]  # Additional filtering

# Key statement
final_diagnostic = analyze_signal(processed_data, threshold_map)

print(f"Result: {final_diagnostic}")