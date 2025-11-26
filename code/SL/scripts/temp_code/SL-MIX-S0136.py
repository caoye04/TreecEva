def analyze_network_packets(packet_data):
    # Distractor: unused packet analysis
    packet_count = len(packet_data)
    max_size = max(packet_data) if packet_data else 0
    
    # Main computation path
    filtered_data = [x for x in packet_data if x % 3 != 0]
    processed_sum = sum(filtered_data)
    
    # Misleading intermediate calculations
    temp_checksum = processed_sum * 2 - 15
    parity_check = temp_checksum & 0xFF
    
    # Dead code path - never executed
    if packet_count > 100:
        unused_value = packet_count // 10
    
    # Red herring variables
    network_load = sum(packet_data) if packet_data else 0
    average_size = network_load / max(1, packet_count)
    
    # Key bitwise operation
    parity_mask = 0b10101010
    final_result = processed_sum ^ parity_mask
    
    # Print result
    print(f"Result: {final_result}")

# Test data
packet_sizes = [8, 15, 22, 30, 41, 55, 63, 74, 89, 97]
analyze_network_packets(packet_sizes)