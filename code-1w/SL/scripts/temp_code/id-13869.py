def analyze_efficiency(logs):
    total_entries = len(logs)
    unique_actions = set(logs)
    action_count = len(unique_actions)
    redundant_ops = total_entries - action_count

    efficiency_ratio = (action_count / total_entries) if total_entries > 0 else 0
    return efficiency_ratio, redundant_ops


def calculate_latency_score(response_times):
    avg_latency = sum(response_times) / len(response_times)
    max_latency = max(response_times)
    score = (100 - avg_latency) * (1 + (max_latency / 100))
    normalized_score = min(max(score, 0), 100)
    return normalized_score

logs = ['input', 'process', 'output', 'process', 'retry', 'input', 'process']
response_times = [12.5, 45.0, 23.1, 67.8, 18.9]

# Irrelevant computations (distractors)
baseline_metrics = {x: logs.count(x) for x in set(logs)}
temp_analysis = [len(action) for action in logs if 'o' in action]
phantom_value = sum(temp_analysis) * 0.1

# Key data
productivity, overhead = analyze_efficiency(logs)
latency_score = calculate_latency_score(response_times)

error_log = ['fail', 'warn', 'fail']
errors = len([e for e in error_log if e == 'fail'])

# Semi-relevant transformation
error_penalty = 10 if errors > 1 else 5
adjusted_latency = latency_score - error_penalty

# Conditional logic with case conversion distraction
status_flags = ['ACTIVE', 'idle', 'PAUSED']
capital_count = sum(1 for s in status_flags if s.isupper())
lower_to_upper_ratio = capital_count / len(status_flags) if len(status_flags) > 0 else 0

# Core computation chain
base_productivity_score = productivity * 100
consistency_bonus = 5 if overhead < 3 else 0

# Final evaluation with set-based filtering
valid_logs = set(logs) - {'retry'}
completion_rate = len(valid_logs) / len(set(['input', 'process', 'output']))

if completion_rate >= 0.8:
    final_score = base_productivity_score + consistency_bonus + adjusted_latency
else:
    final_score = base_productivity_score - 20

# Red herring: character counting in log entries
total_chars = sum(len(entry) for entry in logs)
char_avg = total_chars / len(logs)

Result: final_score