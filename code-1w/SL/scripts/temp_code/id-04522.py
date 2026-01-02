def compute_integrity_score(sequence, threshold_multiplier=3):
    base_seed = 7
    prime_offset = 101
    temp_buffer = []
    running_sum = 0
    checksum = 0
    
    # Preprocess: filter and transform sequence
    for num in sequence:
        if num > threshold_multiplier * base_seed:
            temp_buffer.append(num ** 2)
        else:
            temp_buffer.append(num + base_seed)
    
    # Misleading secondary processing (not used in final result)
    alt_accumulator = 0
    for idx in range(len(temp_buffer)):
        if idx % 2 == 0:
            alt_accumulator += temp_buffer[idx] // 3
    
    # Actual computation path
    processed_values = temp_buffer[::2]  # slicing every other element
    outlier_count = 0
    for value in processed_values:
        if value & 1:  # bitwise check for odd
            running_sum += value >> 1
        else:
            running_sum += value // 2
        
        # Key update point
        checksum = (checksum + value) % prime_offset
        
        # Red herring: tracking outliers that aren't used
        if value > 150:
            outlier_count += 1

    # Dummy recursive call with no effect
    def dummy_recursion(n):
        if n <= 1:
            return 1
        return dummy_recursion(n-1) + dummy_recursion(n-2)
    
    dummy_recursion(5)  # dead function call

    # Final irrelevant transformation
    final_shift = checksum << 1
    final_shift %= 200
    
    print(f"Result: {checksum}")

# Execute
sequence_input = [12, 8, 25, 14, 30, 5]
compute_integrity_score(sequence_input)