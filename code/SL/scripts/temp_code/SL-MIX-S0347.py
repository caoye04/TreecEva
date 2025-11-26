inventory_tracker = {"apples": 42, "oranges": 28, "bananas": 15, "grapes": 33}
stock_check = len(inventory_tracker)
fruit_categories = list(inventory_tracker.keys())
final_quantity = inventory_tracker["apples"] + inventory_tracker["oranges"] - inventory_tracker["bananas"]
print(f"Result: {final_quantity}")