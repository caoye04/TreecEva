def analyze_response(time_taken, threshold=2.5):
    return 'optimal' if time_taken <= threshold else 'delayed'

# Simulate user interaction feedback processing
times = [1.2, 3.4, 2.1, 4.5, 1.8]
event_log = {i: t for i, t in enumerate(times)}

# Irrelevant transformation (distractor)
processed_times = list(map(lambda x: round(x * 100) / 100 + 0.05, times))

# Feedback categorization with side computation
feedback_map = {}
for idx, t in enumerate(times):
    category = analyze_response(t)
    bonus = 10 if category == 'optimal' else 0
    penalty = 5 if t > 3.0 else 0
    base_score = 100 - t * 10
    adjusted_score = base_score + bonus - penalty
    
    # Dead code path - never accessed later (distractor)
    if t < 1.0:
        adjusted_score += 20
    
    feedback_map[idx] = {
        'type': category,
        'score': adjusted_score,
        'timestamp': t
    }

# Misleading intermediate aggregation (not used in final result)
total_penalties = sum(f['score'] for f in feedback_map.values() if f['type'] == 'delayed')

# Core logic: compute average of optimal responses only
optimal_scores = [
    f['score'] for f in feedback_map.values()
    if f['type'] == 'optimal'
]

# Auxiliary helper function (moderately relevant)
def smooth_average(values, dampening=0.9):
    if not values:
        return 0.0
    raw_avg = sum(values) / len(values)
    return raw_avg * dampening

# Another distraction: unused recursive counter
def count_transitions(log, limit=10):
    if limit <= 0 or not log:
        return 0
    return 1 + count_transitions(log[:-1], limit - 1)

# Actual performance aggregation
def aggregate_performance(feedback):
    valid_scores = [entry['score'] for entry in feedback.values()]
    return int(smooth_average(valid_scores))

# Execution point of interest
final_score = aggregate_performance(feedback_map)

# Output result as required
print(f"Target result: {final_score}")