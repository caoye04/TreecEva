from functools import reduce

daily_quantities = [8, 17, 12]
prices = [2, 3, 4]
discount_applied = daily_quantities[0] < 10 and daily_quantities[1] > 15
adjusted_muffin_price = prices[1] - (1 if discount_applied else 0)
total_revenue = reduce(lambda acc, pair: acc + pair[0] * pair[1], zip(daily_quantities, prices), 0) - (daily_quantities[1] if discount_applied else 0)

print(f"Result: {total_revenue}")