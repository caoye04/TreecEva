def analyze_user_activity(logs):
    total_actions = 0
    idle_periods = 0
    temp_buffer = []

    for entry in logs:
        action_type = entry.split(',')[0]
        duration = int(entry.split(',')[1])

        if action_type == 'click':
            total_actions += 1
            if duration > 50:
                temp_buffer.append(duration)
        elif action_type == 'hover':
            if duration < 10:
                idle_periods += 1

    return total_actions, len(temp_buffer)


def calculate_rating(data, limit):
    score = 0
    bonus_tracker = []
    penalty = 0

    for key, value in data.items():
        base = len(key) * value
        adjusted = base // (value + 1) if value > 0 else 0

        if adjusted > limit:
            score += adjusted
            bonus_tracker.append(adjusted * 0.1)
        else:
            penalty += 1

    final_penalty = sum([p for p in bonus_tracker]) if penalty > 2 else 0
    return int(score - final_penalty)

# Simulated user engagement data
raw_logs = [
    'click,60', 'hover,5', 'click,30', 'click,80',
    'hover,2', 'scroll,150', 'click,25'
]

action_count, long_clicks = analyze_user_activity(raw_logs)

engagement_data = {
    'session': action_count,
    'clicks': long_clicks,
    'navigation': 3,
    'interactions': action_count - long_clicks
}

threshold = 4
intermediate_sum = sum(engagement_data.values()) // 2
extra_weight = len(raw_logs) % 4

final_score = calculate_rating(engagement_data, threshold)
print(f"Result: {final_score}")