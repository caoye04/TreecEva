data_points = [24, 18, 35, 42, 15, 29, 8, 51, 33, 27]
threshold = 25
filtered_values = [x for x in data_points if x > threshold]
processed_value = sum(filtered_values)
print(f"Result: {processed_value}")