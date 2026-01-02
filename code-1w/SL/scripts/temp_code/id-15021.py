def calculate_final_score(records, importance):
    base_total = 0
    bonus_adjustment = 0
    penalty_tracker = []
    temp_result = 0

    # Irrelevant pre-processing (distractor)
    normalized_data = {k: v / sum(records.values()) for k, v in records.items()}
    for key in normalized_data:
        if normalized_data[key] < 0.1:
            penalty_tracker.append(key)

    # Core logic begins
    for item, value in records.items():
        weight = importance.get(item, 1)
        raw_contribution = value * weight
        
        # Conditional adjustment based on thresholds
        if value > 50:
            bonus_adjustment += 5
        elif value < 30:
            bonus_adjustment -= 3
        
        base_total += raw_contribution

    # Secondary processing with string manipulation (semi-relevant)
    keys_str = ''.join(records.keys())
    extra_boost = len(keys_str.split('e')) - 1  # Slight boost if 'e' appears multiple times

    # Accumulate final score
    final_score = base_total + bonus_adjustment + extra_boost

    # Dead code path (irrelevant)
    if final_score < 0:
        fallback = sum(records.values())
        final_score = fallback % 100

    return final_score

# Input data
performance_data = {
    'efficiency': 65,
    'accuracy': 45,
    'scalability': 70,
    'usability': 25
}

weights = {
    'efficiency': 1.2,
    'accuracy': 0.8,
    'scalability': 1.5,
    'usability': 0.6
}

# Misleading intermediate calculation (distractor)
baseline_avg = sum(performance_data.values()) / len(performance_data)
scaled_projection = baseline_avg * 1.15

# Key execution point
final_score = calculate_final_score(performance_data, weights)

print(f"Result: {final_score}")