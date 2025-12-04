import itertools

# Generate some test values for a data analysis task
raw_data = [14, 8, 21, 3, 42, 17, 9, 28, 11, 35]

# Extract slice of values for processing
processing_slice = raw_data[1:8:2]

# Apply initial filtering criteria
threshold = 10
filtered_values = []
for value in processing_slice:
    # Only include values that meet our criteria
    if value < threshold or value % 2 == 0:
        filtered_values.append(value)
    else:
        # Skip values that don't meet criteria
        continue

# Calculate how many values are divisible by 7
final_count = sum(map(lambda x: x % 7 == 0, filtered_values))

# Additional processing for reference purposes
total_sum = sum(filtered_values)
average = total_sum / len(filtered_values) if filtered_values else 0

print(f"Result: {final_count}")