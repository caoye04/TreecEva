import math

def legacy_checksum(values):
    # Irrelevant function - dead code path
    return sum(v ** 2 for v in values) % 17

def auxiliary_transform(x):
    # Distractor: used only on decoy data
    return (x << 2) ^ 0xA3

def recursive_mod(n, base):
    # Real but obfuscated component: computes n mod base recursively
    if n < base:
        return n
    return recursive_mod(n - base, base)

def decode_sequence(seq):
    # Mix of relevant and irrelevant operations
    temp_result = 0
    shift_accum = 1
    for i, val in enumerate(seq):
        if i % 2 == 0:
            temp_result += (val * shift_accum) % 97
            shift_accum *= 3
        else:
            # Misleading branch - modifies unused variable
            dummy = (val + 5) * 2
    return temp_result

def analyze_frequency(data):
    # Heavily distracting: builds frequency map but only one entry matters
    freq_map = {}
    for item in data:
        freq_map[item] = freq_map.get(item, 0) + 1
    
    # Decoy computations
    sorted_keys = sorted(freq_map.keys())
    offset = sum(k for k in sorted_keys if k % 3 == 0)
    adjustment = math.ceil(math.log(max(freq_map.values()) + 1, 2))
    
    # Relevant extraction
    primary_key = min(freq_map.keys())
    return freq_map[primary_key] + adjustment  # Used later

def process_pipeline(stream):
    # Core logic buried in distractions
    buffer = []
    for num in stream:
        if num < 0:
            # Red herring: negative numbers are filtered out
            continue
        if num % 7 == 0:
            # Another filter - not obviously critical
            buffer.append(num // 7)
        else:
            buffer.append(num * 2)
    
    # Tuple unpacking distraction
    transformed, *_ = (buffer, [x**2 for x in buffer], [x+1 for x in buffer])
    
    # Real processing begins
    stage_one = decode_sequence(transformed)
    stage_two = analyze_frequency(transformed)
    
    # Bit manipulation decoy
    masked_value = stage_one ^ 0xFFFF
    inverted = ~masked_value & 0xFFFF
    
    # Actual computation path
    mod_control = recursive_mod(stage_one, 13)
    intermediate = (stage_two * mod_control) + len(transformed)
    
    # Final red herring: unused complex structure
    log_table = {i: round(math.log(i + 1), 4) for i in range(1, 21)}
    for key in log_table:
        log_table[key] *= 1.05
    
    # Critical deterministic assignment
    final_output = intermediate + 42
    return final_output

# Simulated sensor data stream - realistic context
raw_readings = [14, 3, 8, 21, 5, 14, 9, 7, 11, 3]
data_stream = [x - 10 for x in raw_readings]  # Introduces negatives

# Unused variables - misleading state
baseline_offset = 0xBADC
reference_frame = (100, 200, 300)
calibration_data = {'gain': 1.05, 'offset': 0xFF}

# Key execution point
final_output = process_pipeline(data_stream)
print(f"Result: {final_output}")