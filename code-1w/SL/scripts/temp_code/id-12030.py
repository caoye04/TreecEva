def analyze_metrics(data, config):
    # Irrelevant preprocessing
    temp_results = {k: v ** 2 for k, v in data.items() if v > 0}
    normalized = [x / sum(temp_results.values()) for x in temp_results.values()]
    
    # Distractor: unused transformation chain
    transformed = []
    for idx, val in enumerate(normalized):
        if idx % 2 == 0:
            transformed.append(val * 1.5)
        else:
            transformed.append(val * 0.8)

    # Meaningless smoothing
    smoothed = []
    for i in range(len(transformed)):
        window = transformed[max(0, i-1):i+2]
        smoothed.append(sum(window) / len(window))

    # Red herring function call (no side effects)
    def evaluate_stability(seq):
        return sum(seq[i] > seq[i-1] for i in range(1, len(seq)))
    stability_index = evaluate_stability(smoothed)

    # Actual relevant logic buried here
    raw_scores = [data[k] for k in sorted(data.keys()) if k.startswith('metric_')]
    adjusted = [x * config.get('scale', 1.0) + config.get('offset', 0) for x in raw_scores]
    filtered = [x for x in adjusted if x >= 0]
    return sum(filtered) / len(filtered) if filtered else 0


def generate_feedback_hierarchy(levels=3):
    # Complex but irrelevant structure generation
    hierarchy = {}
    for level in range(levels):
        hierarchy[level] = {f"node_{i}": {'status': 'active', 'value': i*level} for i in range(5)}
    
    # Unused recursive helper
    def traverse(h, path=[]):
        if isinstance(h, dict) and 'status' in h:
            return [path + [h['status']]]
        results = []
        for k, v in h.items():
            results.extend(traverse(v, path + [k]))
        return results
    
    paths = traverse(hierarchy)
    return hierarchy  # Never used beyond creation

# Decoy data structures
decoys = [
    {'name': 'buffer', 'data': [i**3 % 17 for i in range(20)]},
    {'name': 'checksums', 'values': [sum(ord(c) for c in str(i)) for i in range(10)]}
]

# Real input data
feedback_map = {
    'metric_a': 4.2,
    'metric_b': 3.8,
    'metric_c': 5.0,
    'aux_info_1': 0.5,  # Should be ignored
    'metric_d': 4.6,
    'temp_var_x': -1.2  # Invalid due to sign
}

weights = {'metric_a': 0.2, 'metric_b': 0.3, 'metric_c': 0.1, 'metric_d': 0.4}

# Secondary distractor: complex set operations with no impact
domain_keys = set(name for name in feedback_map.keys() if 'metric_' in name)
shadow_weights = {k: v*1.1 for k, v in weights.items()}
excluded = domain_keys - set(weights.keys())
expanded = domain_keys | {'metric_e', 'metric_f'}

# Use of zip and enumerate in misleading context
correlation_map = {}
for i, (k, w) in enumerate(zip(sorted(feedback_map.keys()), [0.1]*len(feedback_map))):
    correlation_map[k] = w * (i + 1)

# Real aggregation logic buried in distraction
def aggregate_performance(scores, weight_map):
    # Extract only valid metrics present in both
    valid_metrics = set(scores.keys()) & set(weight_map.keys())
    
    # Debug decoy (unused)
    diagnostics = {key: {'raw': scores[key], 'weight': weight_map[key]} for key in valid_metrics}
    
    # Core computation
    total_weighted = 0
    total_weight = 0
    
    for metric in valid_metrics:
        if scores[metric] >= 0:  # Filter negative values
            weight = weight_map[metric]
            total_weighted += scores[metric] * weight
            total_weight += weight
    
    # Final score calculation
    final_score = total_weighted / total_weight if total_weight > 0 else 0
    
    # Irrelevant post-processing
    if final_score > 4.0:
        category = 'excellent'
    elif final_score > 3.0:
        category = 'good'
    else:
        category = 'needs_improvement'
    
    # Additional noise
    summary_stats = {
        'count': len(valid_metrics),
        'max_contrib': max((scores[m] * weight_map[m] for m in valid_metrics), default=0),
        'sparsity': len(excluded) / len(domain_keys) if domain_keys else 0
    }
    
    return final_score

# Call the real function
final_score = aggregate_performance(feedback_map, weights)

# Print result as required
print(f"Result: {final_score}")