def analyze_sequence(data):
    # Irrelevant transformation (distractor)
    transformed = [x ** 2 for x in data if x % 2 == 0]
    temp_sum = sum(transformed)  # Not used later

    # Core logic: count characters in binary representation
    binary_str = ''.join([bin(x)[2:] for x in data])
    ones_count = binary_str.count('1')
    zeros_count = binary_str.count('0')

    # Use slicing to extract middle bits (semi-relevant)
    mid_section = binary_str[len(binary_str)//4 : len(binary_str)//4*3]
    mid_ones = mid_section.count('1')

    # Modular arithmetic on counts
    stability_index = (ones_count * 3 - zeros_count * 2) % 17

    # Return a derived metric
    return ones_count + (stability_index * 2)


def track_metrics(history):
    # Dead code path (distractor)
    if len(history) > 100:
        peak = max(history)
        baseline = sum(history) / len(history)
    else:
        peak = None
        baseline = 0

    # Unused aggregation
    rolling_avg = [sum(history[i:i+3]) / 3 for i in range(len(history)-2)]

    # Actual relevant computation
    recent = history[-5:]
    return sum(recent) % 9


def evaluate_performance():
    # Input sequence with domain-specific meaning
    signal_sequence = [13, 7, 11, 14, 8, 6, 9]
    
    # Distractor variables
    noise_floor = [x ^ 5 for x in signal_sequence]
    filtered = [x for x in noise_floor if x > 4]
    cumulative = 0
    for val in filtered:
        cumulative += val % 6

    # Main analysis chain
    score_a = analyze_sequence(signal_sequence)
    score_b = track_metrics(signal_sequence)
    
    # Secondary irrelevant calculation
    entropy_proxy = 0
    for x in signal_sequence:
        if x > 5:
            entropy_proxy += (x % 4) * 0.5

    # Final integration using slicing and modular arithmetic
    history_slice = signal_sequence[1:-1]  # Exclude first and last
    correction_factor = len(history_slice[::2])  # Every other element count
    
    final_score = score_a + score_b * 3 + correction_factor
    
    # Output required result
    print(f"Result: {final_score}")
    return final_score

# Entry point
result = evaluate_performance()