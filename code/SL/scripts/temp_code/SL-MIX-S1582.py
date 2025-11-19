from itertools import combinations

# Cookie types in the weekend assortment
cookie_types = ['ChocolateChip', 'OatmealRaisin', 'SugarCookie', 'PeanutButter', 'Snickerdoodle', 'MacadamiaNut', 'WhiteChocolate', 'Gingerbread']

# Calculate unique pairs using combinations
unique_cookie_pairs = len(list(combinations(cookie_types, 2)))

print(f'Result: {unique_cookie_pairs}')