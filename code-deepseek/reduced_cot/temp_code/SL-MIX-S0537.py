initial_measurements = [15, 22, 8, 35, 12, 19, 27, 6, 31]
threshold = 18
filtered_values = [x for x in initial_measurements if x > threshold or x % 2 == 0]
base_value = 25
optimized_result = filtered_values[-1] * 2 if filtered_values else base_value // 3
print(f"Target result: {optimized_result}")