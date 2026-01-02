import itertools

# Irrelevant helper function (dead code path)
def unused_transform(x):
    return (x << 2) ^ 0xACE

# Distractor variables
temp_buffer = [0] * 15
offset_mask = 2341
useless_counter = 0

# Real computation starts here
def generate_weights(n):
    weights = []
    for i in range(n):
        if i % 3 == 0:
            weights.append(i * 1.5)
        elif i % 5 == 0:
            weights.append(-i)
        else:
            weights.append(1)
    return weights[:n]

# Another decoy function
def validate_checksum(arr):
    chk = 0
    for val in arr:
        chk = (chk + val) % 97
    return chk == 42

# Core logic disguised among red herrings
def analyze_pattern(seq):
    a, b, c = 0, 1, 1
    result = 0
    for idx, val in enumerate(seq):
        if idx < 2:
            continue
        # Complex condition with misleading intermediate
        temp_val = seq[idx-1] + seq[idx-2]
        if temp_val < val:
            a += 1
        elif temp_val == val:
            b += 2
        else:
            c -= 1
    return a * b - c

# Real processing chain
def process_element(x, shift):
    base = (x ^ 0x5F) + shift
    if base > 100:
        return base // 3
    return (base * 2) ^ 5

def process_sequence(stream):
    # Use of dictionary as state tracker (meaningful)
    stats = {
        'sum': 0,
        'count': 0,
        'flag': False
    }

    # Use of itertools to create distraction but also subtle utility
    paired = list(itertools.pairwise(stream))
    filtered_pairs = [p for p in paired if (p[0] + p[1]) % 2 == 0]

    shifted_values = []
    for i, val in enumerate(stream):
        # Conditional expression used idiomatically
        shift = 7 if i % 4 == 0 else (11 if i % 2 == 0 else 0)
        processed = process_element(val, shift)
        shifted_values.append(processed)

        stats['sum'] += processed
        stats['count'] += 1
        if processed > 50 and not stats['flag']:
            stats['flag'] = True

    # This part looks complex but only one line matters
    dummy_acc = 0
    for _ in range(3):  # Misleading loop
        dummy_acc += offset_mask

    # Critical calculation buried in logic
    key_index = len(shifted_values) // 2
    pivot = shifted_values[key_index] if key_index < len(shifted_values) else 0

    # Final transformation using multiple concepts
    adjustment = sum(1 for p in filtered_pairs if p[0] > p[1])
    raw_score = stats['sum'] * (pivot % 17)

    # The real answer derivation
    final_component = raw_score - (adjustment * 100)

    # Irrelevant cleanup
    temp_buffer.clear()
    useless_counter += 1

    return final_component

# Decoy data structure
dummy_config = {
    'mode': 'debug',
    'flags': [True, False, True],
    'meta': {'version': '2.1', 'build': 9001}
}

# Actual input data
base_input = [12, 15, 23, 34, 45, 56, 67]
data_stream = [(x * 2) + 3 for x in base_input]

# Introduce more noise
extended_stream = data_stream + [x ^ 0xFF for x in data_stream[:3]]

# Main execution point
intermediate_result = analyze_pattern(base_input)  # Looks important, isn't

# The actual target assignment
final_output = process_sequence(data_stream)

print(f"Result: {final_output}")