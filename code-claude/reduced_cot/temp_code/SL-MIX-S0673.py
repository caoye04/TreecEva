# Order processing system analysis

def calculate_stats(orders_data):
    # Process incoming orders data
    processed_orders = {}
    for order in orders_data:
        order_id = order["id"]
        processed_orders[order_id] = {
            "status": order["status"],
            "amount": order["amount"],
            "customer_tier": order["customer_tier"]
        }
    
    # Calculate average order value (not used in final result)
    total_value = 0
    for order_id, details in processed_orders.items():
        total_value += details["amount"]
    avg_order_value = total_value / len(processed_orders) if processed_orders else 0
    
    # Filter orders based on certain criteria
    priority_threshold = 150
    filtered_orders = {}
    for order_id, details in processed_orders.items():
        # Apply priority rules
        is_priority = details["amount"] > priority_threshold
        is_premium = details["customer_tier"] == "premium"
        
        # Calculate delivery estimate (not used in final calculation)
        delivery_days = 1 if is_priority or is_premium else 3
        
        # Only keep orders that are not cancelled
        if details["status"] != "cancelled":
            filtered_orders[order_id] = details
    
    # Count orders by status (including some unnecessary status tracking)
    status_counts = {"pending": 0, "shipped": 0, "delivered": 0, "returned": 0}
    for order_id, details in filtered_orders.items():
        status = details["status"]
        if status in status_counts:
            status_counts[status] += 1
    
    # Calculate result metrics
    total_valid_orders = sum(1 for order_id, details in filtered_orders.items() 
                           if details["status"] == "shipped")
    
    # Calculate some other metrics (not used in final result)
    premium_orders = sum(1 for order_id, details in filtered_orders.items() 
                        if details["customer_tier"] == "premium")
    
    return total_valid_orders

# Test with sample data
orders_data = [
    {"id": 101, "status": "shipped", "amount": 120, "customer_tier": "standard"},
    {"id": 102, "status": "pending", "amount": 85, "customer_tier": "standard"},
    {"id": 103, "status": "shipped", "amount": 250, "customer_tier": "premium"},
    {"id": 104, "status": "cancelled", "amount": 75, "customer_tier": "standard"},
    {"id": 105, "status": "delivered", "amount": 175, "customer_tier": "premium"},
    {"id": 106, "status": "shipped", "amount": 95, "customer_tier": "standard"},
    {"id": 107, "status": "returned", "amount": 200, "customer_tier": "premium"}
]

result = calculate_stats(orders_data)
print(f"Result: {result}")