def calculate_network_load():
    base_weights = [12, 15, 8, 20, 17]
    scaling_factors = [0.5, 0.8, 1.2, 0.9, 1.1]
    
    # Apply scaling using zip and list comprehension
    scaled_weights = [w * s for w, s in zip(base_weights, scaling_factors)]
    
    # Adjust weights above threshold
    adjusted_weights = [w if w <= 14 else w * 0.95 for w in scaled_weights]
    
    # Minor distraction: unused variable (low interference)
    max_weight = max(scaled_weights)
    
    total_load = sum(adjusted_weights)
    print(f"Result: {total_load}")

calculate_network_load()