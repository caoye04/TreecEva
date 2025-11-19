from collections import Counter

daily_sales = Counter({'croissants': 8, 'muffins': 3, 'danish': 7, 'scones': 2, 'bagels': 9})
unique_popular_items = len({item for item, count in daily_sales.items() if count > 5})
print(f"Result: {unique_popular_items}")