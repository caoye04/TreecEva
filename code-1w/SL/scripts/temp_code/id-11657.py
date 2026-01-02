from collections import defaultdict, Counter
import itertools

# Simulate a network node analysis with signal transformations
def analyze_signals(raw_data):
    processed = []
    temp_cache = defaultdict(int)
    for val in raw_data:
        if val < 0:
            temp_cache['negative'] += 1
            processed.append(abs(val) * 1.5)
        elif val == 0:
            temp_cache['zero'] += 1
        else:
            temp_cache['positive'] += 1
            processed.append(val ** 0.5)
    return processed, dict(temp_cache)

def filter_outliers(seq, threshold=2.5):
    avg = sum(seq) / len(seq)
    return [x for x in seq if x <= avg * threshold]

def build_node_map(keys, values):
    # Irrelevant mapping construction (dead abstraction)
    node_map = {}
    for k, v in zip(keys, values):
        node_map[k] = v % 7
    return node_map

def decoy_aggregate(data_list):
    # Misleading function that looks important but isn't used
    total = 0
    for item in data_list:
        if isinstance(item, dict):
            total += sum(item.values())
        else:
            total += len(str(item))
    return total

def signal_strength(sequence):
    strength = 0
    for i, s in enumerate(sequence):
        strength += s * (0.9 ** i)  # exponential decay weighting
    return round(strength, 6)

def transform_sequence(seq):
    # Apply complex transformation with distractor logic
    transformed = []
    history = []
    pivot = len(seq) // 2
    
    for i, x in enumerate(seq):
        if i < pivot:
            transformed.append(x * 2 + 1)
        else:
            transformed.append((x ** 2) - x)
        history.append(len(transformed))  # Red herring: unused tracking
    
    # Dead code path - never executed due to prior logic
    if False and len(history) > 100:
        transformed = [t * 0.1 for t in transformed]
        
    return transformed

def aggregate_transform(nodes):
    base_flows = []
    debug_stats = Counter()
    
    for node in nodes:
        # Simulate multi-stage node processing
        stage1 = [n * 3 for n in node if n % 2 == 1]  # only odd numbers scaled
        stage2 = [s - 1 for s in stage1 if s > 5]     # filter and reduce
        
        if len(stage2) >= 3:
            compressed = list(itertools.accumulate(stage2[:4], lambda a, b: a + b * 0.75))
            base_flows.extend(compressed)
            debug_stats['valid_nodes'] += 1
        else:
            base_flows.append(sum(stage2) * 0.5)
            debug_stats['fallback_nodes'] += 1
    
    # Real computation path
    filtered = filter_outliers(base_flows, threshold=2.2)
    strength = signal_strength(filtered)
    final = int(round(strength * 1.764))  # key scaling factor
    
    # Decoy operations with no impact
    dummy_map = build_node_map(['A','B','C'], [12,24,36])
    temp_result = decoy_aggregate([{'x':1}, {'y':2}])
    
    return final

# Main execution flow
if __name__ == '__main__':
    raw_input_stream = [12, -8, 15, 0, 7, -3, 9, 4, 6]
    signals, meta_info = analyze_signals(raw_input_stream)
    
    # Construct network nodes (core data structure)
    network_nodes = [
        [1, 3, 5, 7],
        [2, 4, 6],
        [5, 9, 11, 13, 15],
        [8, 10, 12]
    ]
    
    # Irrelevant pre-processing (distractor)
    temp_grid = [[i*j for j in range(3)] for i in range(4)]
    checksum = sum(sum(row) for row in temp_grid)
    
    # Transform each node's base values (unused in final logic)
    transformed_nodes = []
    for node in network_nodes:
        transformed_nodes.append(transform_sequence(node))
    
    # Key statement: compute final flux from original network_nodes
    final_flux = aggregate_transform(network_nodes)
    
    # Print result as required
    print(f"Target result: {final_flux}")