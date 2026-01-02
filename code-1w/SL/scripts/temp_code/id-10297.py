from collections import defaultdict, Counter
import math

# Simulated system metrics from a distributed task scheduler
task_logs = [
    {'task': 'A', 'status': 'success', 'duration': 120, 'priority': 3},
    {'task': 'B', 'status': 'failure', 'duration': 45, 'priority': 5},
    {'task': 'C', 'status': 'success', 'duration': 200, 'priority': 2},
    {'task': 'D', 'status': 'success', 'duration': 90, 'priority': 4},
    {'task': 'E', 'status': 'failure', 'duration': 300, 'priority': 1},
    {'task': 'F', 'status': 'success', 'duration': 60, 'priority': 5}
]

# Irrelevant auxiliary function - dead code path
def analyze_network_traffic():
    traffic_data = [12.5, 10.3, 8.7, 15.2, 9.1]
    avg_load = sum(traffic_data) / len(traffic_data)
    threshold_alert = avg_load > 10
    return threshold_alert

# Misleading preprocessing step with decoy output
def preprocess_logs(logs):
    decoy_sum = 0
    for log in logs:
        decoy_sum += log['duration'] * (log['priority'] + 1)
    normalized = [d['duration'] * 0.95 for d in logs]  # Not actually used later
    return normalized

# Another red herring: unused data transformation
temp_records = []
for entry in task_logs:
    if entry['status'] == 'failure':
        temp_records.append({
            'id': entry['task'],
            'penalty': entry['duration'] * 0.1
        })

# Decoy statistical summary that looks important but is unused
decoy_stats = {
    'total_tasks': len(task_logs),
    'success_rate': len([t for t in task_logs if t['status'] == 'success']) / len(task_logs),
    'avg_duration': sum(t['duration'] for t in task_logs) / len(task_logs)
}

# Real processing begins here — deeply nested and obscured by prior noise
raw_data = defaultdict(float)
success_count = 0
failure_penalty = 0

for record in task_logs:
    duration_weight = 1 / (record['duration'] + 1e-5)
    priority_bonus = math.log(record['priority'] + 1)
    
    if record['status'] == 'success':
        raw_data['base_yield'] += duration_weight * priority_bonus
        success_count += 1
    else:
        raw_data['base_yield'] -= priority_bonus ** 1.5
        failure_penalty += record['duration'] * 0.01

# Hidden normalization factor computed via bit manipulation (obscure but valid)
normalizer = (success_count << 2) ^ 7  # XOR with prime for 'hashing'
if normalizer == 0:
    normalizer = 1

raw_data['base_yield'] /= normalizer

# Secondary metric: task diversity index
task_priorities = [t['priority'] for t in task_logs]
priority_counter = Counter(task_priorities)
diversity_index = len(priority_counter)

# Spurious unrelated calculation
redundant_entropy = 0
for count in priority_counter.values():
    prob = count / len(task_priorities)
    redundant_entropy -= prob * math.log(prob)

# Actual metric weights — introduced late and mixed with decoys
metric_weights = {
    'efficiency': 0.4,
    'robustness': 0.35,
    'adaptability': 0.25
}

# Core evaluation logic buried after distractions
def compute_efficiency(data):
    return abs(data['base_yield']) * 100

def compute_robustness(fail_count, total):
    return (1 - fail_count / total) * 80 if total > 0 else 0

def adjust_for_adaptability(diversity):
    return min(diversity * 10, 100) * 0.6

# Final performance evaluator — depends on multiple prior steps
def evaluate_performance(weights, data):
    failures = len([t for t in task_logs if t['status'] == 'failure'])
    total = len(task_logs)
    
    e1 = compute_efficiency(data)
    e2 = compute_robustness(failures, total)
    e3 = adjust_for_adaptability(diversity_index)
    
    # Critical distractor: irrelevant intermediate combination
    phantom_score = (e1 * 0.5) + (e2 * 0.3) + (e3 * 0.2)
    phantom_score = round(phantom_score, 2)  # Looks final but isn't used
    
    # True computation path
    weighted_sum = (
        weights['efficiency'] * e1 +
        weights['robustness'] * e2 +
        weights['adaptability'] * e3
    )
    
    # Final adjustment using bitwise masking to obscure logic
    mask = 0xFF  # Use only lowest 8 bits
    final_value = int(weighted_sum) & mask  # Ensures 0-255 range
    
    return final_value

# Execution point of interest
final_score = evaluate_performance(metric_weights, raw_data)

# Output the target result
print(f"Target result: {final_score}")