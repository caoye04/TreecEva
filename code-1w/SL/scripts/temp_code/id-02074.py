from collections import defaultdict, Counter
import math

# Simulated system performance metrics
def get_raw_metrics():
    return [
        {'response_time': 120, 'throughput': 85, 'errors': 2, 'load': 70},
        {'response_time': 95, 'throughput': 92, 'errors': 1, 'load': 65},
        {'response_time': 130, 'throughput': 78, 'errors': 3, 'load': 75},
        {'response_time': 110, 'throughput': 88, 'errors': 0, 'load': 68}
    ]

# Irrelevant helper - distractor
def analyze_load_distribution(data):
    load_counts = defaultdict(int)
    for entry in data:
        bucket = entry['load'] // 10
        load_counts[bucket] += 1
    return load_counts

# Misleading normalization function - not actually used in final calculation
def normalize_metric(value, min_val, max_val):
    if max_val == min_val:
        return 0.5
    return (value - min_val) / (max_val - min_val)

# Decoy scoring - looks important but unused
def calculate_health_score(metrics_list):
    score = 0
    for m in metrics_list:
        rt_norm = normalize_metric(m['response_time'], 50, 200)
        tp_norm = normalize_metric(m['throughput'], 50, 100)
        err_penalty = m['errors'] * 10
        score += (1 - rt_norm) * 40 + tp_norm * 30 - err_penalty
    return score / len(metrics_list)

# Real processing begins here

def extract_key_indicators(raw_data):
    indicators = []
    for record in raw_data:
        # Compute efficiency ratio: throughput per millisecond response time
        efficiency = record['throughput'] / record['response_time']
        # Latency penalty for response times over 100ms
        latency_penalty = 5 if record['response_time'] > 100 else 0
        # Throughput bonus for high performers
        tp_bonus = 3 if record['throughput'] >= 90 else 0
        indicators.append({
            'efficiency': efficiency,
            'latency_penalty': latency_penalty,
            'tp_bonus': tp_bonus,
            'net_quality': efficiency * 100 - latency_penalty + tp_bonus
        })
    return indicators

# Secondary transformation with red herring operations
def transform_indicators(indicators):
    transformed = []
    efficiency_values = [ind['efficiency'] for ind in indicators]
    avg_efficiency = sum(efficiency_values) / len(efficiency_values)
    
    for ind in indicators:
        deviation = ind['efficiency'] - avg_efficiency
        # Complex-looking but ultimately unused metric
        adjusted_quality = ind['net_quality'] + deviation * 10
        stability_score = 10 - abs(deviation) * 5
        
        # This field will be used later
        weight = 1.0
        if ind['latency_penalty'] == 0 and ind['tp_bonus'] > 0:
            weight = 1.25
        
        transformed.append({
            'weighted_net': ind['net_quality'] * weight,
            'adjusted_quality': adjusted_quality,  # unused
            'stability_score': stability_score,   # unused
            'deviation': deviation               # unused
        })
    
    # Dead code path - never executed due to return above
    sorted_transformed = sorted(transformed, key=lambda x: x['weighted_net'], reverse=True)
    top_three = sorted_transformed[:3]
    return transformed  # Not returning the filtered version

# Core evaluation logic

def evaluate_performance(metrics, baseline):
    total_weighted = sum(entry['weighted_net'] for entry in metrics)
    count = len(metrics)
    
    # Baseline adjustment - only applied if above threshold
    if total_weighted / count > baseline:
        adjustment = 1.1
    else:
        adjustment = 0.95
    
    raw_avg = total_weighted / count
    adjusted_avg = raw_avg * adjustment
    
    # Final nonlinear transformation
    final_score = int(math.floor(adjusted_avg * 2.5))  # Key computation
    
    # Distractor: complex bit manipulation that doesn't affect result
    decoy_value = 0
    for i in range(8):
        decoy_value ^= (final_score + i) & (0xFF >> i)
    decoy_value = ((decoy_value << 3) | (decoy_value >> 5)) & 0xFFFF
    
    return final_score

# Orchestration with irrelevant setup
if __name__ == "__main__":
    # Initial data collection
    raw_metrics = get_raw_metrics()
    
    # Useless distribution analysis
    load_dist = analyze_load_distribution(raw_metrics)
    frequency_counter = Counter(load_dist.values())
    
    # Real pipeline
    key_indicators = extract_key_indicators(raw_metrics)
    processed_metrics = transform_indicators(key_indicators)
    
    # Critical execution point
    baseline = 85.0
    final_score = evaluate_performance(processed_metrics, baseline)
    
    # Side computation - looks important but irrelevant
    outlier_count = 0
    efficiencies = [ind['efficiency'] for ind in key_indicators]
    mean_eff = sum(efficiencies) / len(efficiencies)
    for e in efficiencies:
        if abs(e - mean_eff) > 0.05:
            outlier_count += 1
    
    # Print required result
    print(f"Result: {final_score}")