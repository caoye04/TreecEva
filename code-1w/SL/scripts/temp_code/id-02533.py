from collections import defaultdict

# Simulate user engagement metrics across app sessions
def analyze_engagement(events):
    duration_log = defaultdict(int)
    action_count = 0
    temp_sum = 0

    for event in events:
        session_id = event['session']
        duration = event['duration']
        action_type = event['action']

        duration_log[session_id] += duration
        action_count += 1
        temp_sum += duration * 0.1  # Irrelevant smoothing factor

    avg_duration = sum(duration_log.values()) / len(duration_log) if duration_log else 0
    return avg_duration, action_count

def calculate_rank_efficiency(ranks):
    rank_freq = defaultdict(int)
    total_rank = 0

    for r in ranks:
        rank_freq[r] += 1
        total_rank += r

    # Misleading computation: frequency-based adjustment (not used later)
    adjustment = 0
    for rk, cnt in rank_freq.items():
        if cnt > 1:
            adjustment += rk * 0.5

    normalized = total_rank / len(ranks) if ranks else 0
    return normalized

def calculate_final_score(data, multiplier):
    base = 0
    penalty = 0

    for item in data:
        rank = item['rank']
        score = item['score']
        base += score

        if rank > 5:
            penalty += 1

    # Complex but partially irrelevant transformation
    adjusted_base = base * 0.9 + penalty * -2.5
    final = adjusted_base * multiplier

    # Dead code path - never executed under current logic
    if False and penalty == 0:
        final *= 1.1

    return int(final)

# Main execution block
if __name__ == "__main__":
    raw_events = [
        {'session': 'A', 'duration': 120, 'action': 'click'},
        {'session': 'B', 'duration': 180, 'action': 'swipe'},
        {'session': 'A', 'duration': 60, 'action': 'tap'},
        {'session': 'C', 'duration': 210, 'action': 'scroll'}
    ]

    avg_time, actions = analyze_engagement(raw_events)

    # Rank data from system output
    rank_list = [3, 7, 4, 7, 2, 9]
    efficiency = calculate_rank_efficiency(rank_list)

    # Bonus determined from engagement threshold
    bonus_multiplier = 1.5 if avg_time > 100 else 1.2

    # Scoring dataset
    rank_data = [
        {'rank': 1, 'score': 85},
        {'rank': 4, 'score': 70},
        {'rank': 6, 'score': 65},
        {'rank': 8, 'score': 60}
    ]

    # Intermediate distractor variables
    temp_score = sum(item['score'] for item in rank_data)
    correction_factor = temp_score * 0.05  # Unused adjustment

    final_score = calculate_final_score(rank_data, bonus_multiplier)

    # Print result as required
    print(f"Target result: {final_score}")