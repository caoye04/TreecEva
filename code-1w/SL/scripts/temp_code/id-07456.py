def calculate_performance(records, importance):
    base = 0
    bonus_tracker = []
    penalty_counter = 0
    temp_result = []

    # Irrelevant pre-processing (distractor)
    for i, record in enumerate(records):
        adjusted = record * 1.05
        temp_result.append(adjusted)

    # Real computation begins
    weighted_sum = sum(r * w for r, w in zip(records, importance))
    total_possible = sum(importance)

    # Misleading bonus logic (not actually used)
    for val in records:
        if val > 80:
            bonus_tracker.append(val * 0.1)
        else:
            penalty_counter += 1

    # Core calculation
    efficiency = weighted_sum / total_possible if total_possible != 0 else 0

    # Additional irrelevant string processing (distractor)
    status_labels = ['high' if x > 80 else 'low' for x in records]
    label_count = len([s for s in status_labels if 'high' in s])

    # Final score with red herring variables
    raw_score = efficiency * 100
    final_score = int(raw_score + 0.5)  # Round to nearest integer

    return final_score

# Main data
assessments = [88, 92, 76, 85]
weights = [0.2, 0.3, 0.15, 0.35]

# Unused variables (distraction)
dummy_data = [(x, x**2) for x in range(5)]
placeholder = ''.join(['temp' for _ in range(3)])

# Key execution point
final_score = calculate_performance(assessments, weights)

print(f"Result: {final_score}")