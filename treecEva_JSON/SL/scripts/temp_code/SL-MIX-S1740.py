import itertools

def analyze_packet(hex_data):
    byte_values = [int(hex_data[i:i+2], 16) for i in range(0, len(hex_data), 2)]
    threat_indicators = [0x1B, 0x2F, 0x7E, 0xA3]
    threat_level = 0
    
    # Greedy approach to find longest sequence of threat indicators
    max_sequence = 0
    current_sequence = 0
    
    for byte_val in byte_values:
        if byte_val in threat_indicators:
            current_sequence += 1
            max_sequence = max(max_sequence, current_sequence)
        else:
            current_sequence = 0
    
    # String transformation for obfuscation detection
    hex_chars = ''.join([hex(b)[2:].zfill(2) for b in byte_values])
    reversed_segments = [hex_chars[i:i+4][::-1] for i in range(0, len(hex_chars), 4)]
    obfuscation_score = sum(1 for seg in reversed_segments if seg == seg[::-1])
    
    # Calculate final threat level
    threat_level = max_sequence * 10 + obfuscation_score
    return threat_level

# Packet data from a captured network stream
packet_stream = "1B2F7EA3FF1B2FA37E1B2F7EA3"
threat_level = analyze_packet(packet_stream)
print(f"Result: {threat_level}")