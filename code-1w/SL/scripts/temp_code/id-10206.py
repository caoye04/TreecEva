def analyze_performance(scores, penalties, bonus_multiplier=1.1):
    # Irrelevant tracking variables (distractors)
    total_entries = len(scores)
    invalid_count = 0
    temp_offset = sum([p % 3 for p in penalties])  # Misleading computation

    # Normalize scores using conditional expression
    normalized = [s * (0.95 if s < 70 else 1.05) for s in scores]

    # Track high performers with enumerate
    high_performer_indices = []
    for idx, score in enumerate(normalized):
        if score > 80:
            high_performer_indices.append(idx)

    # Apply penalty only to specific indices
    adjusted = normalized.copy()
    for i, penalty in enumerate(penalties):
        if i < len(adjusted):
            adjusted[i] -= penalty * 0.2

    # Bonus logic based on string-based flag (uses string method)
    flags = ['good', 'excellent', 'outstanding']
    has_excellence = any('excel' in f.lower() for f in flags)  # Semi-relevant check

    base_score = sum(adjusted)
    bonus = base_score * 0.02 if has_excellence else 0

    # Extra distraction: sorting and grouping not used directly
    sorted_adjusted = sorted(adjusted, reverse=True)
    top_three_avg = sum(sorted_adjusted[:3]) / 3
    group_categories = {i: 'A' if v > top_three_avg else 'B' for i, v in enumerate(adjusted)}

    # Unrelated combinatorics
    pair_count = 0
    for i in range(len(adjusted)):
        for j in range(i + 1, len(adjusted)):
            if (adjusted[i] + adjusted[j]) > 100:
                pair_count += 1

    # Core calculation path
    multiplier = bonus_multiplier if len(high_performer_indices) >= 2 else 1.0
    raw_total = base_score + bonus
    final_score = raw_total * multiplier

    # Dead code branch (never executed due to condition)
    if temp_offset < 0:
        final_score += 1000  # Unused

    return final_score


def calculate_final_score(data_str, config):
    # Parse input string
    raw_scores = list(map(int, data_str.split(',')))
    penalties = [config.get('penalty_offset', 5)] * len(raw_scores)

    # Minor transformation
    processed_scores = [s + (s % 4) for s in raw_scores]

    # Use zip to align with dummy labels
    labels = [f'entry_{i}' for i in range(len(processed_scores))]
    paired_data = list(zip(labels, processed_scores))
    unpacked_scores = [val for _, val in paired_data]  # Redundant unpacking

    # Call main logic
    result = analyze_performance(unpacked_scores, penalties, bonus_multiplier=config['multiplier'])
    return result

# Main execution
if __name__ == '__main__':
    data_input = "72,65,88,90,77"
    config_params = {
        'penalty_offset': 8,
        'multiplier': 1.08
    }
    final_score = calculate_final_score(data_input, config_params)
    print(f"Target result: {final_score}")