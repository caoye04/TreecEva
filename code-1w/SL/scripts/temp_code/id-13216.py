def calculate_crop_yield():
    base_yields = [85, 92, 78, 96, 88]
    growth_factors = [1.1, 0.95, 1.05, 0.9, 1.15]
    adjustments = [-3, 2, -1, 4, -2]
    
    # Apply growth factors using element-wise multiplication with zip
    projected_yields = [yield_val * factor for yield_val, factor in zip(base_yields, growth_factors)]
    
    # Adjust yields based on field conditions
    adjusted_yields = [int(projected + adj) for projected, adj in zip(projected_yields, adjustments)]
    
    # Irrelevant distraction: count how many fields have above-average base yield
    avg_base = sum(base_yields) / len(base_yields)
    high_performers = [1 for y in base_yields if y > avg_base]  # Unused variable
    
    total_harvest = sum(adjusted_yields)
    print(f"Result: {total_harvest}")

calculate_crop_yield()