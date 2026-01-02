from collections import defaultdict, Counter
import math

# Simulated sensor fusion system (distractor context)
def fetch_calibration_data():
    return [0.1, 0.3, 0.4, 0.7, 0.9]

def apply_noise_filter(signal):
    return [x for x in signal if x > 0.2]

def deprecated_aggregate_method(data):
    # Dead code path — never called
    return sum(x ** 2 for x in data) / len(data)

def transform_sequence(seq, mode='fast'):
    if mode == 'fast':
        return [int(x * 10) % 7 for x in seq]
    else:
        return [math.ceil(x) for x in seq]

def validate_integrity(hash_sum, length):
    # Irrelevant validation logic
    return (hash_sum + length * 2) % 5 == 0

def compute_dynamic_weights(n):
    # Distractor: complex-looking but unused
    weights = [0] * n
    for i in range(n):
        weights[i] = (i * i + 3 * i + 7) % 11
    return weights

def analyze_patterns(arr):
    count_map = defaultdict(int)
    for x in arr:
        count_map[x] += 1
    freq = Counter(count_map)
    mode_val = freq.most_common(1)[0][1]
    return mode_val > 1

def shift_cipher(data, key):
    # Bit manipulation red herring
    shifted = []
    for d in data:
        shifted.append((d ^ key) & 0xF)
    return shifted

def prepare_dataset(source):
    # Intermediate transformation with decoy outputs
    base = [int(math.log(x + 1) * 10) for x in source]
    filtered = [x for x in base if x % 2 == 0]
    extended = filtered + [sum(filtered)]
    # Unused variables to mislead
    temp_checksum = sum(extended) * 3 % 19
    metadata_flag = len(extended) > 5
    return extended

def evaluate_thresholds(values, limit=15):
    # Linear search and comparison mix
    result = 0
    for v in values:
        if v < limit and v % 3 == 0:
            result += v
    return result

def merge_and_refine(a, b):
    # Merges two lists with conditional logic
    merged = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1
    merged.extend(a[i:])
    merged.extend(b[j:])
    return merged

def extract_diagnostic_code(trace):
    # Complex branching with irrelevant outcome
    code = 0
    for t in trace:
        if t > 5:
            code ^= t
        elif t == 2:
            code += 3
    return code % 256

def process_results(data, config):
    # Core relevant logic embedded in noise
    stage1 = [x * 2 + 1 for x in data]
    
    # Conditional expression used
    stage2 = [x for x in stage1 if x > config['threshold']] if config['filter'] else stage1
    
    # Key computation branch
    if len(stage2) >= 4:
        reduced = stage2[:4]
        xor_accum = 0
        for val in reduced:
            xor_accum ^= val  # bitwise XOR chain
        
        # Actual answer derivation
        sum_part = sum(reduced)
        mod_part = sum_part % 17
        final_value = (xor_accum * 2) - mod_part
        
        # Decoy computations below
        stats = {
            'mean': sum(stage2) / len(stage2),
            'peak': max(stage2),
            'valid': analyze_patterns(stage2)
        }
        debug_trace = shift_cipher(reduced, 5)
        diagnostic = extract_diagnostic_code(debug_trace)
        
        return final_value  # Only this matters
    else:
        return -999  # unreachable under correct input

# Irrelevant global variables
system_status = 'ACTIVE'
calibration_matrix = [[1, 2], [3, 4]]
last_updated = '2023-11-05'

# Main execution flow
if __name__ == '__main__':
    raw_input = [0.5, 1.2, 2.3, 3.1, 4.0, 5.5]
    processed = prepare_dataset(raw_input)
    
    # More distractions
    calibrated = fetch_calibration_data()
    cleaned = apply_noise_filter(calibrated)
    transformed = transform_sequence(cleaned, mode='fast')
    
    # Real data dependency
    config = {
        'threshold': 3,
        'filter': True,
        'mode': 'strict'
    }
    
    # Critical call
    final_output = process_results(processed, config)
    
    # Print required output
    print(f"Target result: {final_output}")