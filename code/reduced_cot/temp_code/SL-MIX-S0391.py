class NetworkNode:
    def __init__(self, identifier, left=None, right=None):
        self.identifier = identifier
        self.left = left
        self.right = right
        self.checksum = 0

# Construct network topology as binary tree
root = NetworkNode(15)
root.left = NetworkNode(7)
root.right = NetworkNode(23)
root.left.left = NetworkNode(3)
root.left.right = NetworkNode(11)
root.right.left = NetworkNode(19)
root.right.right = NetworkNode(31)

# Greedy path selection using bitwise operations
active_routes = {15, 7, 23, 3, 11}  # Initially active routes
backup_routes = {19, 31}            # Backup routes

# Calculate initial checksums using XOR operations
node_map = {node.identifier: node for node in [root, root.left, root.right, root.left.left, root.left.right, root.right.left, root.right.right]}
for node_id in sorted(node_map.keys()):
    node = node_map[node_id]
    children_checksum = 0
    if node.left:
        children_checksum ^= node.left.identifier
    if node.right:
        children_checksum ^= node.right.identifier
    node.checksum = node.identifier ^ children_checksum

# Apply route filtering using set operations
filtered_nodes = {node_map[nid] for nid in active_routes if nid in node_map}
filtered_nodes |= {node_map[nid] for nid in backup_routes if nid in node_map and (nid & 0x1)}  # Only odd backup routes

# Aggregate checksums using greedy selection
checksum_aggregate = 0
for node in sorted(filtered_nodes, key=lambda x: x.identifier):
    if (checksum_aggregate & node.identifier) == 0:  # Greedy condition
        checksum_aggregate ^= node.checksum

print(f"Result: {checksum_aggregate}")