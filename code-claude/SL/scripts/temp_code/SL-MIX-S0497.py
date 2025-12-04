import itertools

# Function to check if a number meets our criteria
def is_valid(number):
    return number % 3 == 0 and number > 10

# Generate sequence of numbers
base_sequence = range(5, 20)

# Create a list of tuples using itertools.product
combinations = list(itertools.product(base_sequence, repeat=2))

# Extract first elements from combinations
first_elements = [pair[0] for pair in combinations]

# Calculate values based on the first elements
calculated_values = [x * 2 - 3 for x in first_elements]

# Filter values based on our criteria
filtered_values = [value for value in calculated_values if is_valid(value)]

# Calculate the sum of filtered values
filtered_sum = sum(filtered_values)

# For verification purposes
print(f"Result: {filtered_sum}")