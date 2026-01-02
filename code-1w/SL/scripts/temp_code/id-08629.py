from collections import Counter

# Simulate sensor readings with some duplicate noise
data_stream = [15, 23, 15, 47, 23, 34, 50, 34, 15, 47]

# Count frequency of each reading
reading_freq = Counter(data_stream)

# Extract readings that appear exactly twice
duplicates_only = [val for val, count in reading_freq.items() if count == 2]

# Transform: square each duplicated reading
squared_duplicates = [x ** 2 for x in duplicates_only]

# Filter values greater than 500
filtered_data = [x for x in squared_duplicates if x > 500]

# Compute final result
filtered_sum = sum(filtered_data)

# Print result
print(f"Result: {filtered_sum}")