from collections import defaultdict, Counter
import math

# Simulated system telemetry data
telemetry_stream = [
    {'node': 'A', 'load': 0.45, 'errors': 2, 'timestamp': 1000},
    {'node': 'B', 'load': 0.78, 'errors': 0, 'timestamp': 1001},
    {'node': 'A', 'load': 0.62, 'errors': 1, 'timestamp': 1002},
    {'node': 'C', 'load': 0.33, 'errors': 4, 'timestamp': 1003},
    {'node': 'B', 'load': 0.85, 'errors': 0, 'timestamp': 1004},
    {'node': 'C', 'load': 0.91, 'errors': 3, 'timestamp': 1005}
]

# Irrelevant helper (distractor)
def smooth_data(data, alpha=0.1):
    smoothed = []
    for i, x in enumerate(data):
        if i == 0:
            smoothed.append(x)
        else:
            smoothed.append(alpha * x + (1 - alpha) * smoothed[i-1])
    return smoothed

# Misleading performance estimator (dead path)
def legacy_evaluate(nodes):
    base = len(nodes) * 100
    penalty = sum([10 for n in nodes if n['load'] > 0.8])
    return base - penalty  # Never used

# Core aggregation logic
def collect_metrics(stream):
    raw_stats = defaultdict(list)
    error_counter = Counter()
    
    for entry in stream:
        node = entry['node']
        raw_stats[node].append(entry['load'])
        if entry['errors'] > 0:
            error_counter[node] += entry['errors']
    
    # Distractor: unused transformation
    normalized_loads = {}
    for node, loads in raw_stats.items():
        avg = sum(loads) / len(loads)
        normalized_loads[node] = avg if avg <= 1.0 else 1.0
    
    # Another red herring: entropy calculation (unused)
    def shannon_entropy(values):
        total = sum(values)
        probs = [v/total for v in values if total > 0]
        return -sum(p * math.log2(p) for p in probs if p > 0)
    
    entropy_val = shannon_entropy(list(error_counter.values()))

    # Actual returned metrics
    metrics = {}
    for node in raw_stats:
        loads = raw_stats[node]
        avg_load = sum(loads) / len(loads)
        max_load = max(loads)
        error_count = error_counter.get(node, 0)
        metrics[node] = {
            'avg_load': avg_load,
            'max_load': max_load,
            'error_count': error_count,
            'stability': 100 * (1 - avg_load)  # Higher is better
        }
    return metrics

# Benchmark reference data (simulated)
benchmark_data = {
    'baseline_stability': 85.0,
    'tolerance_window': 0.15,
    'penalty_rate': 7.5,
    'grace_nodes': ['B'],  # Nodes exempt from certain penalties
    'priority_threshold': 0.7
}

# Core evaluation with complex logic and decoys
def evaluate_performance(metrics, config):
    total_score = 0.0
    penalty_adjustment = 0
    debug_flags = []
    
    # Fake scoring branch (never executed)
    if False and 'simulated_failure' in config:
        return sum(math.sin(m['avg_load']) for m in metrics.values()) * 100
    
    # Real scoring logic
    for node, m in metrics.items():
        score_component = m['stability']
        
        # Base adjustment
        if m['avg_load'] > config['priority_threshold']:
            score_component *= 0.9
            
        # Critical path: error-based deduction
        if m['error_count'] > 0 and node not in config['grace_nodes']:
            reduction = m['error_count'] * config['penalty_rate']
            score_component -= reduction
        
        # Max load bonus (conditional)
        if m['max_load'] < 0.8:
            score_component += 5
            
        # Decoy bitwise manipulation (looks important but irrelevant)
        encoded = 0
        for c in node:
            encoded ^= ord(c) << 2
        encoded &= 0xFF
        if encoded % 3 == 0:
            debug_flags.append(f"Node {node} passed filter")
        
        total_score += score_component
    
    # Secondary correction based on benchmark window
    drift = abs(metrics['A']['avg_load'] - metrics['B']['avg_load'])
    if drift > config['tolerance_window']:
        total_score -= 10
    
    # Final clamping
    final_raw = max(0, min(500, total_score))
    
    # Red herring: floating point refinement (no effect due to int cast later)
    refined = round(final_raw + 0.5 * math.cos(drift * math.pi), 4)
    
    # Key assignment - target variable
    final_score = int(refined)
    return final_score

# Unused diagnostic function (distractor)
def generate_health_report(metrics):
    report = defaultdict(dict)
    for node, data in metrics.items():
        status = 'HEALTHY'
        if data['max_load'] > 0.9:
            status = 'CRITICAL'
        elif data['error_count'] >= 3:
            status = 'WARNING'
        report[node]['status'] = status
        report[node]['score_hint'] = data['stability'] - 5 * data['error_count']
    return report

# Main execution flow
metrics = collect_metrics(telemetry_stream)
evaluation_snapshot = legacy_evaluate([{'load': 0.5}])  # Dead call
final_score = evaluate_performance(metrics, benchmark_data)
print(f"Result: {final_score}")