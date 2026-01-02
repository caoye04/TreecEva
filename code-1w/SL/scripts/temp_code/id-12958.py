import itertools

# System diagnostics simulation with interference

def collect_node_health(nodes):
    health_data = {}
    for node in nodes:
        raw_status = sum(ord(c) for c in node) % 7
        # Irrelevant transformation
        temp_score = (raw_status ** 3) // 2 if raw_status > 3 else raw_status + 5
        health_data[node] = raw_status  # Only raw_status is used later
    return health_data


def analyze_log_sequence(logs):
    # Real logic buried under distractions
    event_chain = [len(log) for log in logs]
    cumulative = []
    running = 0
    for e in event_chain:
        running += e
        cumulative.append(running)
    
    # Distractor: complex but unused calculation
    decoy_moment = list(itertools.accumulate(cumulative, lambda x, y: (x + y) % 5))
    smoothed = [v for i, v in enumerate(cumulative) if i % 2 == 0]
    
    # Actual signal
    return sum(smoothed) % 100


def validate_checksum(structure):
    # Red herring function - looks important but not used
    total = 0
    for s in structure:
        total ^= len(s) * 3
    return total % 17


def filter_active_nodes(node_map, threshold=4):
    # Intermediate processing with misleading paths
    active_list = []
    debug_weights = {}  # Unused debugging artifact
    for k, v in node_map.items():
        weight = (v * 2) + 1
        debug_weights[k] = weight  # Dead assignment
        if v >= threshold:
            active_list.append(k)
    # Real output
    return set(active_list)


def compute_entropy(values):
    # Complex-looking but irrelevant function
    from math import log2
    total = sum(values)
    if total == 0:
        return 0.0
    probs = [v / total for v in values if v > 0]
    return -sum(p * log2(p) for p in probs)


def aggregate_metrics(nodes, logs):
    # Core logic with embedded distractions
    
    # Step 1: Collect base health scores
    health = collect_node_health(nodes)
    
    # Step 2: Analyze log patterns
    log_metric = analyze_log_sequence(logs)
    
    # Step 3: Filter critical nodes
    critical_nodes = filter_active_nodes(health, threshold=3)
    
    # Step 4: Generate dummy statistics (distraction)
    pseudo_entropy = compute_entropy(list(health.values()))
    anomaly_flag = pseudo_entropy > 2.0  # Unused flag
    
    # Step 5: Cross-reference with positional data using zip and enumerate
    indexed_nodes = list(enumerate(nodes))
    position_offset = 0
    for idx, name in indexed_nodes:
        if name in critical_nodes:
            position_offset += idx * (ord(name[0]) % 3)
    
    # Step 6: Use set operations meaningfully
    mirrored_set = {n[::-1] for n in nodes}  # Reversed names
    intersection_count = len(set(nodes) & mirrored_set)  # Palindrome-like detection
    
    # Step 7: Combine relevant signals
    base_score = sum(health.values())
    
    # Step 8: Introduce itertools distraction
    paired = list(itertools.zip_longest(nodes, list(health.values()), fillvalue=0))
    pair_sum = sum(len(str(p[0])) + p[1] for p in paired[:len(nodes)])  # Partial use
    
    # Final computation - only some components matter
    final_diagnostic = (base_score * 17 + log_metric) % 997
    final_diagnostic += position_offset
    final_diagnostic -= intersection_count * 5  # Adjustment based on symmetry
    
    # This print is required for traceability
    print(f"Result: {final_diagnostic}")
    
    return final_diagnostic

# Execution context
network_nodes = ['alpha', 'gamma', 'theta', 'sigma', 'omega']
system_logs = ['ERR@0', 'INIT:OK', 'SYNC!', 'HALT?', 'RESET']

# Triggering statement
debug_trace = validate_checksum(network_nodes)  # Dead call
final_diagnostic = aggregate_metrics(network_nodes, system_logs)