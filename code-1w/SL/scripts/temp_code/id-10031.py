import math

# Simulated sensor data analysis with embedded logic chain
def collect_readings():
    raw_samples = [18, 22, 15, 30, 25, 40, 10, 5]
    offset = 7
    adjusted = [x + offset for x in raw_samples]
    return adjusted

def filter_outliers(data, threshold=20):
    # Irrelevant filtering path (never used)
    if len(data) == 0:
        return []
    filtered = [x for x in data if x > threshold]
    return filtered  # Dead code path: not used in main flow

def transform_sequence(series):
    mapped = {}
    for idx, val in enumerate(series):
        if idx % 2 == 0:
            mapped[f'even_{idx}'] = val ** 2
        else:
            mapped[f'odd_{idx}'] = val * 2 + 1
    # Distractor transformation
    temp_result = sum(mapped[key] for key in mapped if 'even' in key)
    return mapped

def decode_signature(config):
    # Misleading bit manipulation with no real impact
    a = 5
    b = 3
    c = (a << 2) ^ (b >> 1)
    mask = 0xFF
    decoy_hash = (c & mask) + 100
    return decoy_hash  # Unused return value

def compress_data(items):
    # Complex but irrelevant compression routine
    result_str = ''.join(str(len(str(item))) for item in items.values())
    sliced = result_str[1:4]  # Partial slice, not used later
    checksum = sum(int(d) for d in sliced) * 2
    return checksum  # Red herring computation

def calculate_entropy(values):
    total = sum(values)
    probabilities = [v / total for v in values if v > 0]
    entropy = 0
    for p in probabilities:
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 6)

def shift_buffer(arr, n):
    # Slicing-based rotation (distraction)
    n = n % len(arr)
    return arr[n:] + arr[:n]

def analyze_pattern(input_map):
    # Core logic hidden among distractions
    even_keys = [k for k in input_map.keys() if 'even' in k]
    relevant_values = [input_map[k] for k in even_keys]
    
    # Real computation begins here
    base_sum = sum(relevant_values)
    count = len(relevant_values)
    mean_val = base_sum / count
    
    # Apply corrective scaling based on string length of keys
    key_lengths = [len(k) for k in even_keys]
    adjustment = sum(key_lengths) / len(key_lengths)
    
    # Final diagnostic computed from mixed sources
    diagnostic_score = int((mean_val - adjustment) * 2)
    return diagnostic_score

# Main execution with multiple red herrings
readings = collect_readings()
signature = decode_signature(readings)  # Unused
transformed_data = transform_sequence(readings)
compressed = compress_data(transformed_data)  # Computed but unused
entropy_metric = calculate_entropy(readings)  # Meaningful but not final
rotated = shift_buffer(readings, 3)  # Dead end
processed_data = transformed_data
final_diagnostic = analyze_pattern(processed_data)
print(f"Result: {final_diagnostic}")