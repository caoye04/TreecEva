def calculate_discounted_price(inventory, item_name):
    base_prices = {'apple': 2.50, 'banana': 1.25, 'orange': 3.00, 'mango': 4.50, 'kiwi': 2.75}
    seasonal_discount = lambda x: x * 0.85 if x > 3.00 else x * 0.90
    loyalty_bonus = 0.05
    
    # Check if item exists in inventory
    if item_name not in inventory:
        return 0
    
    quantity = inventory.get(item_name, 0)
    alternative_items = {k: v for k, v in inventory.items() if k != item_name}
    total_alternatives = sum(alternative_items.values()) if alternative_items else 0
    
    # Calculate base price
    item_price = base_prices.get(item_name, 0)
    
    # Apply quantity discount
    bulk_factor = 0.95 if quantity > 10 else 1.0
    
    # Apply seasonal discount
    discounted_price = seasonal_discount(item_price)
    
    # Calculate shipping cost (not used in final calculation)
    shipping_cost = 5.0 if sum(inventory.values()) < 20 else 0
    
    # Calculate tax (not directly used)
    tax_rate = 0.08
    tax_amount = item_price * tax_rate
    
    # Calculate final price with all applicable discounts
    final_price = discounted_price * bulk_factor
    
    # Apply loyalty discount if applicable
    if total_alternatives >= 3:
        final_price = final_price * (1 - loyalty_bonus)
    
    return round(final_price * quantity, 2)

# Inventory and target item
inventory = {'apple': 15, 'banana': 8, 'kiwi': 5}
target_item = 'apple'

# Process some alternative scenarios (not affecting result)
potential_savings = {item: base_prices.get(item, 0) - (base_prices.get(item, 0) * 0.9) for item in inventory}
most_expensive = max(inventory.items(), key=lambda x: base_prices.get(x[0], 0) * x[1]) if inventory else None

# Calculate the final price
final_price = calculate_discounted_price(inventory, target_item)

print(f"Result: {final_price}")