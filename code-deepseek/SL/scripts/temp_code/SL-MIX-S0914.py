def analyze_packet_sequence():
    packet_data = [45, 67, 23, 89, 12, 56, 34, 78]
    window_size = 3
    
    # Calculate window sums (distractor - not used in final answer)
    window_sums = []
    for i in range(len(packet_data) - window_size + 1):
        window_sum = sum(packet_data[i:i + window_size])
        window_sums.append(window_sum)
    
    # Extract relevant slice using slicing operation
    target_slice = packet_data[2:6]
    
    # Perform XOR operations on slice
    xor_result = 0
    for value in target_slice:
        xor_result ^= value
    
    # Additional intermediate calculation (distractor)
    temp_calculation = sum(packet_data[:4]) - packet_data[1]
    
    # Main computation using XOR result and modular arithmetic
    base_value = xor_result % 50
    adjustment = packet_data[0] // 10
    
    final_computation = base_value + adjustment * 7
    
    # Final assignment
    result = final_computation
    print(f"Target result: {result}")

analyze_packet_sequence()