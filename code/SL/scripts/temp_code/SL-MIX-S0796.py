from functools import reduce

def simulate_circuit(gate_id, path_delays, visited_gates):
    if gate_id in visited_gates:
        return []
    visited_gates.add(gate_id)
    
    # Simulate different gate behaviors using switch-case pattern
    gate_behaviors = {
        'AND': lambda d: d + 2,
        'OR': lambda d: d + 1,
        'XOR': lambda d: d + 3,
        'NOT': lambda d: d + 1,
        'NAND': lambda d: d + 2,
        'BUFFER': lambda d: d + 0
    }
    
    adjusted_delays = []
    for delay in path_delays:
        # Apply gate-specific transformation
        behavior = gate_behaviors.get(gate_id, lambda d: d)
        adjusted_delays.append(behavior(delay))
    
    # Recursive exploration of connected gates
    next_gates = {
        'AND': ['OR', 'NOT'],
        'OR': ['XOR'],
        'XOR': ['NAND', 'BUFFER'],
        'NOT': ['BUFFER'],
        'NAND': [],
        'BUFFER': []
    }
    
    # Backtrack through all possible paths
    for next_gate in next_gates.get(gate_id, []):
        sub_delays = simulate_circuit(next_gate, adjusted_delays, visited_gates.copy())
        adjusted_delays.extend(sub_delays)
    
    return adjusted_delays

# Initialize simulation
initial_delays = [1, 2, 3]
visited = set()
all_path_delays = simulate_circuit('AND', initial_delays, visited)

# Calculate propagation skew using functional programming
propagation_skew = reduce(lambda acc, delay: acc ^ (delay << 1), all_path_delays, 0)

print(f"Result: {propagation_skew}")