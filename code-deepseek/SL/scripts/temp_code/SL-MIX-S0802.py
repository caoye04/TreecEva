inventory_items = ['widget_a', 'widget_b', 'widget_c', 'widget_d']
item_quantities = [15, 23, 8, 42]
threshold = 20

result_values = []
for item, quantity in zip(inventory_items, item_quantities):
    if quantity > threshold:
        result_values.append(quantity * 2)
    else:
        result_values.append(quantity)

# Calculate final total
final_total = sum(result_values)
print(f"Result: {final_total}")