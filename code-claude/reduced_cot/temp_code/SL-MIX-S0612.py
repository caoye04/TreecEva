def calculate_priority(items, category):
    # Calculate priority score for items in a specific category
    relevant_items = {}
    item_count = 0
    total_weight = 0
    
    # Extract items in the specified category
    for item_id, details in items.items():
        if details['category'] == category:
            relevant_items[item_id] = details
            item_count += 1
            
        # Track total weight for all items (not just category)
        total_weight += details['weight']
    
    # Calculate base score
    if not relevant_items:
        return 0
    
    # Get average value of items in category
    values = [item['value'] for item in relevant_items.values()]
    avg_value = sum(values) / len(values)
    
    # Get rarity factor based on how many items are in this category
    # compared to total items
    rarity_factor = 1.5 if item_count < len(items) / 3 else 1.0
    
    # Calculate priority based on value and rarity
    raw_priority = avg_value * rarity_factor
    
    # Adjust for weight (not actually used in final calculation)
    weight_adjustment = total_weight / 100
    adjusted_priority = raw_priority + weight_adjustment
    
    # Final priority is based on highest value item in category
    # plus average of all items in category
    max_value = max(values)
    priority_score = (max_value + avg_value) / 2
    
    return round(priority_score, 2)

# Sample inventory data
inventory = {
    'A001': {'name': 'Health Potion', 'category': 'HEALTH', 'value': 25, 'weight': 0.5},
    'A002': {'name': 'Mana Potion', 'category': 'MAGIC', 'value': 30, 'weight': 0.5},
    'B001': {'name': 'Iron Sword', 'category': 'WEAPON', 'value': 100, 'weight': 5.0},
    'B002': {'name': 'Leather Armor', 'category': 'ARMOR', 'value': 75, 'weight': 8.0},
    'C001': {'name': 'Healing Herb', 'category': 'HEALTH', 'value': 15, 'weight': 0.1},
    'C002': {'name': 'Bandages', 'category': 'HEALTH', 'value': 5, 'weight': 0.2}
}

# Calculate inventory statistics (not used in final calculation)
stat_data = {}
for item_id, item in inventory.items():
    cat = item['category']
    if cat not in stat_data:
        stat_data[cat] = {'count': 0, 'total_value': 0}
    stat_data[cat]['count'] += 1
    stat_data[cat]['total_value'] += item['value']

# Sort items by value (not used in final calculation)
sorted_items = sorted(inventory.items(), key=lambda x: x[1]['value'], reverse=True)
top_item = sorted_items[0][0] if sorted_items else None

# Calculate priority score for health items
priority_score = calculate_priority(inventory, "HEALTH")
print(f"Result: {priority_score}")