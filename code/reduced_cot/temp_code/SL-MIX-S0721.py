from collections import Counter

inventory_data = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple', 'grape']
category_mapping = {'apple': 'fruit', 'banana': 'fruit', 'orange': 'fruit', 'grape': 'fruit'}

item_counts = Counter(inventory_data)
processed_items = 0
for item, count in item_counts.items():
    if category_mapping[item] == 'fruit':
        processed_items += count

final_count = processed_items
print(f"Result: {final_count}")