def evaluate_performance(raw_score, penalty_rate, thresholds):
    base_points = int(raw_score // 10)
    deduction = round(base_points * penalty_rate)
    adjusted_base = base_points - deduction
    
    # Track skill mastery levels
    mastery_levels = {}
    for level, threshold in enumerate(thresholds):
        if raw_score >= threshold:
            mastery_levels[f'level_{level}'] = True
    
    # Irrelevant tracking variable (minor distraction)
    unused_count = sum(1 for v in mastery_levels.values() if v)
    
    final_score = adjusted_base + len(mastery_levels)
    return final_score

# Main execution
raw_input = 87.5
penalty = 0.2
required = [50, 60, 75, 85]
result = evaluate_performance(raw_input, penalty, required)
print(f"Result: {result}")