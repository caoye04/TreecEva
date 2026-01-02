def evaluate_performance(skills, limits):
    proficiency = set()
    for domain, level in skills.items():
        if level >= limits.get(domain, 7):
            proficiency.add(domain)

    bonus = 0
    if 'algorithms' in proficiency and 'data_structures' in proficiency:
        bonus = 15

    base = len(proficiency) * 10
    penalty = 0
    temp_var = 0  # irrelevant distractor
    unused_list = [1, 2, 3]  # irrelevant distractor

    for domain in skills.keys():
        if domain not in proficiency:
            penalty += 5

    total = base + bonus - penalty
    return total

skill_levels = {
    'algorithms': 8,
    'data_structures': 9,
    'networks': 5,
    'databases': 6
}

default_thresholds = {
    'algorithms': 7,
    'data_structures': 8,
    'security': 9
}

final_score = evaluate_performance(skill_levels, default_thresholds)
print(f"Result: {final_score}")