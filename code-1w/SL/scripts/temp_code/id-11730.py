def analyze_productivity(logs):
    total_hours = 0
    idle_count = 0
    peak_periods = []

    for i, (hour, activity) in enumerate(logs):
        total_hours += hour
        if activity < 20:
            idle_count += 1
        if activity > 80:
            peak_periods.append(i)

    efficiency = total_hours / len(logs) if logs else 0
    return efficiency, idle_count, peak_periods


def calculate_rating(contributions, impacts):
    base_rating = 0
    bonus_factor = 0.0
    penalty = 0

    temp_data = []
    for idx, (contrib, impact) in enumerate(zip(contributions, impacts)):
        score = contrib * impact
        if score > 100:
            bonus_factor += 0.1
        elif score < 30:
            penalty += 5
        
        adjustment = 0
        if idx % 2 == 0:
            adjustment = 2
        else:
            adjustment = -1
        
        temp_data.append(score + adjustment)

    aggregate = sum(temp_data) / len(temp_data) if temp_data else 0

    # Simulate historical comparison (distractor block)
    historical_avg = 45.6
    variance_drift = (aggregate - historical_avg) ** 0.5 if aggregate > historical_avg else 0

    # Core rating logic
    base_rating = aggregate * (1 + bonus_factor) - penalty

    # Dead code path - misleading but syntactically relevant
    if False:
        fallback = 0
        for x in temp_data:
            fallback += x ** 0.1
        base_rating = max(base_rating, fallback)

    return int(base_rating)

# Main execution
activity_logs = [
    (8, 25), (7, 15), (9, 85), (6, 40), (8, 90),
    (5, 10), (9, 95), (7, 50), (8, 80), (6, 30)
]

contribution_list = [10, 15, 20, 12, 18, 14, 16, 11]
impact_levels = [5, 8, 4, 6, 7, 5, 9, 3]

# Irrelevant preprocessing (adds cognitive load)
weighted_pairs = []
for c, i in zip(contribution_list, impact_levels):
    weighted_pairs.append((c * 0.9, i * 1.1))

# Key function call
final_score = calculate_rating(contribution_list, impact_levels)

# Unrelated metrics (distractors)
daily_average = sum([h for h, _ in activity_logs]) / len(activity_logs)
peak_session_count = len(analyze_productivity(activity_logs)[2])

Result: final_score