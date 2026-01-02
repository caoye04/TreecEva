def adjust_capacity(config, usage):
    base = config['initial']
    multiplier = config.get('dynamic', 1)
    threshold = config['threshold']

    load = sum(usage)
    if load > threshold:
        base *= multiplier
    
    adjustments = [val // 2 for val in usage if val > 10]
    total_adjustment = sum(adjustments)
    
    base += total_adjustment
    
    # Irrelevant string transformation (minimal distraction)
    status = "optimized".upper()
    status_check = len(status) > 5
    
    return base

# Configuration and data
base_config = {
    'initial': 150,
    'dynamic': 1.5,
    'threshold': 25
}

usage_levels = [8, 12, 15, 18]

# Execution
final_capacity = adjust_capacity(base_config, usage_levels)
print(f"Result: {final_capacity}")