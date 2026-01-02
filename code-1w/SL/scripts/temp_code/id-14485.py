def analyze_efficiency(logs):
    total_ops = sum([len(entry['tasks']) for entry in logs if entry['status'] == 'active'])
    idle_count = len([e for e in logs if e['status'] == 'idle'])
    avg_tasks = total_ops / (len(logs) - idle_count) if (len(logs) - idle_count) > 0 else 0
    return avg_tasks

logs_data = [
    {'status': 'active', 'tasks': [1, 2, 3], 'priority': 'high'},
    {'status': 'idle', 'tasks': [], 'priority': 'low'},
    {'status': 'active', 'tasks': [4, 5], 'priority': 'medium'},
    {'status': 'active', 'tasks': [6]},
    {'status': 'idle', 'tasks': [0], 'priority': 'low'}
]

baseline = 2.5
productivity = analyze_efficiency(logs_data)

# Simulate risk adjustment based on outlier detection
task_lengths = [len(item['tasks']) for item in logs_data]
outlier_threshold = 1.5 * max(task_lengths)
risk_factor = 1.0
for length in task_lengths:
    if length > outlier_threshold:
        risk_factor *= 0.9

# Unused distraction variables
temp_cache = {i: i**3 for i in range(10)}
redundant_sum = sum(temp_cache[k] for k in temp_cache if k % 2 == 0)
flagged_entries = [entry for entry in logs_data if entry['status'] == 'idle' and entry.get('priority') == 'low']

# Core evaluation logic with conditional expression
performance_index = productivity if productivity > baseline else baseline * 0.85
adjusted_risk = risk_factor if len(flagged_entries) > 0 else 1.0

# Final scoring with dictionary-based weighting
weights = {'efficiency': 0.7, 'risk': 0.3}
raw_score = performance_index * weights['efficiency'] + adjusted_risk * weights['risk']
normalized_score = round(raw_score, 4)

# Secondary transformation
scaled_value = normalized_score * 100
penalty = 5 if redundant_sum > 1000 else 0  # Dead code path (redundant_sum = 200)
final_score = int(scaled_value - penalty)

print(f"Result: {final_score}")