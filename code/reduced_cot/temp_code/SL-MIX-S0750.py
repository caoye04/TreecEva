inventory_counts = [15, 23, 8, 42, 11]
processed_items = [item * 2 for item in inventory_counts[:3]]
enumerate_pairs = [idx * val for idx, val in enumerate(processed_items)]
total_quantity = sum(enumerate_pairs)
print(f"Result: {total_quantity}")