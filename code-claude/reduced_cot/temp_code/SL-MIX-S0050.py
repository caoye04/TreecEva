from collections import Counter

# Analyzing common interests between groups of friends
group_a = ['hiking', 'reading', 'cooking', 'photography', 'gaming']
group_b = ['cooking', 'photography', 'painting', 'hiking', 'dancing']
group_c = ['hiking', 'gaming', 'cooking', 'movies', 'travel']

# Find interests present in at least two groups
all_interests = group_a + group_b + group_c
interest_counts = Counter(all_interests)

# Collect interests that appear multiple times
shared_interests = [interest for interest, count in interest_counts.items() if count >= 2]

# Create sets for each group
set_a = set(group_a)
set_b = set(group_b)
set_c = set(group_c)

# Find interests common to all three groups
common_to_all = set_a.intersection(set_b, set_c)

# Find interests common to at least two groups using set operations
common_ab = set_a.intersection(set_b)
common_ac = set_a.intersection(set_c)
common_bc = set_b.intersection(set_c)

# Combine all common interests
common_interests = common_ab.union(common_ac, common_bc)

# Count how many unique interests are shared between at least two groups
unique_elements = len(common_interests)

print(f"Result: {unique_elements}")