import itertools

# Simulated sensor data processing with red herrings and complex flow
def fetch_raw_readings():
    return [127, 64, 95, 38, 113, 72, 88, 51]

def apply_mask(sequence, mask=0x1F):
    # Bitwise filtering - only lower 5 bits relevant
    return [val & mask for val in sequence]

def shift_scale(values, factor=3):
    # Irrelevant transformation (not used in final path)
    return [(v << 2) / factor for v in values]

def derive_metrics(vals):
    # Dead-end function: calculates unused statistics
    mean = sum(vals) / len(vals)
    variance = sum((v - mean) ** 2 for v in vals) / len(vals)
    return {'avg': round(mean, 2), 'var': round(variance, 3)}

def generate_pairs(data):
    # Creates combinations but only one is actually consumed later
    pairs = list(itertools.combinations(data, 2))
    filtered = [p for p in pairs if (p[0] + p[1]) % 5 == 0]  # Some filtering
    return filtered

def extract_features(stream):
    # Extracts high-bit presence as flags (distraction)
    flags = []
    for x in stream:
        flag = ((x >> 4) & 1) ^ ((x >> 2) & 1)  # XOR of two bit positions
        flags.append(flag)
    return flags

def transform_sequence(seq):
    # Core relevant transformation: reverse and offset
    reversed_seq = seq[::-1]
    offset_seq = [(v - 10) % 256 for v in reversed_seq]
    return offset_seq

def analyze_pattern(data, cfg):
    # Critical function: computes checksum using modular arithmetic
    base = cfg['base']
    mod = cfg['modulus']
    checksum = 0
    for i, val in enumerate(data):
        weighted = (val * (i + 1) * base) % mod
        checksum = (checksum + weighted) % mod
    return checksum

def dummy_aggregator(inputs):  # Unused decoy
    total = 0
    for item in inputs:
        if isinstance(item, tuple):
            total += item[0] * 17
    return total % 997

# Main execution flow
if __name__ == '__main__':
    raw_data = fetch_raw_readings()  # Initial dataset
    masked_data = apply_mask(raw_data)  # Apply bitwise mask (key preprocessing)
    
    # Distractor branch 1: scaling (result not used)
    scaled_vals = shift_scale(masked_data, factor=4)
    metrics = derive_metrics(scaled_vals)  # Computed but ignored
    
    # Distractor branch 2: pair generation
    pairs_list = generate_pairs(masked_data)
    feature_flags = extract_features(raw_data)  # Uses original data, not masked
    
    # Relevant data path
    transformed_data = transform_sequence(masked_data)  # Reverse and offset
    
    # Configuration dictionary with misleading keys
    config = {
        'base': 13,
        'modulus': 983,
        'threshold': 45,
        'debug_mode': False,
        'buffer_size': 2048,
        'scaling_factor': 2.5  # Unused
    }
    
    # Dead code path: aggregator never called
    temp_result = dummy_aggregator(pairs_list)
    
    # Key statement
    final_diagnostic = analyze_pattern(transformed_data, config)
    
    # Print result for extraction
    print(f"Result: {final_diagnostic}")