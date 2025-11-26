data_stream = [12, 45, 78, 23, 56, 89, 34, 67, 90]
filtered_values = [x for x in data_stream if x > 40]
processed_data = filtered_values[1:6]
final_summary = processed_data[-3:]
print(f"Result: {final_summary}")