from collections import defaultdict
import itertools

def process_packets():
    # Packet header tokens (simulated)
    packet_headers = [
        "TCP SRC:192.168.1.1 DST:10.0.0.1 PORT:80",
        "UDP SRC:192.168.1.2 DST:10.0.0.2 PORT:53",
        "TCP SRC:10.0.0.1 DST:192.168.1.1 PORT:80",
        "ICMP SRC:192.168.1.3 DST:10.0.0.3 TYPE:8"
    ]
    
    # State machine for connection tracking
    state_machine = {
        'INIT': {'TCP': 'TCP_CONN', 'UDP': 'UDP_CONN', 'ICMP': 'ICMP_CONN'},
        'TCP_CONN': {'ACK': 'ESTABLISHED', 'RST': 'CLOSED'},
        'UDP_CONN': {'DATA': 'ACTIVE', 'TIMEOUT': 'CLOSED'},
        'ICMP_CONN': {'REPLY': 'COMPLETED', 'TIMEOUT': 'CLOSED'}
    }
    
    connection_states = defaultdict(str)
    anomaly_counter = 0
    security_weights = {'TCP': 3, 'UDP': 2, 'ICMP': 1}
    
    for header in packet_headers:
        tokens = header.split()
        protocol = tokens[0]
        src_ip = tokens[1].split(':')[1]
        dst_ip = tokens[2].split(':')[1]
        
        # Encoding source IP to numerical value
        src_encoded = sum(ord(c) for c in src_ip)
        
        # State machine transition
        current_state = connection_states[(src_ip, dst_ip)]
        if not current_state:
            connection_states[(src_ip, dst_ip)] = state_machine['INIT'].get(protocol, 'UNKNOWN')
        else:
            # Simulate state transition based on protocol
            if protocol == 'TCP' and 'ACK' in header:
                connection_states[(src_ip, dst_ip)] = state_machine.get(current_state, {}).get('ACK', current_state)
            elif protocol == 'ICMP' and 'REPLY' in header:
                connection_states[(src_ip, dst_ip)] = state_machine.get(current_state, {}).get('REPLY', current_state)
        
        # Detect anomalies (simplified)
        if src_encoded > 1000:
            anomaly_counter += 1
    
    # Calculate final security score
    state_scores = {'INIT': 0, 'TCP_CONN': 5, 'UDP_CONN': 3, 'ICMP_CONN': 2, 'ESTABLISHED': 10, 'ACTIVE': 7, 'COMPLETED': 8, 'CLOSED': 1, 'UNKNOWN': 0}
    total_state_score = sum(state_scores[state] for state in connection_states.values())
    final_security_score = (total_state_score * anomaly_counter) - sum(security_weights.values())
    
    return final_security_score

final_security_score = process_packets()
print(f"Result: {final_security_score}")