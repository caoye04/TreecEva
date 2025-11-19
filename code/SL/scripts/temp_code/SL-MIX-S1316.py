from functools import reduce
import math

class TreeNode:
    def __init__(self, name, access_flags, children=None):
        self.name = name
        self.access_flags = access_flags
        self.children = children if children else []

def traverse_and_compute(node, accumulated_mask):
    # Apply bitwise operations based on node properties
    if len(node.name) % 2 == 0:
        current_mask = node.access_flags << 1
    else:
        current_mask = node.access_flags >> 1
    
    # Short-circuit evaluation for special nodes
    if node.name.startswith('sys') and (node.access_flags & 0x4):
        current_mask |= 0xF0
    
    # Combine with accumulated mask using XOR
    combined_mask = accumulated_mask ^ current_mask
    
    # Recursive traversal with functional approach
    child_masks = list(map(lambda child: traverse_and_compute(child, combined_mask), node.children))
    
    # Reduce child masks using OR operation
    if child_masks:
        final_mask = reduce(lambda x, y: x | y, child_masks, combined_mask)
    else:
        final_mask = combined_mask
    
    return final_mask

def main():
    # Build tree structure representing file system
    root = TreeNode('root', 0x1)
    bin_node = TreeNode('bin', 0x2)
    sys_config = TreeNode('sysconfig', 0x4)
    lib_node = TreeNode('lib', 0x8)
    usr_node = TreeNode('usr', 0x10)
    local_bin = TreeNode('localbin', 0x20)
    
    # Construct hierarchy
    root.children = [bin_node, sys_config, lib_node]
    bin_node.children = [local_bin]
    lib_node.children = [usr_node]
    
    # Traverse and compute final access mask
    initial_mask = 0x0
    final_access_mask = traverse_and_compute(root, initial_mask)
    
    print(f"Result: {final_access_mask}")

if __name__ == "__main__":
    main()