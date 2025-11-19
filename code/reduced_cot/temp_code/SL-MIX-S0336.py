from collections import defaultdict

class FractalPlant:
    def __init__(self):
        self.tree = {}
        self.flowering_leaves = 0
    
    def hash_path(self, path):
        return hash(''.join(map(str, path))) % 1000
    
    def build_tree(self, node_id, depth, max_depth, path):
        if depth == max_depth:
            # Terminal node (leaf)
            node_hash = self.hash_path(path)
            self.tree[node_id] = {'hash': node_hash, 'children': {}, 'is_leaf': True}
            if node_hash % 2 == 0:  # Even hash indicates flowering
                self.flowering_leaves += 1
            return
        
        # Internal node
        node_hash = self.hash_path(path)
        self.tree[node_id] = {'hash': node_hash, 'children': {}, 'is_leaf': False}
        
        # Binary branching
        left_child = f"{node_id}L"
        right_child = f"{node_id}R"
        
        self.tree[node_id]['children']['left'] = left_child
        self.tree[node_id]['children']['right'] = right_child
        
        # Recursive construction
        self.build_tree(left_child, depth+1, max_depth, path + [0])
        self.build_tree(right_child, depth+1, max_depth, path + [1])

def simulate_growth():
    plant = FractalPlant()
    plant.build_tree('ROOT', 0, 3, [])
    return plant.flowering_leaves

# Execute simulation
final_count = simulate_growth()
print(f"Result: {final_count}")