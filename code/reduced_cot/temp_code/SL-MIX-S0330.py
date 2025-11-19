def hex_chunk_processor(hex_chunks):
    processed_values = []
    for chunk in hex_chunks:
        # Convert hex to integer and apply modular transformation
        numeric_val = int(chunk, 16)
        transformed = (numeric_val * 17 + 23) % 256
        processed_values.append(transformed)
    
    # Apply secondary transformation using list comprehension
    secondary_vals = [((x << 2) ^ (x >> 1)) & 0xFF for x in processed_values]
    
    # Compute hash-based checksum
    checksum_components = []
    for i, val in enumerate(secondary_vals):
        component = (hash(str(val)) % 1000) * (i + 1)
        checksum_components.append(component)
    
    # Final checksum calculation
    checksum_result = sum(checksum_components) % 997
    return checksum_result

# Data packet chunks in hexadecimal
packet_chunks = ['A1', '2F', 'B8', '4C', '99']
checksum_result = hex_chunk_processor(packet_chunks)
print(f"Result: {checksum_result}")