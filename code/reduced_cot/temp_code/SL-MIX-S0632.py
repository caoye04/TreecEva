initial_stock = 125
processed_orders = [15, 8, 22, 10, 5]
new_shipment = 75
current_stock = initial_stock - sum(processed_orders)
final_inventory = current_stock - processed_orders[2] + new_shipment
print(f"Result: {final_inventory}")