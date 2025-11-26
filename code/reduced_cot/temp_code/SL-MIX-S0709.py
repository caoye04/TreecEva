def analyze_inventory_rotation(items):
    # Track items that need rotation vs those that don't
    rotation_needed = []
    stable_items = []
    
    for idx, item in enumerate(items):
        if item % 3 == 0:
            rotation_needed.append((idx, item * 2))
        else:
            stable_items.append(item - 1)
    
    # Calculate primary metric (only uses rotation_needed)
    primary_total = 0
    for position, value in rotation_needed:
        primary_total += value * (position + 1)
    
    # Distractor calculations (not used in final result)
    secondary_metric = sum(stable_items)
    temp_adjustment = len(rotation_needed) * 5
    
    # Final computation with some irrelevant intermediate steps
    adjustment_factor = 7
    irrelevant_calc = secondary_metric - temp_adjustment
    
    primary_result = primary_total // 3
    final_output = primary_result + adjustment_factor
    
    print(f"Result: {final_output}")

# Test data
inventory_items = [4, 6, 8, 9, 12, 7, 15]
analyze_inventory_rotation(inventory_items)