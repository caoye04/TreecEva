def evaluate_performance(skills, difficulty):
    base_score = 0
    penalty = 0
    bonus = 0
    temp_result = 0

    # Irrelevant preprocessing: case conversion on string labels
    skill_names = [s['name'].upper() for s in skills]
    normalized_names = [name.replace(' ', '_') for name in skill_names]

    # Actual logic begins: compute weighted proficiency
    for skill in skills:
        level = skill['level']
        category = skill['category']

        if category == 'technical':
            base_score += level * 2.5
        elif category == 'creative':
            base_score += level * 1.8
        else:
            base_score += level * 1.2

        # Distractor: unused conditional branch with dead code
        if level > 10:
            temp_result = (level + 5) // 3  # never used

    # Simulate experience multiplier based on combinatorics of skill count
    n_skills = len(skills)
    combination_factor = 1
    for i in range(1, min(n_skills, 4)):
        combination_factor += i  # simplified combinatorial growth

    # Misleading intermediate calculation (not directly used)
    theoretical_max = n_skills * 10 * 2.5
    efficiency_ratio = base_score / theoretical_max if theoretical_max > 0 else 0
    formatted_ratio = f'{efficiency_ratio:.4f}'  # string distractor

    # Difficulty scaling using dictionary-based modifiers
    difficulty_modifiers = {'easy': 0.8, 'medium': 1.0, 'hard': 1.3, 'extreme': 1.7}
    difficulty_multiplier = difficulty_modifiers.get(difficulty, 1.0)

    # Bonus logic based on skill diversity (uses string method to check categories)
    categories = set(skill['category'] for skill in skills)
    diversity_flag = len(categories) >= 3
    if diversity_flag and 'technical' in categories:
        bonus = 12

    # Apply penalties for low individual skills
    weak_skills = [s for s in skills if s['level'] < 4]
    penalty = len(weak_skills) * 3

    # Final score computation
    final_score = (base_score * difficulty_multiplier) + bonus - penalty

    # Red herring: modify string list but don't use it
    adjusted_names = [name.lower().capitalize() for name in normalized_names]
    name_length_sum = sum(len(name) for name in adjusted_names)  # irrelevant

    return int(final_score)

# Input data
skill_levels = [
    {'name': 'algorithm design', 'level': 9, 'category': 'technical'},
    {'name': 'user interface', 'level': 6, 'category': 'creative'},
    {'name': 'project management', 'level': 5, 'category': 'organizational'},
    {'name': 'data analysis', 'level': 7, 'category': 'technical'},
    {'name': 'team coordination', 'level': 3, 'category': 'organizational'}
]
challenge_difficulty = 'hard'

# Execution point
final_score = evaluate_performance(skill_levels, challenge_difficulty)
print(f"Target result: {final_score}")