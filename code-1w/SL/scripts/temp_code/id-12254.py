def evaluate_performance(skills, difficulty):
    # Calculate effective proficiency using lambda
    proficiency_boost = list(map(lambda lvl: round(lvl ** 0.5), skills))
    base_score = sum(proficiency_boost)

    # Adjust for difficulty using set operations to filter relevant skills
    high_demand_skills = {3, 4, 5, 6}  # Skills above threshold
    relevant_skills_count = len(set(proficiency_boost) & high_demand_skills)

    bonus = relevant_skills_count * 2
    penalty = difficulty // 2

    final_score = base_score + bonus - penalty
    return final_score

# Simulate skill assessment in a coding challenge context
skill_levels = [4, 7, 2, 9, 5]
challenge_difficulty = 6

final_score = evaluate_performance(skill_levels, challenge_difficulty)
print(f"Result: {final_score}")