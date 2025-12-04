def apply_discount(price, discount_type):
    if discount_type == "seasonal":
        return price * 0.75
    elif discount_type == "clearance":
        return price * 0.5
    elif discount_type == "member":
        return price * 0.9
    return price

def calculate_shipping_cost(weight, distance):
    base_rate = 5
    weight_factor = weight * 0.1
    distance_factor = distance * 0.05
    return base_rate + weight_factor + distance_factor

def calculate_inventory_value(inventory, priority_items):
    total_value = 0
    potential_revenue = 0
    shipping_costs = 0
    warehouse_capacity = 1000
    warehouse_used = sum(item['quantity'] for item in inventory.values())
    
    # Track items with quantity below threshold
    low_stock_items = {}
    for item_id, details in inventory.items():
        if details['quantity'] < 5:
            low_stock_items[item_id] = details['quantity']
    
    # Calculate weight distribution for shipping optimization
    weight_distribution = {}
    for item_id, details in inventory.items():
        weight_class = details['weight'] // 5
        if weight_class not in weight_distribution:
            weight_distribution[weight_class] = 0
        weight_distribution[weight_class] += details['quantity']
    
    # Calculate value of inventory based on priority items
    for item_id, details in inventory.items():
        item_value = details['price'] * details['quantity']
        
        # Apply seasonal discount to calculate potential revenue
        discounted_price = apply_discount(details['price'], "seasonal")
        potential_revenue += discounted_price * details['quantity']
        
        # Calculate shipping costs for all items
        item_shipping = calculate_shipping_cost(details['weight'], 100)
        shipping_costs += item_shipping * details['quantity']
        
        # Only count items in priority list for the final value
        if item_id in priority_items:
            # Apply priority multiplier based on position in priority list
            priority_index = priority_items.index(item_id)
            priority_multiplier = 1 + (len(priority_items) - priority_index) * 0.1
            total_value += item_value * priority_multiplier
    
    # Calculate storage efficiency
    storage_efficiency = (warehouse_used / warehouse_capacity) * 100
    if storage_efficiency > 80:
        # Storage penalty for overcrowded warehouse
        total_value *= 0.95
    
    # Apply tax adjustment
    tax_rate = 0.08
    total_value *= (1 + tax_rate)
    
    return round(total_value, 2)

# Inventory data
inventory = {
    "A101": {"price": 25.99, "quantity": 15, "weight": 2},
    "B202": {"price": 10.50, "quantity": 8, "weight": 1},
    "C303": {"price": 5.75, "quantity": 3, "weight": 0.5},
    "D404": {"price": 99.99, "quantity": 2, "weight": 10},
    "E505": {"price": 49.95, "quantity": 6, "weight": 5}
}

# Priority items for special valuation
priority_items = ["B202", "E505", "A101"]

# Calculate projected sales based on previous month
previous_month_sales = {
    "A101": 12,
    "B202": 7,
    "C303": 9,
    "D404": 1,
    "E505": 4
}

# Project next month inventory needs
projected_inventory = {}
for item_id, details in inventory.items():
    if item_id in previous_month_sales:
        projected_inventory[item_id] = max(0, details['quantity'] - previous_month_sales[item_id])

# Calculate customer satisfaction index
customer_ratings = {
    "A101": 4.5,
    "B202": 4.8,
    "C303": 3.9,
    "D404": 4.2,
    "E505": 4.7
}
satisfaction_index = sum(customer_ratings.values()) / len(customer_ratings)

# Calculate final inventory value
final_stock = calculate_inventory_value(inventory, priority_items)
print(f"Result: {final_stock}")