from collections import defaultdict

# Simulate system performance metrics over time
def collect_metrics():
    raw_data = [
        (1, 'latency', 120), (1, 'errors', 3), (1, 'requests', 98),
        (2, 'latency', 140), (2, 'errors', 1), (2, 'requests', 105),
        (3, 'latency', 110), (3, 'errors', 4), (3, 'requests', 92),
        (4, 'latency', 130), (4, 'errors', 2), (4, 'requests', 99)
    ]
    
    metrics = defaultdict(list)
    for timestamp, key, value in raw_data:
        metrics[key].append(value)
    
    # Misleading aggregation: average per metric (not used in final score)
    avg_latency = sum(metrics['latency']) / len(metrics['latency'])
    avg_errors = sum(metrics['errors']) / len(metrics['errors'])
    total_requests = sum(metrics['requests'])
    
    # Actual relevant metrics
    min_latency = min(metrics['latency'])
    max_error_burst = max(metrics['errors'])
    stability_ratio = len([e for e in metrics['errors'] if e <= 2]) / len(metrics['errors'])
    
    return {
        'min_latency': min_latency,
        'max_error_burst': max_error_burst,
        'stability_ratio': stability_ratio,
        'total_requests': total_requests,  # red herring
        'avg_latency': avg_latency   # red herring
    }

def apply_calibration(data):
    # Simulate sensor calibration (only modifies unused fields)
    data['avg_latency'] = round(data['avg_latency'] * 0.92, 2)
    data['calibrated'] = True
    return data

def compute_efficiency_index(req_count):
    # Irrelevant efficiency calculation (dead-end function)
    if req_count < 100:
        return 0.8
    elif req_count < 200:
        return 0.9
    else:
        return 1.0

def evaluate_performance(metrics, weights):
    # Core logic uses only three of the five metrics
    score = 0
    score += metrics['min_latency'] * weights[0]           # lower latency → higher penalty
    score += metrics['max_error_burst'] * weights[1]         # more errors → higher penalty
    score -= metrics['stability_ratio'] * weights[2] * 10    # higher stability → lower score (bonus subtracted)
    
    # Dead code branch (never executed due to current data)
    if metrics['total_requests'] > 500:
        extra_penalty = metrics['total_requests'] // 100
        score += extra_penalty
    
    return int(score)

# Main execution flow
def main():
    weights = [0.5, 8, 5]  # weight factors for scoring components
    
    metrics = collect_metrics()
    calibrated_metrics = apply_calibration(metrics)
    
    # Spurious intermediate calculations
    efficiency = compute_efficiency_index(calibrated_metrics['total_requests'])
    adjusted_weights = [w * efficiency for w in weights]  # looks important but unused
    
    # Key computation
    final_score = evaluate_performance(calibrated_metrics, weights)
    
    # Additional noise
    outlier_count = len([x for x in metrics['latency'] if x > 135])
    normalized_score = (final_score - 50) / 10
    classification = 'STABLE' if normalized_score < 7 else 'UNSTABLE'
    
    print(f"Result: {final_score}")

if __name__ == '__main__':
    main()