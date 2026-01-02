def analyze_productivity(logs):
    total_hours = sum([entry['hours'] for entry in logs])
    idle_count = len([e for e in logs if e['status'] == 'idle'])
    active_count = len([e for e in logs if e['status'] == 'active'])
    efficiency = (active_count / len(logs)) * 100 if logs else 0
    return total_hours, efficiency

logs_data = [
    {'hours': 8, 'status': 'active', 'tag': 'core'},
    {'hours': 3, 'status': 'idle', 'tag': 'break'},
    {'hours': 6, 'status': 'active', 'tag': 'core'},
    {'hours': 1, 'status': 'idle', 'tag': 'break'},
    {'hours': 7, 'status': 'active', 'tag': 'core'}
]

hour_sum, efficiency_rate = analyze_productivity(logs_data)

# Simulate task contribution analysis with noise
task_metrics = [12, 15, 9, 14, 11]
weighted_scores = [x * 1.1 for x in task_metrics]
dummy_shift = sum([x << 1 for x in weighted_scores[:2]])  # Irrelevant bit shift
baseline = len(task_metrics) * 10

contributions = []
for i, score in enumerate(weighted_scores):
    normalized = score / max(weighted_scores)
    bonus = 5 if normalized > 0.8 else 0
    contributions.append(int(normalized * 100) + bonus)

# Add dummy filtering step
filtered_contribs = [c for c in contributions if c > 85]
dropped_count = len(contributions) - len(filtered_contribs)

penalty_factor = 1.0
if efficiency_rate < 75:
    penalty_factor += 0.1
else:
    penalty_factor -= 0.05  # This path taken

# Additional distraction: string processing on tags
tag_sequence = ''.join([entry['tag'] for entry in logs_data])
segment = tag_sequence[::2]  # slicing operation - red herring
token_count = len(segment.split('o'))  # semi-relevant distraction

# Conditional expression used here
adjustment = 10 if 'break' in tag_sequence else 5

# Core rating logic obscured by context
contribution_sum = sum(contributions)
adjusted_sum = contribution_sum - adjustment

# Use of conditional expression and slicing
modifier = 1.2 if adjusted_sum > 300 else 0.9
final_score = int((adjusted_sum * modifier) * (1 - penalty_factor))

Result: final_score