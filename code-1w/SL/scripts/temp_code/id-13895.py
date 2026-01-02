def compute_validation_code(sequence):
    raw_data = [ord(c) for c in sequence]
    filtered_data = [x for x in raw_data if x % 2 == 1]
    
    # Slice to take only middle portion
    mid_section = filtered_data[1:-1] if len(filtered_data) > 2 else filtered_data
    
    # Irrelevant debug variable (minimal distraction)
    debug_length = len(mid_section)
    
    valid_parts_sum = sum(mid_section)
    checksum = (valid_parts_sum * 31) % 97
    return checksum

result = compute_validation_code("SecToken2024")
print(f"Result: {result}")