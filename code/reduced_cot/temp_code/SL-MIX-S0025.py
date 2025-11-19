from collections import deque

class WarehouseNode:
    def __init__(self, x, y, items=0):
        self.x = x
        self.y = y
        self.items = items
        self.left = None
        self.right = None

def build_warehouse_tree():
    # Level 0
    root = WarehouseNode(0, 0, 10)
    
    # Level 1
    root.left = WarehouseNode(1, 1, 15)
    root.right = WarehouseNode(2, 0, 8)
    
    # Level 2
    root.left.left = WarehouseNode(3, 1, 12)
    root.left.right = WarehouseNode(4, 2, 20)
    root.right.left = WarehouseNode(5, 1, 6)
    root.right.right = WarehouseNode(6, 0, 18)
    
    # Level 3
    root.left.left.left = WarehouseNode(7, 1, 9)
    root.left.left.right = WarehouseNode(8, 2, 14)
    root.left.right.left = WarehouseNode(9, 3, 11)
    root.left.right.right = WarehouseNode(10, 4, 25)
    root.right.left.left = WarehouseNode(11, 5, 7)
    root.right.left.right = WarehouseNode(12, 6, 13)
    root.right.right.left = WarehouseNode(13, 7, 5)
    root.right.right.right = WarehouseNode(14, 8, 16)
    
    return root

def process_warehouse():
    warehouse = build_warehouse_tree()
    stack = [warehouse]
    total_items = 0
    processed_nodes = 0
    max_depth = 3
    
    # Track depth using a queue with (node, depth) tuples
    queue = deque([(warehouse, 0)])
    
    while queue and processed_nodes < 15:  # 2^(max_depth+1) - 1 = 15 nodes
        current_node, depth = queue.popleft()
        
        if depth > max_depth:
            break
            
        # Process the node
        if current_node.x % 2 == 0 and current_node.y % 2 == 0:
            current_node.items *= 2
        elif current_node.x % 2 != 0 or current_node.y % 2 != 0:
            current_node.items //= 2
        
        total_items += current_node.items
        processed_nodes += 1
        
        # Add children to queue for processing
        if current_node.left and depth < max_depth:
            queue.append((current_node.left, depth + 1))
        if current_node.right and depth < max_depth:
            queue.append((current_node.right, depth + 1))
    
    return total_items

final_item_count = process_warehouse()
print(f"Result: {final_item_count}")