from collections import defaultdict, Counter
import math

# Simulated system metrics from a distributed service
def collect_metrics():
    raw_data = [
        ('request_count', [120, 150, 130, 140, 160]),
        ('latency_ms', [23.5, 27.1, 25.3, 29.8, 24.0]),
        ('error_rate', [0.02, 0.01, 0.03, 0.00, 0.02]),
        ('cpu_util', [0.68, 0.75, 0.71, 0.78, 0.70])
    ]
    
    metrics = defaultdict(list)
    for key, values in raw_data:
        metrics[key].extend(values)
    
    # Irrelevant transformation (distractor)
    temp_snapshot = [math.log(v + 1) for v in metrics['request_count']]
    normalized = [round((x - min(metrics['latency_ms'])) / (max(metrics['latency_ms']) - min(metrics['latency_ms'])), 4) for x in metrics['latency_ms']]
    
    # Decoy aggregation (never used)
    avg_latency = sum(metrics['latency_ms']) / len(metrics['latency_ms'])
    peak_load = max(metrics['request_count'])
    
    return metrics

# Weight configuration for evaluation (some weights are red herrings)
def get_weights():
    weights = {
        'throughput': 0.4,
        'responsiveness': 0.35,
        'stability': 0.2,
        'reliability': 0.05,
        'bandwidth_efficiency': 0.1  # Unused decoy weight
    }
    return weights

# Core evaluation logic with nested dependencies
def evaluate_performance(metrics, weights):
    scores = {}
    
    # Sub-scores calculation
    request_count_series = metrics['request_count']
    latency_series = metrics['latency_ms']
    error_series = metrics['error_rate']
    
    # Throughput score based on average request count
    avg_throughput = sum(request_count_series) / len(request_count_series)
    throughput_score = min(avg_throughput / 100.0, 1.0) * 100
    
    # Responsiveness score: inverse relationship with latency
    avg_latency = sum(latency_series) / len(latency_series)
    responsiveness_score = max(100 - (avg_latency * 2), 0)
    
    # Stability score: based on variance in CPU and latency
    def variance(data):
        mean = sum(data) / len(data)
        return sum((x - mean) ** 2 for x in data) / len(data)
    
    cpu_variance = variance(metrics['cpu_util'])
    latency_variance = variance(latency_series)
    stability_score = 100 - (latency_variance * 2 + cpu_variance * 10) * 5
    
    # Reliability score: based on error rate trends
    recent_errors = error_series[-3:]  # Focus on last 3 samples
    avg_recent_error = sum(recent_errors) / len(recent_errors)
    reliability_score = (1 - avg_recent_error) * 100
    
    # Distractor: unused reliability enhancement logic
    if reliability_score > 95:
        bonus_factor = 1.1
    else:
        bonus_factor = 1.0
    enhanced_reliability = reliability_score * bonus_factor  # Never used
    
    # Aggregate using only relevant weights
    final_score = (
        throughput_score * weights['throughput'] +
        responsiveness_score * weights['responsiveness'] +
        stability_score * weights['stability'] +
        reliability_score * weights['reliability']
    )
    
    # Additional distractor logic
    outlier_count = 0
    for i, lat in enumerate(latency_series):
        if lat > 28.0:
            outlier_count += 1
    adjustment_factor = 1.0 - (outlier_count * 0.02)
    adjusted_score = final_score * adjustment_factor  # Computed but not used
    
    # Red herring: slicing and zipping irrelevant data
    time_windows = ['t0', 't1', 't2', 't3', 't4']
    tagged_data = list(zip(time_windows, request_count_series))
    recent_window = tagged_data[-2:]  # Not used in final computation
    
    # Final clipping to valid range
    final_score = max(0, min(final_score, 100))  # Ensure within bounds
    
    return final_score

# Auxiliary function that looks important but is unused
def calculate_system_health_diagnostic(metrics):
    health_map = Counter()
    for k, v_list in metrics.items():
        for v in v_list:
            if isinstance(v, float) and v > 0.5:
                health_map[k] += 1
    return dict(health_map)

# Execution flow
if __name__ == '__main__':
    # Collect performance metrics
    collected_metrics = collect_metrics()
    
    # Retrieve weighting scheme
    performance_weights = get_weights()
    
    # Evaluate overall performance
    final_score = evaluate_performance(collected_metrics, performance_weights)
    
    # Print result as required
    print(f"Result: {final_score}")
