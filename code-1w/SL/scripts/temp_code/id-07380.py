def preprocess_signal(raw_samples):
    filtered = [x for x in raw_samples if x > -50 and x < 50]
    shifted = [(x + 3) * 2 for x in filtered]
    return shifted

# Irrelevant signal processing function (decoy)
def compute_envelope(signal):
    envelope = []
    for s in signal:
        if s % 4 == 0:
            envelope.append(s // 4)
    return envelope

# Unused transformation path (dead code)
def legacy_transform(data):
    return [d ^ 7 for d in data if d % 3 != 0]

# Auxiliary character analysis (distractor)
def count_characters(text_blocks):
    char_count = 0
    case_stats = {'upper': 0, 'lower': 0}
    for block in text_blocks:
        char_count += len(block)
        for c in block:
            if c.isupper():
                case_stats['upper'] += 1
            elif c.islower():
                case_stats['lower'] += 1
    return char_count, case_stats

# Core data transformation with relevant logic
import math
def transform_sequence(values):
    temp_result = []
    for v in values:
        if v == 0:
            continue
        transformed = int(math.log(abs(v) + 1, 2)) * (1 if v > 0 else -1)
        temp_result.append(transformed)
    # Introduce bit manipulation
    bitwise_shifted = [t << 1 if t > 0 else t >> 1 for t in temp_result]
    return bitwise_shifted

# Pattern analyzer that uses set operations (required feature)
def detect_anomalies(series):
    evens = {x for x in series if x % 2 == 0}
    odds = {x for x in series if x % 2 == 1}
    anomalies = evens.symmetric_difference(odds)
    baseline = {x for x in range(-10, 11)}
    deviation = anomalies.difference(baseline)
    return sum(deviation) if deviation else 0

# Main analysis chain
def analyze_patterns(dataset):
    stage_a = transform_sequence(dataset)
    
    # Distractor: unused intermediate path
    proxy_values = [x + 100 for x in stage_a if x < 0]
    proxy_set = {p * 2 for p in proxy_values}
    
    # Relevant anomaly detection
    anomaly_score = detect_anomalies(stage_a)
    
    # Secondary transformation (red herring)
    dummy_map = {}
    for i, val in enumerate(stage_a):
        dummy_map[i] = val ^ 5 if i % 3 == 0 else val | 7
    
    # Final computation using prior result
    adjustment = len(proxy_set) // 2 if proxy_set else 0
    final_diagnostic = anomaly_score - adjustment
    
    return final_diagnostic

# Simulated sensor readings (input)
sensor_readings = [15, -7, 0, 23, -1, 8, 4, -3, 12]

# Preprocessing (used)
cleaned_signal = preprocess_signal(sensor_readings)

# Dead function call (misleading)
_ = compute_envelope(cleaned_signal)

# Character stats from unrelated metadata (distractor)
document_metadata = ["SensorA", "Node_7", "LOG_2024"]
char_total, case_breakdown = count_characters(document_metadata)

# Key transformation
transformed_data = transform_sequence(cleaned_signal)

# Critical execution point
final_diagnostic = analyze_patterns(transformed_data)

print(f"Result: {final_diagnostic}")