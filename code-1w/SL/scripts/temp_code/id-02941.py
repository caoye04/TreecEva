from collections import defaultdict, Counter

# Simulated player action log for a puzzle game
action_log = [
    ('player1', 'solve_puzzle', 15),
    ('player2', 'solve_puzzle', 12),
    ('player1', 'hint_used', 3),
    ('player3', 'solve_puzzle', 18),
    ('player2', 'solve_puzzle', 10),
    ('player1', 'solve_puzzle', 14),
    ('player3', 'hint_used', 2),
    ('player2', 'hint_used', 1),
    ('player3', 'solve_puzzle', 16)
]

# Track raw counts and totals
action_counter = Counter(action for player, action, _ in action_log)
hint_penalties = defaultdict(int)
score_breakdown = {}
baseline_scores = {}

# Accumulate base scores per player
for player, action, time_taken in action_log:
    if player not in baseline_scores:
        baseline_scores[player] = 0
    if action == 'solve_puzzle':
        # Faster solving gives higher base score
        baseline_scores[player] += max(20 - time_taken, 5)

# Apply penalty for hints (irrelevant accumulation for unused actions)
temp_penalty_map = {'hint_used': 2, 'timeout': 1, 'restart': 3}
for player, action, _ in action_log:
    if action == 'hint_used':
        hint_penalties[player] += temp_penalty_map[action]

# Compute weighted contribution (only some players contribute)
weighted_contribution = 0
participating_players = set(p for p, _, _ in action_log)
for p in participating_players:
    if p in baseline_scores:
        weighted_contribution += baseline_scores[p] * 0.1

# Unused distractor: complex time aggregation
time_analysis = defaultdict(list)
for player, action, time in action_log:
    time_analysis[action].append(time)

average_solve_time = sum(time_analysis['solve_puzzle']) / len(time_analysis['solve_puzzle'])
adjusted_threshold = average_solve_time * 0.9  # Distractor threshold

# Actual scoring logic
def calculate_final_score(data):
    total_bonus = 0
    for player, base in data.items():
        # Bonus for multiple puzzles solved
        puzzle_count = action_counter[f'{player},solve_puzzle_placeholder']  # Misleading key
        actual_puzzle_count = sum(1 for p, a, _ in action_log if p == player and a == 'solve_puzzle')
        if actual_puzzle_count >= 2:
            total_bonus += 5
    return int(sum(data.values()) + total_bonus - sum(hint_penalties.values()))

# Recompute actual puzzle count correctly for final use
final_data = {}
for player in baseline_scores:
    actual_count = sum(1 for p, a, _ in action_log if p == player and a == 'solve_puzzle')
    final_data[player] = baseline_scores[player]

# Final score calculation
final_score = calculate_final_score(final_data)

# Print result as required
print(f"Result: {final_score}")