from collections import defaultdict, Counter
from itertools import zip_longest

# Simulated telemetry data ingestion and integrity verification
raw_packets = [
    [0x1A, 0x2B, 0x3C],
    [0x4D, 0x5E, 0x6F],
    [0x70, 0x81, 0x92],
    [0xA3, 0xB4, 0xC5]
]

stats_log = defaultdict(int)
decode_map = {i: chr(65 + (i % 26)) for i in range(128)}

# Irrelevant decoding attempt for display purposes only
decoded_stream = ''
for packet in raw_packets:
    for byte in packet:
        if byte in decode_map:
            decoded_stream += decode_map[byte]

# Misleading checksum using XOR folding (not used in final result)
legacy_checksum = 0
for packet in raw_packets:
    segment_sum = sum(packet) % 256
    legacy_checksum ^= segment_sum

# Buffer transformation chain with distractor operations
working_stack = []
for i, packet in enumerate(raw_packets):
    shifted = [(b << 1) % 256 for b in packet]  # Bit shift transform
    inverted = [255 - b for b in shifted]     # Invert bytes
    working_stack.append(inverted)

# Dead code path: statistics gathering not used later
pair_counter = Counter()
for layer in working_stack:
    for a, b in zip(layer, layer[1:]):
        pair_key = f"{a}:{b}"
        pair_counter[pair_key] += 1
        stats_log['pairs_seen'] += 1

# Auxiliary tracking structure (partially relevant)
history = []
for idx, row in enumerate(working_stack):
    entry = {
        'index': idx,
        'sum': sum(row),
        'parity': sum(row) % 2,
        'active': True
    }
    if idx % 2 == 0:
        entry['flagged'] = True
    history.append(entry)

# Distractor: unused recursive function definition
def compute_recursive_weight(n):
    if n <= 1:
        return 1
    return n * compute_recursive_weight(n-1) % 100

# Real processing begins here — critical path
intermediate_values = []
for layer in working_stack:
    val = 0
    for i, b in enumerate(layer):
        val += b * (i + 1)  # Weighted sum by position
    intermediate_values.append(val % 1000)

# Combine using modular interaction
aggregate = 0
for x, y in zip_longest(intermediate_values, [7, 11, 13, 17], fillvalue=1):
    aggregate = (aggregate * x + y) % 5000

# Transform step that appears complex but deterministic
temp_buffer = []
carry = 0
for v in intermediate_values:
    temp_val = (v ^ carry) + len(history)
    temp_buffer.append(temp_val % 97)
    carry = v // 10

# Core processing function (only this affects final answer)
def process_segment(buf, log_history):
    total = 0
    for i, val in enumerate(buf):
        record = log_history[i]
        weight = record['sum'] % 7
        total += val * weight
        if record.get('flagged', False):
            total += i
    return total % 10000

# Final computation — key execution point
final_checksum = process_segment(temp_buffer, history)

print(f"Result: {final_checksum}")