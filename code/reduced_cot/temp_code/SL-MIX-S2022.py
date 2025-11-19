beverage_prices = {'espresso': 3.50, 'latte': 4.00, 'cappuccino': 3.75}
daily_sales = [
    {'espresso': 25, 'latte': 15, 'cappuccino': 30},
    {'espresso': 18, 'latte': 22, 'cappuccino': 10},
    {'espresso': 30, 'latte': 20, 'cappuccino': 25},
    {'espresso': 12, 'latte': 18, 'cappuccino': 20},
    {'espresso': 20, 'latte': 25, 'cappuccino': 15},
    {'espresso': 22, 'latte': 10, 'cappuccino': 28},
    {'espresso': 15, 'latte': 30, 'cappuccino': 18}
]

# Calculate daily revenues with dynamic discount
weekly_revenue = 0
for day_sales in daily_sales:
    day_revenue = 0
    for beverage, count in day_sales.items():
        price = beverage_prices[beverage]
        if count > 20:
            day_revenue += count * price * 0.95
        else:
            day_revenue += count * price
    weekly_revenue += day_revenue

print(f'Total weekly revenue: ${weekly_revenue:.2f}')
