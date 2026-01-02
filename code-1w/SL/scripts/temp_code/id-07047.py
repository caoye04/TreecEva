from itertools import combinations
from functools import reduce

# Simulate network node performance evaluation with weighted metrics

def analyze_connectivity(nodes):
    """Compute pairwise reachability in a circular network."""
    n = len(nodes)
    matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                # Simulated connectivity: distance-based decay
                dist = min(abs(i - j), n - abs(i - j))
                matrix[i][j] = max(0, 10 - dist * 2)
    return matrix

def extract_diagonals(matrix):
    """Extract main and anti-diagonal sums (distractor function)."""
    n = len(matrix)
    main_diag = sum(matrix[i][i] for i in range(n))
    anti_diag = sum(matrix[i][n - 1 - i] for i in range(n))
    return main_diag, anti_diag

def calculate_entropy(data):
    """Calculate Shannon entropy of normalized data (unused distractor)."""
    from math import log2
    total = sum(data)
    if total == 0:
        return 0.0
    probs = [x / total for x in data if x > 0]
    return -sum(p * log2(p) for p in probs)

def evaluate_performance(metrics, weights):
    """Weighted sum using lambda and zip."""
    weighted_sum = sum(map(lambda x: x[0] * x[1], zip(metrics, weights)))
    return int(weighted_sum)

# System configuration
node_ids = ['N1', 'N2', 'N3', 'N4', 'N5']
dummy_thresholds = [0.5, 0.7, 0.3, 0.9, 0.6]

# Generate connectivity matrix
raw_nodes = list(range(len(node_ids)))
connectivity_matrix = analyze_connectivity(raw_nodes)

# Extract diagnostic values (not used in final result)
diag_main, diag_anti = extract_diagonals(connectivity_matrix)

central_node_index = len(node_ids) // 2
central_row = connectivity_matrix[central_node_index]

# Compute auxiliary metrics
mean_reachability = sum(central_row) / len(central_row)
max_reachability = max(central_row)
min_reachability = min(central_row)

# Distractor: generate all 2-node combos (irrelevant)
link_combinations = list(combinations(node_ids, 2))
total_links = len(link_combinations)

# Real metric inputs
base_metrics = [
    mean_reachability,
    max_reachability - min_reachability,
    sum(sum(row) for row in connectivity_matrix) % 17,  # modular arithmetic
    len([x for row in connectivity_matrix for x in row if x > 5])
]

# Weight vector
weights = [1.2, 0.8, 2.1, 0.5]

# Add entropy of flattened matrix (computationally intensive but unused)
flattened = [x for row in connectivity_matrix for x in row]
entropy_value = calculate_entropy(flattened)  # dead-end computation

# Key statement
final_score = evaluate_performance(base_metrics, weights)

print(f"Result: {final_score}")