from collections import defaultdict, Counter
import math

# Simulated network packet analyzer with red herrings
def analyze_packet_stream(packets):
    flow_stats = defaultdict(lambda: {'count': 0, 'bytes': 0})
    byte_frequencies = Counter()
    
    # Irrelevant precomputation (distractor)
    prime_lookup = [True] * 100
    for i in range(2, int(99**0.5) + 1):
        if prime_lookup[i]:
            for j in range(i*i, 100, i):
                prime_lookup[j] = False
    
    suspicious_ips = set()
    total_transmissions = 0
    port_activity = [0] * 1024
    entropy_accumulator = 0.0
    
    for pkt in packets:
        src_ip, dst_ip, port, size, flags = pkt
        
        # Real logic: track flows
        flow_key = (src_ip, dst_ip)
        flow_stats[flow_key]['count'] += 1
        flow_stats[flow_key]['bytes'] += size
        
        # Update byte frequency (used later)
        byte_frequencies[size % 256] += 1
        
        # Distractor: update port activity (never used)
        if port < 1024:
            port_activity[port] += 1
        
        # Distractor: detect suspicious IPs based on flag patterns (unused)
        if flags & 0x02 and flags & 0x01:
            suspicious_ips.add(src_ip)
        
        total_transmissions += 1
    
    # Dead code path (misleading entropy calculation)
    if len(flow_stats) > 1:
        prob_sum = 0.0
        for flow in flow_stats.values():
            p = flow['count'] / total_transmissions
            if p > 0:
                entropy_accumulator -= p * math.log2(p)
    
    # Real state construction (critical)
    active_flows = len(flow_stats)
    total_bytes = sum(stat['bytes'] for stat in flow_stats.values())
    unique_sizes = len(byte_frequencies)
    
    # Heavily obscured transformation chain
    intermediate = (active_flows ^ total_bytes) & 0xFFFF
    intermediate = ((intermediate << 3) | (intermediate >> 13)) & 0xFFFF
    
    # Use of Counter to compute rare byte class count (actually used)
    rare_bytes = sum(1 for cnt in byte_frequencies.values() if cnt < 3)
    
    # Another decoy function call
    def decoy_transform(x):
        return (x * 1103515245 + 12345) & 0x7FFFFFFF
    
    # Critical state computation
    state = [
        active_flows * 3,
        total_bytes % 97,
        unique_sizes ^ 50,
        rare_bytes
    ]
    
    # Red herring: unused recursive function
    def explore_subspace(dim, depth):
        if depth == 0:
            return dim
        return sum(explore_subspace((dim + i) % 8, depth - 1) for i in range(2))
    
    # Finalize hash using only first and last elements
    def finalize_hash(s):
        x, y, z, w = s
        result = x
        result = (result * 31 + y) % 1000009
        result = (result * 31 + z) % 1000009
        result = (result * 31 + w) % 1000009
        return result
    
    checksum = finalize_hash(state)
    
    # Distractor: fake verification that's never used
    validation_seq = []
    temp = checksum
    for _ in range(5):
        validation_seq.append((temp ^ 0xABCD) % 987)
        temp = (temp * 2 + 1) % 10000
    
    return checksum

# Input data (deterministic)
packets = [
    ('192.168.1.10', '10.0.0.5', 80, 1500, 0x10),
    ('192.168.1.11', '10.0.0.6', 443, 256, 0x18),
    ('192.168.1.10', '10.0.0.5', 80, 1500, 0x10),
    ('10.0.0.5', '192.168.1.10', 12345, 64, 0x11),
    ('192.168.1.12', '10.0.0.7', 53, 128, 0x00),
    ('192.168.1.11', '10.0.0.6', 443, 256, 0x18),
    ('192.168.1.13', '10.0.0.8', 22, 512, 0x02),
    ('192.168.1.10', '10.0.0.5', 80, 1500, 0x10),
]

# Execute
checksum = analyze_packet_stream(packets)
print(f"Result: {checksum}")