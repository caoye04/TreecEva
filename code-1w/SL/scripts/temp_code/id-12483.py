import math

# Irrelevant helper function (dead code path)
def unused_checksum(data):
    return sum(d % 7 for d in data) * 3

# Decoy transformation with misleading intermediate results
def false_transform(seq):
    return [x ** 2 + 1 for x in seq if x % 3 != 0]

# Real transformation: applies modular arithmetic and bit shifts
def transform_input(raw):
    temp = []
    for val in raw:
        shifted = (val << 1) & 0xFF  # Left shift and mask to 8 bits
        modded = (shifted + 5) % 97
        if modded % 2 == 0:
            temp.append(modded // 3)
        else:
            temp.append((modded * 2) % 43)
    return temp

# String-based distractor: processes irrelevant metadata
def extract_tags(header_str):
    tags = header_str.upper().split(':')
    filtered = [t.strip() for t in tags if 'KEY' in t]
    return {i: f"Tag_{i}_{filtered[i]}" for i in range(len(filtered))}

# Dictionary operation: maps indices to diagnostic codes (some relevant)
def generate_codes(count):
    codes = {}
    for i in range(count):
        if i % 4 == 0:
            codes[i] = f"DX_{(i * 31) % 109}"
        elif i % 3 == 0:
            codes[i] = f"ERR_{(i * 17) % 83}"
        else:
            codes[i] = f"ST_{(i * 7) % 61}"
    return codes

# Core analysis function: computes final result via recursion and filtering
def analyze_pattern(data_list):
    def recursive_reduce(arr, depth):
        if depth <= 0 or len(arr) < 2:
            return arr[0] if arr else 13
        new_arr = []        
        for i in range(len(arr) - 1):
            op = (i + depth) % 4
            if op == 0:
                new_arr.append((arr[i] + arr[i+1]) % 19)
            elif op == 1:
                new_arr.append((arr[i] * arr[i+1]) % 23)
            elif op == 2:
                new_arr.append(abs(arr[i] - arr[i+1]) % 17)
            else:
                new_arr.append((arr[i] ^ arr[i+1]) % 29)  # XOR mod
        return recursive_reduce(new_arr, depth - 1)
    
    # Filtering logic with string method distraction
    valid_indices = []
    for idx, val in enumerate(data_list):
        bin_str = bin(val)[2:]  # Remove '0b' prefix
        if bin_str.count('1') >= 3 and len(bin_str) <= 8:
            valid_indices.append(idx)
    
    # Use dictionary to map and weight values
    weights = generate_codes(len(data_list))
    weighted_vals = []
    for i, v in enumerate(data_list):
        code_key = ''.join([c for c in weights.get(i, 'ST_0') if c.isdigit()])
        mult = int(code_key) % 7 if code_key.isdigit() else 3
        weighted_vals.append((v * mult) % 53)
    
    # Apply reduction on filtered subset
    filtered = [weighted_vals[i] for i in valid_indices if i < len(weighted_vals)]
    if not filtered:
        return sum(weighted_vals) % 101
    
    # Execute recursive reduction
    return recursive_reduce(filtered, 3)

# Main execution flow
if __name__ == '__main__':
    # Initial dataset (real input)
    sensor_readings = [12, 19, 27, 34, 43, 56, 61, 72]
    
    # Irrelevant variables (distractors)
    calibration_matrix = [[1, 0], [0, 1]]
    timestamp_log = "KEY_INIT:2024-05-20T10:30:00Z:KEY_SYNC"
    debug_mode = True
    max_iterations = 99
    
    # Real transformation pipeline
    transformed_data = transform_input(sensor_readings)
    
    # Unused operations (red herring computations)
    dummy_stats = {
        'mean_floor': sum(sensor_readings) // len(sensor_readings),
        'peak_shift': max(transformed_data) << 2,
        'tag_count': len(extract_tags(timestamp_log))
    }
    
    # Critical statement: compute final diagnostic
    final_diagnostic = analyze_pattern(transformed_data)
    
    # Output result as required
    print(f"Result: {final_diagnostic}")