def preprocess_signal(raw_samples, filter_bias=True):
    processed = []
    offset = sum(raw_samples) // len(raw_samples) if raw_samples else 0
    for sample in raw_samples:
        adjusted = sample - offset
        if filter_bias and abs(adjusted) > 3:
            processed.append(adjusted)
    return processed if len(processed) > 0 else [0]


def generate_sequence(seed_value, length):
    sequence = []
    state = seed_value % 97
    for _ in range(length):
        state = (state * 17 + 31) % 97
        sequence.append(state)
    return sequence  # Unused in final logic


def evaluate_stability(readings):
    baseline = sum(readings[:len(readings)//2]) / len(readings[:len(readings)//2])
    recent = sum(readings[len(readings)//2:]) / len(readings[len(readings)//2:])
    deviation = abs(recent - baseline)
    return deviation > 5


def compute_checksum(data_stream):
    checksum = 0
    for i, val in enumerate(data_stream):
        checksum ^= (val + i) & 0xFF
    return checksum  # Red herring, not used later


def analyze_threshold(log_entries, pattern_template):
    temp_result = 0
    threshold_met = []
    
    # Irrelevant transformation
    inverted_pattern = [10 - x for x in pattern_template if x < 8]
    
    for entry in log_entries:
        # Meaningful slicing and conditional expression
        window = entry[1:-1] if len(entry) > 4 else entry
        active_segments = [x for x in window if x > 2]
        
        # Key computation
        segment_sum = sum(active_segments)
        if segment_sum > 10:
            temp_result += segment_sum % 7
        else:
            temp_result -= len(active_segments)
        
        # Dead logic branch
        if len(active_segments) == 5:
            for _ in range(3):
                temp_result *= 2  # Never reached

    # Distractor: unused list accumulation
    for p in pattern_template:
        if p % 2 == 0:
            threshold_met.append(p * 2)

    # Actual answer derivation
    scaling_factor = 13 if temp_result > 0 else 7
    final_score = (temp_result * scaling_factor) + len(pattern_template)
    
    # Final diagnostic is the target
    final_diagnostic = abs(final_score - 41)
    return final_diagnostic

# Main execution
if __name__ == "__main__":
    sensor_data = [5, 2, 8, 3, 9, 1, 6]
    readings_clean = preprocess_signal(sensor_data, filter_bias=True)
    
    # Generate irrelevant sequence
    noise_sequence = generate_sequence(42, 10)
    
    # Stability check - influences nothing
    unstable = evaluate_stability(sensor_data + [4, 5, 6])
    
    # Checksum computation - red herring
    chk = compute_checksum(readings_clean)
    
    # Construct log entries with nested structure
    diagnostics = [
        [1, 4, 5, 6, 2],
        [3, 7, 8],
        [2, 5, 6, 8, 9, 1],
        [4, 3, 2]
    ]
    
    reference_pattern = [3, 5, 2, 8, 1, 4, 6]
    
    # Critical statement
    final_diagnostic = analyze_threshold(diagnostics, reference_pattern)
    
    print(f"Target result: {final_diagnostic}")