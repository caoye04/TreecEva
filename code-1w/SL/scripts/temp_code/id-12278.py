def process_performance_metrics(levels, errors):
    # Irrelevant transformation (distractor)
    normalized_errors = [round(e ** 0.5, 2) for e in errors if e > 0]
    temp_adjustment = sum([e * 0.1 for e in normalized_errors])

    # Core logic: compute weighted score based on skill levels
    base_scores = []
    for level in levels:
        if level < 2:
            base_scores.append(10)
        elif level < 5:
            base_scores.append(25)
        else:
            base_scores.append(40)

    total_base = sum(base_scores)

    # Bonus for high performers
    high_performer_bonus = 0
    for level in levels:
        if level >= 6:
            high_performer_bonus += 8

    # Penalty calculation based on string-encoded error flags
    error_string = "".join([chr(97 + int(e % 26)) for e in errors])  # a-z encoding
    uppercase_count = len([c for c in error_string.upper() if c in 'AEIOU'])  # red herring
    penalty = 0
    for c in error_string:
        if c in 'bcdfg':
            penalty += 3

    # Final adjustment using case conversion and list comprehension
    flag_indicators = [c.upper() for c in error_string[:3]]
    if 'X' in flag_indicators:
        penalty += 10

    final_score = total_base + high_performer_bonus - penalty

    # Dead code path (never executed due to logic above)
    if len(flag_indicators) > 5:
        final_score *= 1.1

    return final_score

# Input data
skill_levels = [1, 6, 3, 7, 4]
error_log = [12, 5, 0, 18, 3]

# Execution point
final_score = process_performance_metrics(skill_levels, error_log)
print(f"Target result: {final_score}")