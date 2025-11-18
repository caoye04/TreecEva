class NutrientTracker:
    def __init__(self):
        self.max_nutrient = float('-inf')
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
    
    def update_max(self, value):
        if value > self.max_nutrient:
            self.max_nutrient = value

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def traverse_and_track(node, tracker):
    if not node:
        return
    tracker.update_max(node.val)
    traverse_and_track(node.left, tracker)
    traverse_and_track(node.right, tracker)

# Create the binary tree representing nutrient concentrations
root = TreeNode(12)
root.left = TreeNode(5)
root.right = TreeNode(18)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.left = TreeNode(15)
root.right.right = TreeNode(22)

# Traverse the tree with nutrient tracking
with NutrientTracker() as tracker:
    traverse_and_track(root, tracker)
    max_nutrient = tracker.max_nutrient

print(f"Result: {max_nutrient}")