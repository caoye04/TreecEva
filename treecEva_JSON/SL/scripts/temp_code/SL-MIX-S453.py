from collections import defaultdict
import math

def simulate_crypto_protocol():
    # Initialize session tracker
    active_sessions = defaultdict(int)
    
    # Base keys for different node types
    node_keys = [12, 18, 24, 30]
    
    # Simulate session creation
    for i, key in enumerate(node_keys):
        encoded_key = key.encode('utf-8') if isinstance(key, str) else str(key).encode('utf-8')
        decoded_key = int(encoded_key.decode('utf-8'))
        scaled_key = int(math.log(decoded_key) * 100)  # Logarithmic scaling
        active_sessions[f'node_{i}'] = scaled_key
    
    # Apply exponential key strengthening
    for node_id in list(active_sessions.keys()):
        base_value = active_sessions[node_id]
        strengthened_key = int(math.exp(base_value / 100))  # Exponential transformation
        active_sessions[node_id] = strengthened_key
    
    # Calculate aggregated security metric
    security_sum = sum(active_sessions.values())
    
    # Apply set-based filtering for compromised nodes
    all_nodes = {f'node_{i}' for i in range(len(node_keys))}
    compromised_nodes = frozenset(['node_1'])
    valid_nodes = all_nodes - compromised_nodes
    
    # Compute final key strength from valid nodes only
    valid_strengths = [active_sessions[node] for node in valid_nodes]
    final_key_strength = sum(valid_strengths) // len(valid_strengths)  # Integer division for stability metric
    
    return final_key_strength

# Execute simulation
final_key_strength = simulate_crypto_protocol()
print(f'Result: {final_key_strength}')