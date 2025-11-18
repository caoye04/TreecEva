from itertools import permutations, combinations

cake_flavors = ['chocolate', 'vanilla', 'strawberry']

# Calculate number of ways to arrange 3 flavors taken 2 at a time (order matters)
arrangement_count = len(list(permutations(cake_flavors, 2)))

# Custom combination function using lambda
calculate_combinations = lambda n, r: len(list(combinations(range(n), r)))

# Calculate combinations of 3 flavors taken 2 at a time (order doesn't matter)
combination_count = calculate_combinations(3, 2)

# Total arrangements is the sum of both counts
total_arrangements = arrangement_count + combination_count

print(f'Result: {total_arrangements}')