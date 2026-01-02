from collections import defaultdict, Counter
from itertools import zip_longest, cycle

# Simulated sensor data stream with noise and redundant readings
def generate_noisy_readings():
    base_signal = [1, 0, 1, 1, 0, 1, 0, 0] * 3
    noise_mask = [1, 1, 0, 1, 0, 0, 1, 0] * 3
    return [signal ^ mask for signal, mask in zip(base_signal, noise_mask)]

# Irrelevant helper: computes checksum (never used in final logic)
def compute_checksum(data):
    return sum(x * (i + 1) for i, x in enumerate(data)) % 256

# Distraction function: processes dummy metadata
def process_metadata(meta):
    stats = defaultdict(int)
    for k, v in meta.items():
        if isinstance(v, list):
            stats['list_len'] += len(v)
        stats['key_chars'] += len(k)
    return dict(stats)

# Unused transformation path (dead code)
def legacy_transform(seq):
    shifted = [(x + 2) % 4 for x in seq]
    return [x for x in shifted if x != 3]

# Core transformation: filter and map using bit patterns
def transform_readings(raw):
    filtered = []
    for i, val in enumerate(raw):
        if i % 3 == 0:
            # Apply bit flip every third element
            filtered.append(1 - val)
        elif val == 1 and (i+1) % 5 == 0:
            continue  # Skip on specific condition
        else:
            filtered.append(val)
    return filtered

# Auxiliary counter (distractor): tracks transitions (not used later)
def count_transitions(seq):
    counts = Counter()
    for a, b in zip(seq, seq[1:]):
        counts[(a, b)] += 1
    return counts

# Main analysis function with nested logic
def analyze_pattern(data, reference):
    accumulator = 0
    temp_state = defaultdict(list)
    
    # First pass: align data with cycling reference
    for d, r in zip_longest(data, cycle(reference), fillvalue=0):
        temp_state['alignment'].append(d ^ r)
    
    # Second pass: compute weighted sum with decay factor
    decay = 1.0
    weighted_sum = 0.0
    for i, val in enumerate(temp_state['alignment']):
        weight = decay * (0.9 ** (i % 7))
        weighted_sum += val * weight
        decay = weight  # chain effect
    
    # Third stage: conditional correction based on parity and length
    alignment = temp_state['alignment']
    length = len(alignment)
    parity = sum(alignment) % 2
    
    if length > 20 and parity == 0:
        accumulator -= int(weighted_sum)
    else:
        accumulator += int(round(weighted_sum))
    
    # Fourth: apply hidden offset from bit counting
    ones = bin(length).count('1')
    zeros = len(bin(length)) - bin(length).count('1') - 1  # exclude '0b'
    accumulator += (ones * 2) - (zeros * 3)
    
    # Final adjustment using XOR folding (critical step)
    folded = length
    while folded >= 16:
        folded = (folded & 0xF) ^ (folded >> 4)
    accumulator ^= folded
    
    return accumulator

# Unused but plausible diagnostic (red herring)
def quick_diagnostic(arr):
    return sum(arr[i] * arr[-i-1] for i in range(len(arr)//2))

# --- Execution Flow ---
if __name__ == '__main__':
    # Generate primary data
    raw_sensor_data = generate_noisy_readings()  # 24 elements
    
    # Distractor: metadata processing (no impact)
    device_meta = {
        'model': 'X27',
        'history': [1984, 2001, 2049],
        'flags': [True, False, True]
    }
    meta_result = process_metadata(device_meta)
    
    # Distractor: transition analysis (computed but unused)
    transitions = count_transitions(raw_sensor_data)
    
    # Core transformation
    transformed_data = transform_readings(raw_sensor_data)
    
    # Checksum distraction
    checksum = compute_checksum(transformed_data)  # computed but not used
    
    # Key sequence for pattern analysis
    key_sequence = [1, 0, 0, 1, 1]
    
    # Critical execution point
    final_diagnostic = analyze_pattern(transformed_data, key_sequence)
    
    # Output result
    print(f"Result: {final_diagnostic}")