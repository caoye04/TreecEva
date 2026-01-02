from collections import defaultdict
import itertools

# Simulate system performance metrics from various subsystems
def collect_diagnostics():
    return {
        'latency': 120,
        'throughput': 850,
        'error_rate': 0.004,
        'memory_usage': 720,
        'cpu_load': 68
    }

def apply_calibration(data):
    # Irrelevant transformation - does not affect final result
    calibrated = {}
    for k, v in data.items():
        calibrated[k] = v * 1.02 if k != 'error_rate' else v * 0.98
    return calibrated

def generate_synthetic_samples(base_data, n=5):
    # Dead code path — never used
    samples = []
    for _ in range(n):
        sample = {k: v + (hash(k) % 10) for k, v in base_data.items()}
        samples.append(sample)
    return samples

def compute_rolling_average(stream, window=3):
    # Unused function — red herring
    averages = []
    for i in range(len(stream)):
        if i < window - 1:
            averages.append(None)
        else:
            avg = sum(stream[i - window + 1:i + 1]) / window
            averages.append(avg)
    return averages

def normalize_metrics(metrics):
    # Normalize metrics to a 0-100 scale based on assumed thresholds
    norm = {}
    norm['latency'] = max(0, 100 - (metrics['latency'] / 2))
    norm['throughput'] = min(100, metrics['throughput'] / 10)
    norm['error_rate'] = max(0, 100 - (metrics['error_rate'] * 10000))
    norm['memory_usage'] = max(0, 90 - (metrics['memory_usage'] / 10))
    norm['cpu_load'] = 100 - metrics['cpu_load']
    return norm

def filter_outliers(data_list, threshold=2.0):
    # Not used — misleading function suggesting data cleaning
    mean_val = sum(data_list) / len(data_list)
    std_dev = (sum((x - mean_val) ** 2 for x in data_list) / len(data_list)) ** 0.5
    return [x for x in data_list if abs(x - mean_val) <= threshold * std_dev]

def calculate_entropy(values):
    # Decoy computation — looks important but unused
    total = sum(values)
    if total == 0:
        return 0
    probs = [v / total for v in values if v > 0]
    from math import log
    return -sum(p * log(p) for p in probs)

def build_dependency_graph(nodes):
    # Irrelevant data structure manipulation
    graph = defaultdict(list)
    for pair in itertools.permutations(nodes, 2):
        if hash(pair) % 7 != 0:
            graph[pair[0]].append(pair[1])
    return dict(graph)

def evaluate_performance(raw_metrics, weights):
    # Core logic — actual path to answer
    normalized = normalize_metrics(raw_metrics)
    
    # Weighted sum calculation — determines final score
    weighted_sum = 0.0
    for metric, weight in weights.items():
        if metric in normalized:
            weighted_sum += normalized[metric] * weight
    
    # Additional adjustment based on hidden rule: if latency score >= 60, add bonus
    if normalized['latency'] >= 60:
        bonus = 8.5
        weighted_sum += bonus  # Critical bonus affecting final result
    
    return int(weighted_sum)  # Final output is integer

# Main execution flow
if __name__ == '__main__':
    raw_system_data = collect_diagnostics()
    
    # Apply irrelevant calibration (result not used later)
    _ = apply_calibration(raw_system_data)
    
    # Generate synthetic data — never used
    synthetic_runs = generate_synthetic_samples(raw_system_data, 7)
    
    # Define weighting schema for evaluation
    benchmark_weights = {
        'latency': 0.3,
        'throughput': 0.25,
        'error_rate': 0.2,
        'memory_usage': 0.15,
        'cpu_load': 0.1
    }
    
    # Build fake dependency graph — distractor
    deps = build_dependency_graph(list(benchmark_weights.keys()))
    
    # Extract throughput history — unused time series
    throughput_history = [800, 820, 830, 840, 850]
    _ = compute_rolling_average(throughput_history)
    
    # Calculate entropy of weights — decoy analysis
    _ = calculate_entropy(list(benchmark_weights.values()))
    
    # Key execution point: evaluate performance
    final_score = evaluate_performance(raw_system_data, benchmark_weights)
    
    print(f"Result: {final_score}")