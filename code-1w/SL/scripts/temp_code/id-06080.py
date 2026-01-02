def preprocess_signal(raw_values):
    # Irrelevant preprocessing step with misleading normalization
    normalized = [x * 0.95 for x in raw_values if x > 0]
    filtered = [y for y in normalized if y < 100]
    return filtered + [0] * (len(raw_values) - len(filtered))  # Padding with zeros (distractor)


def compute_checksum(sequence):
    # Decoy function: looks important but unused in critical path
    checksum = 0
    for i, val in enumerate(sequence):
        checksum ^= val * (i + 1)
    return checksum


def evaluate_stability(risk_profile):
    # Dead code path — never called in execution
    if sum(risk_profile) / len(risk_profile) > 50:
        return 'UNSTABLE'
    return 'STABLE'


def extract_features(signal_data):
    # Extracts features using slicing and string-like labeling (red herring)
    segments = []
    labels = []
    for i in range(0, len(signal_data) - 3, 3):
        segment = signal_data[i:i+3]
        segments.append(segment)
        label = ''.join(str(int(b % 2)) for b in segment)  # Binary pattern as string
        labels.append(label)
    
    # Convert binary strings to integers — seems meaningful but not used later
    pattern_ints = [int(lbl, 2) if lbl != '000' else 0 for lbl in labels]
    
    return segments, pattern_ints  # Partially unused return


def analyze_pattern(seq, limit):
    # Core logic buried among distractions
    temp_buffer = []
    accumulator = 0
    toggle_flag = False
    
    # Real computation begins here — mixed with irrelevant operations
    for idx, num in enumerate(seq):
        if idx % 2 == 0:
            shifted = num >> 1
            temp_buffer.append(shifted)
        else:
            squared = num ** 2
            temp_buffer.append(squared)

    # Actual key transformation
    transformed = []
    for val in temp_buffer:
        if val <= limit:
            transformed.append(val + 1)
        else:
            transformed.append(val // 2)

    # Secondary filter based on bit count (key step)
    count_bits = lambda x: bin(x).count('1')
    filtered_by_parity = [v for v in transformed if count_bits(v) % 2 == 1]

    # Final accumulation via XOR folding (critical)
    result = 0
    for v in filtered_by_parity:
        result ^= v  # Bitwise XOR chain

    # Additional distractor: unused conditional branch
    if len(filtered_by_parity) > 10:
        result += 999  # Never reached due to input size

    # Another red herring: zipping unrelated sequences
    offsets = list(range(len(transformed)))
    decoy_pairs = list(zip(transformed, offsets))
    entropy_approx = sum(abs(a - b) for a, b in decoy_pairs[:5]) if decoy_pairs else 0

    # Correct answer depends only on XOR-reduced result
    return result

# Main execution block
if __name__ == '__main__':
    # Input data — appears arbitrary but deterministic
    raw_input_stream = [127, 48, 23, 64, 15, 88, 31, 52]
    
    # Distractor: preprocess with unused outcome
    cleaned = preprocess_signal(raw_input_stream)
    
    # More distraction: feature extraction with no downstream use
    _, patterns = extract_features(raw_input_stream)
    
    # Threshold set so that only certain values pass the filter
    threshold = 50
    
    # Critical assignment — this is where the answer forms
    final_diagnostic = analyze_pattern(raw_input_stream, threshold)
    
    # Print required output
    print(f"Result: {final_diagnostic}")