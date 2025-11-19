import itertools
from dataclasses import dataclass

def modified_fibonacci(n):
    if n <= 1:
        return n + 1
    a, b = 2, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def matrix_transform(matrix):
    rows, cols = len(matrix), len(matrix[0])
    transformed = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            # Apply bitwise XOR with row-column product
            transformed[i][j] = matrix[i][j] ^ (i * j)
    return transformed

def calculate_weighted_sum(matrix, weights):
    total = 0
    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            total += val * weights[(i + j) % len(weights)]
    return total

# Initialize network topology matrix
network_topology = [
    [3, 7, 2, 9],
    [1, 8, 4, 6],
    [5, 0, 3, 2],
    [7, 1, 8, 4]
]

# Generate Fibonacci weights for each position
fib_weights = [modified_fibonacci(i) for i in range(8)]

# Transform the network matrix
transformed_network = matrix_transform(network_topology)

# Calculate combinations of row indices taken 2 at a time
row_combinations = list(itertools.combinations(range(len(transformed_network)), 2))

# Apply combinatorial influence factor
combinatorial_factor = len(row_combinations) * 3

# Calculate initial weighted influence
initial_influence = calculate_weighted_sum(transformed_network, fib_weights)

# Apply combinatorial adjustment
adjusted_influence = initial_influence + combinatorial_factor

# Final calculation incorporating diagonal elements
main_diagonal_product = 1
for i in range(min(len(transformed_network), len(transformed_network[0]))):
    main_diagonal_product *= transformed_network[i][i]

total_influence = adjusted_influence - (main_diagonal_product // 10)

print(f"Result: {total_influence}")