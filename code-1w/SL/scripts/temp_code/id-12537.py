from collections import defaultdict, Counter
import math

# Simulated system metrics from a distributed task scheduler
task_records = [
    {'node': 'A', 'latency': 120, 'success': True, 'retries': 0},
    {'node': 'B', 'latency': 190, 'success': False, 'retries': 3},
    {'node': 'A', 'latency': 85, 'success': True, 'retries': 0},
    {'node': 'C', 'latency': 210, 'success': True, 'retries': 1},
    {'node': 'B', 'latency': 178, 'success': True, 'retries': 1},
    {'node': 'C', 'latency': 205, 'success': False, 'retries': 2},
    {'node': 'A', 'latency': 92, 'success': True, 'retries': 0},
    {'node': 'D', 'latency': 300, 'success': False, 'retries': 3},
]

# Irrelevant helper (distractor)
def smooth_data(data):
    return [x * 0.95 for x in data]

# Misleading preprocessing (dead path)
raw_latencies = [r['latency'] for r in task_records]
smoothed_latencies = smooth_data(raw_latencies)

# Node-level aggregation
def aggregate_node_metrics(records):
    node_stats = defaultdict(lambda: {
        'total_tasks': 0,
        'successful': 0,
        'retry_count': 0,
        'latency_sum': 0
    })
    
    for r in records:
        n = r['node']
        node_stats[n]['total_tasks'] += 1
        if r['success']:
            node_stats[n]['successful'] += 1
        node_stats[n]['retry_count'] += r['retries']
        node_stats[n]['latency_sum'] += r['latency']
    
    result = {}
    for node, stats in node_stats.items():
        success_rate = stats['successful'] / stats['total_tasks']
        avg_retries = stats['retry_count'] / stats['total_tasks']
        avg_latency = stats['latency_sum'] / stats['total_tasks']
        # Composite score with arbitrary scaling
        score = (success_rate * 50) - (avg_retries * 15) - (avg_latency / 10)
        result[node] = {
            'score': score,
            'details': {
                'success_rate': success_rate,
                'avg_retries': avg_retries,
                'avg_latency': avg_latency
            }
        }
    
    return result

# Secondary analysis - distractor only
failure_counter = Counter([r['node'] for r in task_records if not r['success']])
skew_index = sum([v**2 for v in failure_counter.values()])  # Red herring metric

# Real evaluation logic
node_metrics = aggregate_node_metrics(task_records)

# Weight configuration for final score (subject to change)
weights = {
    'A': 0.4,
    'B': 0.3,
    'C': 0.2,
    'D': 0.1
}

# Decoy normalization function (never called)
def normalize_scores(scores):
    total = sum(scores.values())
    return {k: v/total for k, v in scores.items()}

# Evaluate overall system performance
metrics = {node: data['score'] for node, data in node_metrics.items()}

def evaluate_performance(metrics, weights):
    # Apply modular weighting
    weighted_sum = 0
    for node, score in metrics.items():
        if node in weights:
            contribution = score * weights[node]
            weighted_sum += contribution
    
    # Apply damping factor for stability
    if 'D' in metrics and metrics['D'] < 0:
        weighted_sum *= 0.8
    
    # Additional penalty if node B has low performance
    if metrics.get('B', 0) < 10:
        weighted_sum -= 5
    
    # Final nonlinear transformation
    final_value = math.log(abs(weighted_sum) + 10) * 2
    
    # Dead code branch (misleading)
    if False:
        final_value = max(final_value, 50)  # Never executed
    
    return final_value

# Execute main logic
baseline_shift = sum([r['retries'] for r in task_records])  # Irrelevant summary
intermediate_checksum = len(task_records) * 17 % 13  # Distractor

final_score = evaluate_performance(metrics, weights)

# Print target result
print(f"Result: {final_score}")