import math

# Simulated network node data with health metrics
def generate_node_data():
    return {
        'node_01': {'load': 78, 'temp': 65, 'errors': 3, 'active': True},
        'node_02': {'load': 92, 'temp': 77, 'errors': 8, 'active': True},
        'node_03': {'load': 45, 'temp': 54, 'errors': 1, 'active': False},
        'node_04': {'load': 88, 'temp': 70, 'errors': 12, 'active': True},
        'node_05': {'load': 33, 'temp': 48, 'errors': 0, 'active': True},
        'node_06': {'load': 67, 'temp': 60, 'errors': 5, 'active': True}
    }

# Irrelevant helper: Converts text to binary (distractor)
def text_to_binary(s):
    return ''.join(format(ord(c), '08b') for c in s)

# Misleading normalization function (not used in final path)
def normalize_score(x, min_val=0, max_val=100):
    return (x - min_val) / (max_val - min_val)

# Decoy metric calculation (dead code path)
def compute_reliability_index(errors, age_years):
    decay = math.exp(-0.1 * age_years)
    return (100 - errors * 5) * decay

# Auxiliary transformation: temperature class (partially relevant)
def temp_class(temp):
    if temp > 70:
        return 'overheating'
    elif temp > 60:
        return 'elevated'
    else:
        return 'normal'

# Complex load categorization with slicing distraction
def categorize_load(load_str):
    # Example of slicing misuse as distraction
    category_map = {'low': 'green', 'med': 'yellow', 'high': 'red'}
    if 'o' in load_str:
        return category_map[load_str[:3]]
    return 'unknown'

# Real-time error rate estimator (unused but plausible)
def estimate_error_rate(current, historical):
    return (current + sum(historical)) / (len(historical) + 1)

# Core diagnostic weight calculator (used)
def calculate_health_weight(node):
    base = node['load'] * 0.4
    temp_penalty = (node['temp'] - 50) * 0.3 if node['temp'] > 50 else 0
    error_cost = node['errors'] * 2.5
    return base + temp_penalty - error_cost

# Secondary filter: checks operational status and derives flag
def is_critical_failure(node):
    return node['active'] and node['errors'] > 10 and node['temp'] > 70

# Data transformer: extracts key values into vector (distractor)
def extract_features(node_dict):
    features = []
    for k, v in node_dict.items():
        features.append((v['load'], v['temp']))
    return features[::-1]  # reversed slice - red herring

# Aggregation engine: main computation path
def aggregate_metrics(nodes):
    weights = []
    critical_count = 0
    temp_status = {}

    # Primary loop with nested logic
    for nid, data in nodes.items():
        if not data['active']:
            continue  # Skip inactive nodes

        # Real health assessment
        health = calculate_health_weight(data)
        
        # Track temperature classifications
        t_class = temp_class(data['temp'])
        temp_status[nid] = t_class

        # Check failure state (boolean logic with short-circuit)
        if data['active'] and (data['errors'] > 10 or data['temp'] > 75) and data['load'] > 80:
            critical_count += 1

        weights.append(health)

    # Compute average health, only from active nodes
    avg_health = sum(weights) / len(weights) if weights else 0

    # Spurious combinatorics calculation (irrelevant)
    n_pairs = len(nodes) * (len(nodes) - 1) // 2 if len(nodes) > 1 else 0
    pair_sum = 0
    keys = list(nodes.keys())
    for i in range(min(n_pairs, 5)):
        idx1 = (i * 7) % len(keys)
        idx2 = (i * 13 + 1) % len(keys)
        pair_sum += ord(keys[idx1][5]) + ord(keys[idx2][5])

    # Conditional expression determining fallback (used once)
    adjustment = 10 if critical_count >= 2 else (5 if critical_count == 1 else 0)

    # Final diagnostic score with case conversion distraction
    status_text = "CRITICAL" if critical_count > 0 else "STABLE"
    prefix_val = sum(ord(c.lower()) for c in status_text[:3])  # 'cri' or 'sta'

    # Actual answer computation (non-obvious combination)
    final_score = avg_health - adjustment + (prefix_val * 0.1)

    # Dead code: string joining decoy
    log_entry = '-'.join([nid.upper() for nid in nodes.keys() if nodes[nid]['active']])
    log_entry = log_entry.replace('NODE', 'N').split('-')[::-1]

    return int(final_score)  # deterministic integer output

# Initialization and execution
network_nodes = generate_node_data()

# Extensive irrelevant pre-processing (distractors)
node_list = list(network_nodes.keys())
node_slices = node_list[1:4:2]  # partial slice
binary_tag = text_to_binary("diagnostics")
historical_errors = [2, 4, 1, 0, 3]

# Unused dictionary operations (red herring)
diag_log = {k: {'processed': False, 'flags': []} for k in network_nodes}
for k in diag_log:
    diag_log[k]['processed'] = True

# Main execution point
final_diagnostic = aggregate_metrics(network_nodes)

# Additional meaningless transformation chain
shifted_bin = binary_tag[6:] + binary_tag[:6]
reconstructed = ''.join(chr(int(shifted_bin[i:i+8], 2)) for i in range(0, len(shifted_bin), 8))

# Output result as required
print(f"Target result: {final_diagnostic}")