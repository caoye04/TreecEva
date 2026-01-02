def preprocess_network(nodes):
    weighted_sum = sum([n['weight'] * n['factor'] for n in nodes if n['active']])
    avg_weight = weighted_sum / len(nodes) if nodes else 0
    return avg_weight

nodes = [
    {'weight': 12, 'factor': 3, 'active': True, 'id': 'A'},
    {'weight': 8, 'factor': 4, 'active': True, 'id': 'B'},
    {'weight': 5, 'factor': 2, 'active': False, 'id': 'C'},
    {'weight': 15, 'factor': 1, 'active': True, 'id': 'D'},
    {'weight': 10, 'factor': 5, 'active': True, 'id': 'E'}
]

# Irrelevant helper that computes but isn't used in final path
def analyze_connectivity(graph):
    edges = 0
    for node in graph:
        if 'neighbors' in node:
            edges += len(node['neighbors'])
    return edges

# Dummy data for distraction
network_graph = [
    {'id': 'X1', 'neighbors': ['X2', 'X3']},
    {'id': 'X2', 'neighbors': ['X1']}
]
edge_count = analyze_connectivity(network_graph)

base_score = preprocess_network(nodes)

# Create threshold map with some red herring logic
threshold_map = {}
categories = ['alpha', 'beta', 'gamma']
for i, cat in enumerate(categories):
    threshold_map[cat] = base_score * (i + 1) * 0.1

# Misleading transformation
transformed = {k: v * 1.5 for k, v in threshold_map.items()}
unused_adjustment = sum(transformed.values())

# Extract active nodes and do actual relevant filtering
reduced_nodes = [n for n in nodes if n['weight'] > 9 and n['active']]

# Simulate signal propagation across reduced nodes
def propagate_signals(nodelist):
    signals = []
    for node in nodelist:
        sig_val = node['weight'] ** 2 / (node['factor'] + 1)
        if sig_val > 50:
            signals.append(sig_val * 0.8)
        else:
            signals.append(sig_val)
    return set(signals)  # Use of set operation

signal_set = propagate_signals(reduced_nodes)
signal_count = len(signal_set)

# Core stability calculation function
def calculate_stability(node_list, thresholds):
    total_flux = 0
    flux_records = []
    
    for node in node_list:
        raw_flux = node['weight'] * 2.5
        category_key = 'beta'
        adjusted_flux = raw_flux * 0.9
        
        # Conditional branching with early break possibility
        if adjusted_flux > thresholds['beta']:
            adjusted_flux -= thresholds['alpha']
        else:
            adjusted_flux += thresholds['gamma']
            break  # Early exit under condition (not triggered here)
            
        flux_records.append(adjusted_flux)
    
    # Final aggregation using list comprehension
    valid_flux = [f for f in flux_records if f > 20]
    total_flux = sum(valid_flux)
    
    # Add minor correction based on signal count (inter-concept dependency)
    total_flux += signal_count * 1.5
    
    return int(total_flux)  # Deterministic integer result

final_flux = calculate_stability(reduced_nodes, threshold_map)
print(f"Result: {final_flux}")