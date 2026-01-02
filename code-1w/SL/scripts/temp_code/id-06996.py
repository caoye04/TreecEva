def analyze_node(node_id, threshold=0.5):
    return node_id % 3 == 0 and node_id > threshold

def validate_chain(chain):
    return sum(1 for x in chain if x % 2) > len(chain) // 2

def compute_hash(data_list):
    hash_val = 0
    for i, val in enumerate(data_list):
        hash_val += val * (i + 1)
    return hash_val % 1000

def extract_features(raw_data):
    features = []
    for item in raw_data:
        if isinstance(item, dict) and 'value' in item:
            features.append(item['value'] * 2)
    return features

def filter_redundant(nodes):
    seen = set()
    unique = []
    for n in nodes:
        if n not in seen:
            seen.add(n)
            unique.append(n)
    return unique

def merge_dicts(d1, d2):
    result = d1.copy()
    for k, v in d2.items():
        result[k] = result.get(k, 0) + v
    return result

def evaluate_stability(metrics):
    stable_count = 0
    for i, m in enumerate(metrics):
        if i % 2 == 0 and m > 0.7:
            stable_count += 1
    return stable_count >= 2

def calculate_entropy(seq):
    from math import log2
    freq = {}
    for s in seq:
        freq[s] = freq.get(s, 0) + 1
    entropy = 0
    total = len(seq)
    for f in freq.values():
        p = f / total
        entropy -= p * log2(p)
    return round(entropy, 4)

def process_metrics(data, importance_weights):
    # Core logic begins here
    base_scores = []
    for entry in data:
        if 'active' in entry and entry['active']:
            score = entry.get('magnitude', 0) * 1.5
            if entry.get('type') == 'critical':
                score *= 2.0
            base_scores.append(score)
    
    # Irrelevant transformation (distractor)
    temp_transform = [x ** 0.5 for x in base_scores if x > 5]
    temp_sum = sum(temp_transform)  # unused later
    
    # Key weighting operation
    weighted = []
    for i, b in enumerate(base_scores):
        weight = importance_weights[i % len(importance_weights)]
        weighted.append(b * weight)
    
    # Dead code path (misleading)
    if len(weighted) > 10:
        fallback = 0
        for w in weighted:
            fallback += w // 2
        return fallback  # never reached

    # Decoy function call with side effect that doesn't affect outcome
    decoy_buffer = [{'val': x + 10} for x in weighted]
    buffer_sum = sum(d['val'] for d in decoy_buffer)  # irrelevant

    # Actual aggregation
    aggregate = sum(weighted) / len(weighted) if weighted else 0
    
    # Conditional adjustment based on auxiliary check
    types_present = [e['type'] for e in data if 'type' in e]
    type_set = set(types_present)
    if 'critical' in type_set and 'auxiliary' not in type_set:
        aggregate *= 1.2
    
    # Additional distraction: sorting unrelated list
    dummy_list = [3, 1, 4, 1, 5]
    dummy_list.sort(reverse=True)
    sorted_sum = sum(dummy_list)  # misleading intermediate

    # Final computation
    final_value = int(round(aggregate * 100))
    return final_value

# Main execution
if __name__ == '__main__':
    # Simulated network telemetry data
    network_data = [
        {'id': 101, 'magnitude': 8, 'active': True, 'type': 'critical'},
        {'id': 102, 'magnitude': 6, 'active': True, 'type': 'standard'},
        {'id': 103, 'magnitude': 0, 'active': False, 'type': 'standard'},
        {'id': 104, 'magnitude': 9, 'active': True, 'type': 'critical'},
        {'id': 105, 'magnitude': 5, 'active': True, 'type': 'standard'}
    ]

    # Weights for scoring (cyclic indexing)
    weights = [0.8, 1.1, 0.9]

    # Irrelevant preprocessing (red herring)
    ids = [d['id'] for d in network_data]
    valid_ids = [i for i in ids if analyze_node(i)]
    id_sum = sum(valid_ids)

    # Dummy structures (set and dict operations - distractors)
    status_flags = set(['A', 'B', 'C'])
    config_map = {'A': 10, 'B': 20, 'D': 30}
    overlap = status_flags & set(config_map.keys())  # {'A', 'B'}
    overlap_total = sum(config_map[k] for k in overlap)

    # Another decoy: zipping unrelated sequences
    indices = list(range(len(network_data)))
    paired = list(zip(indices, [d['magnitude'] for d in network_data]))
    pair_product = sum(i * m for i, m in paired)

    # Real processing step
    final_score = process_metrics(network_data, weights)

    # Print required output
    print(f"Result: {final_score}")