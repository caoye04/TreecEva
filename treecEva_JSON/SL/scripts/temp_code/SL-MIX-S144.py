import re
from collections import deque
from dataclasses import dataclass

@dataclass
class Packet:
    header: str
    payload: str
    
def validate_packet(pkt: Packet) -> int:
    # Stage 1: Extract sequence number using regex
    seq_match = re.search(r'SEQ:(\d+)', pkt.header)
    if not seq_match:
        return -1
    seq_num = int(seq_match.group(1))
    
    # Stage 2: Compute hash-like value from payload
    hash_val = sum(ord(c) for c in pkt.payload) % 1000
    
    # Stage 3: Bitwise transformations
    masked_hash = hash_val & 0xFF
    shifted_seq = seq_num << 2
    
    # Stage 4: Process through a stack-based verification
    stack = deque()
    for i in range(4):
        stack.append((shifted_seq + i) ^ masked_hash)
    
    # Stage 5: Aggregate results with alternating signs
    aggregate = 0
    sign = 1
    while stack:
        aggregate += sign * stack.pop()
        sign *= -1
    
    # Stage 6: Final scoring with modulo adjustment
    final_score = (aggregate * 3 + seq_num) % 97
    
    return final_score

# Test packet
packet_data = Packet(
    header="ID:NETSEC|SEQ:42|PROTO:ENCRYPT",
    payload="ENCRYPTED_PAYLOAD_DATA"
)

final_score = validate_packet(packet_data)
print(f"Result: {final_score}")