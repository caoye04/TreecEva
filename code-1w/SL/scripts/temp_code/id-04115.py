from itertools import compress

data_values = [12, -7, 3, 8, -4, 9, 0, 6]
threshold_mask = [(x > 0) and (x % 2 == 0) for x in data_values]
filtered_data = list(compress(data_values, threshold_mask))

duplicate_check = {x: data_values.count(x) for x in set(data_values)}
size_metric = len(data_values) // 2 + 1

filtered_sum = sum(filtered_data)
Result: {filtered_sum}