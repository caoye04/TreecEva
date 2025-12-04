from collections import Counter

data_points = [4, -2, 7, -3, 4, 8, -1, 4]

# Count occurrences of each value
frequency_counter = Counter(data_points)
most_common_value = frequency_counter.most_common(1)[0][0]

# Filter data and calculate processed value
filtered_data = [x for x in data_points if x % 2 == 0]
processed_data = sum(filtered_data) - len(filtered_data)

# Determine final value with conditional expression
final_value = processed_data if processed_data > 0 else -processed_data

print(f"Result: {final_value}")