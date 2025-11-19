from collections import defaultdict

class PlantNode:
    def __init__(self, biomass, left=None, right=None):
        self.biomass = biomass
        self.left = left
        self.right = right

# Predefined plant growth tree structure
plant_growth_tree = PlantNode(10,
    PlantNode(5, 
        PlantNode(2),
        PlantNode(3, 
            PlantNode(1),
            PlantNode(1)
        )
    ),
    PlantNode(7,
        PlantNode(4),
        PlantNode(6, 
            None,
            PlantNode(2)
        )
    )
)

def calculate_efficiency(node):
    if not node:
        return 0
    
    # Base case: leaf nodes have special efficiency calculation
    if not node.left and not node.right:
        return node.biomass * 2
    
    # Divide and conquer: calculate efficiency of subtrees
    left_efficiency = calculate_efficiency(node.left)
    right_efficiency = calculate_efficiency(node.right)
    
    # Combine results with logical conditions
    subtree_sum = left_efficiency + right_efficiency
    is_balanced = abs((node.left.biomass if node.left else 0) - (node.right.biomass if node.right else 0)) <= 2
    
    # Apply efficiency formula with logical operations
    if is_balanced and subtree_sum > 10:
        return (subtree_sum // 2) + node.biomass
    elif not is_balanced or subtree_sum <= 5:
        return subtree_sum + (node.biomass // 2)
    else:
        return subtree_sum

cumulative_efficiency = calculate_efficiency(plant_growth_tree)
print(f"Result: {cumulative_efficiency}")