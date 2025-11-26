def calculate_inventory_metrics():
    # Product inventory analysis with dictionary operations
    inventory_data = {'A': 15, 'B': 8, 'C': 12, 'D': 6, 'E': 9}
    
    # Calculate initial metrics
    total_items = sum(inventory_data.values())
    average_stock = total_items / len(inventory_data)
    
    # Intermediate calculations (distractors)
    max_stock = max(inventory_data.values())
    min_stock = min(inventory_data.values())
    variance_factor = (max_stock - min_stock) ** 2
    
    # Create combination mappings
    unique_combinations = {}
    for key1 in inventory_data:
        for key2 in inventory_data:
            if key1 != key2:
                combo_key = f"{key1}{key2}"
                unique_combinations[combo_key] = inventory_data[key1] + inventory_data[key2]
    
    # Additional intermediate calculation (distractor)
    weighted_sum = sum(inventory_data[k] * 2 for k in inventory_data)
    
    # Target calculation
    combination_key = 'AC'
    adjustment_factor = 3
    final_count = unique_combinations[combination_key] + adjustment_factor
    
    print(f"Result: {final_count}")
    return final_count

calculate_inventory_metrics()