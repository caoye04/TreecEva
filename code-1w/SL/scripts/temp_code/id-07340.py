from functools import reduce

# Inventory data for product codes and their stock counts
current_inventory = {"P100": 15, "P101": 8, "P102": 23, "P103": 4, "P104": 12}
reorder_threshold = 10

# Identify items below threshold using lambda
low_stock_check = lambda stock: stock < reorder_threshold
low_stock_items = list(filter(lambda code: low_stock_check(current_inventory[code]), current_inventory))

# Irrelevant distraction: counting characters in product codes
total_chars = sum(len(code) for code in current_inventory)

# Actual computation path
inventory_values = set(current_inventory.values())
above_threshold_values = {v for v in inventory_values if v >= reorder_threshold}

discount_factor = 0.9
adjusted_values = [int(v * discount_factor) for v in above_threshold_values]

# Key filtering operation based on adjusted values
filtered_items = [v for v in adjusted_values if v > 10]
filtered_sum = sum(filtered_items)

print(f"Result: {filtered_sum}")