def analyze_warehouse_capacity(inventory_levels, storage_units, efficiency_rating):
    # Calculate base capacity from inventory and storage units
    total_inventory = sum(inventory_levels)
    avg_inventory = total_inventory / len(inventory_levels) if inventory_levels else 0
    
    # Track maximum inventory level for reference
    max_inventory = max(inventory_levels) if inventory_levels else 0
    historical_max = max_inventory * 1.2  # Historical buffer (not directly used)
    
    # Calculate storage efficiency
    utilized_units = sum(1 for level in inventory_levels if level > 0)
    efficiency_factor = utilized_units / storage_units if storage_units > 0 else 0
    
    # Potential expansion metric (distractor)
    expansion_metric = (total_inventory / storage_units) * 0.85 if storage_units > 0 else 0
    
    # Determine minimum capacity based on current inventory
    base_multiplier = 1.5
    min_capacity = int(total_inventory * base_multiplier)
    
    # Calculate adjusted capacity based on efficiency and utilization
    utilization_penalty = 100 if efficiency_factor < 0.5 else 0
    seasonal_adjustment = 50 if max_inventory > avg_inventory * 2 else 25
    
    # Compute adjusted capacity with various factors
    adjusted_capacity = int(total_inventory * (1 + efficiency_factor)) - utilization_penalty + seasonal_adjustment
    
    # Determine optimal warehouse capacity
    optimal_capacity = max(min_capacity, adjusted_capacity) if efficiency_factor > 0.75 else min_capacity
    
    # Apply regional modifier (distractor)
    regional_factor = 0.95
    regional_capacity = int(optimal_capacity * regional_factor)
    
    return optimal_capacity

# Test with sample data
inventory_data = [120, 85, 0, 210, 45]
storage_unit_count = 6
efficiency_score = 0.8

result = analyze_warehouse_capacity(inventory_data, storage_unit_count, efficiency_score)
print(f"Result: {result}")