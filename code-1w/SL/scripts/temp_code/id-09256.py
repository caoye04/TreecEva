def calculate_cargo_load():
    base_weights = [120, 180, 95, 210, 140]
    thresholds = {'light': 100, 'heavy': 200}
    
    # Apply adjustment: increase light items by 10%, reduce heavy ones by 5%
    adjusted_weights = []
    for weight in base_weights:
        if weight < thresholds['light']:
            adjusted_weights.append(weight * 1.1)
        elif weight > thresholds['heavy']:
            adjusted_weights.append(weight * 0.95)
        else:
            adjusted_weights.append(weight)
    
    total_weight = sum(adjusted_weights)
    
    # Irrelevant tracking variable (minimal distraction)
    item_count = len(base_weights)
    
    # Final output
    print(f"Result: {total_weight}")

calculate_cargo_load()