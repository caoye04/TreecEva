from collections import Counter

product_categories = ['electronics', 'books', 'clothing', 'electronics', 'books', 'electronics', 'toys', 'books']
category_counts = Counter(product_categories)
processed_items = []
for category, count in category_counts.items():
    if count >= 2:
        processed_items.append(count * 10 + len(category))
    else:
        processed_items.append(count * 5)
processed_items.sort()
final_count = processed_items[-1]
print(f"Result: {final_count}")