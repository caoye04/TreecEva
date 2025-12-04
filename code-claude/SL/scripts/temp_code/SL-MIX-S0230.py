def calculate_inventory_value(inventory, priority_items):
    total = 0
    discount_factor = 0.85
    tax_rate = 0.07
    
    # Sort items by price for analytics (not used in calculation)
    sorted_items = sorted(inventory.items(), key=lambda x: x[1]['price'], reverse=True)
    premium_threshold = sorted_items[0][1]['price'] * 0.75
    
    # Process each inventory item
    for item_id, details in inventory.items():
        quantity = details['quantity']
        price = details['price']
        
        # Calculate base value
        item_value = quantity * price
        
        # Apply priority multiplier if applicable
        if item_id in priority_items:
            priority_index = priority_items.index(item_id) + 1
            # Only odd-indexed priorities get a boost
            if priority_index % 2 == 1:
                item_value *= 1.1
        
        # Track premium items separately (for reporting purposes only)
        premium_items_count = 0
        if price > premium_threshold:
            premium_items_count += 1
            
        # Apply seasonal adjustment (currently inactive)
        seasonal_factor = 1.0
        # season = "winter"  # Uncomment to activate seasonal adjustment
        # if season == "winter":
        #     seasonal_factor = 1.15
        
        # Add to total (ignoring seasonal factor for now)
        total += item_value
    
    # Format for display (not used in calculation)
    display_string = f"Inventory Value: ${total:.2f}"
    
    # Final calculation with tax adjustment
    # Note: We apply discount before tax as per company policy
    discounted_value = total * discount_factor
    final_value = discounted_value * (1 + tax_rate)
    
    return round(final_value)

# Inventory data
inventory = {
    'A101': {'quantity': 5, 'price': 120},
    'B202': {'quantity': 10, 'price': 85},
    'C303': {'quantity': 3, 'price': 250},
    'D404': {'quantity': 7, 'price': 65}
}

# Priority items for special handling
priority_items = ['C303', 'A101', 'D404']

# Calculate the final inventory value
total_stock = calculate_inventory_value(inventory, priority_items)
print(f"Result: {total_stock}")