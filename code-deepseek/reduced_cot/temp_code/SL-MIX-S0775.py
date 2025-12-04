base_stock = [15, 8, 22, 5, 19]
threshold = 10
processed_items = [item * 2 if item > threshold else item + 3 for item in base_stock]
final_inventory = processed_items[-1]
print(f"Result: {final_inventory}")