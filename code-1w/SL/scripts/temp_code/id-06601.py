def decode_segment(segment):
    if len(segment) < 3:
        return 0
    mid = len(segment) // 2
    left = segment[:mid]
    right = segment[mid:]
    if sum(left) > sum(right):
        return sum(left) * 2
    else:
        return sum(right) - sum(left)

# Irrelevant helper (distractor)
def validate_checksum(data):
    return sum(data) % 7 == 0

# Unused transformation (dead code path)
def transform_legacy_format(seq):
    return [x * 3 + 1 for x in seq if x % 2 == 0]

# Complex signal processor with red herrings
def process_transmission(sequence, code_map):
    temp_buffer = []
    history_log = []  # Collected but unused
    scaling_factor = 1.5
    
    for i in range(len(sequence)):
        chunk = sequence[i:i+4]
        if len(chunk) < 4:
            break
            
        # Distractor computation
        checksum = sum(chunk) * 0.1
        if checksum > 5:
            _ = [x ** 0.5 for x in chunk]  # Computed but not used
        
        # Real logic embedded among noise
        key_value = chunk[1] * chunk[2]
        if key_value in code_map:
            temp_buffer.append(code_map[key_value])
        else:
            temp_buffer.append(decode_segment(chunk))
    
    # Misleading accumulation
    fake_accumulator = 0
    for val in temp_buffer:
        fake_accumulator += val * 0.9  # Looks important, unused
    
    # Actual result path
    filtered = [x for x in temp_buffer if x > 10]
    if len(filtered) == 0:
        return -1
    
    # Critical slicing operation
    window = filtered[-3:]  # Last three valid signals
    base_score = sum(window) // len(window)
    
    # Final adjustment using logical and comparison ops
    adjustment = 5 if base_score > 20 and len(window) == 3 else 2
    return base_score + adjustment

# Dictionary mapping (core data structure)
code_dictionary = {
    12: 18,
    15: 25,
    16: 12,
    20: 30,
    24: 22
}

# Tuple unpacking distraction
primary, secondary = (100, 200)
backup_config = (5, 10, 15)

# Main signal sequence
signal_data = [2, 3, 4, 1, 5, 2, 3, 4, 1, 6, 2, 2, 4, 5, 1]

# Dead-end processing branch
if any(x < 0 for x in signal_data):
    signal_data = [abs(x) for x in signal_data]

# Linear search decoy
search_target = 99
found_index = -1
for idx, val in enumerate(signal_data):
    if val == search_target:
        found_index = idx
        break

# Actual execution path
processed_chunk = signal_data[2:11]  # Meaningful slice
final_signal = process_transmission(processed_chunk, code_dictionary)

# Output the target result
print(f"Result: {final_signal}")