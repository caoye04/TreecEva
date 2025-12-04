# Analyze overlapping research domains between two academic groups
research_group_a = {'bioinformatics', 'computational_biology', 'machine_learning', 'data_science'}
research_group_b = {'computational_biology', 'genomics', 'machine_learning', 'statistics'}

# Find common research interests
common_interests = research_group_a.intersection(research_group_b)
print(f"Common research areas: {common_interests}")

# Calculate overlap count
overlap_count = len(common_interests)

# Identify unique research domains for group a
unique_to_a = research_group_a - research_group_b
print(f"Unique to group A: {unique_to_a}")

# Find remaining items after processing
remaining_items = research_group_a.symmetric_difference(research_group_b)
final_count = len(remaining_items)

print(f"Target result: {final_count}")