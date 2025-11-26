inventory_items = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew"]
filter_criteria = lambda x: len(x) >= 5
filtered_items = list(filter(filter_criteria, inventory_items))
category_sizes = [len(item) for item in filtered_items]
total_length = sum(category_sizes)
processed_items = len(filtered_items) * 2 - (total_length // 3)
final_count = processed_items
print(f"Result: {final_count}")