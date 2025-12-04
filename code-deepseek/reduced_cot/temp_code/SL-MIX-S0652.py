items = [1, 3, 5, 2, 4]
weights = [10, 25, 15, 30, 20]
processed_items = [x * 2 for x in items]
item_count = len(items)
total_weight = sum([item[1] for item in zip(items, weights) if item[0] > 2])
print(f"Total weight: {total_weight}")