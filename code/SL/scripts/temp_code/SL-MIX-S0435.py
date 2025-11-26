def process_data_sequence(data_seq, mask_pat):
    # Irrelevant initialization for distraction
    temp_buffer = [0] * len(data_seq)
    offset_calc = sum(x % 3 for x in range(10))  # Distractor computation
    
    # Main processing logic
    processed_values = []
    for idx, value in enumerate(data_seq):
        # Misleading conditional path
        if idx % 2 == 0:
            masked_val = value & mask_pat
        else:
            masked_val = value | mask_pat
        
        # Red herring transformation
        temp_transform = (masked_val << 2) ^ 0xFF
        
        # Actual relevant computation
        if idx > 0 and data_seq[idx-1] < value:
            processed_val = (masked_val + temp_transform) // 2
        else:
            processed_val = (masked_val * temp_transform) % 256
        
        processed_values.append(processed_val)
    
    # Dead code path - never executed
    unused_result = sum(x * 2 for x in processed_values if x % 3 == 0)
    
    return processed_values

# Main execution with multiple distractions
data_sequence = [45, 78, 123, 56, 189, 34, 200]
mask_pattern = 0x7F

# Irrelevant computations for interference
auxiliary_sum = sum(data_sequence) + len(data_sequence)
pattern_shift = mask_pattern << 1

# Critical execution point
processed_data = process_data_sequence(data_sequence, mask_pattern)

# More distractor operations
filtered_data = [x for x in processed_data if x > 50]
weighted_avg = sum(x * i for i, x in enumerate(processed_data)) / len(processed_data)

# Final hash calculation (target variable)
final_hash = 0
for i, val in enumerate(processed_data):
    # Complex bitwise operation chain
    if i < len(processed_data) // 2:
        final_hash ^= (val << (i % 4))
    else:
        final_hash |= (val >> ((i - 3) % 4))
    
    # Misleading intermediate update
    if i % 2 == 0:
        final_hash += 16  # This gets overwritten
    
    # Actual final computation
    final_hash = (final_hash * 31 + val) & 0xFFFF

print(f"Result: {final_hash}")