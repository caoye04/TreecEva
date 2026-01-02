def evaluate_performance(skills, log):
    # Initialize relevant metrics
    proficiency_levels = {'coding': 3, 'design': 5, 'testing': 4, 'docs': 2}
    task_weights = {'implement': 1.5, 'review': 0.8, 'debug': 2.0, 'document': 0.6}
    
    # Irrelevant baseline tracker (distractor)
    idle_time = 0
    for entry in log:
        if entry[1] == 'idle':
            idle_time += 1  # Not used in final calculation

    # Core logic: compute weighted activity score
    total_effort = 0
    skill_bonus = 0
    recent_tasks = []

    for timestamp, action in log:
        base_value = 1
        if action in task_weights:
            base_value = task_weights[action]
        
        effort_contribution = base_value * (timestamp % 4 + 1)
        total_effort += effort_contribution
        
        # Track recent tasks for bonus calculation (semi-relevant)
        recent_tasks.append(action)
        if len(recent_tasks) > 3:
            recent_tasks.pop(0)
    
    # Apply skill multiplier from dictionary
    for skill, level in skills.items():
        if skill in proficiency_levels:
            skill_bonus += level * proficiency_levels[skill]
    
    # Misleading intermediate calculation (dead path)
    phantom_score = 0
    for i in range(len(log)):
        if i % 5 == 0:
            phantom_score += i * 0.1  # Never used

    # Final performance formula
    raw_score = total_effort * 1.2 + skill_bonus * 0.9
    
    # Normalize based on active entries
    active_count = len([x for x in log if x[1] != 'idle'])
    if active_count > 0:
        raw_score /= active_count
    
    final_score = int(raw_score * 10) / 10.0  # Rounded to one decimal

    return final_score

# Input data
skill_map = {'coding': 4, 'testing': 5, 'design': 3}
activity_log = [
    (1, 'implement'), (2, 'review'), (3, 'debug'),
    (4, 'implement'), (5, 'idle'), (6, 'review'),
    (7, 'document'), (8, 'debug')
]

# Execution point
final_score = evaluate_performance(skill_map, activity_log)
print(f"Result: {final_score}")