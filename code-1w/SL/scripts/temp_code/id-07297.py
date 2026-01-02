from collections import Counter, defaultdict
import math

# Simulated system metrics from a distributed logging framework
def collect_logs(node_ids):
    logs = defaultdict(list)
    for node in node_ids:
        if node % 3 == 0:
            logs['warning'].append(f'Node {node} latency spike')
        elif node % 5 == 0:
            logs['error'].append(f'Node {node} timeout')
        else:
            logs['info'].append(f'Node {node} operational')
    return logs

def analyze_errors(log_entries):
    error_count = len(log_entries.get('error', []))
    warning_count = len(log_entries.get('warning', []))
    health_factor = 100 - (error_count * 8) - (warning_count * 3)
    return max(health_factor, 0)

def compute_entropy(data):
    # Irrelevant complexity: entropy calculation not used in final score
    freq = Counter(data)
    total = len(data)
    entropy = 0.0
    for count in freq.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 4)

def legacy_checksum(sequence):
    # Dead code path — never called in execution flow
    checksum = 0
    for i, val in enumerate(sequence):
        checksum ^= (val * (i + 1)) % 256
    return checksum

def normalize_vector(vec):
    # Distractor function: looks important but unused
    mag = math.sqrt(sum(x ** 2 for x in vec))
    return [x / mag for x in vec] if mag > 0 else vec

def filter_outliers(samples, threshold=2):
    mean_val = sum(samples) / len(samples)
    std_dev = math.sqrt(sum((x - mean_val) ** 2 for x in samples) / len(samples))
    filtered = [x for x in samples if abs(x - mean_val) <= threshold * std_dev]
    return filtered  # Used only to create decoy_result

def aggregate_metrics(raw):
    base_score = 0
    for entry in raw:
        if 'timeout' in entry:
            base_score -= 10
        elif 'spike' in entry:
            base_score -= 5
        elif 'operational' in entry:
            base_score += 2
    return base_score

def recursive_weight(depth, limit=4):
    if depth >= limit:
        return 1
    return depth * recursive_weight(depth + 1, limit)

def calculate_weights(levels):
    weights = {}
    for lvl in range(levels):
        weights[lvl] = recursive_weight(lvl + 1)
    return weights  # Computed but not used

def evaluate_performance(metrics, data):
    # Core logic hidden among distractions
    raw_logs = collect_logs(data['nodes'])
    health = analyze_errors(raw_logs)
    
    # Real signal: process performance counters
    counters = data['counters']
    total_ops = sum(counters)
    failed_ops = counters[3] + counters[7]  # Specific indices matter
    success_rate = (total_ops - failed_ops) / total_ops if total_ops > 0 else 0
    
    # Critical transformation
    adjusted_health = health * success_rate
    
    # Decoy computations using irrelevant functions
    decoy_data = [x % 7 for x in data['nodes'] if x % 4 == 0]
    decoy_entropy = compute_entropy(decoy_data)
    decoy_result = filter_outliers([decoy_entropy * 100, 42.5, 39.1, 45.0])
    
    # Unused complex structure
    weight_map = calculate_weights(5)
    vector_norm = normalize_vector([decoy_entropy, adjusted_health])
    
    # Final computation — depends only on adjusted_health and a fixed transform
    scaling_factor = 3.7
    final_value = int(round(adjusted_health * scaling_factor + 17))
    
    # This assignment is the key execution point
    final_score = final_value
    
    return final_score

# Simulated input data
benchmark_data = {
    'nodes': list(range(1, 101)),  # 100 nodes
    'counters': [100, 95, 90, 15, 80, 75, 70, 20, 60, 55],
    'config_id': 'DIST-2024',
    'version': 'v2.3-alpha'
}

metric_set = {'latency': 'high', 'throughput': 'medium'}

# Key execution point
final_score = evaluate_performance(metric_set, benchmark_data)
print(f"Result: {final_score}")