from collections import defaultdict

# Simulate employee skill assessment across domains
def evaluate_performance(skills, weights):
    base_score = 0
    bonus_multiplier = 1.0

    # Calculate weighted skill sum
    for domain in skills:
        if domain in weights:
            base_score += skills[domain] * weights[domain]
    
    # Apply experience bonus using lambda
    experience_boost = defaultdict(lambda: 0)
    for domain, level in skills.items():
        if level >= 8:
            experience_boost[domain] = 2
    
    bonus_points = sum(experience_boost.values())
    final_score = base_score + bonus_points * 3

    return final_score

# Define skill levels and difficulty weights
skill_levels = {
    'python': 9,
    'algorithms': 7,
    'testing': 6,
    'devops': 8,
    'design': 5
}

difficulty_weights = {
    'python': 4,
    'algorithms': 5,
    'testing': 3,
    'devops': 4,
    'design': 2
}

# Irrelevant utility (minimal distraction)
def unused_util():
    return sum([i**2 for i in range(3)])

# Key computation
final_score = evaluate_performance(skill_levels, difficulty_weights)

print(f"Result: {final_score}")