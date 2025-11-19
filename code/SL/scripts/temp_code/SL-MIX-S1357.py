import math
from collections import defaultdict

class SensorNode:
    def __init__(self, sensor_id, readings):
        self.sensor_id = sensor_id
        self.readings = readings
        self.children = []
    
    def add_child(self, child):
        self.children.append(child)

def calculate_cluster_variance(readings):
    if len(readings) <= 1:
        return 0.0
    mean = sum(readings) / len(readings)
    variance = sum((x - mean) ** 2 for x in readings) / len(readings)
    return variance

def process_sensor_tree(root):
    if not root:
        return 0.0
    
    # Calculate local variance
    local_variance = calculate_cluster_variance(root.readings)
    
    # Process children
    child_contributions = []
    for child in root.children:
        child_var = process_sensor_tree(child)
        if child_var > 0.5:  # Early return condition
            child_contributions.append(math.log(child_var + 1))
        else:
            child_contributions.append(child_var)
    
    # Aggregate contributions
    total_contribution = sum(child_contributions)
    stability_metric = local_variance * math.exp(-total_contribution/len(root.readings) if root.readings else 0)
    
    return stability_metric

# Build sensor tree
root_cluster = SensorNode('A', [23.5, 24.1, 22.8, 25.0])
child_b = SensorNode('B', [21.2, 22.0, 20.5])
child_c = SensorNode('C', [26.8, 27.3, 25.9])
grandchild_d = SensorNode('D', [19.5, 20.1, 18.9, 21.0])

root_cluster.add_child(child_b)
root_cluster.add_child(child_c)
child_b.add_child(grandchild_d)

# Process tree and calculate stability index
raw_stability = process_sensor_tree(root_cluster)
stability_index = round(raw_stability * 1000)  # Scale for reporting

print(f"Result: {stability_index}")