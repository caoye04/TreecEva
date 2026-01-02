from collections import defaultdict

# Simulate a resource allocation system for distributed computing nodes
def calculate_load_score(node_weights, distribution):
    score = 0
    temp_adjustment = 0
    
    for node_id in distribution:
        raw_weight = node_weights.get(node_id, 1)
        allocation = distribution[node_id]
        if allocation > 5:
            temp_adjustment += allocation * 0.1
        score += (raw_weight * allocation) ** 0.5
    
    # Distractor computation - not used in final result
    redundancy_check = sum(distribution.values()) / (len(distribution) + 1e-8)
    return int(score - temp_adjustment)


def validate_constraints(resource_map, constraints):
    violations = 0
    debug_log = []
    total_available = sum(resource_map.values())
    
    for key, req in constraints.items():
        slice_key = key[:2]  # slicing operation
        base_node = key[0]
        expected_min = req * 0.8
        if resource_map[slice_key] < expected_min:
            violations += 1
            debug_log.append(f"Low: {slice_key}")
    
    # Dead code path (never executed due to logic above)
    if False and len(debug_log) > 10:
        reset_counter = defaultdict(int)
        for entry in debug_log:
            reset_counter[entry] += 1
    
    return violations == 0


def optimize_distribution(resource_map, constraints):
    temp_storage = {}
    intermediate_results = []
    
    # Initialize working copy
    work_dist = defaultdict(float)
    for k in resource_map:
        work_dist[k] = resource_map[k] * 0.5
    
    # Apply constraint-based scaling
    scale_factor = 1.0
    for ckey in constraints:
        if ckey in resource_map:
            scale_factor *= (constraints[ckey] / (resource_map[ckey] + 1))
    
    scale_factor = max(scale_factor, 0.5)
    
    # Main adjustment loop (nested logic)
    for i in range(2):
        for k in work_dist:
            if k in constraints:
                delta = constraints[k] - work_dist[k]
                adjustment = delta * scale_factor
                work_dist[k] += adjustment
    
    # Secondary distractor computation
    entropy_proxy = 0
    values = list(work_dist.values())
    for v in values:
        if v > 0:
            entropy_proxy -= v * (v + 1e-6)  # fake entropy calc
    
    # Final aggregation
    total_flow = sum(work_dist.values())
    avg_flow = total_flow / len(work_dist)
    peak_flow = max(work_dist.values())
    
    # Critical result computation
    stability_bonus = 1.0 if peak_flow / (avg_flow + 1e-8) < 1.5 else 0.8
    final_capacity = int((total_flow * stability_bonus) + 0.5)
    
    # Unused diagnostic metrics (distractors)
    sparsity_metric = len([v for v in work_dist.values() if v < 0.1])
    uniformity_score = (min(work_dist.values()) + 1) / (max(work_dist.values()) + 1)
    
    return final_capacity

# Setup problem instance
resource_map = {
    'ab': 12,
    'cd': 15,
    'ef': 8,
    'gh': 20
}

constraints = {
    'ab': 10,
    'cd': 14,
    'ef': 9,
    'gh': 18
}

# Execute main logic
node_weights = {'ab': 2, 'cd': 3, 'ef': 2, 'gh': 4}
distribution = {'ab': 6, 'cd': 7, 'ef': 5, 'gh': 8}
score = calculate_load_score(node_weights, distribution)

is_valid = validate_constraints(resource_map, constraints)
final_capacity = optimize_distribution(resource_map, constraints)

# Output target result
print(f"Target result: {final_capacity}")