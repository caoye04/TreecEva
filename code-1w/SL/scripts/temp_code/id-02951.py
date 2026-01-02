import math

# Irrelevant helper function (dead code path)
def unused_helper(x):
    return (x ** 2 + 3 * x) % 7

# Distractor variables
temp_cache = [0] * 100
debug_flag = True
auxiliary_sum = 0
offset_correction = 17
scaling_factor = 2.5
junk_data = [i ^ 42 for i in range(50)]

# Real processing functions
def validate_checksum(arr):
    # Simple XOR checksum
    checksum = 0
    for val in arr:
        checksum ^= val
    return checksum == 0xFF

# Bit manipulation with conditional expression
def transform_value(x, mode):
    shifted = (x << 2) & 0xFF
    flipped = shifted ^ 0xAA
    # Conditional expression used here
    adjusted = flipped + 5 if (flipped % 3 == 0) else flipped - 3
    return adjusted

# Linear search for threshold (used in pipeline)
def find_first_exceeding(arr, threshold):
    for i, val in enumerate(arr):
        if val > threshold:
            return i
    return -1

# Data transformation stage
def encode_sequence(seq):
    result = []
    for item in seq:
        transformed = transform_value(item, mode='encode')
        result.append(transformed)
    return result

# Another irrelevant computation
def compute_entropy(data):
    freq_map = {}
    for d in data:
        freq_map[d] = freq_map.get(d, 0) + 1
    total = len(data)
    entropy = 0.0
    for count in freq_map.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 3)

# Main pipeline logic
def process_pipeline(raw_data):
    # Stage 1: Filter and trim
    filtered = [x for x in raw_data if x % 2 == 1]  # Keep odd numbers
    
    # Stage 2: Transform using bit operations
    encoded = encode_sequence(filtered)
    
    # Stage 3: Find first value exceeding threshold
    threshold_index = find_first_exceeding(encoded, 150)
    index_offset = threshold_index if threshold_index != -1 else len(encoded)
    
    # Stage 4: Apply conditional scaling
    scaled_values = []
    for v in encoded:
        # Complex conditional expression
        scaled = v * scaling_factor if v > 100 else (v + 10) * 1.5 if v > 50 else v * 0.8
        scaled_values.append(int(scaled))
    
    # Stage 5: Aggregate with checksum validation
    if validate_checksum(scaled_values[:5]):
        aggregate = sum(scaled_values)
    else:
        aggregate = sum(scaled_values[:8])
    
    # Introduce more red herring
    dummy_calc = (aggregate ^ 0xFFFF) >> 4
    temp_result = (aggregate + offset_correction) * 3
    
    # Final output depends only on specific calculation
    final_output = (aggregate // 7) + (len(scaled_values) * 2)
    
    # Unused but misleading intermediate
    potential_alternative = temp_result - dummy_calc
    
    return final_output

# Simulated sensor data chunk (real input)
data_chunk = [123, 45, 67, 89, 21, 93, 11, 59, 73, 101]

# Call the main function
final_output = process_pipeline(data_chunk)
print(f"Target result: {final_output}")