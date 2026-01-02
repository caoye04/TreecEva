from collections import defaultdict, Counter
import math

# Simulated system performance metrics (some are red herrings)
def collect_metrics():
    data = defaultdict(float)
    data['latency_ms'] = 120.5
    data['throughput_ops'] = 850
    data['error_rate'] = 0.03
    data['cpu_util'] = 78.2
    data['mem_util'] = 65.4
    data['disk_iops'] = 220  # irrelevant metric
    data['network_latency'] = 45.1  # duplicate latency info
    data['retry_count'] = 7
    data['queue_depth'] = 15
    data['cache_hit_ratio'] = 0.88
    data['gc_pause_time'] = 12.3  # distractor
    return data

def normalize(value, min_val, max_val):
    # Simple normalization function
    return (value - min_val) / (max_val - min_val) if max_val > min_val else 0

def calculate_efficiency(latency, throughput, error_rate):
    # Efficiency score based on key triad
    base = throughput * (1 - error_rate)
    penalty = math.log(1 + latency / 100)
    return base / penalty

def adjust_for_resource_usage(cpu, memory, threshold=80):
    # Adjustment factor for resource pressure
    overuse_count = sum(1 for util in [cpu, memory] if util > threshold)
    return 0.95 ** overuse_count

# Decoy function - looks important but unused
def analyze_security_risk(metrics):
    risk = 0
    if metrics['error_rate'] > 0.05:
        risk += 3
    if metrics['retry_count'] > 10:
        risk += 2
    return risk

def compute_stability_index(metrics):
    # Stability influenced by retries and queue depth
    base_stability = 100
    base_stability -= metrics['retry_count'] * 1.5
    base_stability -= metrics['queue_depth'] * 0.8
    if metrics['latency_ms'] > 100:
        base_stability -= 10
    return max(base_stability, 0)

def filter_relevant_metrics(raw_metrics):
    # Extract only relevant metrics for scoring
    keys_of_interest = [
        'latency_ms', 'throughput_ops', 'error_rate',
        'cpu_util', 'mem_util', 'cache_hit_ratio'
    ]
    filtered = {k: raw_metrics[k] for k in keys_of_interest}
    
    # Introduce irrelevant transformation
    temp = [x for x in filtered.values()]
    temp.sort(reverse=True)
    _ = [x * 1.1 for x in temp if x < 50]  # dead code path
    
    return filtered

def apply_weighted_scoring(components, weights):
    # Apply weights to normalized components
    total = 0.0
    for key, val in components.items():
        if key in weights:
            total += val * weights[key]
    return total

def evaluate_performance(metrics, weights):
    # Core evaluation logic
    filtered = filter_relevant_metrics(metrics)
    
    # Compute derived scores
    efficiency = calculate_efficiency(
        filtered['latency_ms'],
        filtered['throughput_ops'],
        filtered['error_rate']
    )
    
    # Normalize individual metrics to [0,1] scale
    norm_latency = 1 - normalize(filtered['latency_ms'], 50, 200)  # inverted
    norm_throughput = normalize(filtered['throughput_ops'], 500, 1000)
    norm_error = 1 - normalize(filtered['error_rate'], 0, 0.05)
    norm_cache = filtered['cache_hit_ratio']
    
    # Resource adjustment factor
    resource_factor = adjust_for_resource_usage(
        filtered['cpu_util'], filtered['mem_util']
    )
    
    # Stability bonus
    stability_bonus = compute_stability_index(metrics) / 100.0
    
    # Assemble weighted components (note: stability not in original weights)
    components = {
        'efficiency': efficiency / 500,  # scale down
        'latency': norm_latency,
        'throughput': norm_throughput,
        'error': norm_error,
        'cache': norm_cache
    }
    
    # Add invisible correction: if cache > 0.85, boost efficiency
    if filtered['cache_hit_ratio'] > 0.85:
        components['efficiency'] *= 1.15
    
    # Final integration
    raw_score = apply_weighted_scoring(components, weights)
    adjusted_score = raw_score * resource_factor * (1 + 0.1 * stability_bonus)
    
    # Red herring: entropy calculation with no effect
    counts = Counter({'a': 3, 'b': 4, 'c': 5})
    entropy = 0
    total = sum(counts.values())
    for count in counts.values():
        p = count / total
        entropy -= p * math.log(p)
    _ = round(entropy, 2)  # unused
    
    return int(round(adjusted_score * 100))

# Main execution
if __name__ == "__main__":
    # Irrelevant setup
    system_log = set()
    system_log.add("boot")
    system_log.add("init")
    system_state = {"status": "active", "mode": "production"}
    
    # Actual work
    raw_metrics = collect_metrics()
    
    # Weight configuration (stability intentionally excluded)
    weights = {
        'efficiency': 0.4,
        'latency': 0.2,
        'throughput': 0.15,
        'error': 0.15,
        'cache': 0.1
    }
    
    # Dead computation branch
    if len(system_log) > 10:
        snapshot = dict(raw_metrics)
        for k in snapshot:
            snapshot[k] *= 0.9
    
    final_score = evaluate_performance(raw_metrics, weights)
    
    # Print result as required
    print(f"Target result: {final_score}")