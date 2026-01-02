from collections import defaultdict

# Simulate employee performance scoring
def calculate_performance(base_bonus, deductions):
    raw_score = base_bonus * 1.5
    for deduction in deductions:
        raw_score -= deduction
    return int(raw_score)

# Initialize data
bonus = 85
team_penalties = [12, 8, 5]
personal_goals = [True, False, True]

# Irrelevant tracking (distractor)
progress_tracker = defaultdict(int)
for goal in personal_goals:
    progress_tracker['completed' if goal else 'pending'] += 1

# Key computation
penalties = sum(team_penalties)
final_score = calculate_performance(bonus, team_penalties)
print(f"Result: {final_score}")