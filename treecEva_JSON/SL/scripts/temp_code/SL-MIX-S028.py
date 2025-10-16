from itertools import combinations

monday_sales = {'croissants', 'danish', 'muffins'}
tuesday_sales = {'muffins', 'scones', 'croissants'}

unique_pastries = monday_sales.union(tuesday_sales)
unique_count = len(unique_pastries)

# Calculate number of ways to choose 2 items from the unique pastries
arrangements_count = len(list(combinations(unique_pastries, 2)))

print(f"Result: {arrangements_count}")