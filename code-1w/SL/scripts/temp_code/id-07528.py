def calculate_stock_delta(current_stock, new_orders, returned_items):
    supply_adjustment = new_orders if new_orders > 50 else new_orders * 0.9
    demand_correction = sum(returns) // 2 if sum(returns) > 30 else sum(returns)
    stock_delta = current_stock + supply_adjustment - demand_correction
    return stock_delta

# Initial data
current = 120
orders = 65
returns = [8, 12, 15]

# Critical execution point
inventory_balance = calculate_stock_delta(current, orders, returns)

print(f"Result: {inventory_balance}")