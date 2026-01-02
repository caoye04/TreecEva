def process_results(data, limits):
    # Initialize tracking variables
    count_valid = 0
    temp_sum = 0
    penalty_factor = 1.0
    debug_log = []
    
    # Secondary helper logic - partially relevant
    def adjust_value(x, limit):
        if x > limit * 1.5:
            return x * 0.8
        elif x < limit * 0.5:
            return x * 1.1
        return x

    # Preprocess: filter and normalize entries
    normalized = {}
    for key, value in data.items():
        clean_key = key.strip().lower().replace(' ', '_')
        if clean_key.startswith('test') or clean_key.startswith('trial'):
            normalized[clean_key] = abs(value)  # Ensure non-negative

    # Misleading intermediate computation (not used later)
    avg_normalized = sum(normalized.values()) / len(normalized) if normalized else 0
    outlier_count = 0
    for v in normalized.values():
        if v > avg_normalized * 2:
            outlier_count += 1

    # Core scoring logic
    base_scores = []
    for k, v in normalized.items():
        category_cap = limits.get(k.split('_')[0], 100)
        adjusted = adjust_value(v, category_cap)
        capped = min(adjusted, category_cap)
        if capped >= 50:
            count_valid += 1
            temp_sum += capped
        base_scores.append(capped)

    # Sorting is a red herring - only max matters
    base_scores.sort(reverse=True)
    highest_single = base_scores[0] if base_scores else 0

    # Extra distraction: string analysis with no impact
    key_analysis = {k: len(k) for k in normalized.keys()}
    total_chars = sum(key_analysis.values())
    char_penalty = 0.95 if total_chars > 20 else 1.0

    # Final composition
    completeness_bonus = 10 if count_valid >= 3 else 0
    raw_total = temp_sum + completeness_bonus
    stability_modifier = 0.9 if outlier_count > 1 else 1.0

    final_score = int(raw_total * stability_modifier * penalty_factor)  # No actual penalty applied

    # This print is required to output the result
    print(f"Result: {final_score}")
    return final_score

# Input data
user_data = {
    " Test A ": 120,
    "Trial 1": 45,
    "Test B": 85,
    " Trial C ": 60,
    "Control X": 200  # Not included due to key prefix
}
thresholds = {
    "test": 100,
    "trial": 75
}

# Execution point of interest
final_score = process_results(user_data, thresholds)