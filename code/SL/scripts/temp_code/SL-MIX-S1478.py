class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Initialize packet stream as linked list: [0x1F3A, 0x7B4C, 0x2E8F, 0x5D1B]
head = ListNode(0x1F3A)
head.next = ListNode(0x7B4C)
head.next.next = ListNode(0x2E8F)
head.next.next.next = ListNode(0x5D1B)

packet_metadata = {}
signal_strength = 0
node_ptr = head

while node_ptr:
    # Extract metadata (bits 8-15) using bit masking and shifting
    meta_bits = (node_ptr.val & 0xFF00) >> 8
    
    # Compute checksum using XOR of lower 8 bits with magic number 0xA5
    payload = node_ptr.val & 0xFF
    checksum = payload ^ 0xA5
    
    # Validate packet: metadata should equal checksum when masked with 0x7F
    if (meta_bits & 0x7F) == (checksum & 0x7F):
        # Update signal strength with bitwise OR of all valid metadata
        signal_strength |= meta_bits
        packet_metadata[node_ptr.val] = meta_bits
    else:
        # Invalid packet contributes negatively using AND with complement
        signal_strength &= ~meta_bits
    
    node_ptr = node_ptr.next

# Merge with default configuration using dictionary comprehension
config_defaults = {0x1F3A: 0x1F, 0x7B4C: 0x7B, 0x2E8F: 0x2E, 0x5D1B: 0x5D}
final_config = {pkt: packet_metadata.get(pkt, default) for pkt, default in config_defaults.items()}

# Adjust signal strength based on configuration
for val, meta in final_config.items():
    if val & 0x1000:  # If bit 12 is set
        signal_strength ^= meta  # Apply correction using XOR

print(f"Result: {signal_strength}")