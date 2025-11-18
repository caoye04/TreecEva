import heapq
from collections import Counter
def call_tracker(func):
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        return func(*args, **kwargs)
    wrapper.call_count = 0
    return wrapper

@call_tracker
def merge_bands(bands):
    if len(bands) <= 1:
        return bands
    mid = len(bands) // 2
    left = merge_bands(bands[:mid])
    right = merge_bands(bands[mid:])
    return sorted(left + right)

frequency_data = [45, 23, 78, 12, 89, 34, 67, 56]
sorted_frequencies = merge_bands(frequency_data)
peak_heap = []
freq_counter = Counter()
for freq in sorted_frequencies:
    heapq.heappush(peak_heap, -freq)
    freq_counter[freq] += 1
    if len(peak_heap) > 3:
        heapq.heappop(peak_heap)
processed_peaks = sum(-heapq.heappop(peak_heap) for _ in range(len(peak_heap)))
print(f"Result: {processed_peaks}")