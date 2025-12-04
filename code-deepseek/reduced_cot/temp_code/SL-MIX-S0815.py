inventory_data = {"apples": 15, "bananas": 8, "oranges": 12, "grapes": 6, "pears": 9}
threshold = 10
filtered_items = {}
for fruit, quantity in inventory_data.items():
    if quantity >= threshold:
        filtered_items[fruit] = quantity
processed_data = {"filtered_items": len(filtered_items), "total_items": len(inventory_data)}
final_count = processed_data.get("filtered_items", 0)
print(f"Result: {final_count}")