import math

# System diagnostics simulator for a distributed quantum node network

def initialize_node(id_val):
    return {
        'id': id_val,
        'phase': (id_val * 1.7) % 3.14,
        'status': 'active' if id_val % 2 == 0 else 'standby',
        'power_level': abs(math.sin(id_val)) * 100,
        'timestamp': id_val * 100 + 42
    }

def calculate_entropy(seq):
    # Irrelevant entropy calculation (dead-end function)
    entropy = 0.0
    freq = {}
    for item in seq:
        freq[item] = freq.get(item, 0) + 1
    for count in freq.values():
        prob = count / len(seq)
        entropy -= prob * math.log2(prob)
    return entropy

def validate_signature(node_data):
    # Misleading validation logic that isn't actually used in final result
    sig = 0
    for char in node_data['status']:
        sig += ord(char)
    sig = (sig * node_data['id']) % 17
    return sig > 5

def transform_power_levels(nodes, factor=1.3):
    # Distractor transformation with unused result
    transformed = {}
    for node in nodes:
        key = f"node_{node['id']}"
        transformed[key] = node['power_level'] * factor + 10
    return transformed

def filter_active_nodes(nodes):
    # Useful but not directly contributing to final answer
    filtered = []
    for node in nodes:
        if node['status'] == 'active' and node['power_level'] > 20:
            filtered.append(node)
    return filtered

def compute_phase_integral(nodes):
    # Relevant computation: integral approximation over phases
    total = 0.0
    for node in nodes:
        total += math.cos(node['phase']) * math.exp(-node['id'] * 0.1)
    return total

def derive_security_hash(nodes):
    # Complex-looking but irrelevant hashing routine
    hash_val = 0
    for node in nodes:
        temp = (node['id'] ^ int(node['phase'])) & 0xFF
n        hash_val ^= temp
        hash_val = (hash_val << 1) | (hash_val >> 7)
    return hash_val & 0xFFFF

def analyze_system_state(nodes):
    # Core analysis function - computes final diagnostic score
    
    # Step 1: Filter relevant nodes
    active_nodes = [n for n in nodes if n['status'] == 'active']
    
    # Step 2: Compute weighted phase contribution
    phase_sum = 0.0
    weight_sum = 0.0
    for node in active_nodes:
        weight = math.log(node['power_level'] + 1) / (node['id'] + 1)
        phase_sum += node['phase'] * weight
        weight_sum += weight
    
    # Step 3: Normalize phase contribution
    normalized_phase = phase_sum / weight_sum if weight_sum != 0 else 0
    
    # Step 4: Compute stability metric from power variance
    powers = [n['power_level'] for n in active_nodes]
    mean_power = sum(powers) / len(powers) if powers else 0
    variance = sum((p - mean_power) ** 2 for p in powers) / len(powers) if powers else 0
    stability = 100 / (1 + variance)
    
    # Step 5: Compute interference index from timestamp parity
    interference_count = 0
    for node in nodes:
        if node['timestamp'] % 13 == 0:
            interference_count += 1
    
    # Step 6: Calculate decay factor based on node IDs
    ids = [n['id'] for n in nodes]
    decay_factor = math.exp(-len(ids) * 0.05)
    
    # Step 7: Combine into base diagnostic
    base_diagnostic = (normalized_phase * 100) + stability
    
    # Step 8: Apply decay and interference penalty
    final_adjustment = base_diagnostic * decay_factor - (interference_count * 3.7)
    
    # Final result
    return round(final_adjustment, 4)

# --- Main execution ---

# Initialize quantum nodes (critical data structure)
quantum_nodes = []
for i in range(3, 13):  # Nodes 3 through 12
    quantum_nodes.append(initialize_node(i))

# Dead-end operations (distractors)
dummy_sequence = [1, 2, 2, 3, 3, 3, 4]
entropy_result = calculate_entropy(dummy_sequence)
signature_valid = all(validate_signature(node) for node in quantum_nodes[:3])
transformed_powers = transform_power_levels(quantum_nodes, 1.7)
filtered_nodes = filter_active_nodes(quantum_nodes)
security_hash = derive_security_hash(quantum_nodes)
integral_value = compute_phase_integral(quantum_nodes)

# Critical computation path
final_diagnostic = analyze_system_state(quantum_nodes)

# Output result
print(f"Result: {final_diagnostic}")