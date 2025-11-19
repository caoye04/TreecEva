from functools import reduce

def calculate_mutation_paths(matrix, row, col, visited, current_score):
    if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]):
        return 0
    
    if (row, col) in visited:
        return 0
    
    visited.add((row, col))
    current_score += matrix[row][col]
    
    # Define valid transitions using set operations
    nucleotide_set = {matrix[row][col]}
    transition_rules = [{1, 2}, {2, 3}, {3, 4}, {4, 1}]
    valid_transitions = reduce(lambda a, b: a.union(b), 
                              filter(lambda s: nucleotide_set.issubset(s), transition_rules),
                              set())
    
    max_score = current_score if nucleotide_set.issubset(valid_transitions) else 0
    
    # Recursive exploration in four directions
    for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        next_row, next_col = row + dr, col + dc
        if 0 <= next_row < len(matrix) and 0 <= next_col < len(matrix[0]):
            next_nucleotide = matrix[next_row][next_col]
            if next_nucleotide in valid_transitions or valid_transitions == set():
                path_score = calculate_mutation_paths(matrix, next_row, next_col, 
                                                     visited.copy(), current_score)
                max_score = max(max_score, path_score)
    
    return max_score

genomic_matrix = [
    [1, 2, 3],
    [4, 1, 2],
    [3, 4, 1]
]

visited_positions = set()
final_path_score = calculate_mutation_paths(genomic_matrix, 0, 0, visited_positions, 0)
print(f'Result: {final_path_score}')