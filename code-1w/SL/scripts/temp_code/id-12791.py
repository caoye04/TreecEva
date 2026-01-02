from collections import defaultdict

# Simulate user interaction analytics for a productivity tool
user_actions = [
    ('task_complete', 5), ('scroll', 2), ('task_complete', 8), ('click', 1),
    ('task_complete', 7), ('scroll', 3), ('hover', 4), ('task_complete', 6)
]

# Aggregation containers
action_counts = defaultdict(int)
completion_values = []
temp_buffer = []
overhead_tracker = {'latency': 0, 'redundant_ops': 0}

# Process each action with side tracking
for action, duration in user_actions:
    action_counts[action] += 1
    if action == 'task_complete':
        completion_values.append(duration)
        # Redundant but misleading computation
        overhead_tracker['latency'] += duration * 0.1
    else:
        # Dead code path - never affects final result
        temp_buffer.append(duration ** 2)
        overhead_tracker['redundant_ops'] += 1

# Irrelevant transformation (distractor)
squared_completions = list(map(lambda x: x**2, completion_values))
inverse_completions = [1 / x for x in completion_values if x > 0]

# Core logic disguised among alternatives
raw_total = sum(completion_values)
penalty_factor = len(temp_buffer) * 0.5  # Unused distraction
normalization_base = len(completion_values)

# Multiple candidate metrics created, only one used
metric_candidates = {
    'avg_raw': raw_total / normalization_base,
    'weighted': sum(d * i for i, d in enumerate(completion_values)),
    'adjusted': (raw_total + 2) / (normalization_base + 1)
}

# Decision logic with red herring condition
use_adjusted = action_counts['scroll'] > 2
if use_adjusted:
    base_metric = metric_candidates['avg_raw']  # Misleading: condition true but not used
else:
    base_metric = metric_candidates['avg_raw']

# Final aggregation function defined as lambda (core python idiom)
aggregate_performance = lambda data: int(sum(data) / len(data)) + action_counts['task_complete']

# Critical execution point
feedback_summary = completion_values
final_score = aggregate_performance(feedback_summary)

print(f"Result: {final_score}")