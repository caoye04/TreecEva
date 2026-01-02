import math

# Simulated sensor data processing with diagnostic evaluation
def collect_samples():
    raw_readings = [127, 255, 192, 64, 96, 159]
    scale_factor = 0.75
    adjusted = [r * scale_factor for r in raw_readings]
    return adjusted

# Irrelevant helper - dead code path (not used)
def legacy_normalize(data):
    max_val = max(data)
    return [x / max_val for x in data]

# Signal conditioning function
def clean_signal(signal):
    filtered = []
    for s in signal:
        if s > 100:  
            filtered.append(int(s) & 0xFF)  # Bit masking for byte alignment
        else:
            filtered.append(int(s) | 0x0A)
    return filtered

# Unused checksum calculator (distractor)
def compute_checksum(arr):
    chk = 0
    for val in arr:
        chk ^= val
    return chk + 1000  # red herring result

# Core transformation: applies logarithmic scaling and slicing
def transform_readings(data):
    temp_buffer = []
    for d in data:
        if d > 50:
            temp_buffer.append(math.log(d, 2))
        else:
            temp_buffer.append(d ** 0.5)
    segment = temp_buffer[1:5]  # slicing operation
    reversed_seg = segment[::-1]
    return [round(x, 3) for x in reversed_seg]

# Threshold mapping using dictionary and tuples
threshold_map = {
    'level1': (0.0, 3.0),
    'level2': (3.0, 5.0),
    'level3': (5.0, float('inf'))
}

# Diagnostic analyzer based on categorized levels
def evaluate_category(value, thresholds):
    if value < thresholds['level1'][1]:
        return 'low'
    elif value < thresholds['level2'][1]:
        return 'moderate'
    else:
        return 'high'

# Main analysis function combining multiple concepts
def analyze_signal(data_list, config):
    stats = {'low': 0, 'moderate': 0, 'high': 0}
    for item in data_list:
        cat = evaluate_category(item, config)
        stats[cat] += 1
    
    # Complex weighting formula with bitwise twist
    weighted_score = (stats['low'] << 2) + (stats['moderate'] * 3) + (stats['high'] ^ 5)
    adjustment = len(data_list) & 7  # bitwise AND
    return weighted_score - adjustment

# Unused string-based validator (distractor)
def validate_entry(code_str):
    if not isinstance(code_str, str):
        code_str = str(code_str)
    if code_str.isnumeric():
        return int(code_str) % 256
    return sum([ord(c) for c in code_str]) & 0xFF

# Execution flow
raw_data = collect_samples()
cleaned_signal = clean_signal(raw_data)
processed_data = transform_readings(cleaned_signal)

# Critical execution point
final_diagnostic = analyze_signal(processed_data, threshold_map)

# Print final result
print(f"Result: {final_diagnostic}")