from collections import defaultdict

# Simulate player activity data across multiple game sessions
player_data = [
    {'player': 'Alice', 'level': 3, 'score': 85, 'completed': True},
    {'player': 'Bob', 'level': 2, 'score': 90, 'completed': False},
    {'player': 'Alice', 'level': 4, 'score': 95, 'completed': True},
    {'player': 'Charlie', 'level': 3, 'score': 70, 'completed': True}
]

# Aggregate scores by player using defaultdict
scores_by_player = defaultdict(int)
completion_bonus = defaultdict(int)

for record in player_data:
    player = record['player']
    base_score = record['score']
    if record['completed']:
        completion_bonus[player] += 10  # Bonus for completed levels
    scores_by_player[player] += base_score

# Calculate final score with weighted bonus for high-level completion
def calculate_final_score(data):
    total = 0
    for player, base_total in scores_by_player.items():
        bonus = completion_bonus[player]
        weighted_bonus = bonus * 1.5
        total += base_total + weighted_bonus
    return int(total)

# Irrelevant utility function (minimal distraction)
def unused_helper():
    return sum([1 for _ in range(5)])

# Execution point of interest
total_score = calculate_final_score(player_data)

print(f"Result: {total_score}")