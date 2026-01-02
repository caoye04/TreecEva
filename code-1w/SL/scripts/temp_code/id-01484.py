def preprocess_signal(raw_samples, threshold=0.75):
    filtered = [x for x in raw_samples if abs(x) > threshold]
    normalized = [x / max(filtered) for x in filtered] if filtered else [0]
    return normalized


def transform_frequency(data, shift=2):
    shifted = [data[i] * (i + 1) for i in range(len(data))]
    wrapped = [shifted[-i % len(shifted)] for i in range(len(shifted))]
    return [x ^ shift for x in map(int, wrapped)]  # XOR with shift as bitwise distraction


def calculate_entropy(values):
    from math import log2
    freq = {}
    for v in values:
        freq[v] = freq.get(v, 0) + 1
    total = len(values)
    entropy = sum(-(count/total) * log2(count/total) for count in freq.values())
    return round(entropy, 6)


def validate_checksum(sequence):
    # Irrelevant checksum validation (dead path)
    chk = 0
    for num in sequence:
        chk = (chk ^ num) << 1
        if chk > 255:
            chk = chk ^ 0xFF
    return chk % 100


def decode_pattern(sequence):
    # Complex but irrelevant pattern decoder
    result = 0
    for i, val in enumerate(sequence):
        if i % 3 == 0:
            result += val * 2
        elif i % 3 == 1:
            result -= val
        else:
            result ^= val
    return result


def analyze_signal(data, settings):
    # Core logic begins here
    segment_a = data[:len(data)//2]
    segment_b = data[len(data)//2:]
    
    stats = {}
    stats['mean_a'] = sum(segment_a) / len(segment_a) if segment_a else 0
    stats['mean_b'] = sum(segment_b) / len(segment_b) if segment_b else 0
    
    diffs = [abs(a - b) for a, b in zip(segment_a, segment_b) if b != 0]
    stats['drift'] = sum(diffs) / len(diffs) if diffs else 0
    
    # Bitwise manipulation on index positions
    indices = [i for i in range(len(data)) if data[i] > stats['mean_a']]
    flag = 0
    for idx in indices:
        flag ^= idx  # Accumulate XOR of qualifying indices
    
    # Use of enumerate and dictionary construction
    mapped = {i: val * settings['gain'] for i, val in enumerate(data)}
    active_count = sum(1 for v in mapped.values() if v > settings['threshold'])
    
    # Conditional branching with red herring logic
    if active_count > len(data) * 0.5:
        scale = settings['amplify']
        noise_floor = 0.1
        adjusted = [v * scale + noise_floor for v in data]
    else:
        scale = settings['attenuate']
        adjusted = [v * scale for v in data]  # unused
    
    # Real answer depends only on these steps
    base_score = int(stats['mean_a'] * 1000)
    adjustment = len(indices) * flag  # depends on XOR'd indices
    final_score = base_score + adjustment
    
    # Dead code branches with misleading computations
    debug_trace = []
    for i, val in enumerate(mapped.values()):
        if val > 10:
            debug_trace.append(val ** 2)  # never reached due to scaling
    
    # Unused complex structure
    aux_data = {
        'path': [transform_frequency(list(range(5)))],
        'meta': {'version': 2, 'mode': 'diagnostic'},
        'cache': {k: pow(v, 3) for k, v in enumerate(segment_b)}
    }
    
    # Final computation isolated from distractors
    entropy_metric = calculate_entropy([int(x * 100) for x in diffs])
    final_diagnostic = final_score - int(entropy_metric * 100)
    
    # Print required output
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Main execution flow
raw_signal = [0.1, 0.8, 0.3, 1.2, 0.9, 0.4, 1.6, 0.7]
config = {
    'gain': 3,
    'threshold': 0.5,
    'amplify': 1.8,
    'attenuate': 0.5
}

processed_data = preprocess_signal(raw_signal)
processed_data = [x * 1.5 for x in processed_data]  # secondary processing

# Triggering key statement
final_diagnostic = analyze_signal(processed_data, config)