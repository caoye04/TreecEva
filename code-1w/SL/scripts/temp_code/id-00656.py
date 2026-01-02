from itertools import compress

data_stream = [12, -5, 8, 19, -22, 34, 11, -7, 42, 28]
valid_flags = [x > 0 and x % 2 == 0 for x in data_stream]
filtered_data = list(compress(data_stream, valid_flags))

if len(filtered_data) > 3:
    threshold_score = filtered_data[-1]
else:
    threshold_score = sum(filtered_data)

Result: threshold_score