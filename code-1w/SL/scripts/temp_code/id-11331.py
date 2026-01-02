from collections import defaultdict
import math

def calculate_node_weight(edges):
    weight_map = defaultdict(int)
    for src, dst in edges:
        weight_map[src] += 1
        weight_map[dst] += 1
    return weight_map

def calculate_network_load(matrix, factor):
    flat = [val for row in matrix for val in row]
    weighted_sum = sum(x * math.log(x) if x > 0 else 0 for x in flat)
    adjustment = math.sin(math.pi / 4) ** 2
    return int((weighted_sum * factor * adjustment))

def main():
    # Network topology data
    connections = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A'), ('B', 'D')]
    transmission_matrix = [
        [0, 5, 0, 3],
        [5, 0, 2, 6],
        [0, 2, 0, 4],
        [3, 6, 4, 0]
    ]
    efficiency_factor = 1.75
    
    # Irrelevant calculation (minor distraction)
    node_degrees = calculate_node_weight(connections)
    avg_degree = sum(node_degrees.values()) / len(node_degrees)
    
    # Key computation
    total_load = calculate_network_load(transmission_matrix, efficiency_factor)
    
    # Output result
    print(f"Result: {total_load}")

if __name__ == "__main__":
    main()