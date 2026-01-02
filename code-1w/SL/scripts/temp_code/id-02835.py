from collections import defaultdict, Counter
import itertools

# Simulated system telemetry data (distraction: not all fields are used)
technical_metrics = [
    {'node': 'A', 'latency_ms': 120, 'retries': 2, 'success': True, 'version': '2.1'},
    {'node': 'B', 'latency_ms': 85, 'retries': 0, 'success': True, 'version': '2.2'},
    {'node': 'C', 'latency_ms': 150, 'retries': 1, 'success': False, 'version': '2.0'},
    {'node': 'A', 'latency_ms': 95, 'retries': 0, 'success': True, 'version': '2.1'},
    {'node': 'B', 'latency_ms': 110, 'retries': 3, 'success': True, 'version': '2.2'},
]

# Irrelevant auxiliary function (dead code path)
def analyze_version_trends(data):
    version_count = Counter()
    for entry in data:
        version_count[entry['version']] += 1
    return dict(version_count)

# Unused transformation pipeline (distractor)
processed_chain = list(itertools.starmap(
    lambda x, y: x * 2 + y,
    [(10, 5), (20, 10), (30, 15)]
))

# Benchmark thresholds (mixed relevance)
benchmarks = {
    'latency_cap': 100,
    'max_retries': 1,
    'min_success_rate': 0.8
}

# Misleading intermediate calculation (red herring)
total_retry_count = sum(entry['retries'] for entry in technical_metrics)
avg_latency = sum(entry['latency_ms'] for entry in technical_metrics) / len(technical_metrics)

# Core logic disguised among distractions
def extract_node_stats(metrics):
    node_data = defaultdict(list)
    for m in metrics:
        node_data[m['node']].append(m)
    return node_data

# Heavily branched scoring logic with decoy conditions
def calculate_node_efficiency(records):
    if not records:
        return 0.0
    
    # Real metric: percentage of low-latency operations
    fast_ops = sum(1 for r in records if r['latency_ms'] < 100)
    efficiency = fast_ops / len(records)
    
    # Distraction: unused complexity
    penalty = 0
    for r in records:
        if r['retries'] > 2:
            penalty += 1  # never actually applied
    
    return efficiency

# Fake optimization pass (no impact on result)
optimized_metrics = [m for m in technical_metrics if m['success']]
baseline_nodes = ['A', 'B', 'C']

# Real aggregation function buried in noise
def evaluate_performance(raw_data, config):
    stats_per_node = extract_node_stats(raw_data)
    scores = {}
    
    # Actual computation begins here — multiple steps hidden in loop
    for node, entries in stats_per_node.items():
        base_efficiency = calculate_node_efficiency(entries)
        
        # Secondary valid criterion: retry compliance
        compliant_retries = all(e['retries'] <= config['max_retries'] for e in entries)
        
        # Tertiary: must meet latency cap on at least 75% of calls
        latency_compliance = sum(e['latency_ms'] <= config['latency_cap'] for e in entries) / len(entries) >= 0.75
        
        # Combine into composite score (only this matters)
        quality_weight = 1.0 if compliant_retries else 0.5
        timeliness_weight = 1.0 if latency_compliance else 0.6
        
        final_node_score = base_efficiency * quality_weight * timeliness_weight
        scores[node] = final_node_score
    
    # The true answer derives from aggregated scores
    aggregate_values = sorted(scores.values())
    midpoint = len(aggregate_values) // 2
    # Final score is median adjusted by length-normalized pattern
    adjustment = len(aggregate_values) * 0.85
    result = (aggregate_values[midpoint] * 1000) + adjustment  # key computation
    
    # Dead return branch (misleading)
    if False:
        fallback = sum(aggregate_values) / len(aggregate_values)
        return int(fallback * 100)
    
    return int(result)

# Auxiliary unused filter chain (irrelevant)
critical_nodes = list(filter(lambda n: n in ['A', 'B'], stats_per_node.keys()))

# Key execution point — the answer depends on this call
metric_data = extract_node_stats(technical_metrics)
final_score = evaluate_performance(metric_data, benchmarks)

# Output required format
print(f"Result: {final_score}")