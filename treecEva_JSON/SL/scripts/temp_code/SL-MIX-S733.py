import heapq

def process_signal_stream(data_points):
    window_heap = []
    window_size = 7
    
    # Lambda to maintain window size
    trim_window = lambda h, size: heapq.heappop(h) if len(h) > size else None
    
    for point in data_points:
        heapq.heappush(window_heap, point)
        trim_window(window_heap, window_size)
    
    # Calculate checksum
    root_value = window_heap[0]
    even_sum = sum(x for x in window_heap if x % 2 == 0)
    checksum = root_value * 13 + even_sum
    
    return checksum

# Process the data stream
signal_data = [84, 23, 91, 45, 12, 67, 34, 78, 56, 89]
checksum_result = process_signal_stream(signal_data)
print(f"Result: {checksum_result}")