import itertools

def analyze_pattern(sequence):
    # Irrelevant analysis function (dead weight)
    freq = {}
    for item in sequence:
        freq[item] = freq.get(item, 0) + 1
    return {k: v for k, v in freq.items() if v > 1}

def validate_stability(metric):
    # Misleading stability check (not used in final logic)
    if metric < 0:
        return False
    temp = metric * 0.95
    return temp > 1e-3

def optimize_distribution(resources, limits):
    # Core logic embedded with distractions
    sorted_keys = sorted(resources.keys())
    accumulated = 0
    overflow_tracker = []
    
    # Real logic starts here
    filtered = [k for k in sorted_keys if resources[k] > limits.get(k, 0)]
    
    # Distractor: unused intermediate computation
    squared_sums = sum(x**2 for x in resources.values() if x < 50)
    temp_result = list(itertools.combinations(filtered, 2))
    
    adjustment_factor = len(temp_result) if len(temp_result) < 10 else 5
    
    for key in filtered:
        base = resources[key]
        limit = limits.get(key, 10)
        excess = base - limit
        if excess > 0:
            # Only this accumulation matters
            accumulated += excess // 2
            overflow_tracker.append(excess % 2)
    
    # Final meaningful calculation
    final_capacity = accumulated + adjustment_factor
    
    # More red herring operations
    padding = sum(overflow_tracker) * 0.5
    final_capacity += padding  # This has minimal effect due to integer context
    
    # Spurious sorting and slicing
    dummy_list = [final_capacity + i for i in range(-3, 4)]
    midpoint_slice = dummy_list[2:-2]
    smoothed = sum(midpoint_slice) / len(midpoint_slice)
    
    # But answer remains based on original final_capacity before smoothing
    return int(final_capacity)

# Main execution block
resource_map = {
    'node_a': 85,
    'node_b': 42,
    'node_c': 67,
    'node_d': 33,
    'node_e': 91
}

constraints = {
    'node_a': 50,
    'node_c': 60,
    'node_e': 80
}

# Unused data structures to increase cognitive load
baseline_profile = [analyze_pattern(['A','B','A','C','B','B'])]
system_metric = 42.7
is_stable = validate_stability(system_metric)

# Key statement
final_capacity = optimize_distribution(resource_map, constraints)

# Output result as required
print(f"Result: {final_capacity}")