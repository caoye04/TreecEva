import itertools

# Simulated system performance metrics (some are relevant, others are distractions)
def collect_diagnostics():
    return {
        'cpu_load': 78,
        'memory_usage': 4321,
        'disk_iops': 120,
        'network_latency_ms': 45,
        'cache_hit_rate': 0.88,
        'thread_count': 16,
        'error_rate': 0.002,
        'temperature_c': 67
    }

def preprocess_data(raw):
    # Normalize and filter metrics – some transformations are red herrings
    processed = {}
    for k, v in raw.items():
        if k == 'cpu_load':
            processed[k] = min(v, 100) / 100
        elif k == 'memory_usage':
            processed[k] = v / 8192  # Assume 8GB total
        elif k == 'disk_iops':
            processed[k] = v / 200
        elif k == 'network_latency_ms':
            processed[k] = max(0, 1 - (v / 100))
        elif k == 'cache_hit_rate':
            processed[k] = v
        elif k == 'thread_count':
            processed[k] = min(v, 32) / 32
        elif k == 'error_rate':
            processed[k] = 1 - min(v * 10, 1)  # Inverted: lower error = higher score
        elif k == 'temperature_c':
            # Distractor: temperature is not used in final calculation
            processed[k] = max(0, 1 - (v - 50) / 50) if v > 50 else 1
    return processed

# Irrelevant diagnostic function (dead code path)
def analyze_hardware_health(data):
    alerts = []
    if data['temperature_c'] > 0.8:
        alerts.append('OVERHEAT_RISK')
    if data['memory_usage'] > 0.9:
        alerts.append('HIGH_MEMORY')
    return alerts  # Never used

# Another decoy function with misleading intermediate outputs
def compute_stability_index(diag):
    factors = [
        diag.get('cpu_load', 0),
        diag.get('memory_usage', 0) * 1000,
        diag.get('error_rate', 0) * 100000
    ]
    return sum(factors) / 3  # Looks important but unused

# Core evaluation logic
def evaluate_component(base, multiplier, threshold=0.7):
    # Only contributes if above threshold
    if base >= threshold:
        return base * multiplier
    else:
        return base * 0.5 * multiplier  # Penalty for underperformance

def evaluate_performance(metrics, weights):
    # Only a subset of metrics are actually used
    relevant_metrics = [
        'cpu_load',
        'memory_usage',
        'disk_iops',
        'cache_hit_rate',
        'error_rate'
    ]
    
    # Weights are pre-defined; thread_count and temperature are not included
    score = 0.0
    for metric in relevant_metrics:
        if metric in metrics:
            weight = weights.get(metric, 1.0)
            score += evaluate_component(metrics[metric], weight)
    
    # Additional distraction: unused combination logic
    pairs = list(itertools.combinations([metrics[m] for m in ['cpu_load', 'disk_iops', 'cache_hit_rate']], 2))
    synergy = 0
    for a, b in pairs:
        synergy += a * b * 0.05  # Computed but not added to score
    
    # Final score is only the weighted sum
    return int(round(score * 100))  # Discretized for reporting

# Misleading preliminary analysis (distractor)
def generate_report_snapshot():
    raw = collect_diagnostics()
    proc = preprocess_data(raw)
    stability = compute_stability_index(raw)
    health_warnings = analyze_hardware_health(proc)
    # All look useful, but only proc matters
    return {'processed': proc, 'stability': stability, 'warnings': health_warnings}

# Main execution flow
if __name__ == '__main__':
    raw_metrics = collect_diagnostics()
    cleaned = preprocess_data(raw_metrics)
    
    # Weight mapping – only specific keys are used
    weights = {
        'cpu_load': 0.3,
        'memory_usage': 0.2,
        'disk_iops': 0.2,
        'cache_hit_rate': 0.25,
        'error_rate': 0.3  # High weight due to reliability impact
    }
    
    # Critical statement
    final_score = evaluate_performance(cleaned, weights)
    
    # Print result as required
    print(f"Result: {final_score}")