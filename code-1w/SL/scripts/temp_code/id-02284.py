from collections import defaultdict, Counter
import math

# Simulated system metrics from a distributed network node
telemetry_data = [
    {'node': 'A', 'latency': 120, 'throughput': 850, 'errors': 3},
    {'node': 'B', 'latency': 95, 'throughput': 920, 'errors': 1},
    {'node': 'C', 'latency': 140, 'throughput': 700, 'errors': 6},
    {'node': 'A', 'latency': 110, 'throughput': 870, 'errors': 2},
    {'node': 'B', 'latency': 100, 'throughput': 900, 'errors': 0},
    {'node': 'D', 'latency': 80, 'throughput': 950, 'errors': 1}
]

# Irrelevant auxiliary function - dead code path (distractor)
def analyze_security_threats(logs):
    threat_level = 0
    for log in logs:
        if 'malicious' in log.get('activity', ''):
            threat_level += 1
    return threat_level

# Another decoy function that's never called
def calculate_network_diameter(topology):
    return len(topology) * 2 - 1

# Real processing begins here
def extract_node_metrics(data):
    raw_metrics = defaultdict(list)
    for entry in data:
        node = entry['node']
        raw_metrics[node].append({
            'latency': entry['latency'],
            'throughput': entry['throughput'],
            'errors': entry['errors']
        })
    return raw_metrics

# Misleading intermediate aggregation (partially relevant but overcomplicated)
def compute_averages(metrics_list):
    avg_data = {}
    for node, records in metrics_list.items():
        count = len(records)
        total_latency = sum(r['latency'] for r in records)
        total_throughput = sum(r['throughput'] for r in records)
        total_errors = sum(r['errors'] for r in records)
        
        # Decoy calculation with no downstream use
        anomaly_score = 0
        if total_latency / count > 100:
            anomaly_score += 1
        if total_errors > 4:
            anomaly_score += 2
        
        avg_data[node] = {
            'avg_latency': total_latency / count,
            'avg_throughput': total_throughput / count,
            'avg_errors': total_errors / count,
            'sample_count': count
        }
    return avg_data

# Red herring: unused transformation
def normalize_metrics(metrics):
    normalized = {}
    max_latency = max(m['avg_latency'] for m in metrics.values())
    max_throughput = max(m['avg_throughput'] for m in metrics.values())
    
    for node, vals in metrics.items():
        normalized[node] = {
            'n_latency': vals['avg_latency'] / max_latency,
            'n_throughput': vals['avg_throughput'] / max_throughput,
            'n_errors': min(vals['avg_errors'] * 10, 1.0)
        }
    return normalized

# Core evaluation logic
weights = {
    'latency_weight': 0.4,
    'throughput_weight': 0.5,
    'error_weight': 0.1
}

# Another distraction: historical baseline (not used in final calc)
historical_perf = {
    'baseline_latency': 105,
    'baseline_throughput': 880,
    'tolerance_window': 15
}

def evaluate_node_risk(avg_latency, avg_errors):
    # Complex-looking but actually simple risk logic (distraction through nesting)
    if avg_latency > 110:
        if avg_errors > 2.5:
            return 'HIGH'
        elif avg_errors > 1.0:
            return 'MEDIUM'
        else:
            return 'LOW'
    else:
        if avg_errors > 3.0:
            return 'MEDIUM'
        else:
            return 'LOW'
    
    # Dead code: unreachable
    return 'UNKNOWN'

# Key function that contributes to final answer
def evaluate_performance(metrics, weights):
    composite_scores = []
    
    # Process each node's average performance
    for node, data in metrics.items():
        latency_dev = data['avg_latency'] - 100  # target latency
        throughput_bonus = max(0, (data['avg_throughput'] - 800) / 100)
        error_penalty = data['avg_errors'] * 2
        
        # Meaningful score calculation buried in noise
        base_score = 100
        latency_impact = -abs(latency_dev) * 0.3
        throughput_impact = throughput_bonus * 5
        error_impact = -error_penalty * 4
        
        node_score = base_score + latency_impact + throughput_impact + error_impact
        
        # Distracting conditional with side effect that doesn't affect result
        if node_score < 85:
            audit_flag = True
            # Simulate logging (no real impact)
            log_entry = f"Audit: Node {node} score {node_score:.1f}"
        else:
            audit_flag = False
            temp_buffer = [0] * 5  # allocate but unused
        
        composite_scores.append(node_score)
    
    # Final aggregation - this is the real answer source
    raw_final = sum(composite_scores) / len(composite_scores)
    
    # Additional distractions
    outlier_count = 0
    mean_val = raw_final
    for s in composite_scores:
        if abs(s - mean_val) > 15:
            outlier_count += 1
    
    # Actual final score adjustment (minor)
    final_adjustment = 0
    if outlier_count >= 2:
        final_adjustment = -2
    
    final_result = raw_final + final_adjustment
    
    # Irrelevant bit manipulation (looks important but isn't)
    bit_analysis = (int(final_result) & 0xFF) ^ 0x5A
    
    return final_result

# Begin execution
raw_node_data = extract_node_metrics(telemetry_data)
avg_metrics = compute_averages(raw_node_data)
# normalize_metrics(avg_metrics)  # computed but not assigned (distractor)

# Critical statement
final_score = evaluate_performance(avg_metrics, weights)

# Print result as required
print(f"Target result: {final_score}")