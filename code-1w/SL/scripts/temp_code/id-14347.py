def process_entry(data, threshold=5):
    if len(data) < threshold:
        return sum([x ** 2 for x in data if x % 2 == 1])
    else:
        return sum([x for x in data if x % 3 == 0])

# Irrelevant helper (decoy)
def validate_checksum(seq):
    return sum(seq) % 7 == 0

# Unused transformation path
def transform_legacy(arr):
    return [a << 1 for a in arr if a > 3]

# Core diagnostic function
def analyze_pattern(sequence, mode='fast'):
    snapshot = []
    temp_result = 0
    
    for i, val in enumerate(sequence):
        if i % 2 == 0 and val > 0:
            temp_result += val * (i + 1)
        elif val < 0:
            temp_result -= abs(val) // 2
    
    snapshot.append(temp_result)
    
    # Distractor: complex but unused logic
    secondary_trace = list(map(lambda x: (x**2) + 1, sequence))
    filtered_data = [x for x in secondary_trace if x in sequence]
    
    if mode == 'deep':
        extra = sum(filtered_data) // len(filtered_data)
        snapshot.append(extra)
    
    return snapshot[0]  # Only first used

# Aggregation with slicing distraction
def aggregate_metrics(log_str, offset):
    digits = [int(c) for c in log_str if c.isdigit()]
    
    # Real computation path
    segment_a = digits[offset:offset+4]
    segment_b = digits[offset+2:offset+6]
    
    score_1 = sum(segment_a) * 2
    score_2 = sum(segment_b) // 2
    
    # Heavily distracting but irrelevant string operations
    reversed_hex = ''.join([hex(d)[2:] for d in digits[::-1]])
    padded_slice = (reversed_hex + 'xxxx')[:8]
    char_sum = sum([ord(c) - ord('a') for c in padded_slice if c.isalpha()])
    
    # Decoy variable that looks important
    meta_weight = char_sum % 13
    
    # Final metric based on overlapping slices
    return (score_1 - score_2 + offset) * 3

# --- Main execution with red herrings ---

data_stream = [4, -6, 9, 12, 3, -1, 8, 0, 5]
base_config = {'version': 2, 'debug': False}

# Useless pre-processing chain
shifted_data = [x + 2 for x in data_stream]
masked_data = [x & 7 for x in shifted_data]
decoded_signal = ''.join([chr(97 + (x % 26)) for x in masked_data])

# Another decoy call
validation_flag = validate_checksum(data_stream[:5])
legacy_output = transform_legacy(data_stream)

# Key processing step
processed_val = process_entry(data_stream, threshold=4)

# Generate intermediate log (string with numbers)
temp_log = f"log_v2_{processed_val}_chk{sum(masked_data)}_seq9"

# Extract offset using string method distraction
prefix_part = temp_log.split('_')[1]  # 'v2'
num_part = ''.join([c for c in temp_log if c.isdigit()])  # '21299'
base_offset = int(num_part[1:3])  # '12' -> 12

# Critical statement
final_diagnostic = aggregate_metrics(temp_log, base_offset)

# Print result as required
print(f"Result: {final_diagnostic}")