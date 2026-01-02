import itertools

# Simulated sensor fusion system for environmental monitoring
def analyze_pattern(sequence, threshold):
    count = 0
    for val in sequence:
        if val > threshold:
            count += 1
    return count > len(sequence) // 2

# Irrelevant helper: computes average but not used in final result
def compute_average(data):
    total = 0
    for x in data:
        total += x
    return total / len(data)

# Decoy function: looks important but never called
def legacy_calibration(raw_data, factor=1.7):
    adjusted = []
    for d in raw_data:
        adjusted.append(d * factor + 2)
    return adjusted

# Unused signal filter (red herring)
def bandpass_filter(signal_list, low=0.5, high=5.0):
    filtered = []
    for s in signal_list:
        if low < abs(s) < high:
            filtered.append(s)
    return filtered

# Core transformation: applies bit manipulation and modular arithmetic
def transform_signal(raw_values, mask):
    result = 0
    for i, v in enumerate(raw_values):
        shifted = (v ^ mask) << 1
        result ^= (shifted + i) % 97
    return result

# Character frequency analyzer (distractor)
def count_chars(text_block):
    freq = {}
    for ch in text_block:
        freq[ch] = freq.get(ch, 0) + 1
    return freq

# Main processing pipeline
def process_readings(stream, key):
    # Initial filtering (some values excluded)
    valid_entries = [x for x in stream if x >= 0]
    
    # Extract every third reading using itertools (meaningful usage)
    sampled = list(itertools.islice(valid_entries, 0, None, 3))
    
    # Apply XOR-based transformation with calibration key
    transformed = transform_signal(sampled, key)
    
    # Secondary check: count of high-magnitude readings
    high_activity = sum(1 for x in valid_entries if x > 80)
    
    # Dummy aggregation (not directly used but looks important)
    aggregate_score = 0
    for idx, val in enumerate(valid_entries):
        aggregate_score += (val * (idx % 5)) % 11
    
    # Control flow with nested conditions (3 levels deep)
    if len(sampled) > 4:
        if transformed % 3 == 0:
            if high_activity >= 3:
                base = transformed * 2
            else:
                base = transformed + 15
        else:
            if analyze_pattern(valid_entries, 60):
                base = transformed - 8
            else:
                base = transformed
    else:
        base = 100
    
    # Final computation involving dictionary lookup and tuple unpacking
    mode_map = {0: 5, 1: -3, 2: 7, 3: 0, 4: 9}
    status_codes = ('OK', 'WARNING', 'CRITICAL')
    code_index = (base // 10) % 5
    
    # Tuple unpacking (correct path)
    _, adjustment = tuple(mode_map.items())[code_index % 5]
    
    # Dead code path: unreachable due to prior logic
    if False and len(valid_entries) == 0:
        fallback = 0
        for c in str(base):
            if c.isdigit():
                fallback += int(c)
        base = fallback
    
    # Final diagnostic calculation
    final_diagnostic = base + adjustment
    
    # Redundant string operation (distractor)
    log_tag = ''.join([s[0] for s in status_codes])
    id_signature = f"{log_tag}_{len(valid_entries)}"
    
    # This print is NOT the target; it's a distraction
    print(f"Processing complete: {id_signature}")
    
    return final_diagnostic

# Global constants (some irrelevant)
MAX_BUFFER_SIZE = 1024
DEFAULT_TIMEOUT = 15.5
CALIBRATION_OFFSET = 0  # unused

# Input data: simulated sensor readings
sensor_readings = [12, -5, 88, 43, 91, 67, 3, 104, 22, 77, 59, 83]
calibration_key = 13

# Execute main logic
final_diagnostic = process_readings(sensor_stream=sensor_readings, calibration_key=calibration_key)
print(f"Result: {final_diagnostic}")