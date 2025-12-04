from collections import defaultdict

warehouse = defaultdict(int)
warehouse['widget_a'] = 125
warehouse['widget_b'] = 87
warehouse['widget_c'] = 42
backup_stock = 50
reorder_threshold = 100

current_levels = [warehouse['widget_a'], warehouse['widget_b'], warehouse['widget_c']]
inventory_total = sum(warehouse.values())

print(f"Result: {inventory_total}")