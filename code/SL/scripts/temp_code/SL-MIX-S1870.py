from itertools import permutations
import re

def filter_arrangements(arrangements):
    return [arr for arr in arrangements if arr[0] != 'chocolate']

cookies = ['chocolate', 'vanilla', 'strawberry']
all_perms = list(permutations(cookies, 2))
valid_arrangements = filter_arrangements(all_perms)
number_of_valid_arrangements = len(valid_arrangements)
total_price = sum(10 * index + 5 for index in range(number_of_valid_arrangements))
print(f"Result: {total_price}")