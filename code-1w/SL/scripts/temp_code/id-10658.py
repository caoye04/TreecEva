import itertools

# Simulated system performance metrics (some are relevant, others are distractions)
def collect_diagnostics():
    return {
        'latency_ms': 42,
        'throughput_ops': 847,
        'cache_hit_ratio': 0.88,
        'error_rate': 0.012,
        'retry_count': 3,
        'temp_cpu_c': 67,
        'memory_mb': 2048,
        'disk_iops': 1200,
        'bandwidth_mbps': 95,
        'queue_depth': 7
    }

def preprocess_data(raw):
    # Normalize and filter metrics — some transformations are red herrings
    processed = {}
    for k, v in raw.items():
        if k.endswith('_ms'):
            processed[k] = max(1, v / 10)  # arbitrary scaling
        elif k.endswith('_ratio'):
            processed[k] = v * 100
        elif k.startswith('temp_'):
            processed[k] = (v * 9/5) + 32  # convert to Fahrenheit (unused later)
        else:
            processed[k] = v  # pass through
    return processed

def extract_key_features(data):
    # Extract only the features used in final calculation
    return [
        data.get('latency_ms'),
        data.get('throughput_ops'),
        data.get('error_rate'),
        data.get('cache_hit_ratio')
    ]

def calculate_efficiency_index(features):
    latency, throughput, error_rate, cache_hit = features
    # Real computation path starts here
    base = throughput / (latency * (1 + error_rate * 100))
    bonus = cache_hit * 15
    return base + bonus

def assess_stability_log(metrics):
    # Distractor function — computes something plausible but unused
    errors = metrics.get('error_rate', 0)
    retries = metrics.get('retry_count', 0)
    queue = metrics.get('queue_depth', 0)
    score = (1 - errors) * (1 - min(retries / 10, 0.8)) * (1 - queue / 20)
    return round(score * 100, 2)

def compute_health_vector(diag):
    # Another red herring: builds a vector using irrelevant params
    vec = [
        diag['memory_mb'] / 4096,
        diag['disk_iops'] / 500,
        diag['bandwidth_mbps'] / 100
    ]
    return [round(v, 3) for v in vec]

def generate_synthetic_benchmarks(count=5):
    # Dead code path — never called
    return [x**2 + 2*x + 1 for x in range(count)]

def evaluate_performance(metrics, weights):
    # Core logic buried among noise
    features = extract_key_features(metrics)
    efficiency = calculate_efficiency_index(features)
    
    # Irrelevant branching based on fake thresholds
    if efficiency > 100:
        tier = 'premium'
        multiplier = 1.2
    elif efficiency > 60:
        tier = 'standard'
        multiplier = 1.0
    else:
        tier = 'basic'
        multiplier = 0.7
    
    # Actual weighted aggregation (only two weights are used)
    w_latency = weights['latency']
    w_throughput = weights['throughput']
    # w_error and w_cache are defined but not used here — distraction
    
    # Final score uses efficiency and scales by throughput importance
    raw_score = efficiency * w_throughput
    final_score = raw_score * multiplier
    
    # Decoy mutation
    if 'debug' in metrics:
        final_score += 10  # never triggered
    
    return int(round(final_score))

# Main execution flow
if __name__ == '__main__':
    # Collect raw system telemetry
    raw_metrics = collect_diagnostics()
    
    # Preprocess all fields (many irrelevant)
    cleaned = preprocess_data(raw_metrics)
    
    # Define weighting scheme — only two keys matter
    weights = {
        'latency': 0.3,
        'throughput': 0.7,  # this one is used
        'error': 0.1,        # decoy
        'cache': 0.2         # decoy
    }
    
    # Call distractor functions to pollute trace
    _ = assess_stability_log(raw_metrics)
    _ = compute_health_vector(raw_metrics)
    health_subscore = assess_stability_log({'error_rate': 0.05, 'retry_count': 2, 'queue_depth': 5})
    
    # Key statement: this determines the answer
    final_score = evaluate_performance(cleaned, weights)
    
    # Generate unused synthetic data via list comprehension and itertools
    synthetic = [x * x for x in range(10) if x % 2 == 0]
    paired = list(itertools.combinations(synthetic[:4], 2))
    
    # Print result as required
    print(f"Result: {final_score}")