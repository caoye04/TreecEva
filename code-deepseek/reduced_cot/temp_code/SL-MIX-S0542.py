data_points = [15, 22, 37, 22, 8, 15, 41, 8, 37, 15]
threshold = lambda x: x > 20
filtered_data = list(filter(threshold, data_points))
unique_vals = set(filtered_data)
redundant_check = len(data_points) - len(filtered_data)
final_count = len(unique_vals)
print(f"Result: {final_count}")