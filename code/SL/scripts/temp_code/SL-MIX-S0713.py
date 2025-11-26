def analyze_inventory():
    inventory_data = {
        'electronics': {'items': 15, 'active': 12, 'pending': 3},
        'books': {'items': 23, 'active': 20, 'pending': 3},
        'clothing': {'items': 18, 'active': 15, 'pending': 3},
        'furniture': {'items': 7, 'active': 5, 'pending': 2}
    }
    
    # Distractor variables and calculations
    total_items = sum(category['items'] for category in inventory_data.values())
    processed_items = sum(category['active'] for category in inventory_data.values())
    temp_ratio = processed_items / total_items if total_items > 0 else 0
    
    # Main logic - find categories with more than 15 items and count their pending items
    inventory_categories = set(inventory_data.keys())
    large_categories = set()
    final_count = 0
    
    for category in inventory_categories:
        if inventory_data[category]['items'] > 15:
            large_categories.add(category)
            # Distractor operation that doesn't affect final_count
            temp_check = len(large_categories) * 2
    
    # Second iteration to calculate final result
    for category in large_categories:
        final_count += inventory_data[category]['pending']
        # Another distractor calculation
        verification_sum = final_count + len(large_categories)
    
    # Final distractor that looks relevant but isn't used
    category_analysis = {cat: inventory_data[cat]['active'] for cat in large_categories}
    
    print(f"Result: {final_count}")
    return final_count

# Execute the function
analyze_inventory()