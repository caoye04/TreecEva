def analyze_data_stream(data_packet):
    base_shift = 7
    temp_buffer = []
    running_sum = 0
    prime_offset = 101
    checksum = 0
    
    # Preprocess: filter alphanumeric and reverse order
    filtered_chars = [c for c in data_packet if c.isalnum()][::-1]
    
    # Misleading transformation - not used in final result
    encoded_snippet = ''.join([chr((ord(c) + base_shift) % 256) for c in data_packet[:10]])
    entropy_score = sum([ord(c) * 2 for c in encoded_snippet]) % 997
    
    # Accumulate running sum of digit ASCII values
    for c in data_packet:
        if c.isdigit():
            running_sum += ord(c) * 3
    
    # Secondary buffer processing with red herring logic
    for i, c in enumerate(filtered_chars):
        if i % 2 == 0:
            shifted = ord(c) << 1
            temp_buffer.append(shifted)
        else:
            temp_buffer.append(ord(c) + 10)
    
    # Core checksum computation — this is where the answer comes from
    for char in filtered_chars:
        if char.islower():
            checksum = (checksum + ord(char)) % prime_offset
    
    # Distractor: unused statistical calculation
    avg_value = sum(temp_buffer) / len(temp_buffer) if temp_buffer else 0
    deviation = abs(avg_value - running_sum) % prime_offset
    
    # Final irrelevant modification
    final_payload = [ord(c) ^ 5 for c in data_packet if c.isupper()]
    
    print(f"Result: {checksum}")

# Execute with sample data
analyze_data_stream("SecRet_P@ssw0rd!2048")