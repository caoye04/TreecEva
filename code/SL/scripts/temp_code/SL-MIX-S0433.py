inventory = {'apples': 15, 'oranges': 8, 'bananas': 12, 'grapes': 6, 'pears': 9}
item_names = list(inventory.keys())
filtered_items = [item for item in item_names if inventory[item] > 7]
processed_items = [item.upper() for item in filtered_items]
final_count = len(processed_items)
print(f"Result: {final_count}")