def analyze_productivity(logs):
    activity_count = {}
    temp_tracker = []
    for entry in logs:
        day, tasks = entry['day'], entry['tasks_completed']
        if day not in activity_count:
            activity_count[day] = 0
        activity_count[day] += tasks
        if tasks > 5:
            temp_tracker.append(day)

    sorted_days = sorted(activity_count.keys())
    peak_days = [d for d in sorted_days if activity_count[d] >= 8]
    return activity_count, peak_days


def normalize_weights(raw_scores):
    total = sum(raw_scores)
    if total == 0:
        return [0 for _ in raw_scores]
    return [round(s / total, 3) for s in raw_scores]

logs_data = [
    {'day': 'Mon', 'tasks_completed': 7, 'errors': 2},
    {'day': 'Tue', 'tasks_completed': 5, 'errors': 1},
    {'day': 'Wed', 'tasks_completed': 9, 'errors': 3},
    {'day': 'Thu', 'tasks_completed': 4, 'errors': 0},
    {'day': 'Fri', 'tasks_completed': 8, 'errors': 4}
]

# Extract contribution counts and error rates
contributions = []
error_rate_sequence = []
for log in logs_data:
    contributions.append(log['tasks_completed'])
    error_rate = log['errors'] / log['tasks_completed'] if log['tasks_completed'] > 0 else 0
    error_rate_sequence.append(round(error_rate, 3))

# Calculate penalty map based on error frequency
penalty_map = {}
for i, rate in enumerate(error_rate_sequence):
    penalty_map[i] = int(rate * 100)

# Misleading computation: weighted average that isn't used
weights = normalize_weights(contributions)
avg_weighted = sum(w * c for w, c in zip(weights, contributions))

# Auxiliary analysis with side results
activity_levels, high_perf_days = analyze_productivity(logs_data)
total_high_perf = len(high_perf_days)

# Core calculation function
def calculate_rating(contribs, penalties):
    base_score = sum(contribs)
    deduction = 0
    for i, contrib in enumerate(contribs):
        if i in penalties:
            # Apply diminishing penalty effect
            penalty_value = penalties[i] * 0.5
            deduction += min(penalty_value, contrib * 0.8)
    raw_final = base_score - deduction
    
    # Artificial adjustment using string-based key encoding (red herring)
    keys = ['A', 'B', 'C', 'D', 'E']
    encoded = ''.join([k.lower() for k in keys])
    if 'a' in encoded:
        raw_final += 1.5  # Minor offset, unrelated to logic
    
    return round(raw_final, 2)

# Key execution point
final_score = calculate_rating(contributions, penalty_map)

# Print result as required
print(f"Result: {final_score}")