def calculate_priority(items, target_item):
    base_value = 50
    multiplier = 1.5
    
    # Item weights based on rarity
    rarity_weights = {
        "common": 1,
        "uncommon": 2,
        "rare": 3,
        "epic": 4,
        "legendary": 5
    }
    
    # Calculate inventory diversity score (not used in final calculation)
    diversity_score = len(set([item["type"] for item in items.values()]))
    
    # Check if target item exists
    if target_item not in items:
        return 0
    
    item_data = items[target_item]
    quantity = item_data["quantity"]
    rarity = item_data["rarity"]
    
    # Apply weight based on item type (not relevant to final calculation)
    type_bonus = 5 if item_data["type"] == "consumable" else 2
    
    # Calculate usage frequency factor (not used in final priority)
    frequency_factor = min(item_data["usage_frequency"] * 0.8, 10)
    
    # Calculate priority
    if quantity <= 0:
        return 0
    elif rarity in rarity_weights and quantity > 0:
        weight = rarity_weights[rarity]
        raw_score = base_value * (weight / quantity) * multiplier
        priority_score = int(raw_score)
        return priority_score
    else:
        return base_value

# Game inventory with various items
inventory = {
    "health_potion": {"quantity": 3, "rarity": "uncommon", "type": "consumable", "usage_frequency": 8},
    "mana_potion": {"quantity": 5, "rarity": "common", "type": "consumable", "usage_frequency": 6},
    "sword": {"quantity": 1, "rarity": "rare", "type": "weapon", "usage_frequency": 12},
    "shield": {"quantity": 2, "rarity": "epic", "type": "armor", "usage_frequency": 7}
}

# Calculate priority scores for inventory management
sword_priority = calculate_priority(inventory, "sword")
shield_priority = calculate_priority(inventory, "shield")
mana_priority = calculate_priority(inventory, "mana_potion")

# Main priority calculation
priority_score = calculate_priority(inventory, "health_potion")

# Check if we need emergency supplies
emergency_threshold = 75
emergency_needed = any(calculate_priority(inventory, item) > emergency_threshold 
                      for item in ["health_potion", "mana_potion"])

print(f"Result: {priority_score}")