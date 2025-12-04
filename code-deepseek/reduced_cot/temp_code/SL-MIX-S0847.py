def analyze_network_packets(packet_sequence):
    # Initialize tracking variables
    primary_sum = 0
    secondary_offset = 0
    redundant_check = 0
    
    # Simulate packet analysis with zip and enumerate
    packet_ids = [101, 102, 103, 104, 105]
    packet_sizes = [256, 512, 128, 1024, 768]
    flags = [1, 0, 1, 1, 0]
    
    for idx, (packet_id, size, flag) in enumerate(zip(packet_ids, packet_sizes, flags)):
        # Main calculation - only packets with flag=1 contribute to primary_sum
        if flag == 1:
            primary_sum += size
            redundant_check += packet_id  # Distractor - not used in final result
        
        # Secondary calculation - only even indices contribute to secondary_offset
        if idx % 2 == 0:
            secondary_offset += size // 8
        else:
            secondary_offset -= size // 16  # Distractor - opposite logic
    
    # Final computation with some intermediate steps
    intermediate = primary_sum * 2  # Unused calculation
    verification = sum(packet_sizes)  # Distractor - total sum
    
    # The key statement
    final_value = primary_sum + secondary_offset
    
    # Print the target result
    print(f"Result: {final_value}")

# Execute the analysis
analyze_network_packets([])