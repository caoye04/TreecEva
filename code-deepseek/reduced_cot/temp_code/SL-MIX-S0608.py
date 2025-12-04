from collections import Counter

packet_sizes = [128, 256, 512, 1024, 2048, 512, 256, 128]
processed_packets = [size // 8 for size in packet_sizes]
size_counts = Counter(packet_sizes)
common_size = size_counts.most_common(1)[0][0]
transmission_overhead = common_size // 64
network_load = processed_packets[-1] + transmission_overhead
print(f"Result: {network_load}")