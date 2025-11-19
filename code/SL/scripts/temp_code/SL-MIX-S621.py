prices = {'croissants': 2, 'muffins': 3, 'scones': 4}
quantities = {
    'croissants': sum([x + 20 for x in range(2, 9, 2)]),
    'muffins': sum([x - 10 for x in range(9, 16, 2)]),
    'scones': sum([x for x in range(3, 13, 3)])
}
total_revenue = sum(prices[item] * quantities[item] for item in prices)
print(f'Target result: {total_revenue}')