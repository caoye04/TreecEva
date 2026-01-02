import itertools

# Simulated system performance metrics (some are decoys)
def get_raw_metrics():
    base_load = 127
    peak_memory = 984
    io_operations = 43 * 19
    temp_factor = sum(i ** 2 for i in range(6))  # irrelevant
    checksum = (base_load + 17) % 100
    
    # Real metric embedded among noise
    return {
        'latency': 42,
        'throughput': 86,
        'resilience': 73,
        'bandwidth': 55,
        'redundancy': 200  # distractor
    }

# Weight configuration with misleading entries
def load_weights():
    defaults = [0.1, 0.2, 0.3, 0.4]
    labels = ['latency', 'throughput', 'resilience', 'bandwidth']
    extra_noise = {k: v for k, v in zip(labels, defaults)}  # red herring
    
    # Actual weights used
    return {
        'latency': 0.4,
        'throughput': 0.3,
        'resilience': 0.2,
        'bandwidth': 0.1
    }

# Auxiliary function – appears important but unused in final calculation
def calculate_baseline(data):
    avg = sum(data.values()) / len(data)
    variance = sum((v - avg) ** 2 for v in data.values()) / len(data)
    return round(avg + variance * 0.1, 2)

# Decoy transformation using set operations and itertools
def transform_metrics(metrics):
    keys = set(metrics.keys())
    required = {'latency', 'throughput', 'resilience'}
    optional = {'bandwidth', 'redundancy', 'jitter'}
    
    present_optional = keys & optional
    combinations = list(itertools.combinations(present_optional, min(2, len(present_optional))))
    
    # Fake normalization chain
    adjusted = {k: v * 1.01 for k, v in metrics.items() if k in required | {'bandwidth'}}
    return adjusted  # never actually used

# Core evaluation logic buried in distractions
def evaluate_performance(metrics, weights):
    # Filter only relevant keys (distractors filtered here)
    relevant_keys = set(weights.keys())  # {'latency', 'throughput', 'resilience', 'bandwidth'}
    filtered_metrics = {k: metrics[k] for k in relevant_keys}
    
    # Apply weighted sum
    total = 0.0
    for key in filtered_metrics:
        total += filtered_metrics[key] * weights[key]
    
    # Additional adjustment: if resilience > 70, add throughput bonus
    if filtered_metrics['resilience'] > 70:
        bonus = filtered_metrics['throughput'] * 0.05
        total += bonus
    
    # Hidden condition based on digit sum of latency
    latency_digit_sum = sum(int(d) for d in str(filtered_metrics['latency']))
    if latency_digit_sum == 6:  # 4+2=6
        total -= 2  # penalty
    
    return total

# Unused recursive helper – dead code path
def recursive_doubler(n):
    if n <= 1:
        return 1
    return n + recursive_doubler(n - 2)

# Main execution flow
if __name__ == '__main__':
    # Step 1: Retrieve raw data
    raw_data = get_raw_metrics()
    
    # Step 2: Load weighting schema
    config_weights = load_weights()
    
    # Step 3: Transform (but result discarded)
    _ = transform_metrics(raw_data)
    
    # Step 4: Evaluate real performance score
    baseline = calculate_baseline(raw_data)  # computed but unused
    final_score = evaluate_performance(raw_data, config_weights)
    
    # Print target result
    print(f"Result: {final_score}")