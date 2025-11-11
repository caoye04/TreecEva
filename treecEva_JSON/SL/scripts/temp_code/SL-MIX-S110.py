import math
import itertools

def calculate_combination_rank(combo, all_combos):
    return all_combos.index(combo) + 1

# Generate all 3-letter combinations of lowercase English letters
letters = 'abcdefghijklmnopqrstuvwxyz'
combinations = list(itertools.combinations_with_replacement(letters, 3))

# Sort combinations lexicographically
combinations.sort()

# Calculate entropy sum
entropy_sum = 0
for combo in combinations:
    rank = calculate_combination_rank(combo, combinations)
    entropy_sum += math.log2(rank)

print(f"Result: {entropy_sum}")