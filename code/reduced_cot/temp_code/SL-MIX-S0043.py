import itertools

def process_data(data_stream):
    # Distractor: complex bit manipulation that doesn't affect final result
    mask_generator = 0b10101010
    temp_shifter = data_stream[0] << 3
    bit_accumulator = temp_shifter & mask_generator
    
    # Main logic: pairwise combinations and sum filtering
    valid_pairs = []
    for a, b in itertools.combinations(data_stream, 2):
        # Misleading intermediate calculation
        product_distractor = a * b + (a ^ b)
        
        # Actual filtering condition
        if (a + b) % 7 == 0:
            valid_pairs.append((a, b))
    
    # Dead code path - never executed
    if len(valid_pairs) > 100:
        unreachable_sum = sum(x * y for x, y in valid_pairs)
        return unreachable_sum // 2
    
    # Real computation path
    checksum = 0
    for pair in valid_pairs:
        # More distractions with bit operations
        xor_mask = pair[0] ^ pair[1]
        checksum += xor_mask
        
        # Irrelevant intermediate state
        temp_state = (checksum * 3) % 256
    
    # Final transformation with distraction
    final_shift = (checksum >> 2) | (checksum << 6)
    return checksum  # The actual return value

# Initial data processing with distractions
raw_data = [14, 8, 21, 35, 7, 42, 28, 13, 56, 19]

# Irrelevant data transformation
scaled_data = [x * 2 for x in raw_data]
filtered_distractor = [x for x in scaled_data if x % 5 != 0]

# Actual transformation
processed_distractor = [x + 1 for x in raw_data]
transformed = [x - 3 for x in processed_distractor]

# Dead variable initialization
backup_storage = sum(transformed) * 2

# Critical execution point
final_checksum = process_data(transformed)
print(f"Result: {final_checksum}")