def analyze_text_pattern(input_str):
    char_frequency = {}
    for char in input_str:
        char_frequency[char] = char_frequency.get(char, 0) + 1

    unique_chars = set(char_frequency.keys())
    vowel_set = {'a', 'e', 'i', 'o', 'u'}
    consonants = unique_chars - vowel_set

    # Distraction: Count total pairs (not used in final logic)
    total_pairs = 0
    for count in char_frequency.values():
        if count > 1:
            total_pairs += count // 2

    # Base score from unique consonants
    base_points = len(consonants) * 7

    # Secondary distraction: reverse frequency mapping (unused)
    reversed_freq = {v: k for k, v in char_frequency.items()}

    # Determine repeating chars for penalty consideration
    repeating_chars = [char for char, count in char_frequency.items() if count > 2]
    long_repeats = [c for c in repeating_chars if input_str.count(c*3) > 0]  # check triple occurrence

    # Real penalty logic: number of chars repeated 3+ times
    raw_penalty = len(repeating_chars) * 3
    extra_grace = 1 if len(long_repeats) < 2 else 0
    penalty_adjustment = raw_penalty - extra_grace

    # Final computation
    final_score = base_points - penalty_adjustment

    # Dead code path - never executed under normal conditions
    if False:
        fallback = sum([ord(c) for c in unique_chars])
        final_score = fallback % 100

    return final_score

# Execution entry point
text_sample = "abracadabra"
result = analyze_text_pattern(text_sample)
print(f"Result: {result}")