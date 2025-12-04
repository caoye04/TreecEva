def data_processor(packets):
    # Process network packets and extract data segments
    processed_segments = []
    temp_buffer = []
    
    for packet in packets:
        # Distractor: intermediate processing that doesn't affect final result
        packet_size = len(str(packet))
        temp_buffer.append(packet_size)
        
        # Actual relevant processing
        if packet % 2 == 0:
            processed_segments.append(packet ^ 0xFF)
        else:
            processed_segments.append(packet & 0x0F)
    
    # Distractor: unused computation
    buffer_sum = sum(temp_buffer)
    
    return processed_segments

def data_validator(segments):
    # Validate data segments using lambda functions and set operations
    unique_validators = {
        'parity': lambda x: x | 0x01,
        'checksum': lambda x: (x + 1) ^ 0xAA
    }
    
    # Process segments through validation pipeline
    validated_data = []
    for segment in segments:
        # Apply multiple validation steps (only some affect final result)
        step1 = unique_validators['parity'](segment)
        step2 = unique_validators['checksum'](step1)
        
        # Distractor: additional validation that doesn't change outcome
        redundant_check = step2 & 0x55
        
        validated_data.append(step2)
    
    # Final computation using set operations
    data_set = set(validated_data)
    final_result = sum(data_set) % 256
    
    return final_result

# Main execution
raw_packets = [45, 128, 77, 200, 33, 150]
final_checksum = data_validator(data_processor(raw_packets))

# Distractor: unused variable
intermediate_value = len(raw_packets) * 2

print(f"Result: {final_checksum}")