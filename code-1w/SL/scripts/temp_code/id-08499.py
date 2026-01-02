def calculate_performance_rating():
    base_points = 85
    bonus_multiplier = 1.2
    penalty_factor = 0.9

    # Track quarterly outputs
    q1_output = 230
    q2_output = 195
    q3_output = 210
    q4_output = 205

    # Calculate average output
    avg_output = (q1_output + q2_output + q3_output + q4_output) / 4

    # Determine efficiency tier
    if avg_output > 200:
        efficiency_bonus = 15
    elif avg_output > 190:
        efficiency_bonus = 10
    else:
        efficiency_bonus = 5

    # Apply logic to compute raw score
    raw_score = base_points + efficiency_bonus

    # Adjust for performance consistency using list comprehension
    deviations = [abs(x - avg_output) for x in [q1_output, q2_output, q3_output, q4_output]]
    consistent_performer = all(d < 20 for d in deviations)

    # Apply multiplier only if consistent
    if consistent_performer:
        raw_score *= bonus_multiplier
    else:
        raw_score *= penalty_factor

    # Round to nearest integer
    final_score = int(round(raw_score))

    return final_score

result = calculate_performance_rating()
print(f"Result: {result}")