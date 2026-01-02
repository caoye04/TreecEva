from itertools import combinations

def analyze_subsystem_load(base_load, mode_flag):
    # Irrelevant load analysis (distractor)
    if mode_flag:
        adjusted = base_load * 1.15
    else:
        adjusted = base_load * 0.85
    return adjusted

def calculate_redundancy_score(n_components, criticality):
    score = 0
    for i in range(1, n_components + 1):
        score += i * (criticality % i if criticality > i else 1)
    return score

def optimize_system_allocation(resources, threshold, debug_mode=False):
    # Primary logic begins
    active_units = len(resources)
    baseline_efficiency = sum(resources) / active_units if active_units else 0
    
    # Distractor: Debug logging and irrelevant metrics
    debug_metrics = {}
    if debug_mode:
        debug_metrics['initial_mean'] = baseline_efficiency
        debug_metrics['peak_resource'] = max(resources) if resources else 0

    # Simulate subsystem loads (not directly used later)
    _ = [analyze_subsystem_load(r, True) for r in resources]

    # Key: Generate all possible pair allocations above threshold
    valid_pairs = []
    for pair in combinations(resources, 2):
        total_pair = pair[0] + pair[1]
        if total_pair > threshold:
            valid_pairs.append(total_pair)
    
    # Secondary distractor calculation
    redundancy = calculate_redundancy_score(active_units, len(valid_pairs))

    # Core logic: Accumulate excess capacity only from valid pairs
    excess_capacity = 0
    for vp in valid_pairs:
        if vp > threshold * 1.2:
            excess_capacity += vp - threshold

    # Final adjustment based on efficiency tier
    if baseline_efficiency > 75:
        scaling_factor = 1.3
    elif baseline_efficiency > 50:
        scaling_factor = 1.1
    else:
        scaling_factor = 0.9

    final_capacity = int((excess_capacity * scaling_factor) + redundancy) % 10000

    # This print is required for output visibility
    print(f"Result: {final_capacity}")
    
    return final_capacity

# Main execution
resource_pool = [68, 72, 45, 88, 53]
threshold_limit = 120
debug_flag = False

result = optimize_system_allocation(resource_pool, threshold_limit, debug_flag)