def analyze_pattern(sequence, threshold=5):
    # Irrelevant tracking variables (distractors)
    temp_sum = 0
    debug_log = []
    cycle_count = 0

    # Semi-relevant pre-processing (moderately distracting)
    processed = []
    for idx, val in enumerate(sequence):
        if idx % 2 == 0:
            processed.append(val * 2)
        else:
            processed.append(val + 1)

    # Core logic begins: detect oscillation patterns
    oscillations = 0
    for i in range(1, len(processed) - 1):
        if processed[i-1] < processed[i] > processed[i+1] or processed[i-1] > processed[i] < processed[i+1]:
            oscillations += 1

    # Bitwise weighting of oscillation count (relevant)
    weighted_fluctuation = oscillations ^ 7  # XOR with magic number

    # Secondary path: compute cumulative delta (partially relevant)
    deltas = []
    for a, b in zip(processed, processed[1:]):
        deltas.append(abs(b - a))

    total_drift = sum(deltas) // 2 if deltas else 0

    # Dummy loop with side computation (dead code path)
    hypothetical_gains = 0
    for _ in range(3):
        hypothetical_gains += 10
        if hypothetical_gains > 25:
            break  # Misleading early exit

    # Actual scoring logic (key)
    base_score = weighted_fluctuation * 3
    adjustment = total_drift % 9
    final_score = base_score - adjustment

    # Unused state tracker (distractor)
    stats = {
        'length': len(sequence),
        'oscillations_found': oscillations,
        'total_drift': total_drift,
        'hypothetical_gains': hypothetical_gains
    }

    return final_score


# Driver code
input_seq = [4, 7, 2, 8, 6, 3, 9]
final_score = analyze_pattern(input_seq)
print(f"Result: {final_score}")