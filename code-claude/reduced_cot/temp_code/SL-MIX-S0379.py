# Finding common elements between two datasets after filtering

def process_data(data_list):
    # Process the data with some transformations
    processed = [x * 2 if x % 2 == 0 else x - 1 for x in data_list]
    return processed

# Primary dataset
primary = [3, 8, 5, 12, 9, 4, 7]

# Secondary dataset with some noise
secondary = [8, 5, 14, 4, 9, 2, 8]

# Create sets for efficient operations
set_a = set(process_data(primary))
set_b = set(secondary)

# Track some additional metrics
total_elements = len(set_a) + len(set_b)
unique_elements = len(set_a.union(set_b))

# Count elements that appear in both datasets
overlap = set_a.intersection(set_b)

# Calculate potential duplicates based on a threshold
threshold = 3
duplicate_factor = min(len(overlap), threshold)

# Apply a correction factor based on dataset characteristics
correction = 1 if len(set_a) > len(set_b) else 0

# Determine actual duplicates to remove
distinct_factor = unique_elements - total_elements + len(overlap)
distinct_factor = max(0, distinct_factor)
duplicate_count = duplicate_factor - distinct_factor
duplicate_count = max(0, duplicate_count)

# Final adjustment
duplicates = duplicate_count + correction

# Calculate the effective common elements
common_elements = len(set_a.intersection(set_b)) - duplicates

# Display the result
print(f"Result: {common_elements}")