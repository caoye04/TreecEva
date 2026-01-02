import itertools

# Simulated sensor data stream with noise and redundant fields
data_packet = [
    {'id': 1, 'val': 5.0, 'seq': [1, 2, 3], 'meta': 'A', 'flag': True},
    {'id': 2, 'val': -3.2, 'seq': [4, 5], 'meta': 'B', 'flag': False},
    {'id': 3, 'val': 8.1, 'seq': [6, 7, 8, 9], 'meta': 'C', 'flag': True},
    {'id': 4, 'val': 0.0, 'seq': [10], 'meta': 'D', 'flag': True}
]

# Irrelevant helper function (decoy)
def analyze_metadata(packet):
    counts = {}
    for p in packet:
        key = p['meta']
        counts[key] = counts.get(key, 0) + 1
    return sum(counts.values()) * 2  # Misleading computation

# Unused transformation (dead code path)
def legacy_transform(x):
    return [i ** 2 for i in x if i % 2 == 0]

# Auxiliary calculation with red herring variables
total_squares = 0
for item in data_packet:
    temp_sum = 0
    for num in item['seq']:
        temp_sum += num ** 2
    total_squares += temp_sum  # Distractor: used nowhere in logic

average_flagged_val = sum(p['val'] for p in data_packet if p['flag']) / len([p for p in data_packet if p['flag']])

# Redundant list creation (irrelevant)
expanded_seq = []
for p in data_packet:
    expanded_seq.extend(p['seq'])

# Slice-based filtering (actual use of slicing)
trimmed_prefix = expanded_seq[2:-2]  # Remove edges

# Use of itertools: group consecutive even/odd runs
runs = [list(g) for k, g in itertools.groupby(trimmed_prefix, key=lambda x: x % 2)]
run_lengths = [len(r) for r in runs]

# Secondary decoy variable
max_run_length = max(run_lengths) if run_lengths else 0

# Transform data: extract positive values and flatten sequences conditionally
def transform_packet(packet):
    result = []
    for p in packet:
        base_val = abs(p['val'])
        if p['flag']:
            # Apply conditional flattening and scaling
            scaled_seq = [base_val * x for x in p['seq']]
            result.append((scaled_seq, len(scaled_seq)))  # Tuple return
        else:
            # Dead branch effect
            result.append(([0], 1))
    return result

transformed_data = transform_packet(data_packet)

# Core processing function with nested logic
def process_sequence(t_data):
    accumulator = 0
    for seq_tuple in t_data:
        sequence = seq_tuple[0]
        length = seq_tuple[1]
        
        # Nested conditional with misleading intermediate
        if length > 2:
            mid_slice = sequence[1:-1]  # Slicing operation
            slice_avg = sum(mid_slice) / len(mid_slice) if mid_slice else 0
            weight = 1.5 if slice_avg > 10 else 0.5
            
            # Multiple steps of arithmetic
            temp_result = 0
            for val in mid_slice:
                temp_result += val * weight
            
            # Cumulative update
            accumulator += int(temp_result)  # Truncate to integer
        else:
            # Alternate path with no significant impact due to input
            accumulator += length * 10
    
    # Final nonlinear transformation
    final_shift = accumulator ** 2 / (accumulator + 1) if accumulator != -1 else 0
    return round(final_shift, 6)

# Key statement
final_output = process_sequence(transformed_data)

# Print target result
print(f"Result: {final_output}")