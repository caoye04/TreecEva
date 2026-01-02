def simulate_tunneling(states):
    # Irrelevant quantum simulation step (distractor)
    coherence = sum(s ** 2 for s in states if s > 0.5)
    decoherence = len([s for s in states if s < 0.3])
    tunnel_weights = [abs(s - 0.7) for s in states]
    return [w * 1.5 for w in tunnel_weights]  # Unused result

def evaluate_superposition(seq):
    # Another red herring: evaluates symmetry but not used in final logic
    mirrored = list(reversed(seq))
    matches = sum(1 for a, b in zip(seq, mirrored) if a == b)
    return matches > len(seq) // 2

def transform_basis(state_list, factor=1.414):
    # Applies transformation but only one output is used later
    normalized = [s / max(state_list) for s in state_list]
    rotated = [round(n * factor, 3) for n in normalized]
    flipped = [1 - r for r in rotated]
    return rotated  # 'flipped' is dead code

def generate_hamiltonian_edges(n):
    # Complex-looking graph generation - entirely irrelevant
    edges = set()
    for i in range(n):
        for j in range(i+1, n):
            if (i + j) % 3 == 0:
                edges.add((i, j))
    return edges  # Unused throughout

def compute_entropy(arr):
    # Decoy function that calculates Shannon-like entropy
    from math import log2
    total = sum(arr)
    probs = [v / total for v in arr if v > 0]
    return -sum(p * log2(p) for p in probs)

def analyze_phase_transition(states, limit):
    # Core relevant logic begins here
    filtered = [s for s in states if s >= 0.1]
    
    # Step 1: Scale using index-aware mapping
    indexed_shift = []
    for idx, val in enumerate(filtered):
        shift = val * (idx + 1)  # Use enumerate meaningfully
        indexed_shift.append(shift)
    
    # Step 2: Pair with shifted version using zip
    lead = indexed_shift[:-1]
    lag = indexed_shift[1:]
    zipped_pairs = list(zip(lead, lag))
    
    # Step 3: Compute interaction product from pairs
    interactions = []
    for x, y in zipped_pairs:
        if x > y:
            interactions.append(x * y)
        else:
            interactions.append((x + y) / 2)
    
    # Step 4: Aggregate and apply threshold filter
    aggregate = sum(interactions)
    if aggregate > limit:
        branch_factor = 2.5
    else:
        branch_factor = 0.8
    
    # Step 5: Apply branching logic
    adjusted = aggregate * branch_factor
    
    # Step 6: Use set operation to deduplicate rounded values (even though not needed here)
    rounded_set = {round(adjusted + i, 1) for i in range(3)}
    base_value = sum(rounded_set) / len(rounded_set)
    
    # Step 7: Final adjustment based on length of original state
    correction = len(states) % 4
    final_value = base_value - correction * 0.3
    
    # Step 8: Truncate to 3 decimal places
    return round(final_value, 3)

# Main execution with multiple distractions
if __name__ == '__main__':
    # Initialize quantum-like state vector
    quantum_states = [0.12, 0.35, 0.71, 0.88, 0.09, 0.54, 0.67]

    # Irrelevant preprocessing
    sorted_states = sorted(quantum_states, reverse=True)
    inverted_map = {i: round(1.0/v, 2) for i, v in enumerate(quantum_states) if v != 0}

    # Call irrelevant functions (dead paths)
    _ = simulate_tunneling(quantum_states)
    _ = evaluate_superposition(quantum_states)
    _ = generate_hamiltonian_edges(len(quantum_states))
    entropy = compute_entropy(quantum_states)  # Computed but unused

    # Transform basis — this modifies representation
    transformed = transform_basis(quantum_states)

    # Define threshold
    threshold = 3.5

    # Critical statement
    final_flux = analyze_phase_transition(transformed, threshold)

    # Print result as required
    print(f"Target result: {final_flux}")