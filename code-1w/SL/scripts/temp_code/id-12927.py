import itertools

def generate_pattern(seed, length):
    # Irrelevant function: generates a Fibonacci-like sequence
    pattern = [seed]
    for i in range(1, length):
        pattern.append((pattern[-1] + pattern[-2] % 17) if i > 1 else seed + 1)
    return pattern

def validate_sequence(seq):
    # Dead code path: never called but looks important
    return all(x > 0 for x in seq) and len(seq) % 2 == 0

def transform_data(data, factor=3):
    # Distractor transformation with bit manipulation
    shifted = [(x << 1) ^ factor for x in data]
    filtered = [x for x in shifted if x % 5 != 0]
    return [x for x in filtered if x < 100]

def compute_stability_index(matrix):
    # Complex-looking but unused stability calculation (red herring)
    total = 0
    for row in matrix:
        for val in row:
            total += abs(val) ** 0.5
    return total / (len(matrix) * len(matrix[0]) + 1)

def analyze_distribution(values):
    # Unused statistical analysis with misleading intermediate results
    mean = sum(values) / len(values)
    variance = sum((x - mean) ** 2 for x in values) / len(values)
    return {'mean': mean, 'variance': variance, 'peak': max(values)}

def compute_equilibrium(matrix, limits):
    # Core logic hidden among distractions
    rows, cols = len(matrix), len(matrix[0])
    temp_grid = [[0] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            neighbor_sum = 0
            for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < rows and 0 <= nj < cols:
                    neighbor_sum += matrix[ni][nj]
            temp_grid[i][j] = neighbor_sum % 7
    
    # Aggregate transformed neighbors
    aggregate = 0
    for row in temp_grid:
        for val in row:
            aggregate += val * 2
    
    # Secondary processing using itertools
    combinations = list(itertools.combinations_with_replacement(limits, 2))
    adjustment = 0
    for combo in combinations:
        adjustment += (combo[0] - combo[1]) ** 2
    
    # Final computation
    final_score = (aggregate // (len(combinations) or 1)) - adjustment
    
    # Key assignment point
    equilibrium_score = final_score + 42
    
    return equilibrium_score

# Main execution block
if __name__ == '__main__':
    # Input setup
    flow_matrix = [
        [3, 1, 4, 1],
        [5, 9, 2, 6],
        [5, 3, 5, 8],
        [9, 7, 9, 3]
    ]
    
    thresholds = [2, 3, 5, 7]
    
    # Irrelevant data transformations
    signal_chain = generate_pattern(7, 20)
    processed_signal = transform_data(signal_chain, factor=5)
    
    # Unused structures
    metadata_map = {
        'version': '2.1',
        'mode': 'diagnostic',
        'debug_trace': [[i*j for j in range(5)] for i in range(5)]
    }
    
    # Decoy function calls
    stability = compute_stability_index(flow_matrix)  # Computed but unused
    stats = analyze_distribution(processed_signal)     # Computed but unused
    
    # Critical statement
    equilibrium_score = compute_equilibrium(flow_matrix, thresholds)
    
    # Output result
    print(f"Result: {equilibrium_score}")