from itertools import permutations

# Define cookie types
cookies = ['chocolate_chip', 'oatmeal_raisin', 'sugar']

# Calculate all possible permutations of 2 cookies from the available types
cookie_permutations = list(permutations(cookies, 2))

# Using list comprehension to count the valid arrangements where no two same cookies are adjacent
valid_arrangements = [p for p in cookie_permutations if p[0] != p[1]]

total_arrangements = len(valid_arrangements)

print(f"Result: {total_arrangements}")