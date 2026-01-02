def analyze_productivity(logs):
    total_hours = 0
    idle_periods = 0
    efficiency_ratio = 0.0

    for day, log in enumerate(logs):
        daily_hours = sum([h for h in log['hours'] if h > 0])
        total_hours += daily_hours

        if daily_hours < 6:
            idle_periods += 1

    if total_hours > 0 and len(logs) > 0:
        efficiency_ratio = (total_hours / (len(logs) * 8)) * 100

    return total_hours, efficiency_ratio, idle_periods


def calculate_rating(contributions, penalties):
    base_score = 0
    bonus_adjustment = 0.0
    penalty_offset = 0

    # Real logic for score calculation
    for i, contrib in enumerate(contributions):
        if i % 2 == 0:
            base_score += len(contrib.strip())
        else:
            base_score += contrib.count('task')

    # Distractor: irrelevant string processing
    summary = " | ".join(contributions)
    tokens = summary.split(' ')
    word_frequency = {w: tokens.count(w) for w in set(tokens)}
    rare_words = [w for w in word_frequency if len(w) > 5 and word_frequency[w] == 1]
    bonus_adjustment = len(rare_words) * 0.5  # Not used in final score

    # Penalty processing (relevant)
    for reason, count in penalties.items():
        if 'delay' in reason:
            penalty_offset += count * 2
        elif 'error' in reason:
            penalty_offset += count * 3

    # Final score depends only on base_score and penalty_offset
    final_score = base_score - penalty_offset

    # More distractions: unused sorting and zipping
    ranked_contribs = sorted(contributions, key=len, reverse=True)
    paired_data = list(zip(ranked_contribs, [len(c) for c in ranked_contribs]))
    sorted(paired_data, key=lambda x: x[1])  # Dead code, no assignment

    return final_score

# Simulated input data
activity_logs = [
    {'day': 'Mon', 'hours': [8, 0, 4, 2], 'notes': 'normal'},
    {'day': 'Tue', 'hours': [3, 2, 1], 'notes': 'partial'},
    {'day': 'Wed', 'hours': [7, 1, 6], 'notes': 'productive'},
    {'day': 'Thu', 'hours': [0, 0, 0], 'notes': 'idle'},
    {'day': 'Fri', 'hours': [5, 3], 'notes': 'moderate'}
]

contributions = [
    "  finalized task submission ",
    "task completed with task validation",
    "  documentation updated  ",
    "code review and task follow-up"
]

penalties = {
    "delay_filing": 2,
    "error_naming": 1,
    "delay_response": 3,
    "format_issue": 5  # This won't affect score since not 'delay' or 'error' type
}

# Extract useful metrics (distraction)
analysis_results = analyze_productivity(activity_logs)
utilization_rate = analysis_results[1]
idle_days = analysis_results[2]

# Core computation
final_score = calculate_rating(contributions, penalties)

# Output result
print(f"Result: {final_score}")