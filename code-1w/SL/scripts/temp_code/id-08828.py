def calculate_final_score(scores, deductions):
    base_set = {x for x in scores if x > 0}
    penalty_set = {abs(d) for d in deductions}
    
    if len(base_set) == 0:
        return 0
    
    valid_points = sum(base_set)
    applied_deductions = sum(penalty_set.intersection(base_set))
    
    if applied_deductions > valid_points * 0.5:
        applied_deductions = int(valid_points * 0.5)
    
    net_score = valid_points - applied_deductions
    return max(net_score, 10)

raw_scores = [15, -5, 20, 0, 25, 15]
penalties = [-15, -30, -25, -8]
initial_total = sum(raw_scores)  # distractor: not used in final logic
ignore_count = len([x for x in raw_scores if x <= 0])  # distractor: counts non-positive
final_score = calculate_final_score(raw_scores, penalties)
print(f"Result: {final_score}")