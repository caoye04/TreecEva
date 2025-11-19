from itertools import permutations

def count_cookie_arrangements():
    cookie_types = ['chocolate_chip', 'oatmeal_raisin', 'sugar']
    arrangements = list(permutations(cookie_types, 2))
    return len(arrangements)

arrangements_count = count_cookie_arrangements()
print(f'Result: {arrangements_count}')