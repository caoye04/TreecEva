data_stream = [12, -7, 3, 15, -22, 9, 0, 44, -3, 8]

# Extract positive values using list comprehension and slicing
data_slice = data_stream[::2]
positive_only = [x for x in data_slice if x > 0]

# Perform set operations to remove duplicates (though none expected)
unique_values = list(set(positive_only))

# Apply a transformation: square each element
transformed = [x**2 for x in unique_values]

# Filter values greater than 100 using string conversion and length check
# This is a synthetic condition: treat number of digits as proxy for magnitude
digit_filtered = [x for x in transformed if len(str(x)) >= 3]

# Final summation
filtered_sum = sum(digit_filtered)

# Irrelevant distraction: unused variable with plausible name
temp_normalization_factor = max(transformed) / len(transformed) if transformed else 1

print(f"Result: {filtered_sum}")