from collections import defaultdict
import itertools

# Irrelevant helper function (decoy)
def normalize_vector(v):
    magnitude = sum(x ** 2 for x in v) ** 0.5
    return [x / magnitude for x in v] if magnitude else v

# Misleading signal processing chain
def apply_filter(signal, kernel=[0.25, 0.5, 0.25]):
    smoothed = []
    for i in range(len(signal)):
        weighted = 0
        for j, k in enumerate(kernel):
            idx = max(0, min(i + j - 1, len(signal) - 1))
            weighted += signal[idx] * k
        smoothed.append(weighted)
    return smoothed

# Unused transformation path (dead code)
def transform_domain(data, mode='frequency'):
    if mode == 'frequency':
        return [sum(data[:i]) for i in range(1, len(data)+1)]
    return sorted(data, reverse=True)

# Core logic disguised among distractions
def evaluate_node_risk(profile):
    risk_score = 0
    if profile['load'] > 75:
        risk_score += 30
    if profile['temp'] > 80:
        risk_score += 25
    if profile['fluctuation'] in ['high', 'critical']:
        risk_score += 45
    return risk_score

# Real computation buried in abstraction
def generate_weight_matrix(nodes):
    matrix = defaultdict(lambda: 1.0)
    for i, j in itertools.combinations(range(nodes), 2):
        sync_factor = (i + 1) * 0.67 if (i + j) % 3 == 0 else (j + 1) * 0.33
        matrix[(i, j)] = round(sync_factor, 2)
    return matrix

# Decoy data structure
diagnostic_log = [
    {'timestamp': 1001, 'type': 'INFO', 'value': 0.88},
    {'timestamp': 1002, 'type': 'WARN', 'value': 0.92},
    {'timestamp': 1003, 'type': 'ERR', 'value': 0.0}
]

# Red herring variables
baseline_offset = 0.17
reference_anchor = (3.14159, 2.718)  # unused constant tuple
redundant_buffer = [0] * 15

# Primary control flow with nested logic
network_state = [
    {'node': i, 'load': (i * 12 + 7) % 91, 'temp': (i * 8 + 15) % 88, 
     'fluctuation': ['low', 'medium', 'high'][(i*2) % 3]} 
    for i in range(7)
]

# Distractor: irrelevant aggregation
health_summary = defaultdict(int)
for node in network_state:
    load_bin = 'high' if node['load'] > 60 else 'normal'
    health_summary[load_bin] += 1

# Real weight generation (used later)
weights = generate_weight_matrix(len(network_state))

# Complex lambda-based transformation (partially relevant)
compress_data = lambda seq: [round(x * 0.76 + 1.3, 2) for x in seq]

# Dummy container manipulation
temp_snapshot = tuple(compress_data([n['load'] for n in network_state]))
status_flags = {idx: False for idx in range(len(network_state))}

# Central computation chain
aggregated_metrics = []
for i, node in enumerate(network_state):
    risk = evaluate_node_risk(node)
    base_weight = weights[(i, (i+2)%7)]
    adjusted_risk = risk * base_weight * 0.11
    if node['temp'] > 70:
        adjusted_risk *= 1.4
    if i % 2 == 0:
        adjusted_risk += 5.2
    aggregated_metrics.append(round(adjusted_risk, 3))

# Secondary transformation with filter distraction
filtered_metrics = apply_filter(aggregated_metrics)

# Key statement embedded in context
intermediate_sum = sum(filtered_metrics) * 0.85
final_components = [cm * 1.2 for cm in filtered_metrics]
activation_threshold = compute_signal_strength(network_state, weights)

# Final output printing
print(f"Result: {activation_threshold}")

# Supporting function actually used
def compute_signal_strength(state, w_matrix):
    total_power = 0.0
    for idx, node in enumerate(state):
        # Physical load contribution
        power = (node['load'] * 0.3) + (node['temp'] * 0.2)
        
        # Dynamic weighting from matrix
        neighbor_idx = (idx + 3) % len(state)
        weight = w_matrix[(min(idx, neighbor_idx), max(idx, neighbor_idx))]
        
        # Conditional amplification
        if node['fluctuation'] == 'high':
            power *= 1.8
        elif node['fluctuation'] == 'medium':
            power *= 1.3
            
        # Accumulate with weight
        total_power += power * weight * 0.45
        
        # Dead branch (never taken due to construction)
        if idx > len(state):  # Always false
            total_power -= 0.5
            
    # Final non-linear scaling
    return round(total_power ** 1.1, 6) if total_power > 0 else 0.0
