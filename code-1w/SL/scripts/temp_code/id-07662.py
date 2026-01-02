def process_results(entries, bonus):
    # Helper lambda for filtering valid scores
    is_valid = lambda x: x >= 50

    filtered = [e for e in entries if is_valid(e)]
    
    # Irrelevant string processing (distractor)
    status_messages = ['pass' if score >= 70 else 'fail' for score in entries]
    summary = ''.join(status_messages).upper().replace('PASS', 'P').count('P')

    base_sum = sum(filtered)
    count = len(filtered)

    # Dead code path (never executed due to data)
    outlier_count = 0
    for val in filtered:
        if val > 150:  # Impossible condition
            outlier_count += 1

    # Modular arithmetic and integer division
    adjustment = (base_sum % 13) // 2
    
    # Multiple assignments (tuple unpacking)
    multiplier, offset = bonus, 5

    # Core logic hidden among distractions
    raw_score = (base_sum // count) if count > 0 else 0
    boosted = raw_score * multiplier
    final_score = boosted - adjustment + offset

    # Unused variable (red herring)
    temp_result = [x * bonus for x in filtered if x < 60]

    return final_score

# Data setup
raw_data = [45, 70, 55, 80, 40, 90, 60]
bonus_factor = 3

# Key execution point
final_score = process_results(raw_data, bonus_factor)
print(f"Result: {final_score}")