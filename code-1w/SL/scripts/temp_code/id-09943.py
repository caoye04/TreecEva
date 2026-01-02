from collections import defaultdict, Counter
import math

# Simulated sensor data with noise and metadata
data_packets = [
    {'id': 101, 'payload': [3, 1, 4, 1, 5], 'type': 'temp', 'seq': 0},
    {'id': 102, 'payload': [9, 2, 6, 5, 3], 'type': 'temp', 'seq': 1},
    {'id': 201, 'payload': [5, 8, 9, 7, 9], 'type': 'humid', 'seq': 0},
    {'id': 202, 'payload': [3, 2, 3, 8, 4], 'type': 'humid', 'seq': 1}
]

# Irrelevant statistics (distractor)
total_packets = len(data_packets)
avg_payload_length = sum(len(p['payload']) for p in data_packets) / total_packets

# Noise filter mask (partially relevant but overcomplicated)
noise_filter = [1, -1, 1, -1, 1]
filtered_data = []
for packet in data_packets:
    filtered = [a * b for a, b in zip(packet['payload'], noise_filter)]
    filtered_data.append(filtered)

# Data categorization (distractor: not used later)
data_by_type = defaultdict(list)
for packet in data_packets:
    data_by_type[packet['type']].append(packet['payload'])

# Sequence reconstruction (red herring)
reconstructed = {}
for packet in data_packets:
    seq = packet['seq']
    if packet['type'] == 'temp':
        reconstructed[seq] = packet['payload']

# Extract all payload values for processing (relevant)
all_values = []
for packet in data_packets:
    all_values.extend(packet['payload'])

# Apply modular transformation with offset (relevant)
mod_base = 7
transformed = [(x ** 2 + 3) % mod_base for x in all_values]

# Count frequency of transformed values (relevant for next step)
freq_map = Counter(transformed)

# Compute entropy-like metric (distractor: looks important but unused)
total = len(transformed)
entropy = sum(-(count/total) * math.log2(count/total) for count in freq_map.values())

# Group by frequency parity (distractor)
even_freq_groups = defaultdict(list)
for val, cnt in freq_map.items():
    even_freq_groups[cnt % 2].append(val)

# Prepare processed data using only odd-frequency values (critical path)
selected_keys = [k for k, v in freq_map.items() if v % 2 == 1]
processed_data = [v for v in transformed if v in selected_keys]

# Decoy function (dead code path)
def decrypt_sequence(data):
    return [d ^ 5 for d in data[::-1]]

# Real computation function
def compute_checksum(seq):
    checksum = 0
    for i, val in enumerate(seq):
        # Interleave operations: bitwise, arithmetic, modular
        temp = (val << 1) ^ i
        temp = (temp * 3) % 11
        checksum += temp
    # Final non-linear transformation
    checksum = (checksum ** 2) // 7 - checksum
    return checksum

# Misleading alternate checksum (not used)
def alt_checksum(data):
    result = 0
    for x in data:
        result += (x & 5) | (x >> 2)
    return result * 2

# Critical statement
final_checksum = compute_checksum(processed_data)

print(f"Result: {final_checksum}")