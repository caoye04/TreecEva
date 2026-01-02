data = [15, -4, 8, 23, -11, 6, 19]
threshold = 5

# Irrelevant variable (minor distraction)
offset = 2

# List comprehension with enumerate: filtering even-indexed elements greater than threshold
even_indexed_filtered = [x for i, x in enumerate(data) if i % 2 == 0 and x > threshold]

# Additional irrelevant operation (low-level interference)
temp_result = [x * 2 for x in data if x < 0]

# Key computation step
filtered_sum = sum([x for i, x in enumerate(data) if i % 2 == 0 and x > threshold])

# Print final result as required
print(f"Result: {filtered_sum}")