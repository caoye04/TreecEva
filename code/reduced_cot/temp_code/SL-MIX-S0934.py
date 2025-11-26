item_prices = {"apple": 1.5, "banana": 0.8, "orange": 1.2, "grape": 2.5}
item_count = len(item_prices)
stock_limit = 6
threshold = 10

# Calculate final count based on stock limit
final_count = item_count if item_count <= stock_limit else stock_limit

print(f"Result: {final_count}")