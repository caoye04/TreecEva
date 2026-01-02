from itertools import combinations

def analyze_cycles(edges):
    # Irrelevant helper: computes cycle pairs (not used in final result)
    nodes = set()
    for a, b in edges:
        nodes.add(a)
        nodes.add(b)
    return list(combinations(nodes, 3))

def validate_symmetry(matrix):
    # Distractor function: checks if matrix is symmetric (used but doesn't affect answer)
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True

def calculate_net_flow(weights, flow_grid):
    total_inflow = 0
    total_outflow = 0
    n = len(flow_grid)
    
    # Real computation: sum diagonal as base flux
    base_flux = sum(flow_grid[i][i] for i in range(n))
    
    # Semi-relevant: track neighbor contributions (only some used)
    neighbor_contrib = {}
    for i in range(n):
        neighbor_contrib[i] = 0
        for j in range(n):
            if i != j and flow_grid[i][j] > 0:
                neighbor_contrib[i] += weights.get((i, j), 0)
    
    # Misleading accumulation (dead-end)
    temp_accum = 0
    for k in range(n):
        temp_accum += neighbor_contrib.get(k, 0) * 0.1  # Not used later
    
    # Core logic: inflow from odd indices, outflow from even
    for i in range(n):
        if i % 2 == 1:
            total_inflow += base_flux * (i + 1)
        else:
            total_outflow += base_flux * (i + 1)
    
    # Final net flow calculation
    net_difference = total_inflow - total_outflow
    adjustment = len([k for k in neighbor_contrib if k % 2 == 0])  # Only count even keys
    final_result = net_difference // (adjustment + 1) if adjustment != -1 else net_difference
    
    return int(final_result)

# Main execution block
edge_list = [(0,1), (1,2), (2,3), (3,0), (1,3)]
cycle_data = analyze_cycles(edge_list)  # Dead assignment

edge_weights = {
    (0,1): 3, (1,2): 5, (2,3): 2, (3,0): 4, (1,3): 7
}

flow_matrix = [
    [2, 0, 1, 0],
    [0, 3, 0, 1],
    [1, 0, 2, 0],
    [0, 1, 0, 3]
]

# Validate symmetry (distractor call)
symmetric = validate_symmetry(flow_matrix)

# Key computation step
final_flux = calculate_net_flow(edge_weights, flow_matrix)

print(f"Result: {final_flux}")