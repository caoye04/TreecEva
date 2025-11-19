from collections import deque
from math import comb

def calculate_bundle_combinations(apple_pies, cherry_pies, bundle_size):
    queue = deque()
    total_combinations = 0
    
    # Generate all valid combinations of apple and cherry pies in a bundle
    for apples in range(min(bundle_size, apple_pies) + 1):
        cherries = bundle_size - apples
        if 0 <= cherries <= cherry_pies:
            # Calculate combinations for this distribution
            apple_ways = comb(apple_pies, apples)
            cherry_ways = comb(cherry_pies, cherries)
            total_combinations += apple_ways * cherry_ways
            queue.append((apples, cherries))
    
    return total_combinations

# Bakery order
apple_pie_count = 5
cherry_pie_count = 4
bundle_size = 3

# Calculate possible bundle combinations
distinct_bundles = calculate_bundle_combinations(apple_pie_count, cherry_pie_count, bundle_size)
print(f'Result: {distinct_bundles}')