from itertools import combinations

cookie_flavors = ['chocolate', 'vanilla', 'strawberry', 'mint', 'caramel']
total_cookie_pairs = len(list(combinations(cookie_flavors, 2)))
print(f'Result: {total_cookie_pairs}')