import re

def packet_validator(pattern):
    def decorator(func):
        def wrapper(packet_list):
            valid_packets = []
            for packet in packet_list:
                header = packet['header']
                if isinstance(header, str) and re.match(pattern, header):
                    valid_packets.append(packet)
            return func(valid_packets)
        return wrapper
    return decorator

@packet_validator(r'^[0-9A-F]{8}$')
def analyze_packets(packets):
    threat_level = 0
    suspicious_flags = 0b11001010
    
    for packet in packets:
        header_hex = packet['header']
        payload_len = packet['length']
        
        # Convert hex header to integer for bitwise operations
        header_int = int(header_hex, 16)
        
        # Check for suspicious flags using bitwise AND
        if header_int & suspicious_flags == suspicious_flags:
            threat_level += 1
            
        # Nested loop to check payload characteristics
        payload = packet.get('payload', '')
        hidden_pattern_count = 0
        
        for i in range(len(payload) - 2):
            substring = payload[i:i+3]
            # String transformation and pattern matching
            if substring.lower() == 'xor' or substring.upper() == 'ENC':
                hidden_pattern_count += 1
                if hidden_pattern_count >= 2:
                    threat_level += 2
                    break  # Early exit from inner loop
        
        # Logical operations with comparison
        if payload_len > 100 and (header_int >> 16) & 0xFF == 0xAA:
            threat_level += 3
        elif payload_len <= 50 or not (header_int & 0x01000000):
            threat_level -= 1
    
    # Final adjustment based on total packets processed
    if len(packets) >= 5:
        threat_level *= 2
    else:
        threat_level //= 2 if threat_level > 0 else 1
        
    return threat_level

# Packet data for analysis
network_traffic = [
    {'header': 'FFCA1234', 'length': 150, 'payload': 'Some data with XOR encryption'},
    {'header': 'ABCD5678', 'length': 75, 'payload': 'Normal payload content'},
    {'header': 'CAFEBABE', 'length': 200, 'payload': 'ENCrypted data with XOR pattern'},
    {'header': 'DEADBEEF', 'length': 30, 'payload': 'Short message'},
    {'header': '12345678', 'length': 120, 'payload': 'Another ENCrypted XOR payload'}
]

threat_level = analyze_packets(network_traffic)
print(f"Result: {threat_level}")