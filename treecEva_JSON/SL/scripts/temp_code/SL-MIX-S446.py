import heapq

class RootNode:
    def __init__(self, factor, left=None, right=None):
        self.factor = factor
        self.left = left
        self.right = right

# Build a sample binary root structure
root = RootNode(5)
root.left = RootNode(3)
root.right = RootNode(8)
root.left.left = RootNode(2)
root.left.right = RootNode(4)
root.right.left = RootNode(7)
root.right.right = RootNode(10)

# Vitality calculation lambda with closure
vitality_fn = lambda node, acc: acc + (node.factor * 2 if node.factor > 4 else node.factor // 2)

# Heap for tracking top growth factors
factor_heap = []

# Recursive traversal with vitality accumulation and heap updates
def process_root(node, accumulated=0):
    if not node:
        return accumulated
    
    # Update accumulated vitality using ternary logic
    accumulated = vitality_fn(node, accumulated)
    
    # Push factor to heap (negated for max-heap behavior)
    heapq.heappush(factor_heap, -node.factor)
    
    # Traverse children with updated accumulation
    left_acc = process_root(node.left, accumulated)
    right_acc = process_root(node.right, accumulated)
    
    # Return maximum path vitality
    return left_acc if left_acc > right_acc else right_acc

# Process the root system
max_path_vitality = process_root(root)

# Extract top 3 growth factors from heap
pruned_factors_sum = sum(-heapq.heappop(factor_heap) for _ in range(min(3, len(factor_heap))))

# Calculate final vitality score using ternary operator
final_vitality_score = pruned_factors_sum + max_path_vitality if pruned_factors_sum > 20 else pruned_factors_sum - max_path_vitality

print(f"Result: {final_vitality_score}")