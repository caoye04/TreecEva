data_points = [12, 15, 23, 34, 45, 56, 67, 78, 89]

# Irrelevant distraction: unused variable
unused_offset = 7

# Define a filter condition using a lambda function
criteria = lambda x: x % 3 == 0

# Apply filtering using set operations for uniqueness (even though input is unique)
unique_data = set(data_points)
filtered_data = [x for x in unique_data if criteria(x)]

# Perform summation on filtered results
filtered_sum = sum(filtered_data)

# Print result as required
print(f"Result: {filtered_sum}")