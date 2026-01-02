def evaluate_performance(acc, comp):
    base_score = acc * 100
    penalty = 0

    # Complexity adjustment with conditional expression
    adjustment = 1.5 if comp > 2 else (0.8 if comp == 2 else 0.5)
    adjusted_score = base_score * adjustment

    # Irrelevant computation (distractor)
    theoretical_max = 100 * adjustment
    unused_buffer = (theoretical_max - adjusted_score) * 0.1

    # Simulate tolerance thresholds
    thresholds = [60, 70, 85, 90]
    passed_levels = 0
    for t in thresholds:
        if base_score >= t:
            passed_levels += 1

    # Additional state tracking (semi-relevant)
    level_bonus = passed_levels * 3

    # Use of set operations to filter valid bonuses
    valid_bonuses = {1, 2, 3, 4, 5}
    if level_bonus in valid_bonuses:
        adjusted_score += level_bonus

    # Final performance cap
    if adjusted_score > 95:
        adjusted_score = 95 + (adjusted_score - 95) * 0.5  # Diminishing returns

    return int(adjusted_score)

# Main execution
accuracy = 0.87
complexity_factor = 3
temp_data = [i * i for i in range(10) if i % 3 == 0]  # Dead-end list comprehension
buffer_cache = {x: x*2 for x in temp_data}  # Unused dictionary

scaling_constant = 42  # Irrelevant constant
scaling_constant *= 2  # Distractor operation

final_score = evaluate_performance(accuracy, complexity_factor)
print(f"Result: {final_score}")