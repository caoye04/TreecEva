import math

def fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def derive_node_value(depth, position):
    fib_index = fibonacci(depth + position)
    log_factor = int(math.log2(fib_index + 1)) if fib_index > 0 else 1
    geo_adjustment = (position << depth) & 0xFF
    return (fib_index ^ log_factor ^ geo_adjustment) & 0xFFFF

class KeyTree:
    def __init__(self, max_depth):
        self.max_depth = max_depth
        self.nodes = {}
    
    def build_tree(self, depth, pos):
        if depth == self.max_depth:
            self.nodes[(depth, pos)] = derive_node_value(depth, pos)
        else:
            left_child = (depth + 1, pos * 2)
            right_child = (depth + 1, pos * 2 + 1)
            self.build_tree(depth + 1, pos * 2)
            self.build_tree(depth + 1, pos * 2 + 1)
            left_val = self.nodes[left_child]
            right_val = self.nodes[right_child]
            xor_result = left_val ^ right_val
            exp_factor = int(math.exp(depth / 2)) & 0xFF
            self.nodes[(depth, pos)] = (xor_result ^ exp_factor) & 0xFFFF
    
    def get_root(self):
        return self.nodes[(0, 0)]

tree_system = KeyTree(4)
tree_system.build_tree(0, 0)
root_key = tree_system.get_root()
print(f"Result: {root_key}")