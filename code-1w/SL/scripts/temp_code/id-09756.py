def analyze_productivity(logs):
    total_hours = 0
    idle_periods = 0
    efficiency_ratio = 0.0
    distraction_count = 0

    for day, log in enumerate(logs):
        daily_total = sum(log['work_minutes'])
        total_hours += daily_total / 60
        if daily_total < 300:
            idle_periods += 1

        # Distractor: tracking irrelevant UI interactions
        for entry in log['ui_events']:
            if entry['type'] == 'click' and entry['target'].startswith('ad_'):
                distraction_count += 1  # Not used in final logic

    if total_hours > 0:
        efficiency_ratio = (total_hours - idle_periods) / total_hours

    return total_hours, efficiency_ratio


def calculate_rating(contributions, penalties):
    base_score = 0
    bonus_factor = 1.0
    deduction = 0

    severity_map = {1: 0.5, 2: 1.2, 3: 2.0}
    contribution_weights = {'critical': 10, 'major': 5, 'minor': 2}

    # Real logic for score calculation
    for item in contributions:
        base_score += contribution_weights.get(item['level'], 1)

    # Apply penalty deductions
    for penalty in penalties:
        deduction += severity_map.get(penalty['level'], 1) * penalty['count']

    # Distractor: unused transformation
    reversed_weights = {v: k for k, v in contribution_weights.items()}
    temp_scores = [base_score * (1 + i*0.1) for i, _ in enumerate(contributions)]

    # Bonus logic based on clean record
    if len(penalties) == 0 and base_score >= 20:
        bonus_factor = 1.5

    # Final computation
    raw_score = (base_score - deduction) * bonus_factor

    # Normalize to integer
    final_rating = int(round(raw_score))

    # Another red herring: zipping unrelated sequences
    timestamps = [101, 102, 103]
    codes = ['A', 'B', 'C']
    for ts, code in zip(timestamps, codes):
        pass  # Dead loop with no side effects

    return final_rating

# Main execution
logs_data = [
    {
        'work_minutes': [480],
        'ui_events': [
            {'type': 'click', 'target': 'ad_banner'},
            {'type': 'hover', 'target': 'ad_sidebar'}
        ]
    },
    {
        'work_minutes': [200],
        'ui_events': []
    }
]

contributions_list = [
    {'level': 'critical', 'points': 10},
    {'level': 'major', 'points': 5},
    {'level': 'major', 'points': 5},
    {'level': 'minor', 'points': 2}
]

penalties_list = [
    {'level': 2, 'count': 3},
    {'level': 1, 'count': 5}
]

_, _ = analyze_productivity(logs_data)  # Unused return values

final_score = calculate_rating(contributions_list, penalties_list)
print(f"Result: {final_score}")