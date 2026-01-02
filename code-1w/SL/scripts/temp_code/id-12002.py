from collections import defaultdict, Counter
import math

# Simulated system metrics from a distributed network node
raw_data = [
    {'node': 'A', 'latency': 45, 'throughput': 820, 'errors': 3},
    {'node': 'B', 'latency': 67, 'throughput': 910, 'errors': 1},
    {'node': 'C', 'latency': 52, 'throughput': 740, 'errors': 5},
    {'node': 'D', 'latency': 38, 'throughput': 980, 'errors': 0},
    {'node': 'E', 'latency': 58, 'throughput': 850, 'errors': 2}
]

# Irrelevant processing: character frequency in node names (red herring)
def analyze_node_names(data):
    chars = []
    for entry in data:
        chars.extend(list(entry['node'].lower()))
    return Counter(chars)

name_freq = analyze_node_names(raw_data)  # Unused result

# Misleading intermediate calculation: average error rate (not used in final logic)
avg_error_rate = sum(d['errors'] for d in raw_data) / len(raw_data)

# Weight initialization with decoy weights
weights = defaultdict(float)
weights['latency'] = 0.3
weights['throughput'] = 0.5
weights['errors'] = 0.2
weights['decoy_metric'] = 0.1  # Never used

# Transform raw data into normalized feature vectors
def normalize_metrics(data_list):
    norm_data = []
    latencies = [d['latency'] for d in data_list]
    throughputs = [d['throughput'] for d in data_list]
    max_latency = max(latencies)
    min_latency = min(latencies)
    max_throughput = max(throughputs)
    min_throughput = min(throughputs)
    
    for d in data_list:
        norm_lat = (max_latency - d['latency']) / (max_latency - min_latency)  # Inverted: lower latency = higher score
        norm_tp = (d['throughput'] - min_throughput) / (max_throughput - min_throughput)
        norm_er = 1 - (d['errors'] / 10)  # Assume max 10 errors for normalization
        norm_data.append({'latency': norm_lat, 'throughput': norm_tp, 'errors': norm_er})
    return norm_data

normalized_metrics = normalize_metrics(raw_data)

# Decoy function: calculates pairwise correlations (unused)
def compute_pairwise_correlations(metrics_list):
    pairs = zip(metrics_list, metrics_list[1:])
    correlations = []
    for m1, m2 in pairs:
        corr = (m1['latency'] * m2['latency'] + 
                m1['throughput'] * m2['throughput'] + 
                m1['errors'] * m2['errors'])
        correlations.append(corr)
    return correlations

# This call has no effect on final result
dummy_correlations = compute_pairwise_correlations(normalized_metrics)

# Real evaluation logic hidden among distractions
def evaluate_performance(metrics, weight_map):
    composite_scores = []
    for idx, m in enumerate(metrics):
        # Apply weighted sum using only the three real metrics
        score = (m['latency'] * weight_map['latency'] + 
                 m['throughput'] * weight_map['throughput'] + 
                 m['errors'] * weight_map['errors'])
        composite_scores.append((idx, score))
    
    # Sort by score descending
    sorted_scores = sorted(composite_scores, key=lambda x: x[1], reverse=True)
    
    # Boost top performer's score exponentially (bonus)
    if sorted_scores:
        top_idx, top_score = sorted_scores[0]
        boosted_score = top_score * math.exp(0.1)  # Bonus for highest scorer
        composite_scores[top_idx] = (top_idx, boosted_score)
    
    # Final aggregation: harmonic mean of all composite scores (more sensitive to low values)
    non_zero_scores = [s for _, s in composite_scores if s > 0]
    if not non_zero_scores:
        return 0.0
    
    sum_inv = sum(1/s for s in non_zero_scores)
    harmonic_mean = len(non_zero_scores) / sum_inv
    
    # Apply final nonlinear transformation: sigmoid-like compression
    final_value = 100 / (1 + math.exp(-10 * (harmonic_mean - 0.5)))
    
    # DEAD CODE PATH: adjustment based on decoy metric (never reached)
    # if weight_map['decoy_metric'] > 0.05:
    #     final_value *= 0.9
    
    return final_value

# Critical execution point
final_score = evaluate_performance(normalized_metrics, weights)

# Output the target result
print(f"Result: {final_score}")