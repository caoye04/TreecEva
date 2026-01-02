def compute_integrity_value():
    sequence = [17, 23, 4, 58, 91, 34, 5, 67, 29]
    offset = 13
    mod_base = 101
    
    # Slice middle portion for processing
    segment = sequence[2:7]  # [4, 58, 91, 34, 5]
    
    data_sum = 0
    for val in segment:
        data_sum += val % 17  # Use modular arithmetic to limit growth
    
    temp_factor = 2  # Irrelevant distractor variable (minimal interference)
    unused_flag = False  # Another benign variable to slightly raise intervention
    
    checksum = (data_sum + offset) % mod_base
    return checksum

result = compute_integrity_value()
print(f"Result: {result}")