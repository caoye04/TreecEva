def analyze_inventory(items, categories):
    # Calculate some statistics about inventory
    total_items = len(items)
    category_count = len(categories)
    
    # Extract values from inventory items
    inventory_values = []
    for item in items:
        # Apply a discount factor based on item position
        position_factor = (items.index(item) % 3) + 1
        adjusted_value = item['value'] * position_factor
        
        # Track original value for later calculations
        inventory_values.append(item['value'])
    
    # Calculate average value (not used in final result)
    avg_value = sum(inventory_values) / len(inventory_values) if inventory_values else 0
    
    # Apply some transformations to inventory values
    transformed_values = list(map(lambda x: x + 5, inventory_values))
    
    # Filter even values and sum them
    filtered_sum = sum(list(filter(lambda x: x % 2 == 0, inventory_values)))
    
    # Calculate a weighted score based on categories (not used in final result)
    category_weight = sum([len(c) for c in categories]) / category_count if category_count else 0
    weighted_score = avg_value * category_weight
    
    print(f"Result: {filtered_sum}")
    return filtered_sum

# Sample inventory data
items = [
    {'name': 'Widget A', 'value': 12},
    {'name': 'Widget B', 'value': 7},
    {'name': 'Widget C', 'value': 14},
    {'name': 'Widget D', 'value': 9},
    {'name': 'Widget E', 'value': 6}
]

categories = ['electronics', 'tools', 'office']

# Run the analysis
result = analyze_inventory(items, categories)