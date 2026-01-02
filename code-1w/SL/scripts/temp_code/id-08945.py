from collections import defaultdict, Counter

# Simulate employee task logs with metadata
task_logs = [
    {'employee': 'alice', 'task': 'debug', 'duration': 45, 'errors': 1, 'priority': 'high'},
    {'employee': 'bob', 'task': 'deploy', 'duration': 30, 'errors': 0, 'priority': 'medium'},
    {'employee': 'alice', 'task': 'deploy', 'duration': 25, 'errors': 0, 'priority': 'high'},
    {'employee': 'carol', 'task': 'review', 'duration': 60, 'errors': 2, 'priority': 'low'},
    {'employee': 'bob', 'task': 'review', 'duration': 40, 'errors': 1, 'priority': 'medium'},
    {'employee': 'carol', 'task': 'debug', 'duration': 55, 'errors': 3, 'priority': 'high'}
]

# Initialize data structures
employee_stats = defaultdict(lambda: {
    'total_time': 0, 'task_count': 0, 'error_count': 0, 'high_priority_count': 0
})
summary_report = []
dummy_aggregator = []

# Process each log entry
for log in task_logs:
    emp = log['employee']
    employee_stats[emp]['total_time'] += log['duration']
    employee_stats[emp]['task_count'] += 1
    employee_stats[emp]['error_count'] += log['errors']
    if log['priority'] == 'high':
        employee_stats[emp]['high_priority_count'] += 1

    # Irrelevant aggregation (distractor)
    dummy_aggregator.append(log['duration'] * (log['errors'] + 1))

# Compute efficiency scores
efficiency_map = {}
base_threshold = 35
for emp, stats in employee_stats.items():
    avg_time = stats['total_time'] / stats['task_count']
    error_penalty = stats['error_count'] * 10
    priority_bonus = stats['high_priority_count'] * 5
    efficiency = (base_threshold - avg_time) - error_penalty + priority_bonus
    efficiency_map[emp] = max(efficiency, 0)

# Distractor: unused list comprehension
idle_times = [max(0, 60 - log['duration']) for log in task_logs]

# Build summary (semi-relevant)
for emp, eff in efficiency_map.items():
    summary_report.append(f'{emp}:{eff}')

# Character frequency analysis on employee names (distractor)
all_names = ''.join([log['employee'] for log in task_logs])
char_freq = Counter(all_names)
unique_chars = len(char_freq)

# Core evaluation logic
weight_map = {'alice': 1.2, 'bob': 1.0, 'carol': 0.9}
def evaluate_performance(stats_dict, weights):
    total_weighted_score = 0.0
    normalization_factor = 0
    
    for emp, stats in stats_dict.items():
        base_score = stats['total_time']
        # Multi-step transformation
        adjusted = base_score - (stats['error_count'] * 15)
        adjusted += (stats['high_priority_count'] * 8)
        weighted = adjusted * weights.get(emp, 1.0)
        total_weighted_score += weighted
        normalization_factor += weights.get(emp, 1.0)
    
    # Final normalized score
    final_normalized = total_weighted_score / normalization_factor if normalization_factor else 0
    return int(final_normalized // 1)  # Discrete result

# Execute main logic
final_score = evaluate_performance(employee_stats, weight_map)

# Print result as required
print(f"Result: {final_score}")