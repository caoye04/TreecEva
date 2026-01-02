from collections import defaultdict

# Simulate player action logs in a turn-based game
def process_game_logs(logs):
    action_count = defaultdict(int)
    for entry in logs:
        player, action = entry['player'], entry['action']
        action_count[action] += 1

    bonuses = {'defend': 2, 'attack': 1, 'heal': 3}
    base_scores = {action: count * bonuses.get(action, 1) for action, count in action_count.items()}
    
    # Irrelevant distraction: counting players (used nowhere critical)
    unique_players = set(log['player'] for log in logs)
    player_count = len(unique_players)

    return base_scores

def calculate_final_score(stats):
    score = 0
    for action, base in stats.items():
        if action == 'heal':
            score += base * 1.5
        elif action == 'attack':
            score += base + 5
        else:
            score += base
    return int(score)

# Game session data
log_data = [
    {'player': 'A', 'action': 'attack'},
    {'player': 'B', 'action': 'defend'},
    {'player': 'A', 'action': 'heal'},
    {'player': 'C', 'action': 'attack'},
    {'player': 'B', 'action': 'heal'},
    {'player': 'A', 'action': 'attack'},
    {'player': 'C', 'action': 'defend'}
]

# Process the logs and compute final score
processed_stats = process_game_logs(log_data)
total_score = calculate_final_score(processed_stats)
print(f"Result: {total_score}")