data_points = [12, 45, 78, 23, 56, 89, 34, 67, 90, 41]
data_mapping = {i: (x * 2 - 3) % 17 for i, x in enumerate(data_points)}

# Intermediate calculations (distractor)
sum_check = sum(data_points[:5])
length_check = len([x for x in data_points if x > 50])

filter_keys = lambda x: x % 3 == 0
filtered_keys = list(filter(filter_keys, data_mapping.keys()))

# Unused computation (distractor)
redundant_sum = sum([data_mapping[k] ** 2 for k in filtered_keys])

processed_data = data_mapping[filtered_keys[1]]

# More distractor operations
bitwise_check = processed_data & 0b1111
shift_check = processed_data << 2

final_output = processed_data + (bitwise_check // 4)

print(f"Target result: {final_output}")