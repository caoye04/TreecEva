def compute_final_result():
    data_stream = [i for i in range(1, 21) if i % 2 != 0]
    temp_calc = lambda x: (x * 3) ^ (x << 1)
    
    # Distractor operations
    processed_data = [temp_calc(x) for x in data_stream]
    irrelevant_set = {x % 7 for x in processed_data}
    tracking_dict = {k: v for k, v in enumerate(processed_data)}
    
    # Misleading intermediate result (dead code path)
    dead_path_sum = sum([x * 2 for x in data_stream if x > 10])
    
    # Key computation chain
    bit_mask = 0b10101
    intermediate = [x & bit_mask for x in processed_data]
    
    # Another distractor
    misleading_avg = sum(processed_data) // len(processed_data)
    
    # Core logic with slicing
    relevant_slice = intermediate[2:7]
    xor_result = 0
    for val in relevant_slice:
        xor_result ^= val
    
    # Final computation
    adjustment = len(data_stream) - len(relevant_slice)
    result = (xor_result | adjustment) % 1000
    
    # Unused operation
    unused_calc = misleading_avg * dead_path_sum
    
    return result

# Execute and print
final_output = compute_final_result()
print(f"Result: {final_output}")