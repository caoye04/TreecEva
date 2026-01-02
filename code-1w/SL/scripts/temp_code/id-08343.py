def analyze_pattern(sequence):
    counts = {char: sequence.count(char) for char in set(sequence)}
    total_pairs = sum([v // 2 for v in counts.values()])
    unique_chars = len(counts)
    # Distractor variables
    temp_result = [i for i, c in enumerate(sequence) if c == 'A']
    offset_correction = len(temp_result) % 7 if temp_result else 0
    return total_pairs, unique_chars, offset_correction


def evaluate_streak(data):
    streak_value = 0
    max_streak = 0
    for item in data:
        if item > 5:
            streak_value += 1
            max_streak = max(max_streak, streak_value)
        else:
            streak_value = 0
    # Irrelevant computation
    normalized = max_streak / (len(data) or 1)
    dummy_flag = normalized > 0.3
    return max_streak


def calculate_entropy(values):
    from math import log2
    freq = {}
    for v in values:
        freq[v] = freq.get(v, 0) + 1
    entropy = 0.0
    n = len(values)
    for count in freq.values():
        p = count / n
        entropy -= p * log2(p)
    # Unused intermediate
    redundancy = 1 - (entropy / log2(n or 1))
    return entropy


def main():
    input_sequence = "ABACADABBACCAAEB"
    numeric_data = [3, 6, 7, 2, 8, 9, 1, 4, 5, 7, 8, 9, 10]

    # Step 1: Analyze character pattern
    pairs, unique_chars, offset = analyze_pattern(input_sequence)
    
    # Step 2: Evaluate high-value streak
    longest_streak = evaluate_streak(numeric_data)

    # Step 3: Compute entropy (semi-relevant)
    entropy_metric = calculate_entropy(numeric_data)

    # Step 4: Conditional adjustment based on pattern
    adjustment_factor = 2 if pairs >= 5 and unique_chars <= 6 else 1
    
    # Step 5: Intermediate scoring
    base_score = pairs * 3 + longest_streak * 2 + int(entropy_metric)
    adjusted_score = base_score * adjustment_factor

    # Step 6: Apply conditional penalty
    penalty = 0
    if len(input_sequence) > 10:
        penalty += 3
    if 'E' in input_sequence and pairs < 6:
        penalty += 5
    
    # Step 7: Final score calculation (key statement)
    final_score = adjusted_score - penalty

    # Print result
    print(f"Result: {final_score}")
    return final_score

if __name__ == "__main__":
    main()