def preprocess_signal(raw_samples):
    filtered = [x for x in raw_samples if abs(x) > 0.1]
    normalized = [round(x / max(filtered), 3) for x in filtered]
    return normalized


def generate_sequence(n):
    seq = [1, 1]
    for i in range(2, n):
        seq.append(seq[i-1] + seq[i-2])
    return seq

# Irrelevant helper function (dead code path)
def calculate_entropy(data):
    from math import log
    freq = {}
    for x in data:
        freq[x] = freq.get(x, 0) + 1
    total = len(data)
    entropy = 0
    for count in freq.values():
        p = count / total
        entropy -= p * log(p, 2)
    return round(entropy, 3)

# Misleading transformation chain
def transform_readings(readings):
    shifted = [x * 2 + 1 for x in readings]
    inverted = [1 / x if x != 0 else 0 for x in shifted]
    smoothed = []
    for i in range(len(inverted)):
        window = inverted[max(0, i-1):i+2]
        smoothed.append(sum(window) / len(window))
    return smoothed

# Core recursive pattern detector
def detect_cycle(pattern, index=0, seen=None):
    if seen is None:
        seen = {}
    if index >= len(pattern):
        return False
    key = tuple(pattern[:index+1])
    if key in seen:
        return True
    seen[key] = index
    return detect_cycle(pattern, index + 1, seen)

# Main analysis function with distractors
def analyze_pattern(data, limit):
    # Distractor: unused intermediate values
    stats_snapshot = {
        'length': len(data),
        'mean': sum(data) / len(data),
        'variance': sum((x - sum(data)/len(data))**2 for x in data) / len(data),
        'peaks': len([i for i in range(1, len(data)-1) if data[i-1] < data[i] > data[i+1]])
    }
    
    # Relevant computation: frequency of recurring segments
    frequency_map = {}
    for size in range(2, 5):
        for start in range(len(data) - size + 1):
            segment = tuple(data[start:start+size])
            frequency_map[segment] = frequency_map.get(segment, 0) + 1
    
    # Distractor: complex but unused structure
    nested_meta = {
        'layers': [
            {'level': i, 'active': True, 'nodes': [j*i for j in range(i)]}
            for i in range(1, 4)
        ]
    }
    
    # Key logic: find high-frequency cycles above threshold
    cycle_count = 0
    for seq, freq in frequency_map.items():
        if freq > limit and detect_cycle(list(seq)):
            cycle_count += 1
    
    # Secondary path: string-based signature (red herring)
    signature = ''.join(str(int(abs(x)*10))[-1] for x in data[:10] if x != 0)
    checksum = sum(int(c) * (i+1) for i, c in enumerate(signature))
    
    # Final result based on cycle detection
    base_score = cycle_count * 100
    adjustment = len(str(checksum)) * 10
    final_diagnostic = base_score - adjustment  # This will be the answer
    
    return final_diagnostic

# Generate input data
base_fib = generate_sequence(12)
signal_input = [x % 7 + 0.5 for x in base_fib]
transformed_data = preprocess_signal(signal_input)
threshold = 1.5

# Execute main logic
final_diagnostic = analyze_pattern(transformed_data, threshold)
print(f"Result: {final_diagnostic}")