import math

# Simulated system performance metrics
def generate_metrics():
    raw_data = [0.85, 0.92, 0.78, 0.96, 0.88, 0.91, 0.83, 0.87]
    weights = [0.1, 0.2, 0.1, 0.15, 0.1, 0.1, 0.05, 0.2]
    weighted_scores = [raw_data[i] * weights[i] for i in range(len(raw_data))]
    base_metric = sum(weighted_scores)
    return {
        'accuracy': base_metric,
        'throughput': 1245,
        'latency': 45.2,
        'memory_usage': 890,
        'cpu_load': 0.67,
        'reliability': 0.94
    }

# Irrelevant helper function - decoy
def calculate_efficiency_ratio(x, y):
    if x == 0:
        return 0
    ratio = (y / x) * 100
    adjusted = ratio * 0.85 if ratio > 50 else ratio * 1.1
    return round(adjusted, 2)

# Unused transformation - dead code path
def transform_dataset(data_list):
    processed = []
    for item in data_list:
        if isinstance(item, float):
            processed.append(math.log(item + 1) * 100)
        elif item > 100:
            processed.append(item // 3)
    return processed

# Benchmark thresholds (partially relevant)
bm_thresholds = {
    'high': {'accuracy': 0.88, 'throughput': 1000},
    'medium': {'accuracy': 0.80, 'throughput': 700},
    'low': {'accuracy': 0.70, 'throughput': 400}
}

# Simulated external benchmark data
benchmark_data = [
    {'name': 'A', 'score': 87.5, 'valid': True},
    {'name': 'B', 'score': 92.1, 'valid': False},
    {'name': 'C', 'score': 89.7, 'valid': True},
    {'name': 'D', 'score': 95.3, 'valid': True}
]

# Auxiliary state tracking (mostly irrelevant)
current_state = {
    'mode': 'analysis',
    'version': '2.1.5',
    'debug_active': False,
    'cache_hits': 4231,
    'last_updated': '2023-11-05'
}

# Core evaluation logic
def analyze_accuracy_component(acc, thr):
    if acc >= thr['high']['accuracy']:
        return 90 + ((acc - thr['high']['accuracy']) / 0.05) * 10
    elif acc >= thr['medium']['accuracy']:
        return 70 + ((acc - thr['medium']['accuracy']) / 0.08) * 20
    else:
        return max(50, (acc / thr['medium']['accuracy']) * 50)

def adjust_for_latency(lat):
    if lat < 30:
        return 1.1
    elif lat < 60:
        return 1.0
    elif lat < 100:
        return 0.9
    else:
        return 0.75

# Main scoring function
def evaluate_performance(metrics, bench_data):
    # Extract relevant metric
    acc = metrics['accuracy']
    
    # Compute accuracy score
    base_score = analyze_accuracy_component(acc, bm_thresholds)
    
    # Adjust with latency factor
    latency_factor = adjust_for_latency(metrics['latency'])
    adjusted_score = base_score * latency_factor
    
    # Add bonus from valid benchmarks
    valid_benchmarks = [b for b in bench_data if b['valid']]
    benchmark_bonus = sum(b['score'] for b in valid_benchmarks[:2]) / 10  # Only top 2
    
    # Apply bonus cap based on memory usage (red herring condition)
    memory_flag = metrics['memory_usage'] > 850
    cpu_flag = metrics['cpu_load'] > 0.6
    if memory_flag and cpu_flag:
        benchmark_bonus = min(benchmark_bonus, 17.5)  # Cap applied
    
    # Final computation
    final_raw = adjusted_score + benchmark_bonus
    
    # Normalize to scale (this is the actual answer)
    final_score = int(round(final_raw * 1.05))
    
    # Decoy operations below (irrelevant)
    temp_result = math.sin(math.pi / 4) * final_score
    normalized_vector = [temp_result / math.sqrt(2), temp_result / math.sqrt(2)]
    checksum = sum(int(str(int(temp_result))[:3]))
    
    # Distractor: unused nested structure
    diagnostics = {
        'stages': [
            {'name': 'init', 'status': 1},
            {'name': 'process', 'status': 1},
            {'name': 'finalize', 'status': 0}  # Failed stage (unused)
        ],
        'errors': []
    }
    
    # Critical execution point
    return final_score

# Execution flow
metrics = generate_metrics()

# Misleading intermediate call (no effect)
_ = calculate_efficiency_ratio(metrics['throughput'], metrics['latency'])

# Key statement
final_score = evaluate_performance(metrics, benchmark_data)

# Print result
print(f"Result: {final_score}")