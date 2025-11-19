from collections import defaultdict

bakery_sales = defaultdict(int)
bakery_sales['croissants'] = 12
bakery_sales['muffins'] = 5

discount_batch_triggered = bakery_sales['croissants'] + bakery_sales['muffins'] >= 10 and bakery_sales['croissants'] < 15

result = 1 if discount_batch_triggered else 0
print(f'Result: {result}')