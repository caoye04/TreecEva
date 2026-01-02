def preprocess_signal(raw_input):
    # Irrelevant transformation chain (distractor)
    temp_a = [x ** 2 for x in raw_input if x % 2 == 0]
    temp_b = [x for x in raw_input if x > 0]
    filtered = list(set(temp_b))  # Redundant filtering
    normalized = [round(x / max(filtered), 3) for x in filtered] if filtered else [0]
    
    # Critical path disguised among noise
    shifted = [x << 1 for x in raw_input]  # Bit shift relevant to final logic
    masked = [x & 7 for x in shifted]     # Extract lower 3 bits — key operation
    return masked


def transform_sequence(seq):
    # String-based decoy processing
    seq_str = ''.join(map(str, seq))
    reversed_chunks = [seq_str[i:i+3][::-1] for i in range(0, len(seq_str), 3)]
    concat = ''.join(reversed_chunks)
    
    # Decoy counting
    count_ones = sum(1 for c in concat if c == '1')
    padding_length = len(concat) % 4
    if padding_length:
        concat += 'X' * (4 - padding_length)
    
    # Real transformation: interpret as digits and mod 9
    interpreted = [int(c) for c in concat if c.isdigit()]
    reduced = [x % 9 for x in interpreted if x > 0]  # Used later
    return reduced

# Dead function — never called (red herring)
def legacy_calibrate(data):
    cumulative = 0
    for i in range(len(data)):
        if i % 3 == 0:
            cumulative += data[i] * 2
        elif i % 5 == 0:
            cumulative -= data[i]
    return cumulative // 2 if cumulative else 0

# Unused helper (distraction)
def rolling_average(series, window=3):
    avgs = []
    for i in range(len(series) - window + 1):
        avgs.append(sum(series[i:i+window]) / window)
    return avgs

# Key analysis function
def analyze_pattern(pattern):
    # Character frequency distractor
    pattern_str = ''.join(map(str, pattern))
    freq_map = {c: pattern_str.count(c) for c in set(pattern_str)}
    
    # Slicing operation (required Python feature)
    segment = pattern[::2]  # Every other element
    
    # Boolean logic with short-circuiting (core concept)
    base_score = 0
    if len(pattern) > 5 and (sum(pattern) // len(pattern)) >= 3:
        base_score += 10
    
    # Conditional arithmetic branching (relevant)
    adjustment = 0
    for val in segment:
        if val == 0:
            continue
        elif val == 3:
            adjustment += 5
        elif val > 4:
            adjustment -= 2
    
    # Critical computation hidden in loop
    accumulator = 0
    for i, v in enumerate(pattern):
        if i % 2 == 1:  # Odd indices only
            accumulator += v * (i + 1)  # Weighted sum
    
    # Final logic — depends on accumulator
    if accumulator > 20:
        result = accumulator // 3
    else:
        result = accumulator * 2
    
    # Distractor: string method usage
    label = "diagnostic_result".upper().replace('_', '-')
    metadata_tag = f"{label}:V1"
    
    # Actual answer variable
    final_diagnostic = result + adjustment
    return final_diagnostic

# Main execution flow
if __name__ == '__main__':
    # Initial data (real input)
    sensor_readings = [12, 7, 3, 8, 1, 6, 4]
    
    # Irrelevant intermediate variables (distractors)
    baseline_offset = 2.5
    calibration_matrix = [[1, 0], [0, 1]]
    timestamp_log = "2023-11-05T14:32:00Z"
    
    # Step 1: Preprocess signal (bit manipulation pathway)
    processed = preprocess_signal(sensor_readings)
    
    # Step 2: Transform into sequence using string slicing logic
    transformed_data = transform_sequence(processed)
    
    # Step 3: Analyze final pattern (answer point)
    final_diagnostic = analyze_pattern(transformed_data)
    
    # Output result
    print(f"Result: {final_diagnostic}")