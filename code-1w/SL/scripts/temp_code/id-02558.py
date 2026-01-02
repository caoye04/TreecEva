def calculate_inventory_status():
    initial_stock = 987
    shipments = [45, 67, 23]
    returns = [12, 8]
    
    # Process incoming and outgoing units
    total_shipped = sum(shipments)
    total_returned = sum(returns)
    current_stock = initial_stock - total_shipped + total_returned
    
    # Simulate warehouse audit adjustments using slicing
    audit_log = [10, -5, 3, -2, 8]
    recent_adjustments = audit_log[-3:]  # Focus on last three adjustments
    net_adjustment = sum(recent_adjustments)
    adjusted_stock = current_stock + net_adjustment
    
    # Track reserved units for pending orders
    pending_orders = [5, 10, 15]
    reserved_units = sum([order for order in pending_orders if order > 7])  # List comprehension
    
    # Final available inventory
    safety_threshold = 200
    stock_above_threshold = adjusted_stock > safety_threshold
    final_stock = adjusted_stock if stock_above_threshold else safety_threshold
    
    inventory_balance = final_stock - reserved_units
    return inventory_balance

result = calculate_inventory_status()
print(f"Result: {result}")