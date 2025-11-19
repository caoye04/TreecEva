from collections import namedtuple

def analyze_packets(packet_sequence):
    # Define packet structure
    Packet = namedtuple('Packet', ['syn', 'ack', 'fin', 'rst'])
    
    # State definitions
    STATE_NORMAL = 0
    STATE_MONITORING = 1
    STATE_ALERT = 2
    
    # Initialize state machine
    current_state = STATE_NORMAL
    intrusion_score = 0
    
    # Process each packet
    for i, flags in enumerate(packet_sequence):
        packet = Packet(*flags)
        
        # State transition logic with scoring
        if current_state == STATE_NORMAL:
            if packet.syn and not packet.ack:
                current_state = STATE_MONITORING
                intrusion_score += 10
            elif packet.syn and packet.ack:
                intrusion_score += 1
        elif current_state == STATE_MONITORING:
            if packet.fin and packet.rst:
                current_state = STATE_ALERT
                intrusion_score *= 3
            elif not packet.syn and packet.ack:
                intrusion_score += 5
            else:
                intrusion_score -= 2
        elif current_state == STATE_ALERT:
            if packet.rst:
                intrusion_score += 15
            elif not packet.fin:
                intrusion_score -= 5
        
        # Apply additional scoring based on position and flags
        if i % 3 == 0 and packet.syn:
            intrusion_score += 7
    
    return intrusion_score

# Test sequence representing network packets [SYN, ACK, FIN, RST]
packets = [
    (1, 0, 0, 0),  # SYN only
    (1, 1, 0, 0),  # SYN+ACK
    (0, 1, 0, 0),  # ACK only
    (0, 0, 1, 1),  # FIN+RST
    (0, 0, 0, 1),  # RST only
    (1, 0, 0, 0),  # SYN only
    (0, 0, 1, 0),  # FIN only
]

intrusion_score = analyze_packets(packets)
print(f"Result: {intrusion_score}")