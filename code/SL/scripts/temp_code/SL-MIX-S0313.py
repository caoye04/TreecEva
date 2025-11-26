item_count = {'books': 15, 'pens': 23, 'notebooks': 18}
category_sizes = {'small': 12, 'medium': 28, 'large': 16}
temp_total = sum(category_sizes.values())
processed_count = sum(item_count.values())
print(f"Result: {processed_count}")