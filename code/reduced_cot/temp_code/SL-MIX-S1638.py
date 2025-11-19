import heapq
from functools import reduce

class PlantNode:
    def __init__(self, species_id, growth_rate, children=None):
        self.species_id = species_id
        self.growth_rate = growth_rate
        self.children = children if children else []
    
    def calculate_anomaly(self):
        child_anomalies = [child.calculate_anomaly() for child in self.children]
        max_child = max(child_anomalies) if child_anomalies else 0
        return self.growth_rate + (max_child if max_child > 0 else 0)

def build_conservatory_tree():
    # Creating a 3-level tree representing plant species hierarchy
    leaf1 = PlantNode('P-7A', 12, [])
    leaf2 = PlantNode('P-8B', 9, [])
    leaf3 = PlantNode('P-9C', 15, [])
    leaf4 = PlantNode('P-10D', 7, [])
    
    mid1 = PlantNode('P-4X', 5, [leaf1, leaf2])
    mid2 = PlantNode('P-5Y', 8, [leaf3, leaf4])
    
    root = PlantNode('P-1Z', 10, [mid1, mid2])
    return root

def process_growth_data(root_node):
    anomaly_heap = []
    stack = [root_node]
    
    while stack:
        node = stack.pop()
        anomaly = node.calculate_anomaly()
        heapq.heappush(anomaly_heap, anomaly)
        stack.extend(node.children)
    
    # Apply environmental stress factor using ternary operator and short-circuit evaluation
    stress_factor = 1.5 if len(anomaly_heap) > 5 else 1.2
    has_critical = any(anomaly > 20 for anomaly in anomaly_heap) or False
    
    # Calculate priority score using functional programming
    base_score = reduce(lambda x, y: x + y, anomaly_heap, 0)
    priority_score = base_score * stress_factor if has_critical else base_score / 2
    
    return priority_score

# Main execution
conservatory = build_conservatory_tree()
priority_score = process_growth_data(conservatory)
print(f"Result: {int(priority_score)}")