import math

def analyze_signal(x):
    # Irrelevant signal processing function (dead code path)
    return sum(math.sin(xi * 0.1) for xi in x) if len(x) > 5 else 0

def dummy_checksum(arr):
    # Misleading checksum with no impact
    return sum(arr[i] ^ i for i in range(len(arr))) % 100

def transform_entry(val, idx):
    if idx % 3 == 0:
        return val * 2 + (idx & 7)
    elif idx % 5 == 0:
        return val - (idx ** 0.5)
    else:
        return val + idx

def evaluate_condition(pair):
    a, b = pair
    return (a > 0) and (b < a * 0.8)

def process_pipeline(stream):
    # Core logic begins
    temp_buffer = []
    meta_log = {}
    accumulator = 0
    
    # Initialize with transformed stream
    for i, item in enumerate(stream):
        transformed = transform_entry(item, i)
        temp_buffer.append(transformed)
        
        # Red herring: logging unused stats
        if i % 4 == 0:
            meta_log[f'step_{i}'] = {
                'raw': item,
                'processed': transformed,
                'flagged': transformed > 50
            }
    
    # Secondary transformation
    shifted = [x - 15 for x in temp_buffer if x > 10]
    
    # Bit manipulation decoy
    mask = 0
    for j in range(len(shifted)):
        if j % 2 == 1:
            mask ^= int(shifted[j]) & 15
    
    # Real computation path starts here
    paired_data = list(zip(shifted[:-1], shifted[1:]))  # Overlapping pairs
    filtered_pairs = [p for p in paired_data if evaluate_condition(p)]
    
    # Accumulate based on index-weighted sum
    for idx, (x, y) in enumerate(filtered_pairs):
        weight = 1 + (idx * 0.1)
        contribution = (x - y) * weight
        if contribution > 0:
            accumulator += math.floor(contribution)
        else:
            accumulator -= math.ceil(abs(contribution) * 0.5)
    
    # Decoy final check (never affects result)
    if accumulator % 7 == 0:
        dummy = dummy_checksum([int(x) for x in temp_buffer if x > 0])
        accumulator += (dummy * 0.0)  # Neutral operation
    
    # Final adjustment using enumerate idiom
    adjustments = [i * 0.5 for i, v in enumerate(filtered_pairs) if v[0] + v[1] > 40]
    final_output = accumulator + sum(adjustments)
    
    # Output the target result
    print(f"Target result: {final_output}")
    return final_output

# Simulated sensor data stream (deterministic input)
data_stream = [8, 12, 9, 14, 7, 16, 5, 18, 4, 20, 6, 22]

# Dead code calls (distractions)
dummy_signal = analyze_signal(data_stream)
unused_mask = 0
for k in range(len(data_stream)):
    unused_mask |= k << (k % 4)

# Key execution point
final_output = process_pipeline(data_stream)