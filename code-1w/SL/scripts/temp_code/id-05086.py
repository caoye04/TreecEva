import math

def generate_baseline(count):
    return [math.sin(i * 0.1) + 0.5 for i in range(count)]

def filter_noise(signal, threshold=0.3):
    return [x for x in signal if abs(x) > threshold]

def integrate_signal(signal):
    accumulator = 0
    integrated = []
    for val in signal:
        accumulator += val
        integrated.append(accumulator)
    return integrated

def shift_window(data, offset):
    return data[offset:] + data[:offset]

def compute_entropy(values):
    # Irrelevant function - not used in main flow
    from collections import Counter
    counts = Counter(values)
    total = len(values)
    entropy = 0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return entropy

def assess_coherence(sequence):
    # Dead code path - never called
    score = 0
    for i in range(1, len(sequence)):
        if sequence[i] > sequence[i-1]:
            score += 1
    return score / len(sequence)

def extract_features(data_stream):
    features = {}
    features['peak'] = max(data_stream)
    features['trough'] = min(data_stream)
    features['mean'] = sum(data_stream) / len(data_stream)
    features['range'] = features['peak'] - features['trough']
    features['zero_crossings'] = sum(1 for i in range(1, len(data_stream)) if data_stream[i-1] < 0 <= data_stream[i])
    return features

def merge_diagnostics(a, b, c):
    # Decoy function with misleading relevance
    combined_score = (a['peak'] * 0.4) + (b['range'] * 0.3) + (c * 0.3)
    return round(combined_score, 3)

def transform_coordinates(x_vals, y_vals):
    # Irrelevant geometric transformation
    return [(x * math.cos(y), x * math.sin(y)) for x, y in zip(x_vals, y_vals)]

def detect_anomalies(dataset):
    anomalies = []
    for i, val in enumerate(dataset):
        if abs(val) > 1.2 and i % 3 == 0:
            anomalies.append(i)
    return set(anomalies)  # Use of set operation

def normalize_sequence(seq):
    max_val = max(seq)
    min_val = min(seq)
    if max_val == min_val:
        return [0.0] * len(seq)
    return [(x - min_val) / (max_val - min_val) for x in seq]

def accumulate_magnitude(signal):
    total = 0.0
    for x in signal:
        total += abs(x)
    return total

def parse_timestamp(label):
    # String method usage - irrelevant parsing
    parts = label.strip().split('_')
    time_code = parts[-1] if len(parts) > 1 else parts[0]
    digits = ''.join(filter(str.isdigit, time_code))
    return int(digits) if digits else 0

def validate_checksum(tag):
    # Another red herring with string operations
    even_chars = tag[::2]
    odd_chars = tag[1::2]
    checksum = 0
    for char in even_chars:
        checksum ^= ord(char)
    for char in odd_chars:
        checksum += ord(char)
    return checksum % 17

def analyze_readings(readings_list):
    temp_buffer = []
    for reading in readings_list:
        if isinstance(reading, dict) and 'value' in reading:
            temp_buffer.append(reading['value'])
    
    if not temp_buffer:
        return -999
    
    # Begin relevant processing chain
    base_magnitude = accumulate_magnitude(temp_buffer)
    normalized = normalize_sequence(temp_buffer)
    integrated = integrate_signal(normalized)
    
    # Extract key statistical feature
    feature_set = extract_features(integrated)
    
    # Core logic: apply conditional modulation based on feature thresholds
    modulation_factor = 1.0
    if feature_set['mean'] > 0.5:
        modulation_factor *= 1.2
    if feature_set['zero_crossings'] > 2:
        modulation_factor *= 0.9
    if feature_set['range'] < 0.8:
        modulation_factor *= 1.1
    
    intermediate_result = base_magnitude * modulation_factor
    
    # Apply bitwise influence from control flags (simulated)
    control_flag = 0b101010
    shift_amount = len(temp_buffer) % 6
    adjusted = int(intermediate_result) ^ (control_flag << shift_amount)
    
    # Final adjustment using modular arithmetic
    final_value = (adjusted % 97) * 3.141592
    
    return round(final_value, 6)

def process_signal_chain(raw_input, labels, tags):
    # Main processing pipeline with distractions
    baseline = generate_baseline(10)
    noisy_extended = baseline + [x * 1.5 for x in raw_input]
    
    cleaned = filter_noise(noisy_extended)
    
    # Irrelevant timestamp parsing
    timestamps = [parse_timestamp(lbl) for lbl in labels]
    checksums = [validate_checksum(tg) for tg in tags]
    
    # Transform but do not use
    dummy_coords = transform_coordinates(timestamps, checksums)
    
    # Signal integration
    integrated_signal = integrate_signal(cleaned)
    shifted_signal = shift_window(integrated_signal, 2)
    
    # Anomaly detection (not used directly)
    anomalies = detect_anomalies(shifted_signal)
    
    # Prepare structured output
    processed_entries = []
    for idx, val in enumerate(shifted_signal):
        entry = {
            'index': idx,
            'value': val,
            'status': 'anomalous' if idx in anomalies else 'normal',
            'source': 'sensor_b'
        }
        processed_entries.append(entry)
    
    return processed_entries

# Simulated input data
data_stream = [0.1, -0.4, 0.85, -1.1, 0.33, 0.67, -0.2, 0.9, 0.05]
labels_list = ['log_entry_20230401', 'record_20230402', 'data_point_20230403']
tag_ids = ['CHK7B', 'XFR9M', 'DGN0T']

# Execute main processing
processed_signals = process_signal_chain(data_stream, labels_list, tag_ids)

# Critical execution point
final_diagnostic = analyze_readings(processed_signals)

print(f"Target result: {final_diagnostic}")