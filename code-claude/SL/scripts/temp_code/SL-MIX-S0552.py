# Analyzing coordinate overlap between two datasets
import itertools

x_positions = [2, 5, 8, 10, 15, 18, 20, 22]
y_positions = [3, 5, 9, 10, 15, 21, 22, 25]

# Filter positions by different criteria
def filter_positions(positions, threshold):
    return [pos for pos in positions if pos > threshold]

# Process the first dataset
x_threshold = 7
filtered_x_positions = filter_positions(x_positions, x_threshold)

# Process the second dataset
y_threshold = 8
filtered_y_positions = filter_positions(y_positions, y_threshold)

# Display intermediate results for debugging
print(f"Filtered x positions: {filtered_x_positions}")
print(f"Filtered y positions: {filtered_y_positions}")

# Find the overlap between filtered positions
overlap_count = len(set(filtered_x_positions) & set(filtered_y_positions))

# Calculate some additional metrics
total_unique = len(set(filtered_x_positions) | set(filtered_y_positions))
union_ratio = overlap_count / total_unique if total_unique > 0 else 0

# Display the result
print(f"Result: {overlap_count}")