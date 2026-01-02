import math

# Simulated sensor data and configuration
def generate_signals():
    base_freq = 17
    sample_size = 64
    return [int(10 * math.sin(base_freq * i / 7) + 3 * math.cos(i / 5)) % 100 for i in range(sample_size)]

def filter_outliers(data, limit=90):
    # Irrelevant filtering (red herring)
    return [x for x in data if x <= limit]

def encrypt_key(sequence):  # Decoy function – looks important but unused
    key = 0
    for i, val in enumerate(sequence):
        key ^= (val * i) % 257
    return key

def transform_sequence(seq):
    # Applies modular arithmetic and bit shifts (partially relevant)
    shifted = [(v << 1) % 199 for v in seq]
    wrapped = [(v + 5) % 100 for v in shifted]
    return [v if v % 3 != 0 else v // 2 for v in wrapped]  # Conditional expression used

# Data calibration with misleading intermediate steps
def calibrate_readings(raw):
    offset = sum(raw[:5]) % 7
    adjusted = [v - offset for v in raw]
    normalized = [abs(v) % 100 for v in adjusted]
    return normalized

# Core analysis logic
def build_threshold_map(values):
    avg = sum(values) / len(values)
    return {
        'low': avg - 10,
        'mid': avg,
        'high': avg + 15
    }

def classify_point(val, thresholds):
    if val < thresholds['low']:
        return 'A'
    elif val <= thresholds['mid']:
        return 'B'
    else:
        return 'C'

def count_transitions(classes):
    transitions = 0
    for i in range(1, len(classes)):
        if classes[i] != classes[i-1]:
            transitions += 1
    return transitions

def analyze_signal(data, t_map):
    classifications = [classify_point(x, t_map) for x in data]
    
    # Count specific pattern: 'A' -> 'C' jump
    ac_jumps = 0
    for i in range(1, len(classifications)):
        if classifications[i-1] == 'A' and classifications[i] == 'C':
            ac_jumps += 1
    
    # Real computation path
    total_weight = 0
    for val in data:
        if val > t_map['mid']:
            total_weight += val * 0.85
        elif val < t_map['low']:
            total_weight += val * 0.3
        else:
            total_weight += val * 0.6
    
    # Final diagnostic combines multiple factors
    stability_score = len(data) - count_transitions(classifications)
    jump_penalty = ac_jumps * 12
    final_score = int(total_weight - jump_penalty + stability_score)
    
    # Irrelevant transformations below (distractors)
    _ = [math.sqrt(x + 1) for x in data if x > 0]
    _temp_hash = sum((i * v) % 101 for i, v in enumerate(data))
    __ = encrypt_key(data)  # Dead call
    
    return final_score

# Unused helper (dead code path)
def deprecated_normalizer(x):
    return (x + 1) // 2 if x > 50 else x * 2

# Main execution flow
if __name__ == "__main__":
    raw_sensor_data = generate_signals()
    cleaned_data = filter_outliers(raw_sensor_data, limit=95)
    calibrated_data = calibrate_readings(cleaned_data)
    processed_data = transform_sequence(calibrated_data)
    
    # Dummy variables to mislead (irrelevant)
    snapshot_checksum = sum(processed_data[i] * (i+1) for i in range(0, len(processed_data), 8)) % 997
    baseline_reference = [x for x in processed_data if x % 4 == 0]
    
    threshold_map = build_threshold_map(processed_data)
    
    # Key statement
    final_diagnostic = analyze_signal(processed_data, threshold_map)
    
    # Additional distraction
    _ = [deprecated_normalizer(x) for x in processed_data]
    
    print(f"Result: {final_diagnostic}")