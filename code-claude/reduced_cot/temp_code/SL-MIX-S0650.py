import itertools

def calculate_packet_hash(data_stream, window_size=3):
    """Calculate a simple hash based on sliding window of data packets"""
    primary_hash = 0
    secondary_hash = 0
    tertiary_hash = 0  # Used for integrity checking, not part of final result
    
    # Process data in sliding windows
    for window in itertools.islice(itertools.zip_longest(*[iter(data_stream)] * window_size), 10):
        # Filter out None values that might appear in the last window
        valid_packets = [p for p in window if p is not None]
        
        if not valid_packets:
            continue
            
        # Calculate window signature using XOR of packet values
        window_signature = 0
        for packet in valid_packets:
            window_signature ^= packet
        
        # Update primary hash with window signature
        primary_hash = (primary_hash * 31 + window_signature) & 0xFFFF
        
        # Calculate alternative signature for secondary hash
        alt_signature = sum(valid_packets) % 256
        secondary_hash = (secondary_hash + alt_signature * len(valid_packets)) & 0xFFFF
        
        # Update tertiary hash for verification (not used in final result)
        tertiary_hash = (tertiary_hash | (max(valid_packets) & 0xFF)) << 1
        if tertiary_hash > 0xFFFF:
            tertiary_hash = tertiary_hash & 0xFFFF
    
    # Apply final transformations
    primary_hash = (primary_hash * 17) % 65536
    secondary_hash = (secondary_hash + 1000) % 65536
    
    # Combine hashes to get final result
    final_hash = (primary_hash ^ secondary_hash) % 10000
    integrity_check = (primary_hash & secondary_hash) % 1000  # Not used in final result
    
    return final_hash

# Data stream representing network packets (values between 0-255)
packet_stream = [42, 128, 255, 16, 32, 64, 90, 131, 200, 45, 78, 12, 39, 250, 84, 23, 177, 99, 45, 143]

# Calculate the hash
result = calculate_packet_hash(packet_stream)
print(f"Result: {result}")