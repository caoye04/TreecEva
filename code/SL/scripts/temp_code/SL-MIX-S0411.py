import itertools

# Initialize dataset for processing
mixed_values = [5, 12, 8, 18, 7, 15, 9, 21, 6, 24]

# Apply filtering conditions using conditional expressions
filter_condition = lambda x: x % 3 == 0 and x > 10
final_filtered = [x for x in mixed_values if x % 3 == 0 and x > 10]

# Calculate the result
filtered_count = len(final_filtered)

# Additional processing steps (for context)
remaining_values = [x for x in mixed_values if x not in final_filtered]
remaining_sum = sum(remaining_values)

print(f"Result: {filtered_count}")