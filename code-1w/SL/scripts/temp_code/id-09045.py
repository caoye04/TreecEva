def compute_performance_score(base_points, penalties, target, actual, milestone_threshold):
    raw_score = base_points - sum(penalties)
    adjustment_factor = 0.9 if raw_score < target else 1.1
    adjusted_base = int(raw_score * adjustment_factor)
    
    # Evaluate milestone achievement using string-based criteria
    performance_level = 'high' if actual >= milestone_threshold else 'low'
    achieved_milestone = performance_level == 'high'
    
    bonus = 250
    final_score = adjusted_base + (bonus if achieved_milestone else 0)
    
    # Irrelevant tracking variable (minimal distraction)
    log_entry = f'Score computed at {adjusted_base}'
    
    print(f'Result: {final_score}')
    return final_score

# Execute with realistic input
data_penalties = [10, 5, 3]
result = compute_performance_score(base_points=800, penalties=data_penalties, target=750, actual=920, milestone_threshold=900)