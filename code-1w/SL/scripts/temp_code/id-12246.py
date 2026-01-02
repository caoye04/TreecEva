def evaluate_performance(base, missions, efficiency):
    base_score = base * efficiency
    adjusted_base = int(base_score) + 10 if base_score >= 50 else int(base_score) + 5
    
    # Irrelevant tracking variable (minor distractor)
    status_report = "Active" if missions > 3 else "Review"
    
    completed_missions = len([m for m in missions])
    bonus = 25
    penalty = -10
    final_score = adjusted_base + (bonus if completed_missions > 4 else penalty)
    
    # Print result for clarity
    print(f"Result: {final_score}")
    
    return final_score

# Input values
task_base = 45
task_missions = [1, 2, 3, 4, 5]
efficiency_factor = 1.2

result = evaluate_performance(task_base, task_missions, efficiency_factor)