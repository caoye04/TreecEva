data_sequence = [12, 8, 15, 23, 7, 19, 4, 11, 26, 5]
window_size = 3
processing_buffer = data_sequence[2:8]
filtered_values = []
for value in processing_buffer:
    if value > 10:
        filtered_values.append(value)
final_count = len(filtered_values)
result = final_count
print(f"Target result: {result}")