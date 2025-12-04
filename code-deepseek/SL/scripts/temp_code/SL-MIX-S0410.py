data_points = [4, 7, 12, 9, 3, 15, 8, 6, 11]
threshold = 7

# Process data points above threshold
filtered_data = [x for x in data_points if x > threshold]

# Calculate some intermediate metrics (partially relevant)
avg_value = sum(data_points) / len(data_points) if data_points else 0
data_range = max(data_points) - min(data_points)

# Transform filtered data with lambda operations
transformed = list(map(lambda x: (x * 2) - 5, filtered_data))

# Count values in specific ranges (distractor)
low_count = len([x for x in data_points if x < 5])
mid_count = len([x for x in data_points if 5 <= x <= 10])

# Process the transformed data
processed_data = [val + 3 for val in transformed if val % 2 == 0]

# Final computation
final_count = processed_data[-1] if processed_data else 0

print(f"Result: {final_count}")