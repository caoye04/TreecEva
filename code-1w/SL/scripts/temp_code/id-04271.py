import math

# Simulated system diagnostics (irrelevant variables)
default_threshold = 0.85
redundant_flags = [False, True, False]
log_entries = {'errors': 0, 'warnings': 3}

# Core data structures
def initialize_metrics():
    return {
        'latency': 120,
        'throughput': 850,
        'consistency': 0.92,
        'availability': 0.99
    }

def generate_baseline():
    base = set()
    for i in range(10, 100, 7):
        if i % 3 == 0:
            base.add(i * 2)
    base.discard(60)  # red herring operation
    return base

def process_cache(data):
    temp = []
    for x in data:
        if x > 100:
            temp.append(x // 3)
        else:
            temp.append(x + 10)
    return sorted(temp, reverse=True)[1:6]  # partial slice - misleading

def analyze_redundancy(seq):
    counts = {}
    for item in seq:
        counts[item] = counts.get(item, 0) + 1
    return sum(1 for c in counts.values() if c > 1)

# Decoy function - looks important but unused
def deprecated_calibrate(x):
    return (x ** 0.5) * 1.8

# Conditional scaling with integer division
def scale_factor(val, ref):
    if val < ref:
        return val // 10 + 1
    else:
        return int(val / 15) + 2

# Complex evaluation with set operations and logic chaining
def evaluate_performance(metrics, base):
    # Extract values
    lat = metrics['latency']
    thr = metrics['throughput']
    cons = metrics['consistency']
    avail = metrics['availability']
    
    # Compute derived scores (some distractors)
    speed_score = 100 - (lat / 2)
    efficiency = thr // 100  # integer division
    reliability = int(avail * 100)
    
    # Set-based anomaly detection (core relevant path)
    anomaly_pool = {i for i in range(50, 200, 13)}
    critical_anomalies = anomaly_pool.intersection(base)
    anomaly_count = len(critical_anomalies)  # used later
    
    # Dummy transformation chain
    transformed = []
    for a in sorted(critical_anomalies):
        if a % 2 == 0:
            transformed.append(a // 4)
        else:
            transformed.append(a // 5)
    shuffle_score = sum(transformed) / (anomaly_count + 1) if anomaly_count else 0
    
    # Boolean logic chain with short-circuiting
    meets_latency = lat < 130
    high_throughput = thr >= 800
    strong_consistency = cons > 0.90
    
    # Key composite condition
    if meets_latency and high_throughput and strong_consistency:
        performance_bonus = 25
    elif meets_latency or high_throughput:
        performance_bonus = 10
    else:
        performance_bonus = 0
    
    # Irrelevant statistical moment calculation
    mean_base = sum(base) / len(base) if base else 0
    variance_proxy = sum((x - mean_base) ** 2 for x in base[:5]) / 5 if len(base) >= 5 else 0
    
    # Final score computation - depends on multiple paths
    raw_score = speed_score + efficiency + reliability + performance_bonus
    
    # Apply anomaly penalty only if anomalies exist
    anomaly_penalty = 0
    if anomaly_count > 0:
        anomaly_penalty = int(shuffle_score) * 2
    
    # The actual answer depends on this line
    final_score = raw_score - anomaly_penalty
    
    # Dead code branch - never reached due to logic structure
    if final_score < 0:
        final_score = 0
    
    return final_score

# Orchestration block
if __name__ == '__main__':
    metric_set = initialize_metrics()
    baseline_data = generate_baseline()
    cache_diagnostic = process_cache(baseline_data)  # distractor call
    redundancy_check = analyze_redundancy(cache_diagnostic)  # irrelevant
    
    # Key execution point
    final_score = evaluate_performance(metric_set, baseline_data)
    
    print(f"Target result: {final_score}")