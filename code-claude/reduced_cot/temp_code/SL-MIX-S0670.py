def analyze_inventory(items):
    # Initialize tracking variables
    total_value = 0
    item_count = 0
    max_price = 0
    checksum = 0
    
    # Process inventory items
    for item_id, details in items.items():
        # Calculate item metrics
        price = details['price']
        quantity = details.get('quantity', 0)
        category_code = ord(details['category'][0])
        
        # Update tracking variables
        item_value = price * quantity
        total_value += item_value
        item_count += 1
        max_price = max(max_price, price)
        
        # Build checksum from item properties
        if quantity > 0:
            checksum += (price * category_code) & 0xFF
        
        # Apply discount for special items
        if 'discount' in details and quantity >= 5:
            total_value -= item_value * details['discount']
    
    # Calculate inventory health score (not used in final result)
    inventory_score = (total_value / max(1, item_count)) * (1 + (max_price / 1000))
    
    # Generate hash based on inventory properties
    base_hash = (item_count * 17) ^ (int(total_value) & 0xFF)
    modifier = (max_price > 500) * 23
    current_hash = (base_hash + modifier) | (item_count << 2)
    
    # Final hash calculation
    final_hash = (current_hash ^ (checksum & 0xFF)) % 1000
    
    return {
        "total_value": total_value,
        "item_count": item_count,
        "inventory_score": inventory_score,
        "hash": final_hash
    }

# Inventory data
inventory = {
    "A101": {"price": 150, "quantity": 3, "category": "Electronics"},
    "B202": {"price": 75, "quantity": 8, "category": "Books", "discount": 0.1},
    "C303": {"price": 450, "quantity": 2, "category": "Furniture"},
    "D404": {"price": 25, "quantity": 0, "category": "Stationery"}
}

# Analyze inventory and print result
result = analyze_inventory(inventory)
print(f"Result: {result['hash']}")