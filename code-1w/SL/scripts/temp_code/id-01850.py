def calculate_performance(flags, data):
    base = len(data)
    adjustments = 0
    
    # Analyze flag conditions using set operations
    critical_flags = {'optimize', 'validate', 'secure'}
    active_critical = flags & critical_flags
    adjustments += len(active_critical) * 2
    
    # Process metric values with dictionary and arithmetic
    valid_metrics = {k: v for k, v in data.items() if v > 0}
    total = sum(valid_metrics.values())
    
    # Apply string-based rule on concatenated keys
    key_pattern = ''.join(sorted(valid_metrics.keys()))
    if 'cfg' in key_pattern:
        adjustments += 3
    
    result = total + adjustments - base
    return result

# Input construction
bonus_flags = {'debug', 'optimize', 'log', 'secure'}
metrics = {
    'cfg_init': 8,
    'load_time': 5,
    'memory_use': -2,
    'cfg_cache': 4
}

# Execution point of interest
final_score = calculate_performance(bonus_flags, metrics)
print(f"Result: {final_score}")