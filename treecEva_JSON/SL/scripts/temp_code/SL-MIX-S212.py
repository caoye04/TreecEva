from functools import reduce
from itertools import compress

def call_counter(func):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper

data_stream = [3, 7, 2, 9, 1, 8, 4, 6, 5]
threshold_filter = lambda x: x > 4
transformer = lambda x: x * 2 if x % 2 == 0 else x + 1

@call_counter
def process_chunk(chunk):
    squared_values = map(lambda val: val**2, chunk)
    filtered_mask = map(threshold_filter, squared_values)
    selected_items = list(compress(squared_values, filtered_mask))
    return selected_items

processed_data = process_chunk(data_stream)
transformed_values = list(map(transformer, processed_data))
sorted_values = sorted(transformed_values, reverse=True)

final_metric = reduce(lambda acc, val: acc + val if val > 10 else acc, sorted_values, 0)

print(f"Result: {final_metric}")