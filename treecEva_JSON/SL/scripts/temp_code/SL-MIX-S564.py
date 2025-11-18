from collections import defaultdict

def process_packets():
    # Initialize packet tracking system
    packet_registry = defaultdict(int)
    validation_flag = 0x1F3C
    
    # Encrypted packet headers
    packet_headers = [0xA7, 0x3B, 0x9E, 0x64, 0xF1]
    
    # Process each packet
    for idx, header in enumerate(packet_headers):
        # Register packet occurrence
        packet_registry[header & 0x0F] += 1
        
        # Apply custom checksum: XOR with shifted header
        validation_flag ^= (header << (idx & 3))
        
        # Conditional update based on packet registry
        active_channels = sum(1 for count in packet_registry.values() if count > 0)
        validation_flag = validation_flag & 0xFFFF if active_channels > 2 else validation_flag | 0x8000
        
        # Apply modular adjustment
        validation_flag = (validation_flag + (header * idx)) % 0xFFFF
    
    # Final security check
    channel_diversity = len([k for k in packet_registry if packet_registry[k] > 0])
    validation_flag = validation_flag ^ (0xFF & (channel_diversity << 4))
    
    return validation_flag

# Execute packet processing
final_validation_flag = process_packets()
print(f"Result: {final_validation_flag}")