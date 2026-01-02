from collections import defaultdict

# Simulate user engagement analytics across multiple app modules
def analyze_engagement(log_entries):
    event_count = defaultdict(int)
    session_duration = 0
    idle_time = 0

    for entry in log_entries:
        event_type = entry['type']
        duration = entry['duration']
        event_count[event_type] += 1
        session_duration += duration

        if duration > 100:
            idle_time += duration * 0.1

    # Distractor computation: rarely impacts final result
    avg_duration = session_duration / len(log_entries) if log_entries else 0
    high_engagement = sum(1 for count in event_count.values() if count > 5)

    return event_count, session_duration, avg_duration, high_engagement


def rank_users(event_count, base_score):
    tier_map = {'click': 1, 'scroll': 2, 'tap': 3, 'swipe': 4}
    dynamic_tier = defaultdict(int)
    total_actions = 0

    for event, count in event_count.items():
        if event in tier_map:
            dynamic_tier[event] = count * tier_map[event]
            total_actions += count

    # Misleading intermediate score
    phantom_score = sum(dynamic_tier.values()) * 0.5

    adjusted_score = base_score + total_actions * 1.5
    return adjusted_score, total_actions

def calculate_final_score(rank_data, bonus_multiplier):
    base_rank, actions = rank_data
    penalty = 0

    if actions > 30:
        penalty = 5
    elif actions > 20:
        penalty = 2

    # Core calculation
    raw_score = (base_rank + 10) * bonus_multiplier
    final_score = raw_score - penalty

    # Dead code path — never reached under current logic
    if penalty > 10:
        final_score += 15  # Irrelevant branch

    return final_score

# Main execution
log_data = [
    {'type': 'click', 'duration': 20},
    {'type': 'scroll', 'duration': 120},
    {'type': 'tap', 'duration': 45},
    {'type': 'swipe', 'duration': 60},
    {'type': 'click', 'duration': 30},
    {'type': 'tap', 'duration': 25},
    {'type': 'scroll', 'duration': 80},
    {'type': 'swipe', 'duration': 90},
    {'type': 'click', 'duration': 10},
    {'type': 'swipe', 'duration': 70},
    {'type': 'tap', 'duration': 55},
    {'type': 'click', 'duration': 40},
    {'type': 'scroll', 'duration': 110},
    {'type': 'swipe', 'duration': 85},
    {'type': 'tap', 'duration': 35},
]

# Extract analytics
event_counter, total_duration, mean_duration, engaged_types = analyze_engagement(log_data)

# Compute base ranking
initial_score = 25
rank_result = rank_users(event_counter, initial_score)

# Bonus based on average session intensity (distractor: not actually used)
binary_flags = [1 if d['duration'] > 50 else 0 for d in log_data]
intensity_score = sum(binary_flags) * 2.5
bonus_multiplier = 3 if intensity_score > 20 else 2

# Key statement
final_score = calculate_final_score(rank_result, bonus_multiplier)

print(f"Result: {final_score}")