import re
from collections import defaultdict

def process_packet_headers():
    packet_data = [
        "TCP:src=192.168.1.100:dst=10.0.0.5:port=443:flags=SYN",
        "UDP:src=172.16.0.20:dst=8.8.8.8:port=53:len=72",
        "TCP:src=10.0.0.5:dst=192.168.1.100:port=80:flags=ACK"
    ]
    
    protocol_counts = defaultdict(int)
    port_values = []
    flag_masks = {'SYN': 0b0001, 'ACK': 0b0010, 'FIN': 0b0100, 'RST': 0b1000}
    
    for header in packet_data:
        # Pattern matching to extract fields
        proto_match = re.match(r'(\w+):(.*)', header)
        if proto_match:
            protocol = proto_match.group(1)
            protocol_counts[protocol] += 1
            
            fields = proto_match.group(2)
            # Extract port number
            port_match = re.search(r'port=(\d+)', fields)
            if port_match:
                port = int(port_match.group(1))
                port_values.append(port)
            
            # Process flags for TCP packets
            if protocol == 'TCP':
                flags_match = re.search(r'flags=([A-Z]+)', fields)
                if flags_match:
                    flag = flags_match.group(1)
                    if flag in flag_masks:
                        # Bitwise operations on flag masks
                        port_values[-1] ^= flag_masks[flag] << 4
    
    # Compute checksum using bitwise operations
    checksum = 0
    for i, port in enumerate(port_values):
        # Rotate left by index positions and XOR with protocol count
        rotated_port = ((port << (i % 8)) | (port >> (8 - (i % 8)))) & 0xFFFF
        checksum ^= rotated_port + protocol_counts['TCP']
    
    # Final checksum computation
    final_checksum = (checksum & 0xFF) ^ ((checksum >> 8) & 0xFF)
    return final_checksum

final_checksum = process_packet_headers()
print(f"Result: {final_checksum}")