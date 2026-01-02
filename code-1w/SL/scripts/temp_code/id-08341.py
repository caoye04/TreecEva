def evaluate_performance(metrics, thresholds):
    # Initialize tracking variables
    base_score = 0
    penalty_count = 0
    bonus_applied = False

    # Irrelevant distraction: unused list for hypothetical metrics
    hypothetical_metrics = [x * 1.5 for x in range(10)]

    # Core logic begins
    high_performers = {x for x in metrics if x > thresholds[0]}
    medium_performers = {x for x in metrics if thresholds[1] < x <= thresholds[0]}
    low_performers = {x for x in metrics if x <= thresholds[1]}

    # Distraction: dead code path (never executed due to fixed condition)
    debug_mode = False
    if debug_mode:
        print(f'High: {high_performers}, Medium: {medium_performers}')

    # Scoring logic with interdependent steps
    base_score += len(high_performers) * 10
    base_score += len(medium_performers) * 4
    
    for val in metrics:
        if val < thresholds[2]:
            penalty_count += 1

    # Apply penalty if more than 2 severe underperformers
    if penalty_count > 2:
        base_score -= 15

    # Bonus condition using set intersection (semi-relevant)
    target_set = {85, 90, 95, 100}
    exceptional_overlap = high_performers & target_set
    if len(exceptional_overlap) >= 2:
        base_score += 20
        bonus_applied = True

    # Unused computation: misleading efficiency ratio
    efficiency_ratio = sum(metrics) / len(metrics) if metrics else 0  # Not used

    # Final adjustment based on conditional chain
    final_score = base_score
    if bonus_applied and len(low_performers) == 0:
        final_score += 10

    return final_score

# Main execution context
productivity_data = [78, 82, 85, 90, 65, 93, 88]
threshold_levels = [85, 75, 60]  # High, medium, fail thresholds

# Dummy preprocessing (distraction)
processed_data = [x + 2 for x in productivity_data]
dropped_values = [x for x in processed_data if x < 70]

# Key execution point
final_score = evaluate_performance(productivity_data, threshold_levels)
print(f'Result: {final_score}')