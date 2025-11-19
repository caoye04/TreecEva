from collections import defaultdict

class GrowthNode:
    def __init__(self, phase_id, children=None):
        self.phase_id = phase_id
        self.children = children if children else []
    
def simulate_growth(root_node, seasons):
    accumulator = 0
    stack = [root_node]
    
    while stack:
        node = stack.pop()
        # Modular arithmetic to simulate seasonal influence
        seasonal_factor = (node.phase_id * 3 + seasons) % 7
        accumulator = (accumulator + seasonal_factor) % 13
        
        # Add children to stack for traversal
        stack.extend(node.children)
    
    return accumulator

def create_growth_tree():
    # Creating a 3-level growth tree
    leaf1 = GrowthNode(5)
    leaf2 = GrowthNode(2)
    leaf3 = GrowthNode(8)
    leaf4 = GrowthNode(1)
    
    branch1 = GrowthNode(3, [leaf1, leaf2])
    branch2 = GrowthNode(7, [leaf3, leaf4])
    
    root = GrowthNode(4, [branch1, branch2])
    return root

# Main execution
flora_tree = create_growth_tree()
seasonal_accumulator = simulate_growth(flora_tree, 9)
print(f"Result: {seasonal_accumulator}")