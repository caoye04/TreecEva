import heapq
from collections import defaultdict

def process_network_packets():
    packet_sizes = [1500, 512, 64, 1400, 128, 1024, 256, 2048, 32, 768]
    size_frequency = defaultdict(int)
    min_heap = []
    
    # Process packets and build frequency map
    for size in packet_sizes:
        size_frequency[size] += 1
        if len(min_heap) < 5:
            heapq.heappush(min_heap, size)
        else:
            if size > min_heap[0]:
                heapq.heapreplace(min_heap, size)
    
    # Calculate weighted sum of top 5 largest packets
    weighted_sum = 0
    weight = 1
    while min_heap:
        packet = heapq.heappop(min_heap)
        weighted_sum += packet * weight
        weight += 1
    
    # Compute analyzer metric
    unique_sizes = len(size_frequency)
    total_packets = sum(size_frequency.values())
    if unique_sizes == 0:
        return 0
    
    avg_frequency = total_packets // unique_sizes
    analyzer_metric = weighted_sum + (avg_frequency << 2) - (unique_sizes & 3)
    
    return analyzer_metric

analyzer_metric = process_network_packets()
print(f"Result: {analyzer_metric}")