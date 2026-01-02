def evaluate_performance(skills, difficulty):
    base_potential = len(skills)
    modifier = 0
    
    # Irrelevant computation: track unused learning curve
    learning_curve = [i ** 1.5 for i in range(1, base_potential + 1)]
    temp_sum = sum(learning_curve) / base_potential if base_potential > 0 else 0
    
    # Core logic begins
    proficiency_set = {skill for skill in skills if skill >= difficulty - 2}
    backup_skills = {skill for skill in skills if skill < difficulty - 2}
    
    # Red herring: unused filtering
    filtered_backup = set()
    for s in backup_skills:
        if s % 3 == 0:
            filtered_backup.add(s * 1.1)
    
    # Scoring logic
    raw_score = 0
    for p in proficiency_set:
        if p >= difficulty:
            raw_score += 3
        elif p == difficulty - 1:
            raw_score += 2
        else:
            raw_score += 1
    
    # Apply bonus for diversity
    diversity_bonus = len(proficiency_set.intersection({x+1 for x in proficiency_set}))
    
    # Distractor: complex but unused weight adjustment
    weights = []
    for i in range(len(proficiency_set)):
        weights.append((i + 1) * 0.75)
    avg_weight = sum(weights) / len(weights) if weights else 0
    
    final_score = raw_score + diversity_bonus
    
    return final_score

# Problem setup
skill_levels = [3, 5, 6, 4, 7, 5]
challenge_level = 6

# State tracking variables (some irrelevant)
current_focus = [s for s in skill_levels if s >= 5]
retraining_needed = len([s for s in skill_levels if s < 4])

# Key execution point
target_result = evaluate_performance(skill_levels, challenge_level)
print(f"Result: {target_result}")