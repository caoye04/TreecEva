import itertools

def analyze_pattern(sequence):
    # Irrelevant helper function (dead code path)
    return sum(1 for a, b in zip(sequence, sequence[1:]) if a != b)

def preprocess_data(data):
    # Distractor transformation: modifies data but not used in final result
    shifted = [(x >> 2) ^ 3 for x in data if x % 3 != 0]
    filtered = [x for x in shifted if x > 5]
    return [x * 2 for x in filtered][:10]

def validate_checksum(items):
    # Unused validation logic (red herring)
    checksum = 0
    for i, val in enumerate(items):
        checksum ^= (val + i) % 7
    return checksum == 4

def calculate_entropy(values):
    # Misleading scientific-looking computation (not part of answer)
    total = sum(values)
    if total == 0:
        return 0.0
    probs = [v / total for v in values]
    from math import log2
    return -sum(p * log2(p) for p in probs if p > 0)

def extract_features(record):
    # Complex unpacking and string manipulation (distractor)
    key_str = ''.join([chr(97 + (r % 26)) for r in record[:5]])
    tokens = [t for t in key_str.upper() if t in 'AEIOU']
    return len(tokens), len(key_str)

def compute_aggregate(input_data, mode='advanced'):
    # Core logic embedded within noise
    base_values = [x for x in input_data if x > 0]  # Filter negatives
    
    # Tuple unpacking with distraction
    n = len(base_values)
    if n < 3:
        return 0
    
    # Real computation begins
    doubled = [v * 2 for v in base_values]
    modded = [d % 97 for d in doubled]  # Modular arithmetic
    
    # Bit manipulation relevant to result
    transformed = []
    for m in modded:
        temp = (m ^ 42)  # XOR mask
        if temp & 1:      # Check LSB
            temp = (temp >> 1) + (temp << 31)  # Rotate (conceptually)
            temp &= 0xFFFFFFFF
        transformed.append(temp)
    
    # Actual critical calculation
    window_sums = []
    for i in range(len(transformed) - 2):
        window_sums.append(sum(transformed[i:i+3]))
    
    # Conditional expression determines flow
    primary_sum = max(window_sums) if len(window_sums) > 5 else min(window_sums) if window_sums else 0
    
    # Early termination decoy (never reached due to logic)
    if primary_sum < 0:
        return -1
    
    # Final computation using itertools (required feature)
    rolling_avgs = list(itertools.accumulate(
        [primary_sum // 3, primary_sum // 5, primary_sum // 7]
    ))
    
    # Key assignment
    final_score = rolling_avgs[-1] + (primary_sum % 19)
    
    # Dead code below (misleading)
    outlier_flags = [1 if f > 100 else 0 for f in transformed]
    compression_ratio = len(outlier_flags) / float(len(input_data)) if input_data else 0
    
    # Irrelevant string method chain
    metadata_tag = "processed_result_v2".replace('_', '-').upper().strip('-')
    
    return final_score

# Main execution
raw_input = [12, -5, 23, 8, 19, 3, 7, 14, 6, 22, 9, 11]
decoy_data = preprocess_data(raw_input)
entropy_val = calculate_entropy(raw_input)
vowels_count, length_key = extract_features(raw_input)

# Critical execution point
final_score = compute_aggregate(raw_input, mode='advanced')

print(f"Result: {final_score}")