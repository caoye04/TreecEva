def calculate_store_metrics(sales_data, inventory):
    # Process sales data to track popular items
    popular_items = {}
    for sale in sales_data:
        item_id = sale['item_id']
        quantity = sale['quantity']
        if item_id in popular_items:
            popular_items[item_id] += quantity
        else:
            popular_items[item_id] = quantity
    
    # Calculate potential revenue from top sellers (not used in final calculation)
    top_items = sorted(popular_items.items(), key=lambda x: x[1], reverse=True)[:3]
    potential_revenue = sum(inventory[item_id]['price'] * count for item_id, count in top_items if item_id in inventory)
    
    # Apply seasonal discount to inventory prices
    season = "summer"
    discount_factors = {"winter": 0.9, "summer": 0.85, "spring": 0.95, "fall": 0.92}
    discount = discount_factors.get(season, 1.0)
    
    # Process inventory with discount
    processed_inventory = {}
    for item_id, details in inventory.items():
        # Only apply discount to non-clearance items
        if details.get('clearance', False):
            processed_inventory[item_id] = details['price'] * details['quantity']
        else:
            processed_inventory[item_id] = details['price'] * discount * details['quantity']
    
    # Calculate inventory statistics
    avg_price = sum(details['price'] for details in inventory.values()) / len(inventory) if inventory else 0
    median_price = sorted([details['price'] for details in inventory.values()])[len(inventory)//2] if inventory else 0
    
    # Filter out items with low stock
    low_stock_threshold = 5
    final_inventory = {item_id: processed_inventory[item_id] for item_id in processed_inventory 
                      if inventory[item_id]['quantity'] > low_stock_threshold}
    
    # Calculate total inventory value
    inventory_value = sum(item_value for item_value in final_inventory.values())
    
    return {
        "total_value": inventory_value,
        "avg_price": avg_price,
        "potential_revenue": potential_revenue
    }

# Sample data
sales_data = [
    {"item_id": "A001", "quantity": 10},
    {"item_id": "B002", "quantity": 5},
    {"item_id": "C003", "quantity": 8},
    {"item_id": "A001", "quantity": 7},
    {"item_id": "D004", "quantity": 3}
]

inventory = {
    "A001": {"price": 20, "quantity": 15, "clearance": False},
    "B002": {"price": 30, "quantity": 10, "clearance": False},
    "C003": {"price": 15, "quantity": 4, "clearance": True},
    "D004": {"price": 25, "quantity": 8, "clearance": False}
}

result = calculate_store_metrics(sales_data, inventory)
print(f"Result: {result['total_value']}")