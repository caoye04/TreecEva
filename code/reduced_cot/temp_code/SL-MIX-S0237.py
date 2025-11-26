initial_inventory = 150
warehouse_capacity = 500
current_stock = initial_inventory - 45
incoming_shipment = 120 if warehouse_capacity - current_stock >= 100 else 80
urgent_orders = 35
final_quantity = current_stock + incoming_shipment - urgent_orders
print(f"Result: {final_quantity}")