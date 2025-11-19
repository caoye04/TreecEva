prices = {'croissant': 2.5, 'baguette': 3.0, 'muffin': 1.5}

# Daily sales data: [croissants_sold, baguettes_sold, muffins_sold]
daily_sales = [
    [10, 5, 8],
    [0, 7, 6],
    [12, 8, 10],
    [5, 0, 3],
    [9, 6, 7]
]

calculate_revenue = lambda sales: sum(sales[i] * prices[item] 
                                      for i, item in enumerate(['croissant', 'baguette', 'muffin']))

all_items_sold_days = set(range(len(daily_sales)))
for day_idx, sales in enumerate(daily_sales):
    if 0 in sales:
        all_items_sold_days.discard(day_idx)

revenue_all_items_days = 0
for day in all_items_sold_days:
    revenue_all_items_days += calculate_revenue(daily_sales[day])

print(f"Result: {revenue_all_items_days}")