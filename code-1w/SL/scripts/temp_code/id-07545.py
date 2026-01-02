from collections import defaultdict

# Simulated network packet analysis with decoy computations
packets = [
    {'src': '192.168.1.10', 'dst': '10.0.0.5', 'size': 1440, 'flags': 0b1010},
    {'src': '192.168.1.11', 'dst': '10.0.0.6', 'size': 1200, 'flags': 0b1100},
    {'src': '192.168.1.10', 'dst': '10.0.0.5', 'size': 512,  'flags': 0b0010},
    {'src': '192.168.1.12', 'dst': '10.0.0.7', 'size': 1440, 'flags': 0b1001}
]

# Irrelevant statistics (distractors)
total_bytes = sum(p['size'] for p in packets)
unique_hosts = len(set(p['src'] for p in packets) | set(p['dst'] for p in packets))
flag_distribution = defaultdict(int)
for p in packets:
    flag_distribution[p['flags']] += 1

# Unused transformation chain (dead path)
transformed = []
for p in packets:
    transformed.append({
        'id': hash(p['src']) % 1000,
        'meta': (p['size'] >> 4) ^ p['flags']
    })

# Decoy checksum using only size (misleading intermediate)
decoy_checksum = 0
for p in packets:
    if p['size'] > 1000:
        decoy_checksum ^= p['size']

def process_flags(flag_list):
    # Complex but irrelevant recursive reduction (red herring)
    if len(flag_list) <= 1:
        return flag_list[0] if flag_list else 0
    mid = len(flag_list) // 2
    left = process_flags(flag_list[:mid])
    right = process_flags(flag_list[mid:])
    return (left << 1) ^ right ^ 0b101

# Unused recursive result (distractor)
recursive_flag_trace = process_flags([p['flags'] for p in packets])

# Real computation begins: filter and aggregate by source
source_aggregate = defaultdict(list)
for p in packets:
    source_aggregate[p['src']].append(p['size'])

# Compute meaningful aggregates
active_sources = []
for src, sizes in source_aggregate.items():
    avg_size = sum(sizes) / len(sizes)
    if avg_size > 800:  # threshold filter
        active_sources.append(src)

# Key values for actual answer
base_key = len(active_sources) * 1000  # 2000

# Secondary metric: total packets from high-volume sources
high_volume_count = sum(
    1 for p in packets 
    if p['src'] in active_sources and p['size'] >= 1200
)  # 3 packets

# Nested list comprehension with zip (python idiom) - real use
paired_shifts = [
    (a ^ b) << 1 
    for a, b in zip(
        [p['flags'] for p in packets if p['size'] > 500],
        [p['flags'] >> 1 for p in packets if p['src'] == '192.168.1.10'] * 2
    )
]
final_key = sum(paired_shifts)  # [ (0b1010^0b101) << 1, (0b1010^0b101) << 1 ] => (0b1111 << 1) * 2 => 30 * 2 = 60

# Bit manipulation chain with masking (real logic)
aggregate = 0
for p in packets:
    aggregate += p['size'] & 0xFF  # sum of low bytes
mask = 0xFFFF ^ (len(packets) << 8)  # 0xFFFF ^ 0x400 = 0xFBFF

# Critical statement
checksum = final_key ^ (aggregate & mask)

# Print result as required
print(f"Result: {checksum}")