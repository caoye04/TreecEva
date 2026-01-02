import itertools

def analyze_flow_components(matrix):
    # Irrelevant helper: computes row sums (not used in final logic)
    return [sum(row) for row in matrix]

def generate_threshold_combinations(thresholds):
    # Distractor function: generates combinations but only one is used
    return list(itertools.combinations(thresholds, 2))

def validate_stability(pattern):
    # Semi-relevant: checks alternating signs, actually used once
    return all(a * b < 0 for a, b in zip(pattern, pattern[1:]))

# Initial system parameters
base_signals = [3, -7, 5, -2, 8]
offset_grid = [[i + j for j in range(4)] for i in range(5)]

# Simulate signal harmonics (distractor computation)
harmonic_series = []
for x in base_signals:
    series = []
    for n in range(1, 4):
        series.append((x ** n) % 11)
    harmonic_series.append(series)

# Construct flow matrix using modular arithmetic and combinatorics
flow_matrix = []
for i in range(5):
    row = []
    for j in range(4):
        val = (base_signals[i] * offset_grid[i][j]) % 9
        if val == 0:
            val = 1  # Avoid zero values
        row.append(val)
    flow_matrix.append(row)

# Define threshold set with red herring elements
thresholds = [2, 3, 5, 7, 11]

# Generate unnecessary combination data (intermediate distractor)
combo_data = generate_threshold_combinations(thresholds)
filtered_pairs = [pair for pair in combo_data if sum(pair) > 10]

# Track state transitions (partially used)
state_log = []
current_state = 0
for row in flow_matrix:
    active_count = sum(1 for x in row if x > 4)
    state_log.append(active_count)
    if active_count >= 3:
        current_state += 1
    else:
        current_state -= 1

# Critical function: calculate equilibrium score
def calculate_equilibrium(matrix, tholds):
    score = 0
    prime_mod = tholds[2]  # Use 5 as modulus
    
    # Use itertools to process diagonal-like patterns
    indices = list(itertools.permutations(range(4), 2))
    edge_contributions = []
    
    for i, (r, c) in enumerate(indices):
        if r < len(matrix) and c < len(matrix[r]):
            edge_val = matrix[r][c] % prime_mod
            if i % 3 == 0:  # Every third index contributes
                edge_contributions.append(edge_val)
    
    # Core calculation
    for idx, val in enumerate(edge_contributions):
        score += (val * (idx + 1)) % 7
    
    # Incorporate state_log indirectly
    adjustment = sum(state_log) % 4
    score = (score + adjustment) * 2
    
    return score

# Execute main computation
equilibrium_score = calculate_equilibrium(flow_matrix, thresholds)

# Print result as required
print(f"Result: {equilibrium_score}")