import heapq
from collections import deque
from statistics import mean, variance
data_stream = [127, 63, 255, 31, 191, 95, 223, 159]
bitwise_mask = lambda x: x & 0b11110000
processing_stack = []
filter_queue = deque()
for val in data_stream:
    masked_val = bitwise_mask(val)
    if masked_val > 100:
        processing_stack.append(masked_val)
    else:
        filter_queue.appendleft(masked_val)
heapq.heapify(processing_stack)
while filter_queue:
    high_priority = heapq.heappop(processing_stack) if processing_stack else 0
    low_priority = filter_queue.pop()
    combined = high_priority ^ low_priority
    heapq.heappush(processing_stack, combined)
filtered_values = []
while processing_stack:
    filtered_values.append(heapq.heappop(processing_stack))
signal_mean = mean(filtered_values)
signal_variance = variance(filtered_values)
normalized_peak = round((max(filtered_values) - signal_mean) / (signal_variance ** 0.5), 2)
print(f"Result: {normalized_peak}")