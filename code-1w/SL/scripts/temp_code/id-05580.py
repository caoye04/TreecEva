from collections import defaultdict, Counter
import math

# Simulated system metrics from a distributed task scheduler
task_logs = [
    {'node': 'A', 'status': 'success', 'duration': 120, 'retries': 0},
    {'node': 'B', 'status': 'failure', 'duration': 85, 'retries': 3},
    {'node': 'C', 'status': 'success', 'duration': 95, 'retries': 1},
    {'node': 'A', 'status': 'success', 'duration': 110, 'retries': 0},
    {'node': 'B', 'status': 'success', 'duration': 140, 'retries': 2},
    {'node': 'D', 'status': 'failure', 'duration': 70, 'retries': 4},
    {'node': 'C', 'status': 'failure', 'duration': 60, 'retries': 1},
    {'node': 'D', 'status': 'success', 'duration': 130, 'retries': 0}
]

# Irrelevant auxiliary function - dead code path (distractor)
def analyze_network_topology(nodes):
    return sum([hash(n) % 10 for n in nodes])

# Misleading intermediate metric (red herring)
effective_bandwidth = 0.0
for log in task_logs:
    if log['status'] == 'success':
        effective_bandwidth += 1 / (log['duration'] + 1)

effective_bandwidth *= 1000  # Decoy value, not used later

# Extract node-specific data
node_stats = defaultdict(list)
for log in task_logs:
    node_stats[log['node']].append(log)

# Compute success rate per node (relevant)
success_rates = {}
for node, logs in node_stats.items():
    successes = sum(1 for l in logs if l['status'] == 'success')
    success_rates[node] = successes / len(logs)

# Compute average duration for successful tasks only (relevant)
avg_durations = {}
for node, logs in node_stats.items():
    success_logs = [l for l in logs if l['status'] == 'success']
    if success_logs:
        avg_durations[node] = sum(l['duration'] for l in success_logs) / len(success_logs)
    else:
        avg_durations[node] = float('inf')

# Bit manipulation decoy (irrelevant)
flag_register = 0
for i, node in enumerate(node_stats.keys()):
    flag_register ^= (i + 1) << (i % 8)

# Another red herring: combinatorics on retry counts (not directly used)
all_retries = [log['retries'] for log in task_logs]
retry_counter = Counter(all_retries)
expected_retry_entropy = sum(
    -v/len(all_retries) * math.log(v/len(all_retries)) 
    for v in retry_counter.values()
)

# Baseline thresholds (reference values)
baseline = {
    'min_success_rate': 0.5,
    'max_avg_duration': 125.0
}

# Performance scoring function
def score_node(success_rate, avg_duration, baseline):
    # Base score from success rate
    base = 100 * success_rate
    
    # Penalty for exceeding duration threshold
    if avg_duration > baseline['max_avg_duration']:
        base -= 20 * (avg_duration - baseline['max_avg_duration']) / 10
    
    # Bonus for high reliability (low retries implied via status history)
    if success_rate >= 0.7:
        base += 15
    
    # Artificial cap
    return min(max(base, 0), 100)

# Evaluate overall performance
metrics = []
for node in sorted(node_stats.keys()):
    sr = success_rates[node]
    ad = avg_durations[node]
    score = score_node(sr, ad, baseline)
    metrics.append({'node': node, 'score': score})

# Final aggregation function
def evaluate_performance(metrics, baseline):
    total_weighted = 0.0
    total_nodes = len(metrics)
    
    # Apply weighting based on node load (simulated by name length - absurd but consistent)
    for m in metrics:
        weight = len(m['node'])  # Trivial but deterministic
        total_weighted += m['score'] * weight
    
    if total_nodes > 0:
        final = total_weighted / total_nodes
    else:
        final = 0.0
    
    # Additional adjustment: if any node had perfect score, add bonus
    perfect_bonus = 10 if any(m['score'] >= 99.9 for m in metrics) else 0
    final += perfect_bonus
    
    # Normalize to prevent overflow (not actually necessary here, but looks important)
    return round(final, 4)

# Critical statement
final_score = evaluate_performance(metrics, baseline)

# Print result as required
print(f"Target result: {final_score}")