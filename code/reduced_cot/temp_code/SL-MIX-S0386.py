data_points = [12, 8, 15, 23, 7, 19, 31, 4, 11]
threshold = 10
filtered_data = [x for x in data_points if x > threshold]
temp_calc = sum(filtered_data) * len(data_points)
processed_data = [x % 7 for x in filtered_data]
final_result = processed_data[-1]
print(f"Result: {final_result}")