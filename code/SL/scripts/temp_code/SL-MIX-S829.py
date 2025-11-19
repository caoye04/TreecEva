from collections import defaultdict

def compute_dynamic_price(initial_price, sales_threshold=10, increase_rate=0.1):
    return initial_price * (1 + increase_rate) if sales_threshold else initial_price

beverage_prices = {'coffee': 3.0, 'tea': 2.5, 'latte': 4.0}
beverage_sales_log = [
    {'coffee': 8, 'tea': 12, 'latte': 5},
    {'coffee': 15, 'tea': 7, 'latte': 11},
    {'coffee': 9, 'tea': 13, 'latte': 6},
    {'coffee': 11, 'tea': 4, 'latte': 14},
    {'coffee': 6, 'tea': 10, 'latte': 9}
]

for day_sales in beverage_sales_log:
    updated_prices = {}
    for bev, sales in day_sales.items():
        if sales > 10:
            updated_prices[bev] = beverage_prices[bev] * 1.1
    beverage_prices.update(updated_prices)

latte_price_on_sixth_day = beverage_prices['latte']
print(f"Result: {latte_price_on_sixth_day}")