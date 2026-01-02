def calculate_cargo_load():
    base_weights = [120, 200, 150, 180, 130]
    adjustments = [0.9, 1.1, 1.0, 0.95, 1.05]
    
    # Apply adjustment factors using zip
    adjusted_weights = []
    for weight, adj in zip(base_weights, adjustments):
        adjusted_weights.append(weight * adj)
    
    # Minor distraction: counting valid categories
    valid_count = 0
    threshold = 150
    for w in adjusted_weights:
        if w >= threshold:
            valid_count += 1
    
    total_weight = sum(adjusted_weights)
    
    # Additional irrelevant counter
    index_sum = 0
    for i, _ in enumerate(adjusted_weights):
        index_sum += i
    
    print(f"Result: {total_weight}")

calculate_cargo_load()