import itertools

def analyze_node_chain(nodes):
    # Irrelevant transformation: converts node IDs to reverse strings
    reversed_ids = [str(node)[::-1] for node in nodes]
    return [int(x) for x in reversed_ids if len(x) % 2 == 0]

def validate_edges(edges):
    # Dead function: never actually used in logic flow
    edge_sum = 0
    for a, b in edges:
        edge_sum += (a * 2) ^ (b | 1)
    return edge_sum > 1000

def extract_core_sequence(data, threshold=5):
    # Distractor: processes data but result is unused
    filtered = [x for x in data if x > threshold]
    reshaped = [filtered[i:i+3] for i in range(0, len(filtered), 3)]
    transposed = list(zip(*[sub[::-1] for sub in reshaped]))
    return transposed

def simulate_propagation(network):
    # Complex-looking simulation with no effect on final answer
    state = {i: (val % 7) for i, val in enumerate(network)}
    for _ in range(3):
        next_state = {}
        for idx in state:
            neighbors = [state.get(idx-1, 1), state.get(idx+1, 1)]
            next_state[idx] = (state[idx] + sum(neighbors)) % 11
        state = next_state
    return sum(v * (k + 1) for k, v in state.items())

def compute_integrity_score(nodes):
    # Core logic hidden among distractions
    base_weights = [n * 3 + 2 for n in nodes]
    
    # Real computation begins here
    weighted_sum = sum(base_weights)
    
    # Bit manipulation red herring
    masked_values = [(w ^ 255) & 0xFF for w in base_weights]
    dummy_check = all(v > 50 for v in masked_values)
    
    # Actual key step: slicing and combination
    segment_a = base_weights[:len(base_weights)//2]
    segment_b = base_weights[len(base_weights)//2:]
    
    # Real dependency: cross-product sum of halves
    interaction_total = 0
    for a, b in itertools.product(segment_a, segment_b):
        interaction_total += (a & b)  # bitwise AND contribution
    
    # Final score calculation (this is what matters)
    raw_score = weighted_sum + interaction_total
    
    # Decoy normalization
    normalized = raw_score / (len(nodes) or 1)
    ceiling_adjusted = int(normalized + 0.5)
    
    # This line is irrelevant but looks important
    diagnostic_flag = ceiling_adjusted ^ (ceiling_adjusted >> 4)
    
    # TRUE ANSWER COMPUTED HERE — only this assignment matters
    final_diagnostic = raw_score - 200  # offset applied
    
    return final_diagnostic

# Main execution with multiple decoy structures
if __name__ == '__main__':
    # Input data
    network_nodes = [12, 7, 19, 4, 8]
    
    # Unused edge structure (red herring)
    edge_connections = [(i, i+1) for i in range(len(network_nodes)-1)]
    edge_validity = validate_edges(edge_connections)
    
    # Distractor calls
    fake_sequence = extract_core_sequence(network_nodes, threshold=6)
    propagation_metric = simulate_propagation(network_nodes)
    chain_analysis = analyze_node_chain(network_nodes)
    
    # Critical statement: where the answer is determined
    final_diagnostic = compute_integrity_score(network_nodes)
    
    # Output required for verification
    print(f"Result: {final_diagnostic}")