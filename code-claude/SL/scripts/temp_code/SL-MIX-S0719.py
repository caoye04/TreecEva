from itertools import combinations

# Analyzing overlapping elements between consecutive data groups
data = [(1, 3, 5, 7), (3, 5, 9, 11), (5, 7, 9, 13), (7, 9, 11, 13)]
groups = [list(d) for d in data]  # Convert tuples to lists for processing

# Calculate some statistics about the data
total_elements = sum(len(g) for g in groups)
avg_value = sum(sum(g) for g in groups) / total_elements

# Find elements that appear in multiple groups
all_elements = set()
for group in groups:
    all_elements.update(group)

# Count elements appearing in each consecutive pair of groups
common_elements = sum(len(set(a) & set(b)) for a, b in zip(groups[:-1], groups[1:]))

# Additional analysis (not relevant to the main calculation)
pair_sums = [sum(pair) for pair in combinations(all_elements, 2)]
max_pair_sum = max(pair_sums) if pair_sums else 0

print(f"Result: {common_elements}")