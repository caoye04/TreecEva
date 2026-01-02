from collections import defaultdict

# Simulate user activity logs with action types
logs = [
    'click', 'scroll', 'click', 'keypress', 'scroll',
    'click', 'click', 'hover', 'keypress', 'scroll',
    'hover', 'click', 'scroll', 'scroll', 'keypress'
]

# Count frequency of each action
counts = defaultdict(int)
for action in logs:
    counts[action] += 1

# Irrelevant distraction: unused variable (minimal interference)
dummy_flag = True

# Scoring rules: click=2, scroll=1, keypress=3, hover=1
score_map = {'click': 2, 'scroll': 1, 'keypress': 3, 'hover': 1}

# Calculate final score based on weighted counts
def calculate_final_score(action_counts):
    total = 0
    for action, count in action_counts.items():
        if action in score_map:
            total += score_map[action] * count
    return total

# Compute total score
total_score = calculate_final_score(counts)

# Output result
print(f"Result: {total_score}")