def calculate_rating(entries, penalties):
    base_score = 0
    adjustment_factor = 0.0
    temp_result = 0

    # Process contribution types and apply weights
    weights = {'code': 3, 'docs': 2, 'test': 2.5, 'design': 4}
    for key in entries:
        if key in weights:
            base_score += entries[key] * weights[key]

    # Irrelevant computation: tracking unused category stats
    category_count = {k: 1 for k in entries.keys()}
    total_categories = len(category_count)  # Not used later

    # Apply penalty scaling based on violation severity
    severity_scale = {'minor': 1, 'medium': 2, 'critical': 5}
    penalty_deduction = 0
    for issue, count in penalties.items():
        if issue in severity_scale:
            penalty_deduction += count * severity_scale[issue]

    # Simulate legacy threshold check (no effect)
    legacy_threshold = 100
    if base_score > legacy_threshold:  # Dead logic path
        adjustment_factor += 5.0

    # Real adjustment: reduce score by half the penalty deduction
    adjustment_factor -= penalty_deduction * 0.5

    # Complex but necessary final computation
    running_total = base_score + adjustment_factor

    # Secondary validation pass (some values reused)
    validation_pass = True
    for val in entries.values():
        if val < 0:
            validation_pass = False
            break

    # Final scoring with conditional bonus
    final_score = running_total
    if validation_pass and running_total > 20:
        final_score += 10  # Bonus for clean record and solid base

    return final_score

# Input data
contributions = {'code': 7, 'docs': 4, 'test': 6, 'design': 3}
penalty_map = {'minor': 3, 'medium': 2}

# Misleading intermediate calculations
buffer_size = 256
scaling_constant = buffer_size / 8  # Unused in logic
intermediate_checksum = sum(contributions.values()) * 2  # Distractor

# Key execution point
final_score = calculate_rating(contributions, penalty_map)

# Output result
print(f"Result: {final_score}")