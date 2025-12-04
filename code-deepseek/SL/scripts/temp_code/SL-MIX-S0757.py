warehouse = {"widgets": 45, "gadgets": 32, "tools": 78, "supplies": 23}
item_count = len(warehouse)
category_names = list(warehouse.keys())
total_inventory = sum(warehouse.values())
print(f"Result: {total_inventory}")