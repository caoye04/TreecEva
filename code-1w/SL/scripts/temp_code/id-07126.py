from collections import defaultdict

# Student assessment scores and bonus rules
def calculate_final(scores, extra):
    base = sum(scores.get('exam', [0]))
    project_bonus = extra['project'] if scores['project_count'] > 0 else 0
    participation = scores.get('participation', 0)
    return base + project_bonus + participation

# Irrelevant distraction: unused grading scale
grading_scale = lambda g: 'A' if g >= 90 else 'B' if g >= 80 else 'C'

# Data setup
assessments = {
    'exam': [78, 85],
    'project_count': 1,
    'participation': 5
}

bonus = defaultdict(int, {'project': 12})

# Key computation step
final_score = calculate_final(assessments, bonus)

# Output result
print(f"Result: {final_score}")