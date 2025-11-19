class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for v in values[1:]:
        current.next = ListNode(v)
        current = current.next
    return head

def process_packets(node_head):
    node_map = {i: [] for i in range(1, 6)}
    current = node_head
    index = 1
    while current:
        node_map[index].append(current.val)
        current = current.next
        index += 1
        if index > 5:
            index = 1
    
    base_config = {k: sum(v) for k, v in node_map.items()}
    adjustments = {k: (v << 1) & 0xFF if k % 2 == 0 else v ^ 0x55 for k, v in base_config.items()}
    merged = {**base_config, **adjustments}
    
    routing_sum = 0
    for k in sorted(merged.keys()):
        val = merged[k]
        if k < 4:
            for i in range(1, k+1):
                if i & k:
                    val ^= i
        else:
            val = val | ((val >> 2) & 0x0F)
        routing_sum += val
    
    return routing_sum

with open('temp_data.txt', 'w') as f:
    f.write('')

packet_sequence = [0x12, 0x34, 0x56, 0x78, 0x9A, 0xBC, 0xDE, 0xF0]
head_node = build_linked_list(packet_sequence)
final_routing_key = process_packets(head_node) + (len(packet_sequence) << 2)
print(f'Result: {final_routing_key}')