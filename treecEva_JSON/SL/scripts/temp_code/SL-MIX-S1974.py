import re
from functools import reduce
from statistics import variance

def log_calls(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        wrapper.call_count += 1
        return result
    wrapper.call_count = 0
    return wrapper

@log_calls
def process_packet_size(size):
    return size * 2 if size % 2 == 0 else size + 5

packet_data = ['PKT_150', 'PKT_200', 'PKT_75', 'PKT_300', 'PKT_125']
extracted_sizes = list(map(int, [re.search(r'\d+', pkt).group() for pkt in packet_data]))
processed_sizes = list(map(process_packet_size, extracted_sizes))
size_variance = variance(processed_sizes)
anomaly_threshold = reduce(lambda x, y: x if x > y else y, processed_sizes) * 0.1
anomaly_score = round(size_variance / anomaly_threshold)

print(f'Result: {anomaly_score}')