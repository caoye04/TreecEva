from collections import defaultdict
import math

# Simulated packet data with metadata
data_packets = [
    {'id': 101, 'flags': 0b1010, 'payload': 'A', 'seq': 3},
    {'id': 102, 'flags': 0b1100, 'payload': 'B', 'seq': 1},
    {'id': 103, 'flags': 0b1010, 'payload': 'C', 'seq': 4},
    {'id': 104, 'flags': 0b0110, 'payload': 'A', 'seq': 2},
    {'id': 105, 'flags': 0b1010, 'payload': 'D', 'seq': 5}
]

# Irrelevant statistical counters (distractors)
stats = defaultdict(int)
total_weight = 0
entropy_accum = 0.0
auxiliary_flag = False

for pkt in data_packets:
    stats[pkt['payload']] += 1
    total_weight += pkt['id'] % 7
    entropy_accum += math.log(pkt['seq'] + 1e-6)

# Dead computation path: never used later (red herring)
if len(stats) > 3:
    auxiliary_flag = True
    temp_scale = sum(stats.values()) ** 0.5
else:
    temp_scale = 1.0

# Core analysis setup
sequence_sorted = sorted(data_packets, key=lambda x: x['seq'])
flag_analysis = [p['flags'] for p in sequence_sorted]

# Misleading intermediate checksums (decoy values)
current_hash = 0
for f in flag_analysis:
    current_hash = (current_hash * 31 + f) % 10007

# Another distraction: character frequency using list comprehension
distinct_chars = set([p['payload'] for p in data_packets])
frequencies = {c: len([p for p in data_packets if p['payload'] == c]) for c in distinct_chars}
expected_char = 'A'
char_sum = sum([ord(c) * frequencies[c] for c in frequencies])

# Real logic begins: find packets with specific flag pattern (0b1010)
reference_flag = 0b1010
matching_indices = []
valid_count = 0

for i, pkt in enumerate(sequence_sorted):
    if pkt['flags'] == reference_flag:
        matching_indices.append(i)
        valid_count += 1

# Secondary filter: only odd sequence numbers qualify
filtered_valid = [i for i in matching_indices if sequence_sorted[i]['seq'] % 2 == 1]
final_count = len(filtered_valid)

# Compute disorder index based on position scattering
if final_count > 1:
    disorder_index = max(filtered_valid) - min(filtered_valid)
else:
    disorder_index = final_count

# Prime offset based on packet count (deterministic)
prime_offset = 103 if len(data_packets) > 4 else 97

# Critical statement
checksum = (valid_count * prime_offset) ^ disorder_index

# Irrelevant transformation chain (unused)
transformed = 0
for i in range(5):
    transformed = (transformed ^ (char_sum >> i)) % 5000

# Unused function (dead code - distractor)
def diagnose_integrity(packets):
    return sum(p['flags'] & 0x3 for p in packets) % 100

# Print target result
print(f"Result: {checksum}")