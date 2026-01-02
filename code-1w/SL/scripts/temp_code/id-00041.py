class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree_from_list(vals):
    if not vals:
        return None
    root = TreeNode(vals[0])
    queue = [root]
    i = 1
    while queue and i < len(vals):
        node = queue.pop(0)
        if i < len(vals) and vals[i] is not None:
            node.left = TreeNode(vals[i])
            queue.append(node.left)
        i += 1
        if i < len(vals) and vals[i] is not None:
            node.right = TreeNode(vals[i])
            queue.append(node.right)
        i += 1
    return root

def validate_tree(node, hash_val):
    if not node:
        return True
    if node.val > hash_val:
        return False
    return validate_tree(node.left, hash_val) and validate_tree(node.right, hash_val)

def hash_permission(perm):
    return sum(ord(c) for c in perm) % 100

def compute_clearance(validated_nodes):
    from functools import reduce
    hashes = list(map(hash_permission, validated_nodes))
    max_hash = max(hashes) if hashes else 0
    min_hash = min(hashes) if hashes else 0
    return reduce(lambda x, y: x ^ y, hashes, 0) if max_hash > min_hash else 0

permissions = ['read', 'write', 'execute', 'delete']
validation_tree_vals = [50, 30, 70, 20, 40, 60, 80]
tree_root = build_tree_from_list(validation_tree_vals)
validated_perms = []
for perm in permissions:
    h = hash_permission(perm)
    if validate_tree(tree_root, h):
        validated_perms.append(perm)
encoded_validated = list(map(lambda s: ''.join(chr(ord(c)+1) for c in s), validated_perms))
clearance_level = compute_clearance(encoded_validated) if validated_perms else 0
is_critical = len(validated_perms) >= 3
final_clearance = clearance_level | (1 << 4) if is_critical else clearance_level & ~(1 << 4)
print(f"Result: {final_clearance}")