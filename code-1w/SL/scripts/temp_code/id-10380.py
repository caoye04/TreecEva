def evaluate_performance(skills, challenges):
    cumulative = 0
    bonuses = {1: 5, 2: 3, 3: 2}
    base_adjustment = 1.5
    
    for idx, (skill, difficulty) in enumerate(zip(skills, challenges)):
        effort = skill - difficulty
        if effort > 0:
            level = min(effort, 3)
            cumulative += effort * base_adjustment + bonuses[level]
    
    return int(cumulative)

# Irrelevant auxiliary data (mild distraction)
employee_ids = [101, 102, 103]
salary_scale = {'junior': 50, 'senior': 80}

skill_levels = [7, 5, 4]
challenge_difficulties = [5, 3, 6]

final_score = evaluate_performance(skill_levels, challenge_difficulties)
print(f"Result: {final_score}")