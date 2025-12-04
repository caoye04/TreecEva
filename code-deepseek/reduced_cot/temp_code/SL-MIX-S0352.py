warehouse_stock = {'item_a': 45, 'item_b': 12, 'item_c': 78, 'item_d': 3, 'item_e': 56}
threshold = 15
backup_items = ['item_x', 'item_y', 'item_z']
stock_report = "Inventory Analysis Complete"
final_inventory_count = sum([stock for stock in warehouse_stock.values() if stock > threshold])
print(f"Result: {final_inventory_count}")