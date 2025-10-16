from collections import namedtuple
from functools import reduce
import hashlib

def calculate_hash_mod(value, mod_base):
    return int(hashlib.md5(str(value).encode()).hexdigest(), 16) % mod_base

def compute_variance(values):
    mean_val = sum(values) / len(values)
    return sum((x - mean_val) ** 2 for x in values) / len(values)

PacketData = namedtuple('PacketData', ['source_ip', 'destination_ip', 'payload_size'])

network_packets = [
    PacketData('192.168.1.10', '10.0.0.5', 1024),
    PacketData('192.168.1.20', '10.0.0.5', 2048),
    PacketData('172.16.0.30', '10.0.0.5', 512),
    PacketData('192.168.1.10', '10.0.0.8', 4096),
    PacketData('10.0.0.4', '10.0.0.5', 256)
]

# Process packet source IPs for hash analysis
source_ips = [packet.source_ip for packet in network_packets]
ip_hashes = [calculate_hash_mod(ip, 1000) for ip in source_ips]

# Calculate statistical measures
hash_mean = reduce(lambda a, b: a + b, ip_hashes) / len(ip_hashes)
hash_variance = compute_variance(ip_hashes)

# Identify repeated source IPs
unique_sources = set(source_ips)
repeated_ips_count = len(source_ips) - len(unique_sources)

# Compute intrusion score based on hash distribution and repetition
intrusion_score = (hash_variance % 100) + (repeated_ips_count * 7) + int(hash_mean // 10)

print(f"Result: {intrusion_score}")