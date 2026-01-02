def evaluate_performance(skills, feedback):
    # Normalize skill levels using z-score (irrelevant to final result)
    mean_skill = sum(skills) / len(skills)
    variance = sum((x - mean_skill) ** 2 for x in skills) / len(skills)
    std_dev = variance ** 0.5
    normalized = [(x - mean_skill) / std_dev for x in skills] if std_dev > 0 else skills

    # Track progress through learning phases (partially relevant)
    phases = ['exploration', 'refinement', 'mastery']
    progress_tracker = {phase: False for phase in phases}
    threshold = 75

    # Compute weighted score with experience multipliers (distractor computation)
    exp_weights = [0.2, 0.3, 0.5]
    weighted_sum = sum(skills[i] * exp_weights[i % len(exp_weights)] for i in range(len(skills)))

    # Core logic: count how many skills are above threshold and in feedback set
    skill_names = ['python', 'algorithms', 'design', 'testing', 'devops']
    skill_map = dict(zip(skill_names, skills))
    strong_skills = {name for name, level in skill_map.items() if level >= threshold}
    feedback_set = set(feedback)

    # Determine overlap between strong skills and feedback (semi-relevant)
    validated_skills = strong_skills.intersection(feedback_set)

    # Additional state tracking (distractor)
    improvement_candidates = {name for name, level in skill_map.items() if level < 60}
    stability_ratio = len([x for x in skills if 60 <= x <= 80]) / len(skills)

    # Final performance score based on unique contributions
    base_score = len(validated_skills) * 100
    bonus = 0
    for idx, (name, level) in enumerate(skill_map.items()):
        if name in validated_skills and level > 85:
            bonus += 10 + idx  # Extra credit for high mastery

    # Irrelevant sorting operation
    sorted_feedback = sorted(list(feedback_set), key=str.lower)

    # Critical assignment point
    final_score = base_score + bonus
    return final_score

# Input data
skill_levels = [88, 76, 92, 65, 81]
feedback_list = ['python', 'algorithms', 'devops']

# Execution flow
interim_result = sum(skill_levels) // len(skill_levels)  # distractor
auxiliary_data = {k: v for k, v in enumerate(skill_levels)}  # unused structure
result_buffer = []

final_score = evaluate_performance(skill_levels, feedback_list)
print(f"Result: {final_score}")