from collections import deque

class DeliveryNode:
    def __init__(self, zone_id, left=None, right=None):
        self.zone_id = zone_id
        self.left = left
        self.right = right
        self.visited = False

def count_non_overlapping_zones(root):
    if not root:
        return 0
    
    # Stack for DFS traversal
    stack = [root]
    selected_zones = set()
    
    while stack:
        node = stack.pop()
        
        # Greedy selection: pick leaf nodes first if not visited
        if not node.left and not node.right and not node.visited:
            selected_zones.add(node.zone_id)
            # Mark all ancestors as visited to prevent overlap
            temp = root
            path_stack = []
            
            # Find path to current leaf
            def find_path(node, target, path):
                if not node:
                    return False
                path.append(node)
                if node == target:
                    return True
                if find_path(node.left, target, path) or find_path(node.right, target, path):
                    return True
                path.pop()
                return False
            
            path_to_leaf = []
            find_path(root, node, path_to_leaf)
            
            # Mark all nodes in path as visited
            for n in path_to_leaf:
                n.visited = True
        
        # Add children to stack
        if node.right and not node.right.visited:
            stack.append(node.right)
        if node.left and not node.left.visited:
            stack.append(node.left)
    
    return len(selected_zones)

# Create delivery tree
#       1
#      / \
#     2   3
#    /|   |\
#   4 5   6 7
#  /|
# 8 9

zone_1 = DeliveryNode(1)
zone_2 = DeliveryNode(2)
zone_3 = DeliveryNode(3)
zone_4 = DeliveryNode(4)
zone_5 = DeliveryNode(5)
zone_6 = DeliveryNode(6)
zone_7 = DeliveryNode(7)
zone_8 = DeliveryNode(8)
zone_9 = DeliveryNode(9)

zone_1.left = zone_2
zone_1.right = zone_3
zone_2.left = zone_4
zone_2.right = zone_5
zone_3.left = zone_6
zone_3.right = zone_7
zone_4.left = zone_8
zone_4.right = zone_9

max_zones = count_non_overlapping_zones(zone_1)
print(f"Result: {max_zones}")