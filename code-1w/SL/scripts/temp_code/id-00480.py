def analyze_data_stream(data_packets, threshold=128):
    flow_state = [0] * 256
    temp_accum = 0
    checksum = 54321
    entropy_count = 0
    
    for index, packet in enumerate(data_packets):
        if len(packet) == 0:
            continue
            redundant_flag = True  # Dead code path

        size_metric = len(packet) % 256
        flow_state[size_metric] += 1
        
        # Irrelevant entropy tracking
        if sum(1 for x in packet if x % 7 == 0) > 2:
            entropy_count += 1

        for byte_idx, byte_val in enumerate(packet):
            masked_byte = byte_val & 0x7F
            inverted_index = 255 - index
            
            # Distractor computation with conditional expression
            adjustment = byte_val if byte_val > threshold else (~byte_idx + 3)
            temp_accum += adjustment % 19
            
            # Core logic: process only specific bytes
            if masked_byte % 3 == (index % 3):
                processed_value = (masked_byte ^ (byte_idx % 17)) | 0x10
                checksum = (checksum << 1) ^ processed_value  # Key statement

        # Extra distraction: unused state update
        if index % 5 == 0:
            flow_state[(index * 3) % 256] ^= index % 10

    # Final red herring calculation
    final_offset = sum(flow_state[i] for i in range(0, 256, 16))
    temp_accum = (temp_accum + final_offset) % 10000  # Not affecting checksum

    print(f"Result: {checksum}")

# Deterministic input
packets = [
    [0x9A, 0x1B, 0x2C, 0x3D],
    [0x4E, 0x5F],
    [0x60, 0x71, 0x82, 0x93, 0xA4],
    []
]
analyze_data_stream(packets)