def analyze_performance(records):
    # Irrelevant preprocessing: normalize names (not used in result)
    normalized_names = [name.strip().title() for name, _ in records]

    # Semi-relevant transformation: extract durations and statuses
    durations = []
    statuses = []
    for _, entry in records:
        if 'duration' in entry and 'status' in entry:
            durations.append(entry['duration'])
            statuses.append(entry['status'])

    # Distractor computation: average duration (not used in final logic)
    avg_duration = sum(durations) / len(durations) if durations else 0
    threshold_exceeded = [d > 2 * avg_duration for d in durations]

    # Key data: count successful completions with conditional unpacking
    success_count = 0
    bonus_flags = []
    for i, status in enumerate(statuses):
        is_fast = durations[i] < avg_duration * 0.5
        bonus_flags.append(True if is_fast and status == 'completed' else False)
        success_count += 1 if status == 'completed' else 0

    # Misleading combinatorics: possible pairs (unused)
    possible_pairs = 0
    if len(durations) >= 2:
        possible_pairs = len(durations) * (len(durations) - 1) // 2

    # Core logic: weighted score based on success and bonuses
    base_weight = 10
    bonus_multiplier = 1.5
    raw_score = success_count * base_weight
    
    # Conditional expression with lambda filter for 'fast completions'
    fast_completion_filter = lambda x: x < avg_duration * 0.6
    fast_completions = list(filter(fast_completion_filter, [durations[i] for i in range(len(durations)) if statuses[i] == 'completed']))
    bonus_awarded = len(fast_completions) * base_weight * bonus_multiplier

    # Final aggregation using zip and enumerate (key python idioms)
    components = zip([raw_score], [bonus_awarded])
    adjustments = 0
    for idx, (raw, bonus) in enumerate(components):
        if idx == 0:
            adjustments += bonus * 0.2  # partial adjustment

    # Critical assignment point
    final_score = raw_score + bonus_awarded + adjustments

    # Dead code path: never executed due to logic above
    if possible_pairs < 0:
        final_score *= 0.9
        normalized_names = []  # reassignment, unused

    return final_score

# Input data
session_data = [
    ("user1", {"duration": 120, "status": "completed"}),
    ("user2", {"duration": 300, "status": "failed"}),
    ("user3", {"duration": 80, "status": "completed"}),
    ("user4", {"duration": 450, "status": "completed"}),
    ("user5", {"duration": 90, "status": "completed"})
]

# Execute
result = analyze_performance(session_data)
final_score = round(result, 4)
print(f"Target result: {final_score}")