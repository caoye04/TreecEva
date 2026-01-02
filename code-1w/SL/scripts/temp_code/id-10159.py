from collections import defaultdict, Counter
import math

# Simulated system metrics with irrelevant and relevant data
def get_system_metrics():
    raw_data = [150, 200, 300, 400, 500]
    metadata_log = ['start', 'init', 'run', 'error', 'retry', 'success']
    
    # Distractor: complex but unused transformation
    transformed = [math.log(x + 10) * 1.5 for x in raw_data if x > 250]
    stats_map = defaultdict(float)
    
    for i, val in enumerate(raw_data):
        stats_map[f'metric_{i}'] = val * (0.1 if i % 2 == 0 else 0.2)
    
    # Relevant metrics embedded in noise
    metrics = {
        'latency': 120,
        'throughput': 85,
        'consistency': 92,
        'availability': 99,
        'redundant_metric_x': sum(transformed),  # red herring
        'debug_flag': len(metadata_log) > 5
    }
    
    return metrics

def analyze_stability(data):
    # Irrelevant analysis path
    if data.get('debug_flag'):
        counts = Counter([len(k) for k in data.keys()])
        avg_key_len = sum(counts.elements()) / len(counts)
        return avg_key_len > 5
    return False

def calculate_adjustment(base, factor=1.05):
    # Decoy function - looks important but unused
    temp = base * factor
    for _ in range(2):
        temp = math.sqrt(temp) if temp > 100 else temp ** 2
    return int(temp)

def validate_inputs(metrics):
    required = ['latency', 'throughput', 'consistency', 'availability']
    return all(m in metrics for m in required)

def compute_efficiency(lat, thr, cons):
    # Real computation part
    score = (thr * 0.4) + (cons * 0.3)
    penalty = lat * 0.05
    return score - penalty

def evaluate_reliability(avail, cons):
    if avail >= 95:
        return cons * 0.2
    else:
        return -10

def final_aggregation(eff, rel, offset=5.0):
    # Core logic step
    aggregate = eff + rel + offset
    # Distractor: dead code branch
    if aggregate < 0:
        aggregate = abs(aggregate) * 0.5
    return round(aggregate, 4)

def apply_weights(components, wts):
    # Another layer of distraction with list comprehension
    weighted = [v * wts.get(k, 0) for k, v in components.items() if k in ['efficiency', 'reliability']]
    return sum(weighted)

def main():
    # Initialize weights (some are decoys)
    weights = {
        'efficiency': 0.6,
        'reliability': 0.4,
        'latency_penalty': 0.0,  # unused weight
        'ghost_factor': 0.1     # misleading
    }
    
    # Get metrics
    metrics = get_system_metrics()
    
    # Validate
    if not validate_inputs(metrics):
        return -1
    
    # Compute core components
    efficiency = compute_efficiency(metrics['latency'], metrics['throughput'], metrics['consistency'])
    reliability = evaluate_reliability(metrics['availability'], metrics['consistency'])
    
    # Intermediate values that look important but aren't final
    temp_results = {
        'efficiency': efficiency,
        'reliability': reliability,
        'raw_sum': efficiency + reliability
    }
    
    # Apply weighting (distractor usage)
    preliminary = apply_weights(temp_results, weights)
    
    # Final aggregation using direct calculation, bypassing weights
    final_score = final_aggregation(efficiency, reliability)
    
    # Dead code path - looks like it might affect result
    if analyze_stability(metrics):
        adjustment = calculate_adjustment(final_score)
        final_score = (final_score + adjustment) / 2
    
    print(f"Result: {final_score}")
    return final_score

if __name__ == '__main__':
    main()