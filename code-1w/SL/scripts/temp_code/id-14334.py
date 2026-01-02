def evaluate_performance(records, importance):
    total = 0
    bonus = 0
    penalty = 0
    temp_result = []

    # Irrelevant pre-processing: calculating average duration (not used in final score)
    durations = [r[2] for r in records]
    avg_duration = sum(durations) / len(durations)
    threshold = avg_duration * 0.75

    # Relevant logic: scoring based on status and priority
    for record in records:
        tag, value, duration, status = record
        weight = importance.get(tag, 1)

        if status == 'completed':
            total += value * weight
            if duration < threshold:
                bonus += value * 0.1
        elif status == 'failed':
            penalty += value * weight * 0.5

    # Distractor: complex lambda-based filtering (unused)
    filter_recent = lambda x: x[2] > 10
    filtered_data = list(filter(filter_recent, records))
    dummy_aggregate = sum([f[1] * 0.1 for f in filtered_data]) if filtered_data else 0

    # Semi-relevant: slicing last 3 records for special adjustment
    recent_records = records[-3:]
    adjustment_factor = len([r for r in recent_records if r[3] == 'completed'])

    # Final score computation
    base_score = total + bonus - penalty
    final_score = int(base_score + adjustment_factor * 2.5)

    # Dead code: unused state tracking
    stats = {
        'processed': len(records),
        'bonus_applied': bonus,
        'penalty_applied': penalty
    }

    return final_score

# Main execution
raw_data = [
    ('A', 10, 8, 'completed'),
    ('B', 15, 12, 'failed'),
    ('C', 20, 5, 'completed'),
    ('D', 12, 15, 'completed'),
    ('E', 8, 7, 'failed')
]

weights_config = {'A': 2, 'C': 1.5, 'D': 1}
data_slice = raw_data[1:4]

# Key statement
final_score = evaluate_performance(data_slice, weights_config)
print(f"Result: {final_score}")