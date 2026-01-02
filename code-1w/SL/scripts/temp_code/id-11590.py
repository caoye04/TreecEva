def analyze_pattern(sequence, threshold=0.75):
    # Irrelevant transformation: character frequency analysis
    char_freq = {}
    for char in sequence:
        char_freq[char] = char_freq.get(char, 0) + 1
    total_chars = sum(char_freq.values())
    entropy = 0
    for count in char_freq.values():
        p = count / total_chars
        entropy -= p * (p and __import__('math').log2(p))

    # Distractor: unused complex structure
    decoy_matrix = [[i ^ j for j in range(len(sequence))] for i in range(4)]
    decoy_checksum = 0
    for row in decoy_matrix:
        for val in row:
            decoy_checksum ^= val

    # Relevant logic begins: extract numeric transitions
    numeric_sequence = [ord(c) % 17 for c in sequence]
    transitions = []
    for i in range(1, len(numeric_sequence)):
        if numeric_sequence[i] > numeric_sequence[i-1]:
            transitions.append(1)
        elif numeric_sequence[i] < numeric_sequence[i-1]:
            transitions.append(-1)
        else:
            transitions.append(0)

    # Use enumerate and zip (required features)
    trend_pairs = list(zip(transitions, transitions[1:]))
    pattern_count = 0
    for idx, (current, next_val) in enumerate(trend_pairs):
        if current == 1 and next_val == -1:  # peak detection
            pattern_count += 1

    # Another red herring: simulate statistical test
    mean_trans = sum(transitions) / len(transitions) if transitions else 0
    variance = sum((x - mean_trans)**2 for x in transitions) / len(transitions) if transitions else 0
    z_score = (mean_trans - 0.1) / (variance**0.5 + 1e-8)

    # Conditional branch with early return decoy
    if z_score > 1.96:
        dummy_result = sum(decoy_matrix[0]) * 0.5
        return int(dummy_result) % 100  # dead end

    # Actual relevant path: set operations on transition indices
    up_indices = {i for i, t in enumerate(transitions) if t == 1}
    down_indices = {i for i, t in enumerate(transitions) if t == -1}
    oscillations = up_indices & {i+1 for i in down_indices}  # overlapping up-down

    # Compute base score
    base_score = len(oscillations) * 13

    # Secondary feature: tuple unpacking and conditional expression
    extra_bonus = 0
    if len(up_indices) > len(down_indices):
        strength, direction = len(up_indices), 'up'
    else:
        strength, direction = len(down_indices), 'down'
    
    modifier = 1.5 if direction == 'up' and entropy > threshold else 0.8

    # Critical distractor: misleading intermediate printed value (not used)
    temp_result = (base_score + strength) * modifier
    _ = (temp_result * 2) % 97  # looks important but isn't

    # Final aggregation with correct answer
    final_components = [base_score, pattern_count * 5, len(char_freq) * 2]
    final_score = sum(final_components) - (len(sequence) // 3)

    # Answer must be printed at the end
    Result: {final_score}
    return final_score

# Execute with input
result = analyze_pattern("CODEXGEN")
print(f"Target result: {result}")