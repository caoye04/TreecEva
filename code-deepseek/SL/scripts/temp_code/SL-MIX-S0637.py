temperatures = [22.5, 25.8, 18.3, 30.1, 16.7, 28.9, 19.4]
threshold = 20.0
filtered_values = [temp for temp in temperatures if temp > threshold]
count_above_threshold = len(filtered_values)
temp_adjustment = 2.5
adjusted_values = [temp - temp_adjustment for temp in filtered_values]
final_result = sum(filtered_values)
print(f"Result: {final_result}")