from functools import reduce
from collections import namedtuple

class PacketNode:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

def build_packet_chain(segments):
    head = None
    for segment in reversed(segments):
        head = PacketNode(segment, head)
    return head

def process_packets(machine_state, packet_head):
    current = packet_head
    xor_accumulator = 0b10101010
    
    while current:
        # State transition logic
        if machine_state == 'INIT':
            mask = 0xF0 if current.data > 100 else 0x0F
            transformed = current.data & mask
            machine_state = 'FILTERING'
        elif machine_state == 'FILTERING':
            shifted = current.data << 2
            transformed = shifted ^ 0b11110000
            machine_state = 'VERIFYING'
        else:  # VERIFYING
            transformed = current.data | 0b00110011
            machine_state = 'INIT'
        
        # Bitwise accumulation
        xor_accumulator ^= transformed
        current = current.next
    
    return xor_accumulator

# Protocol configuration
PacketSegment = namedtuple('PacketSegment', ['sequence_id', 'payload'])
segments = [
    PacketSegment(1, 187),
    PacketSegment(2, 42),
    PacketSegment(3, 203),
    PacketSegment(4, 96)
]

# Extract payload data for packet chain
payload_data = list(map(lambda seg: seg.payload, segments))
packet_chain = build_packet_chain(payload_data)

# Process through state machine
initial_state = 'INIT'
final_verification_code = process_packets(initial_state, packet_chain)

print(f"Result: {final_verification_code}")