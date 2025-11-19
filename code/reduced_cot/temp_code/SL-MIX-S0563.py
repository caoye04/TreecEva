from collections import defaultdict
from functools import reduce
import math

def calculate_base_score(flags, size):
    frag_flag = (flags >> 2) & 1
    df_flag = (flags >> 1) & 1
    mf_flag = flags & 1
    base = (frag_flag << 3) | (df_flag << 2) | (mf_flag << 1)
    return base if size <= 1024 else base ^ 0xF

packets = [
    {'flags': 0b110, 'size': 512},
    {'flags': 0b011, 'size': 2048},
    {'flags': 0b101, 'size': 768},
    {'flags': 0b000, 'size': 4096}
]

flag_counts = defaultdict(int)
threat_components = []

for pkt in packets:
    flags, size = pkt['flags'], pkt['size']
    base_score = calculate_base_score(flags, size)
    normalized_size = size / 1024.0
    size_factor = math.log(normalized_size + 1) if normalized_size > 0 else 0
    component = int(base_score * size_factor * 10) & 0xFF
    threat_components.append(component)
    
    # Update flag counts using bitwise inspection
    for i in range(3):
        if flags & (1 << i):
            flag_counts[i] += 1

# Calculate final threat index
xor_accum = reduce(lambda x, y: x ^ y, threat_components, 0)
count_sum = sum(flag_counts.values())
threat_index = (xor_accum << 2) | (count_sum & 0x3) if count_sum > 5 else (count_sum << 4) ^ xor_accum

print(f"Result: {threat_index}")