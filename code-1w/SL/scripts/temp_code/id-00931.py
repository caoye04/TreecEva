def analyze_workload(data, base_limit):
    temp_results = []
    cumulative = 0
    peak_moment = None
    for i, entry in enumerate(data):
        load = entry['usage'] * entry['nodes']
        adjusted_load = load / (entry['efficiency'] or 1)
        
        # Irrelevant metric tracking
        if adjusted_load > base_limit * 2:
            temp_results.append({'index': i, 'overload': True})
        
        # Real accumulation
        cumulative += adjusted_load
        
        # Misleading conditional that doesn't affect final result
        if not peak_moment and adjusted_load > base_limit:
            peak_moment = i

    return cumulative


def calculate_stability(profile, limit):
    total_usage = analyze_workload(profile, limit)
    
    # Distractor: complex but unused calculation
    shadow_factor = sum([max(0, x['usage'] - limit) for x in profile])
    dummy_score = 100 * (shadow_factor / (total_usage or 1)) if total_usage else 0
    
    # Actual logic path
    valid_entries = [x for x in profile if x['efficiency'] > 0.5]
    high_efficiency_load = sum(x['usage'] for x in valid_entries)
    
    # Secondary distractor: dead code path
    if len(valid_entries) > 10:
        baseline = high_efficiency_load // len(valid_entries)
    else:
        baseline = 0  # never used
    
    # Core computation
    penalty = 0
    for entry in profile:
        if entry['nodes'] > 4:
            penalty += entry['usage'] * 0.1
    
    stabilized = total_usage - penalty + (high_efficiency_load * 0.05)
    
    # Final adjustment using slicing and conditional expression
    recent_slice = profile[-3:] if len(profile) >= 3 else profile
    recent_boost = sum(item['usage'] * 0.02 for item in recent_slice)
    
    result = stabilized + recent_boost
    
    # This is the key statement
    final_load = int(result) if result > 0 else 0
    return final_load

# Main execution data
system_log = [
    {'usage': 80, 'nodes': 3, 'efficiency': 0.8},
    {'usage': 120, 'nodes': 5, 'efficiency': 0.6},
    {'usage': 60, 'nodes': 2, 'efficiency': 0.9},
    {'usage': 200, 'nodes': 6, 'efficiency': 0.7},
    {'usage': 90, 'nodes': 4, 'efficiency': 0.55},
    {'usage': 110, 'nodes': 3, 'efficiency': 0.85},
    {'usage': 75, 'nodes': 1, 'efficiency': 0.95}
]

threshold = 100
final_load = calculate_stability(system_log, threshold)
print(f"Target result: {final_load}")