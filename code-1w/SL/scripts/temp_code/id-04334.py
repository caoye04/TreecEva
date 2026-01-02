from collections import defaultdict, Counter
import math

# Simulate neural network node activation states
def initialize_network(rows, cols):
    grid = [[(i + j) % 7 for j in range(cols)] for i in range(rows)]
    return grid

# Irrelevant helper - decoy function
def analyze_symmetry(pattern):
    return sum(sum(1 for x in row if x == 3) for row in pattern)

# Core transformation: apply nonlinear activation
def activate_nodes(state):
    new_state = []
    for row in state:
        activated = []
        for val in row:
            transformed = int(math.sin(val * math.pi / 4) * 100) + 50
            activated.append(abs(transformed) % 9)
        new_state.append(activated)
    return new_state

# Weight generator with red herring logic
def generate_weights(shape):
    weights = {}
    total = 1
    for i in range(shape[0]):
        for j in range(shape[1]):
            if (i * j + 1) % 3 == 0:
                weights[(i, j)] = (i + j) / 3.0
            else:
                weights[(i, j)] = abs(math.cos(i) - math.sin(j))
    # Dead code path - never used
    temp_buffer = [weights[k] * 2 for k in sorted(weights.keys()) if k[0] % 2 == 0]
    return weights

# Misleading diagnostic tool
def calculate_robustness_score(net):
    flat = [item for row in net for item in row]
    count_map = Counter(flat)
    return sum(v ** 2 for v in count_map.values()) // len(flat)

# Real computation: entropy-based stability index
def compute_entropy(seq):
    freq = defaultdict(int)
    for s in seq:
        freq[s] += 1
    probs = [f / len(seq) for f in freq.values()]
    return -sum(p * math.log2(p) for p in probs if p > 0)

# Cross-layer correlation (distractor)
def cross_correlation(net):
    if len(net) < 2:
        return 0
    corr = 0
    for i in range(len(net[0])):
        col_vals = [net[r][i] for r in range(len(net))]
        corr += abs(sum(col_vals) - sum(1 for x in col_vals if x > 4))
    return corr

# Main stability index calculation (actual answer path)
def compute_stability_index(network, w):
    # Extract values in specific diagonal order
    sequence = []
    for i in range(len(network)):
        for j in range(len(network[i])):
            if (i + j) % 4 == 0:
                sequence.append(network[i][j])
    
    # Apply relevant weights only to key positions
    weighted_vals = []
    for idx, val in enumerate(sequence):
        pos = (idx % len(network), (idx * 2) % len(network[0]))
        weight = w.get(pos, 0.5)
        weighted_vals.append(val * weight)
    
    # Decoy normalization
    norm_factor = max(weighted_vals) if weighted_vals else 1
    normalized = [x / norm_factor for x in weighted_vals] if norm_factor != 0 else weighted_vals
    
    # Actual answer depends on average of first half only
    mid = max(1, len(normalized) // 2)
    relevant_part = normalized[:mid]
    
    # Final index based on mean and entropy combination
    mean_val = sum(relevant_part) / len(relevant_part)
    entropy_val = compute_entropy([int(x * 10) for x in relevant_part])
    
    # Critical distraction: unused alternate formula
    alternate = math.sqrt(mean_val ** 2 + (entropy_val * 2) ** 2)  # NOT USED
    
    # TRUE RESULT
    result = (mean_val * 1.5) + (entropy_val * 0.8)
    return round(result, 6)

# Orchestration function with multiple calls
def run_diagnostics():
    # Initialize network
    raw_grid = initialize_network(6, 6)
    
    # First transformation
    network_state = activate_nodes(raw_grid)
    
    # Generate weight map
    weights = generate_weights((6, 6))
    
    # Irrelevant analysis calls (distractors)
    symmetry_score = analyze_symmetry(network_state)
    robustness = calculate_robustness_score(network_state)
    correlation = cross_correlation(network_state)
    
    # Key computation
    final_diagnostic = compute_stability_index(network_state, weights)
    
    # Unused derived metrics
    diagnostics_log = {
        'symmetry': symmetry_score,
        'robustness': robustness,
        'correlation_index': correlation,
        'raw_diagnostic': final_diagnostic * 0.95
    }
    
    # Print target result
    print(f"Target result: {final_diagnostic}")
    return final_diagnostic

# Execute
run_diagnostics()