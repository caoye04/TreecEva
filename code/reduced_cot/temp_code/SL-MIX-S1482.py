from functools import reduce

dessert_prices = {'croissant': 3, 'muffin': 2, 'cake': 5}
sold_desserts = ['croissant', 'muffin', 'cake']
daily_counts = [10, 15, 8]

# Calculate daily revenue using map and reduce
daily_revenues = list(map(lambda item, count: dessert_prices[item] * count, sold_desserts, daily_counts))
total_revenue = reduce(lambda x, y: x + y, daily_revenues)

# Apply a recursive discount function for bulk purchases
def apply_discount(remaining_days, current_total):
    if remaining_days <= 0:
        return current_total
    return apply_discount(remaining_days - 1, current_total * 0.95)

# Apply discount for 7 days
final_revenue = apply_discount(7, total_revenue)

print(f'Result: {int(final_revenue)}')