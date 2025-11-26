def process_inventory(items):
    # Distractor: calculate total items (not used in final result)
    total_items = sum(items.values())
    
    # Main logic: filter items with quantity > 5
    filtered_items = {k: v for k, v in items.items() if v > 5}
    
    # Distractor: create a sorted list of keys (not used directly)
    sorted_keys = sorted(filtered_items.keys())
    
    # Apply lambda function to process quantities
    process_quantity = lambda x: x * 2 - 3
    processed_data = {k: process_quantity(v) for k, v in filtered_items.items()}
    
    # Distractor: calculate average (not used in final result)
    avg_quantity = sum(processed_data.values()) / len(processed_data) if processed_data else 0
    
    # Key slicing operation to get specific keys
    filtered_keys = list(processed_data.keys())[1:3]
    
    # Final target calculation
    final_quantity = processed_data[filtered_keys[1]]
    
    # Distractor: additional unused calculation
    potential_max = max(processed_data.values()) if processed_data else 0
    
    print(f"Result: {final_quantity}")
    return final_quantity

# Main execution
inventory = {
    'widget_a': 8,
    'widget_b': 3,
    'widget_c': 12,
    'widget_d': 6,
    'widget_e': 15
}

result = process_inventory(inventory)
print(f"Target result: {result}")