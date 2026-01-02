def preprocess_segment(segment):
    """Irrelevant preprocessing function that normalizes signal segments."""
    return [x / max(segment) for x in segment]


def compute_entropy(data):
    """Misleading entropy calculation - not used in final result."""
    from math import log
    freq = {}
    for d in data:
        freq[d] = freq.get(d, 0) + 1
    total = len(data)
    entropy = 0
    for count in freq.values():
        p = count / total
        entropy -= p * log(p)
    return round(entropy, 4)


def generate_checksum(sequence):
    """Dead code path: generates a checksum but never called."""
    chk = 0
    for i, val in enumerate(sequence):
        chk ^= (val + i) << 2
    return chk & 0xFFFF

# Irrelevant global constants
MAX_BUFFER_SIZE = 1024
DEFAULT_TIMEOUT = 0.5
CALIBRATION_FACTOR = 0.987
NOISE_FLOOR = [-0.01, 0.02, -0.03, 0.01]

# Simulated sensor data buffer (mixed valid and dummy)
data_stream = [
    [12, 8, 15, 7],
    [6, 11, 9, 14],
    [13, 5, 10, 6],
    [9, 12, 11, 8]
]

# Threshold map with red herring entries
threshold_map = {
    'low': 6,
    'medium': 10,
    'high': 13,
    'critical': 15,
    'unused_mode': 20  # decoy value
}

# Auxiliary diagnostic variables (mostly irrelevant)
current_state_flag = 0b1010
state_history = []
running_diagnostics = True

# Core processing function with key logic buried in distractions
def analyze_signal_pattern(buffer, thresholds):
    cumulative_score = 0
    penalty_factor = 1.0
    
    # Real logic starts here — analyzing pattern using enumerate and zip
    for idx, row in enumerate(buffer):
        if idx % 2 == 0:
            # Only even-indexed rows contribute
            adjusted_values = [x * (idx + 1) for x in row]  # Amplify by index+1
            
            # Use zip to pair values with static reference (distractor included)
            reference_curve = [8, 9, 10, 11]
            deviations = []
            for val, ref in zip(adjusted_values, reference_curve):
                dev = abs(val - ref)
                deviations.append(dev)
                
                # Actual contribution to answer
                if dev > thresholds['medium']:
                    cumulative_score += int(dev)
                    
            # Irrelevant branching
            if sum(deviations) > 25:
                penalty_factor *= 0.95
                state_history.append('fluctuation')
        else:
            # Odd rows are skipped but contain distracting computations
            temp_snapshot = preprocess_segment(row)
            entropy = compute_entropy([int(x*100) for x in temp_snapshot])
            state_history.append(f'entropy_{entropy}')

    # Decoy transformation (not affecting result)
    transformed_score = (cumulative_score * 1000) ^ 0xABCD
    normalized = transformed_score / 97
    
    # Final computation uses only cumulative_score
    final_weight = len(state_history) or 1
    result = cumulative_score - (5 * (final_weight // 2))
    
    return int(result)

# Misleading early exit guard
if __name__ != '__main__':
    print("Module mode active")
else:
    # Main execution flow
    filtered_segments = []
    for seg in data_stream:
        if sum(seg) > 30:  # filters first and fourth rows
            filtered_segments.append(seg)
    
    # Critical assignment point
    final_diagnostic = analyze_signal_pattern(filtered_segments, threshold_map)
    
    # Output required format
    print(f"Result: {final_diagnostic}")