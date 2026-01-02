from collections import defaultdict
import itertools

def calculate_network_load(matrix, efficiency):
    base_load = 0
    adjustment_factor = 1.5
    temp_store = []
    
    # Process each node pair in the transmission matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i != j and matrix[i][j] > 0:
                load_contribution = matrix[i][j] * efficiency[(i, j)]
                temp_store.append(load_contribution)
    
    # Sum contributions and apply adjustment
    base_load = sum(temp_store)
    final_load = base_load * adjustment_factor
    
    # Dummy variables for slight distraction (LOW interference)
    max_single_load = max(temp_store) if temp_store else 0
    connection_count = len(temp_store)
    
    return int(final_load)

# Network transmission matrix (weighted graph representation)
transmission_matrix = [
    [0, 20, 15, 0],
    [10, 0, 25, 30],
    [0, 5, 0, 20],
    [15, 0, 10, 0]
]

# Efficiency map for each directed link using defaultdict for missing defaults
efficiency_map = defaultdict(float)
for i, j in itertools.product(range(4), repeat=2):
    if i != j:
        efficiency_map[(i, j)] = 0.8 + (0.05 * (i + j))  # Gradual efficiency increase based on indices

# Irrelevant tracking variable (minor distraction, intervention level 5)
current_phase = "diagnostic"

total_load = calculate_network_load(transmission_matrix, efficiency_map)
print(f"Result: {total_load}")