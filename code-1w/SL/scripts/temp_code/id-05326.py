import math

# Simulated sensor data and configuration
def generate_signals():
    raw_samples = [i * 0.1 for i in range(100)]
    return [math.sin(x) + 0.5 * math.cos(3*x) for x in raw_samples]

def filter_outliers(data, limit=3.0):
    mean_val = sum(data) / len(data)
    std_dev = (sum((x - mean_val)**2 for x in data) / len(data))**0.5
    return [x for x in data if abs(x - mean_val) / std_dev <= limit]

def compress_sequence(seq):
    # Irrelevant compression function (dead code path)
    return ''.join([hex(int(x * 10))[2:] for x in seq[:5]])

def calculate_entropy(data):
    # Misleading auxiliary calculation
    freqs = {}
    for x in data:
        bucket = int(x * 10)
        freqs[bucket] = freqs.get(bucket, 0) + 1
    total = len(data)
    return -sum((count / total) * math.log2(count / total) for count in freqs.values())

def extract_features(signal):
    # Real feature extraction with distractors
    magnitudes = [abs(x) for x in signal]
    avg_mag = sum(magnitudes) / len(magnitudes)
    peak = max(magnitudes)
    zero_crossings = sum(1 for i in range(1, len(signal)) if signal[i-1] * signal[i] < 0)
    
    # Decoy statistics
    variance = sum((x - avg_mag)**2 for x in magnitudes) / len(magnitudes)
    skewness = sum(((x - avg_mag)/variance**0.5)**3 for x in magnitudes) / len(magnitudes) if variance > 0 else 0
    
    return {
        'avg': avg_mag,
        'peak': peak,
        'zero_cross': zero_crossings,
        'meta_tag': 'DIAG_42'
    }

def validate_checksum(tag_str):
    # Unused validation function (red herring)
    return sum(ord(c) for c in tag_str) % 17 == 0

def build_lookup_table():
    # Complex-looking but irrelevant mapping
    table = {}
    for i in range(16):
        key = hex(i)[2:].upper()
        val = (i ** 3) ^ 0xA5
        table[key] = val
    return table

def transform_coordinates(x_list):
    # Bit manipulation decoy
    transformed = []
    for x in x_list:
        bits = int(x * 100) & 0xFF
        flipped = bits ^ 0xAA
        shifted = ((flipped << 1) | (flipped >> 7)) & 0xFF
        transformed.append(shifted / 100.0)
    return transformed

def normalize_signal(data):
    min_d, max_d = min(data), max(data)
    scale = 1.0 / (max_d - min_d) if max_d != min_d else 1.0
    return [(x - min_d) * scale for x in data]

def apply_mask(signal, pattern='AB'):
    # String method distraction
    mask_key = ''.join(sorted(set(pattern))) * 4
    indices = [i for i, c in enumerate(mask_key) if c == 'A']
    return [signal[i % len(signal)] for i in indices]

def analyze_signal(data, thresholds):
    features = extract_features(data)
    base_score = features['avg'] * 100
    
    # Conditional logic chain with distractions
    adjustment = 0
    if features['peak'] > thresholds['critical']:
        adjustment += 25
    elif features['peak'] > thresholds['warning']:
        adjustment += 10
    
    # Bitwise red herring
    flag_code = 0x1F & (~0x0A)
    if features['zero_cross'] > thresholds['activity'] and flag_code & 0x10:
        adjustment += 15
    
    # Lambda function used meaningfully but with decoy behavior
    modifier = lambda x, t: x * 1.5 if t > 0.7 else x * 0.8
    adjusted_score = modifier(base_score + adjustment, features['avg'])
    
    # Final computation buried in noise
    temp_result = int(round(adjusted_score))
    final_value = (temp_result ^ 0x5A5A) & 0xFFFF  # Key transformation
    return final_value

def main():
    # Main execution with multiple irrelevant steps
    raw_data = generate_signals()
    cleaned = filter_outliers(raw_data)
    processed_data = normalize_signal(cleaned)
    
    # Dead code assignments (distractors)
    entropy_metric = calculate_entropy(processed_data)
    compressed_sig = compress_sequence(processed_data)
    transformed_coords = transform_coordinates(processed_data)
    lookup = build_lookup_table()
    masked_vals = apply_mask(processed_data, 'XYZ')
    
    # Actual relevant configuration
    threshold_map = {
        'critical': 0.85,
        'warning': 0.65,
        'activity': 15
    }
    
    # Critical execution point
    final_diagnostic = analyze_signal(processed_data, threshold_map)
    
    # Print required result
    print(f"Result: {final_diagnostic}")
    
    # Unused debug prints (misleading output)
    debug_state = f"State:{lookup['A']}:{len(masked_vals)}"
    checksum_valid = validate_checksum(debug_state)
    
    return final_diagnostic

if __name__ == '__main__':
    main()