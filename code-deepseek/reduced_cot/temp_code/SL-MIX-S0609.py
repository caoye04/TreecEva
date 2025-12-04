def analyze_inventory():
    inventory_data = [
        ('electronics', 'laptop', 15),
        ('electronics', 'phone', 23),
        ('furniture', 'chair', 8),
        ('electronics', 'tablet', 12),
        ('furniture', 'desk', 5),
        ('books', 'novel', 31)
    ]
    
    category_counts = {}
    temp_calculations = []
    
    for category, item, quantity in inventory_data:
        if category not in category_counts:
            category_counts[category] = 0
            temp_calculations.append(quantity * 2)  # Distractor - not used
        category_counts[category] += quantity
    
    target_category = 'electronics'
    multiplier = 3
    
    # Intermediate calculation that doesn't affect final result
    total_items = sum(category_counts.values())
    average_items = total_items // len(category_counts)
    
    final_count = category_counts.get(target_category, 0) * multiplier
    
    print(f"Result: {final_count}")

analyze_inventory()