from collections import Counter

def evaluate_performance(logs):
    success_count = 0
    for log in logs:
        if 'success' in log and log['success']:
            success_count += 1
    return success_count

def calculate_final_score(attempts, multiplier):
    base = sum(attempts)
    adjustment = len([x for x in attempts if x > 2])
    return base * multiplier - adjustment

def analyze_user_behavior(session_data):
    actions = [event['type'] for event in session_data]
    action_count = Counter(actions)
    return action_count.most_common(1)[0][1] if action_count else 0

# Simulated input data
user_logs = [
    {'timestamp': 1, 'action': 'start', 'success': True},
    {'timestamp': 2, 'action': 'attempt', 'success': False},
    {'timestamp': 3, 'action': 'attempt', 'success': True},
    {'timestamp': 4, 'action': 'attempt', 'success': True}
]

session_events = [
    {'type': 'click', 'value': 1},
    {'type': 'click', 'value': 2},
    {'type': 'hover', 'value': 3},
    {'type': 'click', 'value': 4}
]

attempts_per_round = [3, 1, 4, 2]
difficulty_multiplier = 1.5

# Irrelevant utility function (mild distraction)
def format_timestamp(t):
    return f"Time-{t}"

# Key computation chain
successful_attempts = evaluate_performance(user_logs)
behavior_metric = analyze_user_behavior(session_events)
total_score = calculate_final_score(attempts_per_round, difficulty_multiplier)

print(f"Result: {total_score}")