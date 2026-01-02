def analyze_performance(scores, threshold=75):
    # Track passing scores using list comprehension
    passing = [s for s in scores if s >= threshold]
    failing = [s for s in scores if s < threshold]
    
    # Auxiliary metrics (some are distractions)
    avg_passing = sum(passing) / len(passing) if passing else 0
    improvement_potential = len(failing) * 5  # Not used in final result
    max_score_gap = threshold - min(failing) if failing else 0

    # Compute weighted contribution from different tiers
    high_performers = len([s for s in passing if s >= 90])
    mid_performers = len([s for s in passing if 75 <= s < 90])

    # Apply non-linear weighting
    performance_bonus = 0
    if high_performers > 2:
        performance_bonus += 10
    elif mid_performers >= 3:
        performance_bonus += 5

    # Hidden logic: adjust based on distribution symmetry
    sorted_scores = sorted(scores)
    median = sorted_scores[len(sorted_scores)//2]
    symmetric_deviation = abs(sorted_scores[-1] - median) - abs(median - sorted_scores[0])

    # Distractor computation: looks important but unused
    normalized_variance = sum((s - sum(scores)/len(scores))**2 for s in scores) / len(scores) if scores else 0
    stability_index = 100 - normalized_variance

    # Core scoring logic
    base_score = len(passing) * 8
    tier_bonus = high_performers * 3 + mid_performers * 2
    
    # Final adjustment based on symmetry (only actual use of symmetric_deviation)
    symmetry_penalty = 0
    if symmetric_deviation > 10:
        symmetry_penalty = 4
    elif symmetric_deviation < -10:
        symmetry_penalty = 2

    total = base_score + tier_bonus + performance_bonus - symmetry_penalty
    return int(total)

# Main execution
student_scores = [88, 92, 76, 81, 64, 94, 85, 73]

# Irrelevant preprocessing (distraction)
doubled_scores = [2*s for s in student_scores]
filtered_doubled = [ds for ds in doubled_scores if ds > 150]
score_summary = {
    'count': len(student_scores),
    'peak': max(student_scores),
    'floor': min(student_scores)
}

# Unused helper function (dead code path)
def calculate_zscore(val, mean, std):
    return (val - mean) / std if std != 0 else 0

# Key statement
final_score = analyze_performance(student_scores)

# Output result
print(f"Target result: {final_score}")