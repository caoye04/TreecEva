class PacketNode:
    def __init__(self, packet_id, flags):
        self.packet_id = packet_id
        self.flags = flags
        self.next = None

class PacketQueue:
    def __init__(self):
        self.head = None
    
    def append(self, packet_id, flags):
        new_node = PacketNode(packet_id, flags)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    
    def to_list(self):
        packets = []
        current = self.head
        while current:
            packets.append((current.packet_id, current.flags))
            current = current.next
        return packets

# State machine definition
states = {
    'IDLE': {'SYN': 'HANDSHAKE', 'DATA': 'PROCESSING'},
    'HANDSHAKE': {'ACK': 'ESTABLISHED', 'RST': 'IDLE'},
    'PROCESSING': {'FIN': 'CLOSING', 'DATA': 'PROCESSING'},
    'ESTABLISHED': {'DATA': 'PROCESSING', 'FIN': 'CLOSING'},
    'CLOSING': {'ACK': 'IDLE'}
}

def process_packets(queue):
    current_state = 'IDLE'
    state_counter = {'IDLE': 0, 'HANDSHAKE': 0, 'PROCESSING': 0, 'ESTABLISHED': 0, 'CLOSING': 0}
    
    for packet_id, flags in queue.to_list():
        # Sort flags for consistent processing
        sorted_flags = sorted(flags)
        
        # State transition logic
        for flag in sorted_flags:
            if current_state in states and flag in states[current_state]:
                current_state = states[current_state][flag]
                break
        
        state_counter[current_state] += 1
    
    return state_counter

# Initialize packet queue
packet_queue = PacketQueue()
packet_data = [
    (1001, ['SYN']),
    (1002, ['ACK']),
    (1003, ['DATA']),
    (1004, ['DATA']),
    (1005, ['FIN']),
    (1006, ['ACK'])
]

for pid, flags in packet_data:
    packet_queue.append(pid, flags)

# Process packets through state machine
final_state_counts = process_packets(packet_queue)

# Calculate protocol state tally using dictionary comprehension
protocol_state_tally = sum({k: v*len(k) for k, v in final_state_counts.items() if v > 0}.values())

print(f"Result: {protocol_state_tally}")