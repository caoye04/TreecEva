from collections import defaultdict, Counter

# Simulated sensor data with noise and redundant fields
data_stream = [
    {'id': 'A7', 'values': [1, 1, 0, 1], 'status': 'active', 'meta': {'t': 1623, 'v': 2}},
    {'id': 'B4', 'values': [0, 1, 1, 0], 'status': 'active', 'meta': {'t': 1624, 'v': 1}},
    {'id': 'A7', 'values': [1, 0, 0, 1], 'status': 'idle',   'meta': {'t': 1625, 'v': 2}},
    {'id': 'C9', 'values': [1, 1, 1, 1], 'status': 'active', 'meta': {'t': 1626, 'v': 3}},
    {'id': 'B4', 'values': [0, 0, 1, 1], 'status': 'active', 'meta': {'t': 1627, 'v': 1}}
]

# Irrelevant statistical tracker (distractor)
avg_magnitude = 0.0
sample_count = 0
for entry in data_stream:
    magnitude = sum(v ** 2 for v in entry['values']) ** 0.5
    avg_magnitude += magnitude
    sample_count += 1
avg_magnitude /= sample_count if sample_count else 1

# Redundant transformation map (partly unused)
transformation_map = defaultdict(lambda: 'X')
for i, char in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    transformation_map[char] = chr(ord('Z') - i)

# Bitmask generator for error detection (only some results are used)
def generate_syndrome(bits):
    syndrome = 0
    for i, bit in enumerate(bits):
        if bit:
            syndrome ^= (i + 1)
    return syndrome

# Checksum based on positional weights (distractor function, not used in final result)
def compute_legacy_checksum(values):
    return sum((i + 1) * val for i, val in enumerate(values)) % 256

# Core transformation: extract and flip bits based on device ID hashing
def transform_entry(entry):
    raw_bits = entry['values']
    device_id = entry['id']
    
    # Hash ID to derive transformation key (using string methods as required)
    hash_key = sum(ord(c) for c in device_id.strip().upper()) % 8
    
    # Rotate bits cyclically based on hash_key
    rotated = raw_bits[hash_key % 4:] + raw_bits[:hash_key % 4]
    
    # Apply bit flip pattern determined by syndrome
    syndrome = generate_syndrome(rotated)
    flipped = [bit ^ ((syndrome >> i) & 1) for i, bit in enumerate(rotated)]
    
    # Attach diagnostic tag (unused in logic but looks important)
    tag = ''.join([transformation_map[c] for c in device_id])
    
    return {
        'node': device_id,
        'transformed': flipped,
        'key': hash_key,
        'tag': tag,
        'original': raw_bits.copy()
    }

# Misleading pre-analysis (dead path)
def preliminary_assessment(stream):
    counts = Counter()
    for entry in stream:
        counts[entry['status']] += 1
        counts['total'] += 1
    return dict(counts)

prelim_analysis = preliminary_assessment(data_stream)  # Dead assignment

# Actual processing pipeline
def collect_by_node(entries):
    grouped = defaultdict(list)
    for e in entries:
        grouped[e['node']].append(e)
    return grouped

# Recursive reduction of node sequences
def reduce_sequence(bits_list, depth=0):
    if len(bits_list) == 1 or depth >= 3:
        return bits_list[0]
    
    # Combine adjacent vectors using XOR and shift
    reduced = []
    for i in range(0, len(bits_list) - 1, 2):
        combined = [(bits_list[i][j] ^ bits_list[i+1][j]) << 1 for j in range(4)]
        normalized = [b if b <= 1 else 1 for b in combined]  # Clamp to binary-like
        reduced.append(normalized)
    
    if len(bits_list) % 2 == 1:
        reduced.append(bits_list[-1])
    
    return reduce_sequence(reduced, depth + 1)

# Main analysis function
def analyze_pattern(dataset):
    # Transform all entries
    transformed = [transform_entry(entry) for entry in dataset]
    
    # Group by node
    grouped = collect_by_node(transformed)
    
    # Extract and reduce sequences per node
    reduced_vectors = {}
    for node, records in grouped.items():
        bit_sequences = [r['transformed'] for r in records]
        final_seq = reduce_sequence(bit_sequences)
        reduced_vectors[node] = final_seq
    
    # Compute final diagnostic metric: weighted sum of specific positions
    diagnostic_score = 0
    position_weights = [1, 2, 4, 8]
    
    for vector in reduced_vectors.values():
        # Use only first reduced vector's pattern
        for i, bit in enumerate(vector):
            diagnostic_score += position_weights[i] * bit
    
    # Inject irrelevant floating point adjustment (looks important but cancels)
    temp_adjust = 0.0
    for v in reduced_vectors.values():
        temp_adjust += sum(float(b) * 0.1 for b in v)
    temp_adjust = round(temp_adjust, 1)
    
    # Final deterministic result (unaffected by temp_adjust)
    return diagnostic_score

# Secondary transformation chain (creates distractor variables)
transformed_data = []
total_entries_processed = 0
for item in data_stream:
    xformed = transform_entry(item)
    xformed['processed'] = True
    
    # String-based tagging with manipulation
    status_flag = item['status'][0].upper() + '_T'
    xformed['flag'] = status_flag.replace('_T', '_TRANSFORMED')
    
    transformed_data.append(xformed)
    total_entries_processed += 1

# Critical statement
final_diagnostic = analyze_pattern(transformed_data)

# Print result as required
print(f"Result: {final_diagnostic}")