from collections import defaultdict, Counter

# Simulated system metrics from a distributed task scheduler
task_logs = [
    {'node': 'A', 'status': 'success', 'duration': 120, 'retries': 0, 'priority': 3},
    {'node': 'B', 'status': 'failure', 'duration': 85, 'retries': 2, 'priority': 5},
    {'node': 'A', 'status': 'success', 'duration': 95, 'retries': 1, 'priority': 4},
    {'node': 'C', 'status': 'success', 'duration': 200, 'retries': 0, 'priority': 2},
    {'node': 'B', 'status': 'success', 'duration': 110, 'retries': 1, 'priority': 5},
    {'node': 'D', 'status': 'failure', 'duration': 60, 'retries': 3, 'priority': 1},
    {'node': 'C', 'status': 'failure', 'duration': 180, 'retries': 2, 'priority': 3}
]

# Irrelevant helper (distractor)
def calculate_efficiency(logs):
    total_time = sum(entry['duration'] for entry in logs)
    total_retries = sum(entry['retries'] for entry in logs)
    return total_time / (total_retries + 1) if total_retries > 0 else total_time

efficiency_metric = calculate_efficiency(task_logs)  # Distractor variable

# Misleading performance indicator (dead path)
node_success_rate = defaultdict(int)
total_per_node = defaultdict(int)
for log in task_logs:
    total_per_node[log['node']] += 1
    if log['status'] == 'success':
        node_success_rate[log['node']] += 1

for node in node_success_rate:
    node_success_rate[node] /= total_per_node[node]

# Unused transformation (red herring)
sorted_logs = sorted(task_logs, key=lambda x: (-x['priority'], x['duration']))
filtered_logs = [log for log in sorted_logs if log['priority'] >= 3]

# Core metric computation
base_scores = []
penalty_map = defaultdict(float)
for entry in task_logs:
    base = entry['duration'] * 0.1
    retries_penalty = entry['retries'] * 15
    priority_bonus = 10 if entry['priority'] >= 4 else 0
    status_penalty = 50 if entry['status'] == 'failure' else 0
    total_entry_score = base + retries_penalty - priority_bonus + status_penalty
    base_scores.append(total_entry_score)
    penalty_map[entry['node']] += retries_penalty  # Aggregation not used later

# Secondary distractor: string-based anomaly detection
anomalies = []
critical_nodes = set()
for log in task_logs:
    duration_str = str(log['duration'])
    if '0' in duration_str and log['retries'] > 1:
        anomalies.append(log['node'])
if len(anomalies) > 2:
    critical_nodes.update(anomalies)

# Another red herring: character frequency analysis on node names
node_name_chars = ''.join(set(log['node'] for log in task_logs))
char_freq = Counter(node_name_chars * 2)  # Useless but looks meaningful

# Conditional expression with nested logic (core relevance starts here)
adjusted_base = sum(
    score * (0.9 if i % 2 == 0 else 1.1) 
    for i, score in enumerate(base_scores)
)

# Benchmark thresholds (misleading constants)
thresholds = {
    'low': 100,
    'medium': 200,
    'high': 500
}

# Actual evaluation logic buried in distractions
def evaluate_performance(scores, bench):
    avg = sum(scores) / len(scores)
    volatility = max(scores) - min(scores)
    
    # Complex conditional logic with decoy branches
    if avg < bench['low']:
        level = 'optimal'
        multiplier = 1.2
    elif avg < bench['medium']:
        level = 'stable'
        multiplier = 1.0
    elif avg < bench['high']:
        level = 'warning'
        multiplier = 0.85
    else:
        level = 'critical'
        multiplier = 0.6
    
    # Additional adjustment based on failure count
    failure_count = sum(1 for log in task_logs if log['status'] == 'failure')
    if failure_count == 0:
        multiplier += 0.1
    elif failure_count <= 2:
        pass  # Neutral
    else:
        multiplier -= 0.05 * (failure_count - 2)
    
    # Final adjustment using conditional expression
    final_value = (avg * multiplier) if volatility < 150 else (avg * multiplier * 0.9)
    
    # Dead code block (never reached due to logic above)
    if False:
        backup = 0
        for s in scores:
            backup += s ** 0.5
        final_value = backup
    
    return int(final_value)

metrics = base_scores
final_score = evaluate_performance(metrics, thresholds)

# Print result as required
print(f"Result: {final_score}")