import re
from itertools import combinations

def compute_normalized_entropy(packet_sizes):
    if not packet_sizes:
        return 0
    size_counts = {}
    for size in packet_sizes:
        size_counts[size] = size_counts.get(size, 0) + 1
    total_packets = len(packet_sizes)
    probabilities = [count / total_packets for count in size_counts.values()]
    import math
    entropy = -sum(p * math.log2(p) for p in probabilities if p > 0)
    max_entropy = math.log2(len(size_counts)) if len(size_counts) > 1 else 1
    return entropy / max_entropy if max_entropy > 0 else 0

def sliding_window_entropy(data, window_size):
    entropies = []
    for i in range(len(data) - window_size + 1):
        window = data[i:i+window_size]
        entropies.append(compute_normalized_entropy(window))
    return entropies

network_traffic_log = """
PACKET_SRC=192.168.1.10 SIZE=1448 TIME=10:01:23
PACKET_SRC=192.168.1.10 SIZE=1448 TIME=10:01:24
PACKET_SRC=192.168.1.10 SIZE=52 TIME=10:01:25
PACKET_SRC=192.168.1.10 SIZE=1448 TIME=10:01:26
PACKET_SRC=192.168.1.10 SIZE=1448 TIME=10:01:27
PACKET_SRC=192.168.1.10 SIZE=1448 TIME=10:01:28
PACKET_SRC=192.168.1.10 SIZE=1300 TIME=10:01:29
PACKET_SRC=192.168.1.10 SIZE=52 TIME=10:01:30
PACKET_SRC=192.168.1.10 SIZE=1448 TIME=10:01:31
PACKET_SRC=192.168.1.10 SIZE=1448 TIME=10:01:32
PACKET_SRC=192.168.1.10 SIZE=52 TIME=10:01:33
PACKET_SRC=192.168.1.10 SIZE=1448 TIME=10:01:34
PACKET_SRC=192.168.1.10 SIZE=1448 TIME=10:01:35
"""

# Extract packet sizes using regex
packet_entries = network_traffic_log.strip().split('\n')
extracted_sizes = [int(re.search(r'SIZE=(\d+)', entry).group(1)) for entry in packet_entries]

# Calculate entropy values using sliding window
window_entropy_values = sliding_window_entropy(extracted_sizes, 5)

# Apply weighted scoring based on entropy thresholds
weight_factors = [1 + (entropy > 0.7) * 2 + (entropy > 0.85) * 3 for entropy in window_entropy_values]
weighted_scores = [entropy * weight for entropy, weight in zip(window_entropy_values, weight_factors)]

# Calculate suspicious score as weighted average with polynomial adjustment
suspicious_score = sum(weighted_scores) / len(weighted_scores) if weighted_scores else 0
suspicious_score = round(suspicious_score ** 1.5 * 100)

print(f"Result: {suspicious_score}")