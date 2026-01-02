def analyze_pattern_distribution():
    # Simulate analysis of binary pattern frequencies in a fixed-length sequence
    sequence_length = 8
    threshold = 3
    
    # Generate all 8-bit patterns with at least three 1s
    candidates = []
    for i in range(2 ** sequence_length):
        bit_repr = format(i, '08b')
        ones_count = bit_repr.count('1')
        if ones_count >= threshold:
            candidates.append(i)

    # Misleading computation: analyze symmetry (not used later)
    palindromic_count = 0
    for c in candidates:
        bit_str = format(c, '08b')
        if bit_str == bit_str[::-1]:
            palindromic_count += 1

    # Track transitions between consecutive bits across all candidates
    transition_scores = []
    for c in candidates:
        bit_str = format(c, '08b')
        score = 0
        for j in range(len(bit_str) - 1):
            if bit_str[j] != bit_str[j + 1]:
                score += 1
        transition_scores.append(score)

    # Compute average transition (distractor)
    avg_transition = sum(transition_scores) / len(transition_scores) if transition_scores else 0

    # Identify combinations where transition score exceeds median
    sorted_transitions = sorted(transition_scores)
    median_transition = sorted_transitions[len(sorted_transitions) // 2]

    high_transition_indices = []
    for idx, ts in enumerate(transition_scores):
        if ts > median_transition:
            high_transition_indices.append(idx)

    # Extract corresponding values
    high_transition_values = [candidates[i] for i in high_transition_indices]

    # Further filter: only those divisible by 4
    filtered_by_divisibility = [v for v in high_transition_values if v % 4 == 0]

    # Use set operations to simulate overlap analysis with another rule
    even_ones_candidates = {c for c in candidates if format(c, '08b').count('1') % 2 == 0}
    divisible_by_4_set = set(filtered_by_divisibility)
    valid_combinations = list(even_ones_candidates & divisible_by_4_set)

    # Introduce enumeration and zip usage in a semi-relevant transformation
    indexed_map = list(enumerate(zip(valid_combinations, transition_scores[high_transition_indices[i]] for i in range(len(high_transition_indices)) if candidates[high_transition_indices[i]] in valid_combinations)))
    
    # Final computation
    final_tally = sum(valid_combinations)
    print(f"Result: {final_tally}")

analyze_pattern_distribution()