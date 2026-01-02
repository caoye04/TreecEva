def analyze_productivity(logs):
    base_efficiency = 0
    penalty_count = 0
    temp_factor = 1

    for log in logs:
        hours = log['hours_worked']
        tasks = log['tasks_completed']
        if hours > 8:
            excess = hours - 8
            base_efficiency -= excess * 0.5
            penalty_count += 1

        if tasks < 3:
            base_efficiency -= 2

        overtime_boost = (hours - 8) * 0.8 if hours > 8 else 0
        base_efficiency += overtime_boost

    distraction_score = penalty_count * temp_factor
    return base_efficiency - distraction_score


def process_performance(metrics, level):
    adjustment = 0
    thresholds = {1: 5, 2: 10, 3: 15}
    cap = thresholds.get(level, 20)

    # Irrelevant mapping for different tiers
    tier_map = {'basic': 1, 'pro': 2, 'elite': 3}
    multiplier = level * 0.1

    raw_value = sum(metrics)

    # Apply non-linear adjustment
    for i in range(len(metrics)):
        if metrics[i] > cap:
            adjustment += (metrics[i] - cap) * multiplier

    enhanced_metrics = [x * multiplier for x in metrics]
    filtered_metrics = list(filter(lambda x: x > 0.5, enhanced_metrics))

    base_score = raw_value + adjustment

    if len(filtered_metrics) > 2:
        base_score += 5

    # Dummy set operation with no real impact
    s1 = {1, 2, 3, 4}
    s2 = {3, 4, 5, 6}
    dummy_union = s1 | s2
    dummy_diff = s1 - s2

    final_score = int(base_score + len(dummy_diff))
    return final_score

# Simulated input data
activity_logs = [
    {'hours_worked': 9, 'tasks_completed': 5},
    {'hours_worked': 7, 'tasks_completed': 2},
    {'hours_worked': 10, 'tasks_completed': 6}
]

productivity = analyze_productivity(activity_logs)

# Core metrics derived from productivity
base_metrics = [productivity, productivity * 0.8, 12, 7]
bonus_level = 3

# Key statement
final_score = process_performance(base_metrics, bonus_level)

print(f"Result: {final_score}")