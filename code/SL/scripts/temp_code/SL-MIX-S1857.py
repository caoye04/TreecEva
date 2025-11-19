from itertools import combinations

def get_average_price():
    cookie_prices = [1.50, 2.00, 2.50]
    arrangements = list(combinations(cookie_prices, 2))
    total_price = sum(sum(arrangement) for arrangement in arrangements)
    avg_price = total_price / len(arrangements)
    return avg_price

with open('bakery_log.txt', 'w') as f:
    avg_price = get_average_price()
    f.write(f'Average price: {avg_price}')

print(f'Result: {avg_price}')