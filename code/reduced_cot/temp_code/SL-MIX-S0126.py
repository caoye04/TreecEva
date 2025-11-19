monday_sales = {'croissants', 'bagels', 'muffins'}
tuesday_sales = {'muffins', 'scones', 'donuts'}
combined_sales = monday_sales.union(tuesday_sales)
total_unique_items = len(combined_sales)
print(f'Result: {total_unique_items}')