from collections import defaultdict, Counter
import math

# Simulated system telemetry data
telemetry_stream = [
    {'node': 'A', 'load': 0.7, 'errors': 2, 'latency': 120},
    {'node': 'B', 'load': 0.9, 'errors': 5, 'latency': 180},
    {'node': 'A', 'load': 0.6, 'errors': 1, 'latency': 95},
    {'node': 'C', 'load': 0.4, 'errors': 0, 'latency': 60},
    {'node': 'B', 'load': 0.95, 'errors': 7, 'latency': 210},
    {'node': 'D', 'load': 0.3, 'errors': 0, 'latency': 45}
]

# Irrelevant baseline configuration (distractor)
default_config = {
    'timeout': 30,
    'retries': 3,
    'protocol': 'tcp',
    'buffer_size': 4096
}

# Decoy function - never called but looks relevant
def compute_health_v1(nodes):
    return sum([1 for n in nodes if n['load'] < 0.8])

# Data aggregator with red herring logic
def aggregate_metrics(stream):
    node_stats = defaultdict(lambda: {'total_load': 0, 'error_count': 0, 'response_times': []})
    performance_flags = set()
    temp_buffer = []  # Unused buffer (dead code path)

    for event in stream:
        node_id = event['node']
        node_stats[node_id]['total_load'] += event['load']
        node_stats[node_id]['error_count'] += event['errors']
        node_stats[node_id]['response_times'].append(event['latency'])

        if event['errors'] > 4:
            performance_flags.add(f"HIGH_ERRORS_{node_id}")

    # Dead code: this block is logically unreachable due to prior structure
    if len(temp_buffer) > 100:
        overflow_flag = True
        performance_flags.add("BUFFER_OVERFLOW")

    return node_stats

# Secondary analysis - partially relevant but contains decoys
def analyze_stability(metrics):
    stability_scores = {}
    transient_issues = Counter()

    for node, data in metrics.items():
        avg_load = data['total_load'] / len(data['response_times'])
        error_rate = data['error_count'] / len(data['response_times'])
        latency_variance = sum((t - sum(data['response_times'])/len(data['response_times']))**2 
                                for t in data['response_times']) / len(data['response_times'])

        # Meaningless transformation (distractor)
        synthetic_metric = math.log(1 + avg_load * 10) + math.sqrt(latency_variance / 100)

        stability_scores[node] = {
            'score': 100 * (1 - avg_load) - 10 * error_rate,
            'variance': latency_variance,
            'synthetic': synthetic_metric  # Unused downstream
        }

        if error_rate > 0.05:
            transient_issues['high_error'] += 1
        if latency_variance > 2000:
            transient_issues['high_jitter'] += 1

    return stability_scores

# Core evaluation logic with key computation buried in noise
def evaluate_performance(raw_data, threshold=0.75):
    aggregated = aggregate_metrics(raw_data)
    analyzed = analyze_stability(aggregated)

    # Distractor variables
    debug_trace = []
    audit_log = []
    anomaly_report = defaultdict(list)

    total_value = 0
    node_contributions = []

    for node, profile in analyzed.items():
        base_score = profile['score']
        jitter_penalty = 0

        # Real logic: only nodes with variance below threshold contribute
        if profile['variance'] < 2500:  # Actual filter condition
            adjusted = base_score * (1.0 if base_score >= 60 else 0.8)
            node_contributions.append(adjusted)

        # Dead branch: never taken due to fixed constants above
        if profile['synthetic'] > 10:
            anomaly_report[node].append('ABNORMAL_SYNTHETIC')

        # Irrelevant logging simulation
        audit_entry = f"Node {node}: Score={base_score:.1f}"
        audit_log.append(audit_entry)

    # Critical calculation embedded among distractors
    raw_sum = sum(node_contributions)
    count_bonus = len(node_contributions) * 5
    penalty_factor = 2 if len(anomaly_report) > 0 else 0  # Always 0 due to dead branch

    final_raw = raw_sum + count_bonus - penalty_factor

    # Additional distraction: unused complex structure
    summary_matrix = [
        [math.sin(i * 0.1) for i in range(5)] for _ in range(len(node_contributions))
    ]

    # This is the actual answer variable
    final_score = int(round(final_raw))

    # Print required for execution trace
    print(f"Result: {final_score}")
    return final_score

# Misleading pre-processing (looks important but only used once)
filtered_telemetry = [event for event in telemetry_stream if event['load'] > 0.25]
efficiency_threshold = 0.75
metric_data = filtered_telemetry  # Renamed reference

# Key execution point
final_score = evaluate_performance(metric_data, efficiency_threshold)