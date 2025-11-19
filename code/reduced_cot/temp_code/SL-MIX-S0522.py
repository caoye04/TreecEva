import heapq
from collections import defaultdict
import math

def compute_entropy(freq_map):
    total = sum(freq_map.values())
    entropy = 0.0
    for freq in freq_map.values():
        if freq > 0:
            p = freq / total
            entropy -= p * math.log2(p)
    return entropy

packet_sizes = [128, 64, 128, 256, 64, 128, 512, 256, 128]
frequency_map = defaultdict(int)
max_heap = []

for size in packet_sizes:
    frequency_map[size] += 1
    heapq.heappush(max_heap, -size)  # Max heap using negative values

base_entropy = compute_entropy(frequency_map)
unique_sizes = len(frequency_map)
smoothing_factor = 0.1 if unique_sizes < 5 else 0.05

# Extract top 3 largest packet sizes
largest_packets = []
for _ in range(min(3, len(max_heap))):
    largest_packets.append(-heapq.heappop(max_heap))

entropy_adjustment = sum(largest_packets) * smoothing_factor / 1000
adjusted_entropy = base_entropy + entropy_adjustment

print(f"Result: {adjusted_entropy:.6f}")