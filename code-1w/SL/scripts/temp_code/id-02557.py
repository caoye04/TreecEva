def evaluate_performance(feedback):
    score = 0
    bonus = 10
    adjustments = {'minor': -2, 'major': -5, 'critical': -8}
    issues = ['minor', 'minor', 'major']
    for issue in issues:
        if issue in adjustments:
            score += adjustments[issue]
    
    # Irrelevant string processing (distractor)
    report = "Performance review completed."
    report.upper()
    report.replace(" ", "_")

    if score < -10:
        score -= bonus
    else:
        score += bonus
    
    final_score = abs(score)
    return final_score

feedback_dict = {'issues_found': 3, 'severity_levels': ['low', 'low', 'high']}
final_score = evaluate_performance(feedback_dict)
print(f"Result: {final_score}")