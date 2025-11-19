from collections import defaultdict

def process_packet_sequence():
    # State machine representation
    states = {
        'IDLE': 0,
        'RECEIVING': 1,
        'PROCESSING': 2,
        'TRANSMITTING': 3,
        'ERROR': -1
    }
    
    # Packet flag definitions
    flags = {
        'SYN': 1,
        'ACK': 2,
        'FIN': 4,
        'RST': 8
    }
    
    # Initialize state tracking
    current_state = 'IDLE'
    state_history = []
    transition_scores = defaultdict(int)
    
    # Process packet sequence
    packet_headers = [3, 6, 12, 9, 5, 10, 15, 7, 14, 13, 11, 8]
    
    for i, header_flags in enumerate(packet_headers):
        # State transition logic
        if current_state == 'IDLE':
            if header_flags & flags['SYN']:
                current_state = 'RECEIVING'
                transition_scores[current_state] += 3
            else:
                current_state = 'ERROR'
                transition_scores[current_state] -= 2
        elif current_state == 'RECEIVING':
            if header_flags & flags['ACK'] and header_flags & flags['SYN']:
                current_state = 'PROCESSING'
                transition_scores[current_state] += 5
            elif header_flags & flags['RST']:
                current_state = 'ERROR'
                transition_scores[current_state] -= 1
            else:
                current_state = 'IDLE'
                transition_scores[current_state] += 1
        elif current_state == 'PROCESSING':
            if header_flags & flags['FIN']:
                current_state = 'TRANSMITTING'
                transition_scores[current_state] += 4
            elif header_flags & flags['RST']:
                current_state = 'ERROR'
                transition_scores[current_state] -= 3
            else:
                current_state = 'RECEIVING'
                transition_scores[current_state] += 2
        elif current_state == 'TRANSMITTING':
            if header_flags & flags['ACK']:
                current_state = 'IDLE'
                transition_scores[current_state] += 3
            else:
                current_state = 'ERROR'
                transition_scores[current_state] -= 2
        else:  # ERROR state
            if header_flags & flags['SYN'] and header_flags & flags['ACK']:
                current_state = 'RECEIVING'
                transition_scores[current_state] += 2
            else:
                current_state = 'IDLE'
                transition_scores[current_state] += 1
        
        state_history.append(current_state)
    
    # Calculate final checksum
    final_state_checksum = sum(transition_scores.values()) * len([s for s in state_history if s != 'ERROR'])
    
    return final_state_checksum

final_state_checksum = process_packet_sequence()
print(f"Result: {final_state_checksum}")