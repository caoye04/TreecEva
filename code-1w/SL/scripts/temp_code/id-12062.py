from collections import defaultdict
import math

# Simulated network packet processing with decoy analytics

def analyze_traffic(flow_data):
    stats = defaultdict(int)
    anomalies = []
    total_bytes = 0
    entropy = 0.0

    for pkt in flow_data:
        size = pkt['size']
        proto = pkt['protocol']
        stats[proto] += size
        total_bytes += size

        if size > 1500:
            anomalies.append(proto)

    if total_bytes > 0:
        for count in stats.values():
            prob = count / total_bytes
            if prob > 0:
                entropy -= prob * math.log(prob, 2)

    # Distractor: unused deep analysis
    def deep_insight(x):
        return sum([i**2 for i in x]) if x else 0

    return total_bytes, entropy  # Unused return components


def process_fragments(raw_chunks, threshold=256):
    valid_parts = []
    overflow_log = []
    fragment_map = defaultdict(list)

    for i, chunk in enumerate(raw_chunks):
        chunk_size = len(chunk)
        key_segment = chunk[:4]

        if chunk_size >= threshold:
            transformed = int.from_bytes(key_segment, 'big') ^ 0xFFFF
            valid_parts.append(transformed)
            fragment_map['large'].append((i, transformed))
        else:
            adjusted = int.from_bytes(key_segment, 'little') << 2
            overflow_log.append(adjusted)
            fragment_map['small'].append((i, adjusted))

    # Irrelevant aggregation
    summary_stats = {
        'valid_count': len(valid_parts),
        'overflow_count': len(overflow_log),
        'ratio': len(valid_parts) / (len(overflow_log) + 1)
    }

    return valid_parts, fragment_map  # Only valid_parts is used later


def generate_control_sequence(seed_vector):
    sequence = []
    mask = 0xAAAA

    for val in seed_vector:
        # Complex but irrelevant transformation
        temp = (val ^ mask) & 0xFFFF
        temp = ((temp >> 4) | (temp << 12)) & 0xFFFF
        sequence.append(temp % 257)
    
    # Dead path: never called
    def debug_trace():
        return [s ^ 0xFF for s in sequence]

    return sequence  # Unused in final logic


def reduce_segments(data_list, mode='xor'):
    if not data_list:
        return 0
    
    accumulator = data_list[0]
    for item in data_list[1:]:
        if mode == 'xor':
            accumulator ^= item
        elif mode == 'add':
            accumulator += item
        else:
            accumulator = (accumulator + item * 3) % 10007
    
    return accumulator

# Misleading auxiliary function that looks important
def compute_integrity_tree(elements):
    if len(elements) == 0:
        return 1337
    
    tree_hash = 0
    for idx, elem in enumerate(elements):
        tree_hash += elem * (idx + 1) ** 2
    
    return tree_hash % 98765

# Critical lambda: used in final computation
finalize = lambda values, flag: sum(values) ^ flag if flag else sum(values)

# Simulated input data
packets = [
    {'size': 1280, 'protocol': 'tcp'},
    {'size': 2048, 'protocol': 'udp'},
    {'size': 512, 'protocol': 'tcp'},
    {'size': 3072, 'protocol': 'icmp'},
    {'size': 1024, 'protocol': 'udp'}
]

raw_data_chunks = [
    bytes([0x1A, 0x2B, 0x3C, 0x4D, 0xFF]),
    bytes([0x5E, 0x6F, 0x70, 0x81, 0xAA, 0xBB]),
    bytes([0x92, 0xA3, 0xB4, 0xC5, 0xDD]),
    bytes([0xD6, 0xE7, 0xF8, 0x09, 0xEE])
]

seed_values = [100, 200, 300, 400]

# Execute core logic with distractions
_, fragments = process_fragments(raw_data_chunks, threshold=3)
sum_fragments = reduce_segments(fragments['large'], mode='xor')

# Generate but do NOT use
_ = analyze_traffic(packets)
_ = generate_control_sequence(seed_values)
_ = compute_integrity_tree(fragments['small'])

# Key execution point
control_flag = len(fragments['large']) * 17
checksum = finalize(sum_fragments, control_flag)

print(f"Result: {checksum}")