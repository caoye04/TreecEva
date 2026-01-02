def process_data(data, settings):
    temp_result = 0
    scaling_factor = settings['scale']
    offset = settings.get('offset', 0)
    mode = settings['mode']
    
    intermediate_values = []
    checksum = 0
    
    for item in data:
        if isinstance(item, int):
            checksum += item * 3
        elif isinstance(item, str):
            checksum += len(item) // 2
    
    normalized_checksum = checksum % 100
    
    # Irrelevant transformation (distractor)
    transformed_data = [x.upper() if isinstance(x, str) else x for x in data]
    filtered_data = [x for x in transformed_data if isinstance(x, int)]
    
    accumulation = 0
    for val in filtered_data:
        if val > 10:
            accumulation += val // 2
        else:
            accumulation += val
    
    # Key logic path
    if mode == 'aggressive':
        temp_result = (accumulation * scaling_factor) + offset
    elif mode == 'conservative':
        temp_result = accumulation + normalized_checksum
    else:
        temp_result = accumulation * 2
    
    # Dead computation - doesn't affect result
    redundant_sum = sum([i**2 for i in range(3)])  # Always 5, irrelevant
    metadata_log = {'entries': len(data), 'checksum': normalized_checksum}
    
    final_value = temp_result + 5
    return final_value

# Setup inputs
packet_buffer = [12, 'signal', 8, 'ACK', 15, 4, 'retry']
config = {
    'scale': 3,
    'mode': 'normal',
    'threshold': 7
}

# Misleading pre-processing (semi-relevant)
duplicate_check = {x: packet_buffer.count(x) for x in set(packet_buffer) if isinstance(x, int)}
buffer_length = len(packet_buffer)
size_factor = buffer_length * 0.5

final_output = process_data(packet_buffer, config)
print(f"Result: {final_output}")