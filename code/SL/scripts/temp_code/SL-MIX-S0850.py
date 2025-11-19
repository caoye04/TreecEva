from collections import defaultdict

daily_sales = defaultdict(int, {'croissants': 20, 'muffins': 15, 'scones': 25})
prices = {'croissants': 2, 'muffins': 3, 'scones': 4}
total_units = sum(daily_sales.values())
revenue = sum(daily_sales[item] * prices[item] for item in daily_sales)
final_revenue = revenue * 0.9 if total_units > 50 else revenue
print(f'Result: {final_revenue}')