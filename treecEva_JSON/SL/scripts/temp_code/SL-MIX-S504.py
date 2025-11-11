class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_network_topology():
    # Build a binary tree with 7 nodes
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(15)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(9)
    root.right.left = TreeNode(11)
    root.right.right = TreeNode(13)
    return root

def process_packets_through_network(root, packets):
    routing_accumulator = 0
    
    for packet_id in packets:
        current_node = root
        path_xor = packet_id
        
        # Traverse the tree, applying XOR at each node
        while current_node:
            path_xor ^= current_node.val
            # Greedy choice: go left if path_xor is even, else go right
            if path_xor & 1 == 0:
                current_node = current_node.left
            else:
                current_node = current_node.right
        
        routing_accumulator ^= path_xor
    
    return routing_accumulator

def calculate_final_key(base_key, modifier_sequence):
    result = base_key
    for mod in modifier_sequence:
        if mod & 0x80:  # Check sign bit in 8-bit representation
            result = (result << 1) & 0xFF  # Left shift with masking
        else:
            result = (result >> 1)  # Right shift
        result ^= mod  # Apply modifier
    return result

# Main execution
network_root = build_network_topology()
incoming_packets = [42, 18, 73, 29]
routing_result = process_packets_through_network(network_root, incoming_packets)
shift_modifiers = [0xC3, 0x4A, 0xF1, 0x88]
final_routing_key = calculate_final_key(routing_result, shift_modifiers)

print(f"Result: {final_routing_key}")