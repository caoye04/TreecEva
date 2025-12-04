raw_data = [12, 8, 15, 23, 7, 19, 4, 31, 11, 6]
threshold = 10
filtered_data = [x for x in raw_data if x > threshold]
multiplier = 2
final_result = sum(filtered_data) * multiplier
print(f"Result: {final_result}")