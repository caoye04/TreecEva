import math

def transform_value(x, mode):
    if mode == 'A':
        return (x ** 2) + 3 * x - 1
    elif mode == 'B':
        return int(abs(math.sin(x)) * 100)
    else:
        return x

def analyze_sequence(seq, threshold):
    count = 0
    temp_result = 0
    for i in range(len(seq)):
        if seq[i] > threshold:
            count += 1
            temp_result += seq[i]
    intermediate_avg = temp_result / count if count > 0 else 0
    return count, intermediate_avg

def filter_and_shift(data, shift):
    # Irrelevant transformation chain
    shifted = [data[i] + shift for i in range(0, len(data), 2)]
    mirrored = [data[-j-1] for j in range(len(data))]
    combined = shifted + mirrored[:len(shifted)]
    return sorted(combined, reverse=True)

def compute_signature(arr):
    sig = 0
    for val in arr:
        sig ^= int(val * 7) % 19
    return sig

def normalize_chunk(chunk):
    mean_val = sum(chunk) / len(chunk)
    adjusted = [c - mean_val for c in chunk]
    squared_sum = sum([a**2 for a in adjusted])
    norm_factor = math.sqrt(squared_sum) if squared_sum != 0 else 1
    return [a / norm_factor for a in adjusted], mean_val

def process_segment(data, depth):
    # Core logic embedded in noise
    segment_size = len(data) // 4
    raw_segment = data[segment_size:segment_size*2]
    
    # Distractor: complex but unused slicing and transforms
    decoy_slice = data[::-2][:5]
    decoy_transform = [transform_value(x, 'B') for x in decoy_slice]
    dummy_sig = compute_signature(decoy_transform)
    
    # Real processing begins
    clean_part, offset = normalize_chunk(raw_segment)
    filtered_clean = [x for x in clean_part if x > -0.5]
    
    # More red herrings
    stats = analyze_sequence([abs(x) for x in data], 10)
    phantom_map = {i: transform_value(i, 'A') for i in range(3)}
    
    # Actual computation path
    base_value = sum(filtered_clean) * 100
    adjustment = 0
    for i in range(len(filtered_clean)):
        if i % 2 == 0:
            adjustment += math.cos(filtered_clean[i] * math.pi)
    
    # Final result built from non-obvious steps
    final = int(base_value + adjustment * 50)
    
    # Dead code path - never executed
    if len(decoy_slice) > 100:
        fallback = filter_and_shift(decoy_slice, 5)
        final -= sum(fallback)
    
    return final

# Main execution with layered distractions
raw_input = [12, -5, 8, 22, 3, 17, 4, 19, 1, 6, 9, 14]

# Irrelevant preprocessing
extended_copy = raw_input + [x * 2 for x in raw_input if x < 10]
duplicate_filtered = [x for x in extended_copy if x not in [12, 19]]
sorted_mirror = sorted(extended_copy)[::-1]

# Decoy statistical summaries
count_pos = len([x for x in raw_input if x > 0])
sum_neg = sum([x for x in raw_input if x < 0])
avg_raw = sum(raw_input) / len(raw_input)

# Real data flow starts here
normalized_data, _ = normalize_chunk(raw_input)

# Key distracting transformations
shadow_processed = filter_and_shift(normalized_data, 7)
phantom_analysis = analyze_sequence(shadow_processed, 0.3)

# Critical statement
final_output = process_segment(normalized_data, 3)

print(f"Result: {final_output}")