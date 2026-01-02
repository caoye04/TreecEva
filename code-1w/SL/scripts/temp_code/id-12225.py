import itertools

# Simulate biochemical equilibrium in a metabolic pathway
def main():
    # Core data structures
    metabolite_ids = ['M1', 'M2', 'M3', 'M4']
    base_levels = [12.5, 8.3, 15.7, 6.2]
    reaction_constants = [0.88, 1.05, 0.73, 1.12]
    
    # Construct concentration matrix using tuple unpacking and slicing
    concentration_matrix = []
    for i, id_ in enumerate(metabolite_ids):
        cycle_phases = [base_levels[i] * (1 + 0.1 * j) for j in range(4)]
        concentration_matrix.append(cycle_phases)
    
    # Irrelevant secondary matrix (distractor)
    placeholder_data = [[0 for _ in range(4)] for _ in range(4)]
    for x, y in itertools.product(range(4), range(4)):
        placeholder_data[x][y] = (x + y) ** 2 % 7  # Dead computation
    
    # Flow rates with conditional expression initialization
    flow_direction = 'bidirectional'
    flow_rates = [1.2 if flow_direction == 'unidirectional' else 0.9 for _ in metabolite_ids]
    scaling_factor = 1.0
    
    # Secondary derived values (some irrelevant)
    adjusted_levels = [base_levels[i] * reaction_constants[i] for i in range(4)]
    temp_aggregate = sum(adjusted_levels) / len(adjusted_levels)
    noise_offset = 0.0  # Unused in final logic
    
    # Helper function with nested logic
    def calculate_equilibrium(matrix, flows):
        total_influence = 0.0
        stability_weights = []
        
        # Compute weights using diagonal slicing (relevant)
        for i in range(len(matrix)):
            diagonal_slice = [matrix[j][(j+i) % 4] for j in range(4)]
            avg_diag = sum(diagonal_slice) / 4
            weight = avg_diag * flows[i]
            stability_weights.append(weight)
        
        # Red herring: permutation analysis (not used in output)
        permutations = list(itertools.permutations([0,1,2]))
        perm_entropy = 0.0
        for p in permutations:
            perm_entropy += abs(p[0] - p[-1]) * 0.1
        
        # Actual equilibrium calculation
        for i in range(4):
            contribution = stability_weights[i] * (1 + 0.25 * (-1)**i)
            total_influence += contribution
        
        # Final nonlinear transformation
        normalized = abs(total_influence) * 0.75
        return round(normalized, 4)
    
    # Key execution point
    equilibrium_score = calculate_equilibrium(concentration_matrix, flow_rates)
    
    # Additional unused tracking (distraction)
    state_log = {}
    for step in range(3):
        state_log[f'step_{step}'] = {'temp': step * 2.5, 'flag': False}
    
    print(f"Result: {equilibrium_score}")

if __name__ == '__main__':
    main()