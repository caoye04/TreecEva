def generate_network_keys(data_packets, security_level=3):
    # Initialize base values
    base_key = 42
    secondary_key = 0
    validation_sum = 0
    packet_metrics = []
    
    # Process data packets to generate keys
    for idx, packet in enumerate(data_packets):
        if idx % 2 == 0:  # Process even-indexed packets
            secondary_key += len(packet)
        else:  # Process odd-indexed packets for validation only
            validation_sum += sum(ord(c) for c in packet if c.isalpha())
        
        # Track metrics for logging purposes
        packet_metrics.append((idx, len(packet)))
    
    # Apply security transformations
    security_factor = security_level * 2
    base_key = (base_key * security_factor) % 256
    
    # Generate potential keys based on different algorithms
    potential_keys = []
    for i, (idx, length) in enumerate(packet_metrics[:3]):
        potential_keys.append((base_key + length) ^ (idx + 10))
    
    # Determine mask based on security level
    mask = 0xFF if security_level < 4 else 0x1FF
    
    # Apply bitwise operations to generate final key
    encryption_key = (base_key ^ secondary_key) & mask
    
    # Alternate key for backup (not used in final result)
    backup_key = sum(potential_keys) % 128
    
    # Apply final transformation based on validation
    if validation_sum > 1000:
        encryption_key = (encryption_key + 50) % 256
    
    print(f"Result: {encryption_key}")
    return encryption_key

# Test with sample data
data_packets = ["Hello", "Network", "Security", "Protocol"]
result = generate_network_keys(data_packets)