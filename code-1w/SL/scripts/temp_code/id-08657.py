def analyze_system_metrics():
    # Simulate sensor readings and performance metrics
    cpu_load_samples = [0.78, 0.82, 0.75, 0.91, 0.83]
    memory_usage_samples = [0.65, 0.71, 0.69, 0.76, 0.72]
    network_latency_ms = [45, 38, 52, 41, 39]

    # Derived aggregate values (some used, some not)
    avg_cpu = sum(cpu_load_samples) / len(cpu_load_samples)
    avg_memory = sum(memory_usage_samples) / len(memory_usage_samples)
    avg_latency = sum(network_latency_ms) / len(network_latency_ms)
    peak_cpu = max(cpu_load_samples)
    min_latency = min(network_latency_ms)

    # Threshold checks (used in logic)
    high_load = avg_cpu > 0.75
    stable_memory = avg_memory < 0.73
    responsive_network = min_latency < 40

    # Intermediate scoring with irrelevant transformations
    raw_score = 0
    if high_load:
        raw_score += 20
    if stable_memory:
        raw_score += 15
    if responsive_network:
        raw_score += 25

    # Unused distraction variables
    projected_load = avg_cpu * 1.08  # predicted next interval (not used)
    compression_ratio = 0.88  # assumed data comp (irrelevant)
    theoretical_max_throughput = 987.65  # red herring metric

    # Define evaluation criteria using sets
    critical_metrics = {'cpu', 'memory'}
    optional_metrics = {'network', 'disk', 'gpu'}
    available_metrics = {'cpu', 'memory', 'network'}

    # Set operations to determine coverage
    required_present = critical_metrics.intersection(available_metrics)
    optional_present = optional_metrics.intersection(available_metrics)
    coverage_bonus = 10 if len(required_present) == 2 else 0

    # Benchmark weights for final calculation
    benchmark_weights = {
        'base': raw_score,
        'coverage': coverage_bonus,
        'stability': 5 if stable_memory and not peak_cpu > 0.9 else 0
    }

    # Metric set construction (key input to final function)
    metric_set = set()
    if high_load:
        metric_set.add('high_load_observed')
    if stable_memory:
        metric_set.add('stable_memory')
    if responsive_network:
        metric_set.add('low_latency')
    if len(optional_present) >= 1:
        metric_set.add('partial_optional')

    # Dead code path - never executed due to fixed conditions above
    if 'disk' in metric_set:
        benchmark_weights['disk'] = 5  # unreachable

    # Core evaluation logic
    def evaluate_performance(metrics, weights):
        score = weights['base'] + weights['coverage'] + weights['stability']
        if 'low_latency' in metrics and 'stable_memory' in metrics:
            score += 12
        if 'high_load_observed' in metrics:
            score -= 8  # penalty for high load
        if len(metrics) >= 3:
            score += 5  # complexity bonus
        return int(score)

    # Final computation
    final_score = evaluate_performance(metric_set, benchmark_weights)

    # Irrelevant post-processing
    normalized_score = round(final_score / 100.0, 3)
    efficiency_class = 'A' if normalized_score > 0.7 else 'B'

    print(f"Result: {final_score}")

analyze_system_metrics()