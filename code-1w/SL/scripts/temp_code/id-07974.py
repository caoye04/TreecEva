def calculate_final_score(log, limits):
    base = 0
    bonus = 0
    penalties = 0

    # Count activity categories
    counts = {}
    for entry in log:
        category = entry['type']
        duration = entry['duration']
        if category not in counts:
            counts[category] = 0
        counts[category] += duration

    # Apply scoring rules
    if 'work' in counts and counts['work'] >= limits['work']:
        base += 25
        bonus += 10
    if 'exercise' in counts and counts['exercise'] >= limits['exercise']:
        base += 20
    if 'leisure' in counts and counts['leisure'] > limits['leisure']:
        penalties += 15

    # Conditional bonus based on balance
    if 'work' in counts and 'leisure' in counts:
        if counts['work'] >= 60 and counts['leisure'] >= 30:
            bonus += 5

    return base + bonus - penalties

# Simulated daily activity log
activity_log = [
    {'type': 'work', 'duration': 45},
    {'type': 'work', 'duration': 30},
    {'type': 'exercise', 'duration': 40},
    {'type': 'leisure', 'duration': 35},
    {'type': 'work', 'duration': 15}
]

thresholds = {
    'work': 80,
    'exercise': 30,
    'leisure': 40
}

# Irrelevant tracking variable (minimal interference)
total_entries = len(activity_log)

final_score = calculate_final_score(activity_log, thresholds)
print(f"Result: {final_score}")