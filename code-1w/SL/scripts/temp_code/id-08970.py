def process_segments(data, importance_weights):
    total_segments = len(data)
    base_score = 0
    penalty_adjustment = 0
    temp_result = []

    # Irrelevant pre-processing: counting vowels in segment labels
    vowel_count = 0
    for label, _ in data:
        for char in label.lower():
            if char in 'aeiou':
                vowel_count += 1

    # Semi-relevant normalization factor based on weight sum (not fully used)
    norm_factor = sum(importance_weights) / len(importance_weights) if importance_weights else 1

    # Core logic: score calculation with conditional adjustments
    for i, (label, value) in enumerate(data):
        weight = importance_weights[i % len(importance_weights)]
        raw_contribution = value * weight
        
        # Conditional bonus/penalty based on index and value magnitude
        if i % 2 == 0:
            if value > 50:
                raw_contribution *= 1.1
            else:
                penalty_adjustment -= 3
        else:
            if value < 30:
                raw_contribution *= 0.9

        # Track intermediate results (only final sum matters)
        temp_result.append(raw_contribution)
        base_score += raw_contribution

    # Secondary loop: character analysis (mostly irrelevant)
    all_chars = ''.join([label for label, _ in data])
    char_freq = {}
    for c in all_chars:
        char_freq[c] = char_freq.get(c, 0) + 1

    # Dummy bitwise manipulation (distractor)
    magic_flag = 0
    for freq in char_freq.values():
        magic_flag ^= freq & 7

    # Final adjustment using only base_score and fixed logic
    stability_check = len(temp_result) > 0 and base_score > 0
    final_score = int(base_score - penalty_adjustment)

    # Dead code path (never executed under normal input)
    if magic_flag > 100:
        final_score = int(final_score * 0.95)

    return final_score

# Input data setup
segment_data = [
    ('alpha', 65),
    ('beta', 42),
    ('gamma', 73),
    ('delta', 28)
]
weights = [1.2, 0.8, 1.0]

# Execute main logic
final_score = process_segments(segment_data, weights)
print(f"Result: {final_score}")