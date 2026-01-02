def evaluate_performance(skills, difficulty):
    # Core metrics
    base_proficiency = len(skills)
    advanced_skills = {s for s in skills if 'advanced' in s}
    bonus_points = len(advanced_skills) * 2

    # Distractor: irrelevant computation on unused variables
    legacy_modules = [s.replace('advanced_', '') for s in skills if 'legacy' in s]
    deprecated_count = sum(1 for m in legacy_modules if m.startswith('v1'))
    temp_offset = deprecated_count * 0.5  # never used

    # Conditional scaling based on difficulty level
    scaling_factor = 1.0
    if difficulty > 6:
        scaling_factor += 0.8
        if 'advanced_algorithm' in skills:
            scaling_factor += 0.3
    elif difficulty == 5:
        scaling_factor += 0.4

    # Simulate experience decay for outdated skills
    current_year = 2024
    skill_ages = {'advanced_ml': 2, 'api_integration': 3, 'advanced_algorithm': 1}
    decay_penalty = 0
    for skill, age in skill_ages.items():
        if skill in skills and age > 2:
            decay_penalty += 1

    # Accumulate score with multiple factors
    raw_score = base_proficiency * 10 + bonus_points * 5 - decay_penalty * 3
    adjusted_score = raw_score * scaling_factor

    # Secondary distractor: complex but unused data structure
    skill_hierarchy = {
        level: [s for s in skills if len(s) % 3 == i]
        for i, level in enumerate(['short', 'medium', 'long'])
    }
    deep_analysis_flag = any(len(v) > 2 for v in skill_hierarchy.values())  # not used

    # Final performance model
    stability_bonus = 5 if 'advanced_algorithm' in skills and difficulty > 6 else 0
    final_score = int(adjusted_score + stability_bonus)

    return final_score


# Simulation setup
skill_set = ['basic_logic', 'advanced_ml', 'api_integration', 'advanced_algorithm']
challenge_level = 8

# Execute key statement
final_score = evaluate_performance(skill_set, challenge_level)
print(f"Result: {final_score}")