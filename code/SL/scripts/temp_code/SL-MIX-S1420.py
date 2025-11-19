prices = {'croissant': 3.5, 'muffin': 2.0, 'scone': 2.5}
sales_counts = {'croissant': 20, 'muffin': 15, 'scone': 25}

item_revenues = {item: prices[item] * count for item, count in sales_counts.items()}
total_revenue = sum(item_revenues.values())
total_items_sold = sum(sales_counts.values())

is_weekend = total_items_sold > 50
final_revenue = total_revenue * (0.9 if is_weekend else 1.0)

print(f'Result: {final_revenue}')