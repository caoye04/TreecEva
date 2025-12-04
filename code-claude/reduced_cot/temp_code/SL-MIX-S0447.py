# Network packet analysis utility function
def analyze_packet(raw_data, filter_type='none'):
    # Decode packet data
    packet_bytes = [ord(c) if isinstance(c, str) else c for c in raw_data]
    
    # Calculate initial checksum (distractor)
    initial_checksum = sum(packet_bytes) % 256
    
    # Apply protocol-specific transformations
    transformed = ''.join([chr((b ^ 0x5A) & 0xFF) for b in packet_bytes])
    
    # Filter based on type
    noise_chars = "!@#$%^&*()"
    important_chars = "abcdefABCDEF0123456789"
    
    # Apply different filters (only one actually matters)
    if filter_type == 'noise':
        filtered_text = ''.join([c for c in transformed if c not in noise_chars])
    elif filter_type == 'hex':
        filtered_text = ''.join([c for c in transformed if c in important_chars])
    else:
        # Default filter keeps alphanumeric
        filtered_text = ''.join(filter(lambda x: x.isalnum(), transformed))
    
    # Calculate filtered length (distractor)
    filtered_len = len(filtered_text)
    
    # Store both filtered and unfiltered data in set (distractor)
    data_set = set(filtered_text + transformed)
    
    # Compute hash value of filtered text
    filtered_hash = sum([ord(c) for c in filtered_text]) & 0xFF
    
    # Calculate alternative hash (distractor)
    alt_hash = filtered_len ^ initial_checksum
    
    print(f"Result: {filtered_hash}")
    return filtered_hash

# Sample packet data
packet = "P4ck3t@Data#123"

# Process with default filter
result = analyze_packet(packet)
