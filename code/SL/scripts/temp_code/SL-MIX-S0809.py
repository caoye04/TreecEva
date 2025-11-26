inventory = {'widgets': 45, 'gadgets': 78, 'tools': 23, 'parts': 91}
threshold = 50
filtered_items = {k: v for k, v in inventory.items() if v > threshold}
total_inventory = sum(filtered_items.values())
print(f"Result: {total_inventory}")