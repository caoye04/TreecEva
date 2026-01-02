from collections import defaultdict, Counter

# Simulated packet data with metadata
data_packets = [
    {'id': 101, 'payload': [65, 66, 67, 68], 'flags': 0b1010, 'seq': 1},
    {'id': 102, 'payload': [69, 70, 71], 'flags': 0b1100, 'seq': 4},
    {'id': 103, 'payload': [72, 73, 74, 75, 76], 'flags': 0b1001, 'seq': 7},
    {'id': 104, 'payload': [77], 'flags': 0b0011, 'seq': 12}
]

# Irrelevant statistical counters (distractors)
statis = defaultdict(int)
flag_counter = Counter()

# Spurious variables and decoy computations
aggregate = 0
running_hash = 0
buffer_size = 0
offset_tracker = [0] * 5
redundant_sum = sum(range(10))  # Dead computation

# Real processing begins here
checksum = 17
base_shift = 5
residue = 0

for packet in data_packets:
    payload = packet['payload']
    seq = packet['seq']
    
    # Update flag counter (partially relevant but over-tracked)
    flag_counter[packet['flags']] += 1
    
    # Linear search for sequences divisible by 3 (red herring)
    if seq % 3 == 0:
        offset_tracker[seq // 3] = len(payload)

    # Core checksum logic embedded in noise
    temp_val = 0
    for byte in payload[:]:  # slicing used idiomatically
        temp_val += byte ^ base_shift
        aggregate += byte % 7  # irrelevant aggregation

    # Critical path: update residue using modular arithmetic
    if len(payload) > 1:
        residue += (temp_val * 2) % 257
    else:
        residue += temp_val % 100

    # Decoy conditional - never triggered due to data
    if packet['id'] == 999:
        running_hash ^= temp_val
        break  # dead code path

    # Key update mixed with distractions
    buffer_size += len(payload)
    checksum = (checksum + temp_val) % 65537
    checksum = (checksum * 3) ^ residue  # <-- key statement

    # Extra distraction: string splitting simulation
    ids = "101,102,103,104".split(',')
    lookup = {int(k): v for v, k in enumerate(ids)}

# More irrelevant transformations
final_aggregate = aggregate * 2 - redundant_sum
lookup_values = list(lookup.values())
sorted_flags = sorted(flag_counter.keys())

# Output only the target result
print(f"Target result: {checksum}")