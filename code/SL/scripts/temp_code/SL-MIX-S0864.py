data_stream = [15, 8, 23, 42, 17, 31, 9, 55]
intermediate_calc = sum(data_stream) // len(data_stream)
filtered_data = [x for x in data_stream if x > 20]
temp_storage = [x * 2 for x in data_stream[:3]]
processed_items = [x % 10 for x in filtered_data]
sorted_data = sorted(filtered_data, reverse=True)
unused_metric = intermediate_calc * 3 - 10
final_analysis = sorted_data[-1] * 2 - processed_items[1]
print(f"Target result: {final_analysis}")