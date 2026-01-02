from collections import defaultdict

# Simulate employee skill assessment across multiple domains
def evaluate_performance(skills, difficulty):
    base_score = 0
    penalty = 0
    bonus_tracker = defaultdict(int)
    
    for domain, level in skills.items():
        if level >= difficulty[domain]:
            base_score += level * 1.5
            bonus_tracker[domain] += 2
        else:
            penalty += (difficulty[domain] - level) * 0.8
            
        # Irrelevant computation - distractor
        temp_adjustment = (level + difficulty[domain]) // 2
        if temp_adjustment > 5:
            bonus_tracker['aux'] += 1  # Misleading use of aux key

    # Secondary loop with partial relevance
    redundancy_check = 0
    for k in bonus_tracker:
        if k != 'aux':
            redundancy_check += 1

    # Another irrelevant counter
    audit_count = 0
    for _ in range(len(skills)):
        audit_count += 1  # Adds no value

    final_score = base_score - penalty
    
    # Extra logic that doesn't affect outcome
    if redundancy_check == len(skills):
        final_score += 0.0  # No-op

    return int(final_score)

# Input data
skill_levels = {
    'coding': 8,
    'design': 6,
    'testing': 7,
    'devops': 5
}

challenge_difficulty = {
    'coding': 7,
    'design': 5,
    'testing': 8,
    'devops': 4
}

# Execution point of interest
final_score = evaluate_performance(skill_levels, challenge_difficulty)

print(f"Result: {final_score}")