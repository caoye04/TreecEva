def preprocess_segment(segment):
    # Irrelevant transformation (dead path)
    if len(segment) > 10:
        return [x * 2 for x in segment]
    return segment

# Decoy data structure
historical_readings = {
    'baseline': [1, 3, 7],
    'anomalies': {6: 'spike', 9: 'drop'},
    'flags': set()
}

# Unused but misleading intermediate
aggregate_buffer = []
running_checksum = 0

# Real logic begins: signal analysis with red herrings
signal_snapshot = [8, 12, 10, 15, 7]

# Distractor: checksum calculation (not used in final result)
for val in signal_snapshot:
    running_checksum += val ^ 3
    aggregate_buffer.append(val // 2)

# Decoy function that looks important
def compute_robustness_index(data):
    return sum(data) % 5

# Actual relevant logic hidden among noise
def extract_core_signature(seq):
    filtered = [x for x in seq if x > 9]
    return tuple(filtered)

# Bit manipulation decoy
def shift_diagnostic(value):
    return (value << 2) | 1

# Core analysis function with nesting and set operations
def analyze_signal_pattern(signal):
    # Level 1: filtering
    high_freq = [x for x in signal if x % 2 == 0]
    
    # Level 2: transformation
    processed = []
    temp_flags = set()
    for item in high_freq:
        if item > 10:
            processed.append(item ** 2)
            temp_flags.add(shift_diagnostic(item))  # Red herring usage
        else:
            processed.append(item + 5)
    
    # Level 3: set-based exclusion
    exclusions = {x + 1 for x in processed if x < 50}
    refined = [p for p in processed if p not in exclusions]
    
    # Level 4: recursive reduction
    def reduce_sequence(seq):
        if len(seq) <= 1:
            return seq[0] if seq else 0
        return reduce_sequence([seq[0] - seq[-1]] + seq[1:-1])
    
    # Final computation chain
    signature_tuple = extract_core_signature(signal)
    base_score = reduce_sequence(refined)
    adjustment = len(signature_tuple) * 3
    
    # Misleading rounding operation (irrelevant)
    fake_precision = round(base_score / adjustment, 4) if adjustment else 0
    
    # Actual answer path
    final_diagnostic = base_score + adjustment
    
    # Dead code branch
    if final_diagnostic < 0:
        final_diagnostic *= -1
    
    return final_diagnostic

# Trigger execution
final_diagnostic = analyze_signal_pattern(signal_snapshot)
print(f"Target result: {final_diagnostic}")