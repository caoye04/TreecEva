from collections import Counter

def analyze_defense(events):
    event_count = Counter(events)
    return event_count['block'] + event_count['rebound']

def calculate_efficiency(actions):
    total_actions = len(actions)
    effective = actions.count('assist') + actions.count('score')
    return round(effective / total_actions, 3) if total_actions > 0 else 0

def evaluate_performance(defense_log, efficiency_metric):
    defense_points = analyze_defense(defense_log)
    normalized_efficiency = int(efficiency_metric * 100)
    adjustment = defense_points // 5
    return defense_points * 2 + normalized_efficiency + adjustment

# Game data
recent_defense = ['rebound', 'block', 'foul', 'block', 'steal', 'block', 'rebound']
player_actions = ['dribble', 'pass', 'assist', 'shoot', 'miss', 'assist', 'score']

# Irrelevant distraction: unused variable
baseline_average = 78.5

efficiency = calculate_efficiency(player_actions)
final_score = evaluate_performance(recent_defense, efficiency)

print(f"Result: {final_score}")