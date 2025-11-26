inventory_items = ['hammer', 'nails', 'saw', 'hammer', 'paint', 'nails', 'brush']
item_categories = {'hammer': 'tools', 'nails': 'fasteners', 'saw': 'tools', 'paint': 'supplies', 'brush': 'tools'}
unique_items = {item for item in inventory_items}
category_counts = {category: 0 for category in set(item_categories.values())}
for item in inventory_items:
    category = item_categories[item]
    category_counts[category] += 1
final_count = len(unique_items)
print(f"Result: {final_count}")