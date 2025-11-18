from collections import defaultdict

class PacketNode:
    def __init__(self, layer_id, metadata, children=None):
        self.layer_id = layer_id
        self.metadata = metadata
        self.children = children if children else []

def aggregate_metadata(node, depth=0):
    # Base case: leaf node
    if not node.children:
        return node.metadata * (depth + 1)
    
    # Recursive case: process children and aggregate
    child_values = [aggregate_metadata(child, depth + 1) for child in node.children]
    
    # Apply transformation based on layer type
    if node.layer_id % 3 == 0:
        # Sum and multiply by metadata
        result = sum(child_values) * node.metadata
    elif node.layer_id % 3 == 1:
        # XOR all child values with metadata
        result = node.metadata
        for val in child_values:
            result ^= val
    else:
        # Bitwise AND reduction
        result = node.metadata
        for val in child_values:
            result &= val
    
    return result

def build_packet_tree():
    # Layer 4: leaf nodes
    leaf_a = PacketNode(4, 5)
    leaf_b = PacketNode(5, 5)
    leaf_c = PacketNode(6, 3)
    leaf_d = PacketNode(7, 7)
    
    # Layer 3: intermediate nodes
    node_3a = PacketNode(3, 2, [leaf_a, leaf_b])
    node_3b = PacketNode(4, 4, [leaf_c, leaf_d])
    
    # Layer 2: intermediate nodes
    node_2a = PacketNode(2, 6, [node_3a])
    node_2b = PacketNode(3, 1, [node_3b])
    
    # Layer 1: root node
    root = PacketNode(1, 3, [node_2a, node_2b])
    
    return root

def compute_packet_signature():
    packet_tree = build_packet_tree()
    signature = aggregate_metadata(packet_tree)
    
    # Apply final transformation using dictionary comprehension
    transform_map = {i: (signature >> i) & 1 for i in range(8)}
    active_bits = sum(transform_map.values())
    
    # Final signature calculation
    final_signature = signature ^ (active_bits << 4)
    return final_signature

final_signature = compute_packet_signature()
print(f"Result: {final_signature}")