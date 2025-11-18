import math
from collections import defaultdict

def calculate_entropy(packet_sizes):
    if not packet_sizes:
        return 0
    size_counts = defaultdict(int)
    for size in packet_sizes:
        size_counts[size] += 1
    total_packets = len(packet_sizes)
    entropy = 0
    for count in size_counts.values():
        probability = count / total_packets
        entropy -= probability * math.log2(probability)
    return entropy

network_packets = [128, 256, 512, 128, 64, 256, 128, 1024, 512, 128]
packet_frequency = defaultdict(int)
for packet in network_packets:
    packet_frequency[packet] += 1

entropy_base = calculate_entropy(network_packets)
threat_contributions = []
for size, freq in sorted(packet_frequency.items()):
    normalized_size = size / 128
    log_component = math.log(normalized_size) if normalized_size > 0 else 0
    exp_factor = math.exp(freq * 0.1)
    contribution = (log_component * exp_factor + entropy_base) ** 2
    threat_contributions.append(contribution)

final_threat_score = round(sum(threat_contributions) * 1000)
print(f"Result: {final_threat_score}")