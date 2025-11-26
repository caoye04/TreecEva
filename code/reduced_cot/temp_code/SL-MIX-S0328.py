raw_data = [45, 78, 23, 91, 56, 34, 67, 12, 89, 41]
selected_slice = raw_data[2:7]
slice_sum = sum(selected_slice)
processed_data = slice_sum * 2
final_value = processed_data // 3
print(f"Target result: {final_value}")