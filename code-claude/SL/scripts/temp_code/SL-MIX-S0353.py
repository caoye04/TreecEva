def calculate_final_score(messages, keys):
    # Initialize values
    base_value = 120
    multiplier = 3
    validation_count = 0
    penalty = 0
    
    # Process messages with their keys
    for idx, (msg, key) in enumerate(zip(messages, keys)):
        # Apply XOR operation between first chars of message and key
        first_char_xor = ord(msg[0]) ^ ord(key[0])
        
        # Track message length for statistics (not used in calculation)
        message_length = len(msg)
        stats = {
            'length': message_length,
            'uppercase': sum(1 for c in msg if c.isupper()),
            'digits': sum(1 for c in msg if c.isdigit())
        }
        
        # Apply validation rules
        if first_char_xor % 2 == 0:
            validation_count += 1
        
        # Calculate penalty based on message index and key
        if idx > 0 and idx % 2 == 1:
            bit_count = bin(ord(key[-1])).count('1')
            penalty += bit_count
        
        # Log processing (not affecting result)
        log_entry = f"Message {idx}: {stats['length']} chars"
    
    # Calculate intermediate scores
    raw_score = base_value + (validation_count * multiplier)
    temp_score = raw_score - penalty
    
    # Apply bitwise operation to finalize score
    final_score = temp_score & 0xFF
    
    return final_score

# Test data
encrypted_messages = ["H3llo", "W0rld", "Py7h0n", "C0d1ng"]
validation_keys = ["key1", "key2", "key3", "key4"]

# Calculate the message score
message_score = calculate_final_score(encrypted_messages, validation_keys)

# Other operations that don't affect the result
debug_mode = False
if debug_mode:
    for i, msg in enumerate(encrypted_messages):
        print(f"Debug: {i} -> {msg}")

print(f"Result: {message_score}")