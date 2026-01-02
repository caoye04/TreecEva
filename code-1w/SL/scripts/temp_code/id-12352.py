def calculate_cargo_load():
    items = ['engine', 'battery', 'sensor', 'actuator']
    base_weights = [320, 145, 23, 89]
    conditions = [0.9, 1.0, 0.95, 1.1]
    
    # Apply environmental adjustment factors
    adjusted_weights = []
    for i, (name, weight) in enumerate(zip(items, base_weights)):
        adjusted = weight * conditions[i]
        if adjusted > 100:
            adjusted_weights.append(round(adjusted))
        else:
            adjusted_weights.append(int(adjusted + 5))  # Minor calibration
    
    total_weight = sum(adjusted_weights)
    return total_weight

result = calculate_cargo_load()
print(f"Result: {result}")