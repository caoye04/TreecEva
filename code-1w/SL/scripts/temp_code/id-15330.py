def evaluate_performance(skills, challenges):
    # Irrelevant preprocessing: count total characters in skill names
    total_chars = sum(len(skill) for skill in skills.keys())
    dummy_offset = total_chars % 7

    # Relevant: determine mastered skills based on thresholds
    mastered = set()
    for skill, level in skills.items():
        if level >= challenges.get(skill, 80):
            mastered.add(skill)

    # Distractor: unused computation on unrelated metric
    avg_skill = sum(skills.values()) / len(skills) if skills else 0
    penalty = 0
    if avg_skill < 75:
        penalty = 10  # This path is not taken in this case

    # Semi-relevant: map proficiency categories
    proficiency_map = {
        'basic': [s for s in skills if skills[s] < 60],
        'intermediate': [s for s in skills if 60 <= skills[s] < 85],
        'advanced': [s for s in skills if skills[s] >= 85]
    }

    # Core logic: score calculation
    base_score = len(mastered) * 25
    challenge_bonus = 0
    for skill in mastered:
        if skills[skill] > 90:
            challenge_bonus += 15

    # Additional red herring: unused data structure transformation
    skill_pairs = [(s1, s2) for s1 in skills for s2 in skills if s1 != s2 and abs(skills[s1] - skills[s2]) < 10]
    pair_count = len(skill_pairs)  # Not used

    final_score = base_score + challenge_bonus - dummy_offset
    return final_score


# Main execution context
skill_levels = {
    'algorithms': 92,
    'data_structures': 87,
    'machine_learning': 74,
    'software_design': 95
}
challenge_thresholds = {
    'algorithms': 85,
    'data_structures': 80,
    'machine_learning': 70,
    'software_design': 90
}

tracking_log = []  # Unused logging structure
for module in skill_levels:
    tracking_log.append(f"Reviewing {module}")  # Distractor loop

final_score = evaluate_performance(skill_levels, challenge_thresholds)
print(f"Result: {final_score}")