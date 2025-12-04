def process_message(message, key):
    # Convert message and key to bytes
    message_bytes = [ord(c) for c in message]
    key_bytes = [ord(c) for c in key]
    
    # Calculate message statistics (not used in encryption)
    avg_ascii = sum(message_bytes) / len(message_bytes)
    max_ascii = max(message_bytes)
    min_ascii = min(message_bytes)
    
    # Prepare transformation matrix (distraction)
    transform = {
        'shift': (max_ascii - min_ascii) // 4,
        'scale': avg_ascii / 50
    }
    
    # Extract segments for processing
    segment_a = message_bytes[0:5]
    segment_b = message_bytes[2:8:2]  # Every other character from index 2 to 7
    segment_c = key_bytes[1:7:2]      # Every other character from index 1 to 6
    
    # Apply transformations (some are distractions)
    transformed_a = [x + transform['shift'] for x in segment_a]
    transformed_b = [int(x * transform['scale']) for x in segment_b]
    
    # XOR operation between segments
    encrypted_message = segment_b[0] ^ segment_c[0]
    
    # Secondary encryption (not used in final result)
    secondary_encryption = sum([a ^ b for a, b in zip(segment_a, key_bytes[:5])])
    
    # This is the key operation that determines the answer
    encrypted_message = 0
    for i in range(len(segment_b)):
        if i < len(segment_c):
            encrypted_message ^= segment_b[i] ^ segment_c[i]
    
    # Alternative calculation (distraction)
    alternative = sum(transformed_a) - sum(transformed_b)
    
    print(f"Result: {encrypted_message}")
    return encrypted_message

# Test with sample data
message = "Hello World!"
key = "secretkey"
result = process_message(message, key)