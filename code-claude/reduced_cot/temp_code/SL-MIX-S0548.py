# Analyzing common elements between two student groups

# First student group's preferred programming languages
group_a = ['Python', 'Java', 'JavaScript', 'C++', 'Ruby']

# Second student group's preferred programming languages
group_b = ['Java', 'Python', 'C#', 'PHP', 'Go']

# Extract languages starting with 'J' from group_a
j_languages = [lang for lang in group_a if lang.startswith('J')]

# Convert lists to sets for set operations
set_a = set(group_a)
set_b = set(group_b)

# Calculate statistics
total_unique = len(set_a.union(set_b))
multiplier = 3

# Find number of common elements and apply multiplier
common_elements = len(set_a.intersection(set_b)) * multiplier

# Calculate difference - languages in group_a but not in group_b
unique_to_a = len(set_a - set_b)

print(f"Result: {common_elements}")