from itertools import combinations

# Available cookie cutters
cookie_cutters = ['Star', 'Heart', 'Circle', 'Square', 'Diamond', 'Triangle', 'Moon', 'Sun']

# Calculate all possible unique pairs
unique_pairs = list(combinations(cookie_cutters, 2))

# Count the number of unique pairs
pair_count = len(unique_pairs)

print(f'Result: {pair_count}')