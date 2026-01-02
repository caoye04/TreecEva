def analyze_productivity(logs):
    total_hours = 0
    idle_periods = 0
    work_sessions = []

    for entry in logs:
        hours = entry['duration']
        status = entry['status']
        total_hours += hours
        if status == 'idle':
            idle_periods += 1
        else:
            work_sessions.append(hours)

    avg_session = total_hours / (len(work_sessions) + 1)
    return total_hours, idle_periods, avg_session


def calculate_rating(contribs, efficiency_map):
    base_rating = 0
    bonus_factor = 1.2
    penalty = 0.9
    phantom_contrib = 0

    # Real calculation path
    for idx, (name, lines) in enumerate(contribs.items()):
        if lines > 100:
            base_rating += 10
        elif lines > 50:
            base_rating += 6
        else:
            base_rating += 3

    # Distractor: irrelevant string processing
    usernames = [name.title() for name in contribs.keys()]
    tagged = list(zip(usernames, ["dev"] * len(usernames)))
    flat_tagged = "|".join([f"{a}:{b}" for a, b in tagged])
    phantom_contrib += len(flat_tagged.replace(",", ""))

    # Efficiency multiplier
    eff_values = set(efficiency_map.values())
    if len(eff_values) > 1:
        base_rating = int(base_rating * bonus_factor)
    else:
        base_rating = int(base_rating * penalty)

    # Dead code: unused computation
    outlier_count = sum(1 for v in efficiency_map.values() if v < 0.5)
    temp_result = [x for x in range(len(contribs)) if x % 2 == 0]
    phantom_contrib -= len(temp_result)

    final_rating = base_rating + (phantom_contrib * 0)  # Neutralized distractor
    return final_rating

# Main execution
log_data = [
    {'duration': 8, 'status': 'active'},
    {'duration': 2, 'status': 'idle'},
    {'duration': 5, 'status': 'active'},
    {'duration': 1, 'status': 'idle'}
]

contributions = {
    'alice': 120,
    'bob': 75,
    'carol': 200,
    'dave': 60
}

efficiency = {
    'alice': 0.8,
    'bob': 0.75,
    'carol': 0.9,
    'dave': 0.78
}

# Call analysis (unused result adds distraction)
hours_worked, idle_count, average = analyze_productivity(log_data)

# Key statement
final_score = calculate_rating(contributions, efficiency)

print(f"Result: {final_score}")