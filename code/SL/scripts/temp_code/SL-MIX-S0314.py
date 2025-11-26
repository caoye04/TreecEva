data_set = {1, 3, 5, 7, 9, 11, 13}
complement_set = {2, 4, 6, 8, 10, 12, 14}
combined_data = data_set.union(complement_set)
unused_computation = sum(complement_set) - min(data_set)

filtered_data = {}
for num in combined_data:
    if num % 3 == 0:
        filtered_data[num] = num * 2 + 1
    elif num % 4 == 0:
        filtered_data[num] = num // 2 - 1
    else:
        filtered_data[num] = num + 5

processed_keys = sorted(filtered_data.keys())
redundant_operation = max(processed_keys) - min(processed_keys)
final_result = filtered_data[processed_keys[2]]
print(f"Result: {final_result}")