from collections import defaultdict
import math

class SensorNode:
    def __init__(self, delay):
        self.delay = delay
        self.connections = []
    
    def connect(self, other):
        self.connections.append(other)

def calculate_cumulative_delay(node, memo):
    if node in memo:
        return memo[node]
    
    if not node.connections:
        memo[node] = node.delay
        return node.delay
    
    max_subdelay = 0
    for connected_node in node.connections:
        subdelay = calculate_cumulative_delay(connected_node, memo)
        max_subdelay = max(max_subdelay, subdelay)
    
    total_delay = node.delay + max_subdelay
    memo[node] = total_delay
    return total_delay

def build_sensor_network():
    nodes = [SensorNode(i * 2) for i in range(1, 6)]
    
    # Create connections forming a directed acyclic graph
    nodes[0].connect(nodes[1])
    nodes[0].connect(nodes[2])
    nodes[1].connect(nodes[3])
    nodes[2].connect(nodes[3])
    nodes[3].connect(nodes[4])
    
    return nodes

def main():
    network = build_sensor_network()
    memoization_table = {}
    
    # Calculate delays for all nodes using dynamic programming
    delays = [calculate_cumulative_delay(node, memoization_table) for node in network]
    
    # Apply a transformation using array operations
    transformed_delays = [math.floor(d / 3) for d in delays]
    
    # Find the maximum transformed delay
    max_transformed = max(transformed_delays)
    
    # Calculate final delay using a combinatorial approach
    final_delay = sum(transformed_delays) * max_transformed
    
    return final_delay

final_delay = main()
print(f"Result: {final_delay}")