initial_data = [12, 8, 15, 23, 7, 19, 4, 11, 6]
threshold = 10
filtered_values = [x for x in initial_data if x > threshold]
sorted_data = sorted(filtered_values)
processed_data = sorted_data[::-1]
final_result = processed_data[-3:]
print(f"Result: {final_result}")