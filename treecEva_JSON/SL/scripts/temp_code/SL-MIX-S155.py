import re

class PacketNode:
    def __init__(self, seq_num, payload, next_node=None):
        self.seq_num = seq_num
        self.payload = payload
        self.next = next_node

def create_packet_chain():
    # Create a linked list of packets with sequence numbers and payloads
    packets = [
        (1001, "AUTH:admin|CMD:read"),
        (1002, "AUTH:user|CMD:write"),
        (1003, "AUTH:guest|CMD:read"),
        (1004, "AUTH:admin|CMD:delete"),
        (1005, "AUTH:user|CMD:execute")
    ]
    
    head = None
    for seq, payload in reversed(packets):
        head = PacketNode(seq, payload, head)
    return head

def validate_packets(head):
    clearance = 0
    current = head
    
    while current:
        # Extract command using regex
        cmd_match = re.search(r'CMD:(\w+)', current.payload)
        auth_match = re.search(r'AUTH:(\w+)', current.payload)
        
        if cmd_match and auth_match:
            command = cmd_match.group(1)
            auth_level = auth_match.group(1)
            
            # Assign weights based on authorization level
            auth_weight = {'admin': 3, 'user': 2, 'guest': 1}[auth_level]
            
            # Assign command weights
            cmd_weight = {'read': 1, 'write': 2, 'execute': 3, 'delete': 4}[command]
            
            # Calculate packet validity score
            validity = (current.seq_num % 7) * auth_weight + cmd_weight
            
            # Apply bitwise operations for security checksum
            if validity & 1:  # If odd
                clearance ^= validity
            else:
                clearance |= (validity >> 1)
        
        current = current.next
    
    # Final adjustment based on packet count
    packet_count = 0
    temp = head
    while temp:
        packet_count += 1
        temp = temp.next
    
    # Apply final transformation
    security_clearance_level = (clearance * packet_count) % 128
    return security_clearance_level

# Main execution
packet_chain = create_packet_chain()
security_clearance_level = validate_packets(packet_chain)
print(f"Result: {security_clearance_level}")