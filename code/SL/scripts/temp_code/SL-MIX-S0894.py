item_counts = {'widget_a': 15, 'widget_b': 23, 'widget_c': 8}
backup_stock = {'widget_a': 5, 'widget_d': 12}
temp_calc = len(item_counts) * 2
for item in backup_stock:
    if item in item_counts:
        item_counts[item] += backup_stock[item]
    else:
        item_counts[item] = backup_stock[item]
final_count = sum(item_counts.values())
print(f"Result: {final_count}")