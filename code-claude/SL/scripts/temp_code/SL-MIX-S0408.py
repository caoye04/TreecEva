from collections import Counter

# Dataset of most frequent programming languages in two regions
region_a_langs = ['Python', 'JavaScript', 'Java', 'C++', 'PHP', 'Ruby', 'Python', 'JavaScript']
region_b_langs = ['JavaScript', 'Python', 'C#', 'TypeScript', 'Java', 'Go', 'JavaScript']

# Count occurrences of each language
lang_count_a = Counter(region_a_langs)
lang_count_b = Counter(region_b_langs)

# Languages that appear at least twice in their respective regions
popular_a = [lang for lang, count in lang_count_a.items() if count >= 2]
popular_b = [lang for lang, count in lang_count_b.items() if count >= 2]

# Convert to sets for comparison
set_a = set(popular_a)
set_b = set(popular_b)

# Unique languages in either region
unique_langs = len(set_a.symmetric_difference(set_b))

# Common languages between both regions that are popular
common_elements = len(set_a.intersection(set_b))

# Total distinct popular languages
total_distinct = len(set_a.union(set_b))

print(f"Result: {common_elements}")