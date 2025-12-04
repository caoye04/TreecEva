# Finding common elements between two temperature datasets after filtering

temperatures_a = [23.5, 22.1, 19.8, 25.0, 21.3, 20.7, 24.6]
temperatures_b = [22.1, 23.9, 20.7, 18.5, 25.0, 19.2, 21.3]

# Filter out temperatures below 21 degrees
filtered_a = [temp for temp in temperatures_a if temp >= 21.0]
filtered_b = [temp for temp in temperatures_b if temp >= 21.0]

# Find common temperatures in both datasets after filtering
common_elements = set(filtered_a) & set(filtered_b)

# Count the number of common elements
common_count = len(common_elements)

print(f"Result: {common_count}")