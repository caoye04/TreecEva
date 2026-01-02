from itertools import compress

data_stream = [12, -5, 8, 19, -23, 0, 44, -7]
threshold = 10
data_above_threshold = [x > threshold for x in data_stream]
valid_entries = list(compress(data_stream, data_above_threshold))
filtered_sum = sum(valid_entries)
Result: filtered_sum