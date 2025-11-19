import math
from collections import deque

class SensorNode:
    def __init__(self, temp, salt, left=None, right=None):
        self.temperature = temp
        self.salinity = salt
        self.left = left
        self.right = right

def compute_tree_stats(root):
    if not root:
        return []
    stats = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        stats.append((node.temperature, node.salinity))
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return stats

def calculate_variance(values):
    if len(values) <= 1:
        return 0
    mean_val = sum(values) / len(values)
    squared_diffs = [(x - mean_val) ** 2 for x in values]
    return sum(squared_diffs) / len(values)

def process_sensor_data(sensor_tree_root):
    readings = compute_tree_stats(sensor_tree_root)
    temperatures = [temp for temp, _ in readings]
    salinities = [salt for _, salt in readings]
    
    temp_variance = calculate_variance(temperatures)
    salt_variance = calculate_variance(salinities)
    
    # State machine for data fusion
    state = 'INIT'
    dispersion_metric = 0
    
    for i in range(len(temperatures)):
        if state == 'INIT':
            if temperatures[i] > 20:
                state = 'WARM_ZONE'
            else:
                state = 'COLD_ZONE'
        elif state == 'WARM_ZONE':
            if salinities[i] > 35:
                dispersion_metric += temp_variance * 0.7 + salt_variance * 0.3
                state = 'HIGH_SALINITY'
            else:
                dispersion_metric += temp_variance * 0.5 + salt_variance * 0.5
        elif state == 'COLD_ZONE':
            if salinities[i] < 30:
                dispersion_metric += temp_variance * 0.3 + salt_variance * 0.7
                state = 'LOW_SALINITY'
            else:
                dispersion_metric += temp_variance * 0.4 + salt_variance * 0.6
        elif state == 'HIGH_SALINITY':
            dispersion_metric += max(temp_variance, salt_variance)
            state = 'CRITICAL'
        elif state == 'LOW_SALINITY':
            dispersion_metric += min(temp_variance, salt_variance)
            state = 'STABLE'
        elif state == 'CRITICAL' or state == 'STABLE':
            dispersion_metric += (temp_variance + salt_variance) / 2
    
    return dispersion_metric

# Build sensor tree
sensor_tree = SensorNode(22.5, 35.2)
sensor_tree.left = SensorNode(18.3, 34.1)
sensor_tree.right = SensorNode(25.7, 36.8)
sensor_tree.left.left = SensorNode(17.9, 29.5)
sensor_tree.left.right = SensorNode(19.2, 33.7)
sensor_tree.right.left = SensorNode(24.1, 37.2)
sensor_tree.right.right = SensorNode(26.8, 38.1)

oceanic_variance = process_sensor_data(sensor_tree)
print(f"Result: {oceanic_variance}")