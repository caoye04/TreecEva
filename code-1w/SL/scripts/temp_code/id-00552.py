def evaluate_candidate(test_scores, attendance_rate, project_complete):
    avg_score = sum(test_scores) / len(test_scores)
    is_attentive = attendance_rate > 0.85
    base_score = avg_score * 0.7
    bonus = 15 if project_complete and is_attentive else 0
    penalty = 10 if not project_complete else 0
    final_rank = base_score + bonus
    rank_status = 'High' if final_rank >= 80 else 'Standard'
    is_eligible = rank_status == 'High' and project_complete
    threshold_score = final_rank if is_eligible else base_score + penalty
    return threshold_score

result = evaluate_candidate([88, 92, 78], 0.88, True)
print(f"Result: {result}")