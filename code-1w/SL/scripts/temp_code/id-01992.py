from collections import defaultdict

# Simulate daily task tracking across teams
task_logs = [
    ['write', 'debug', 'write', 'review', 'write', 'write'],
    ['debug', 'debug', 'review', 'write', 'review', 'debug'],
    ['write', 'write', 'write', 'debug', 'review', 'review']
]

# Irrelevant frequency count (distractor)
action_frequency = defaultdict(int)
for log in task_logs:
    for action in log:
        action_frequency[action] += 1

# Compute team productivity metrics
productivity = []
errors = []
penalty_weights = {'write': 1, 'debug': 2, 'review': 1}

for i, log in enumerate(task_logs):
    total_effort = sum(penalty_weights[action] for action in log)
    debug_count = log.count('debug')
    review_ratio = log.count('review') / len(log) if log else 0

    # Intermediate score with misleading calculation (semi-relevant)
    raw_score = total_effort * (1 + review_ratio) - debug_count * 0.5
    productivity.append(round(raw_score, 2))

    # Error metric based on debug prevalence
    error_metric = debug_count * 3 - review_ratio * 5
    errors.append(max(error_metric, 0))

# Unused helper function (dead code - distractor)
def calculate_team_synergy(logs):
    synergy = 0
    for log in logs:
        if 'write' in log and 'review' in log and 'debug' not in log:
            synergy += 1
    return synergy

# Threshold logic with nested conditions
threshold = 8.0
high_performance_count = 0
for p in productivity:
    if p > threshold:
        high_performance_count += 1

# Auxiliary computation that looks important but isn't used (distractor)
avg_productivity = sum(productivity) / len(productivity) if productivity else 0
adjusted_threshold = avg_productivity * 0.9

# Real evaluation logic buried among distractions
def evaluate_performance(efficiency, fault_rate, limit):
    score = 100
    for i in range(len(efficiency)):
        if efficiency[i] > limit:
            score += 10
        if fault_rate[i] > 4:
            score -= 15
        elif fault_rate[i] > 2:
            score -= 5
    # Additional penalty for imbalance
    balanced_pairs = 0
    for i in range(len(efficiency)):
        for j in range(i+1, len(efficiency)):
            if abs(efficiency[i] - efficiency[j]) < 2.0:
                balanced_pairs += 1
    if balanced_pairs >= 3:
        score += 8
    return score

# Misleading normalization step (not affecting final result)
normalized_errors = [e / max(errors) if max(errors) > 0 else 0 for e in errors]

# Critical statement
final_score = evaluate_performance(productivity, errors, threshold)

# Result output
print(f"Result: {final_score}")