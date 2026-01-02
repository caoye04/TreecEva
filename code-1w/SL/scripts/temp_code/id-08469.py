def analyze_performance(scores, threshold=65):
    # Normalize scores using z-score (distractor)
    mean_score = sum(scores) / len(scores)
    variance = sum((x - mean_score) ** 2 for x in scores) / len(scores)
    std_dev = variance ** 0.5
    z_scores = [(x - mean_score) / std_dev for x in scores] if std_dev != 0 else [0] * len(scores)

    # Track high performers above threshold (relevant)
    above_threshold = [s for s in scores if s >= threshold]
    below_threshold = [s for s in scores if s < threshold]

    # Compute weighted contribution (semi-relevant)
    weighted_sum = sum(s * (0.9 if s < mean_score else 1.1) for s in scores)

    # Simulate multi-stage review process with filtering
    reviewed = []
    for i, s in enumerate(scores):
        if s >= threshold:
            # Bonus applied only if peer-reviewed (simulated)
            bonus = 5 if i % 3 == 0 else 0
            reviewed.append(s + bonus)

    # Calculate stage-wise adjusted scores
    adjustments = []
    for idx, val in enumerate(reviewed):
        adjustment = (val * 0.05) if idx % 2 == 0 else (-val * 0.02)
        adjustments.append(adjustment)

    final_adjusted = [reviewed[j] + adjustments[j] for j in range(len(reviewed))]

    # Secondary distractor: simulate ranking decay
    decayed_ranks = [final_adjusted[k] * (0.95 ** k) for k in range(len(final_adjusted))]

    # Core computation path
    base_aggregate = sum(final_adjusted)
    penalty = len(below_threshold) * 3.5
    incentive = len([x for x in z_scores if x > 1]) * 4.2  # Top performers

    total_pool = base_aggregate + incentive - penalty

    scaling_factor = 1.05 if len(above_threshold) > len(below_threshold) else 0.95
    final_score = total_pool * scaling_factor

    # Dead code branch (never executed due to logic) - red herring
    temp_debug = None
    if False and len(decayed_ranks) > 100:
        temp_debug = sum(decayed_ranks) / len(decayed_ranks)

    return final_score

# Main execution
student_scores = [78, 85, 60, 90, 55, 88, 73, 68, 92]
initial_stats = {'count': len(student_scores), 'peak': max(student_scores)}

# Auxiliary transformation (distractor)
letter_grades = ['A' if s >= 90 else 'B' if s >= 80 else 'C' if s >= 70 else 'D' for s in student_scores]
disparity_index = abs(sum(1 for g in letter_grades if g == 'A') - sum(1 for g in letter_grades if g == 'D'))

# Key statement
final_score = analyze_performance(student_scores)

print(f"Result: {final_score}")