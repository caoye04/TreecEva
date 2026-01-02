from collections import defaultdict, Counter
import math

# Simulated system performance metrics (some are red herrings)
def generate_metrics():
    raw_data = [78, 85, 92, 64, 73, 88, 91]
    stats = {}
    stats['mean_response'] = sum(raw_data) / len(raw_data)
    stats['peak_throughput'] = max(raw_data) * 1.5
    stats['error_rate'] = 0.037
    stats['latency_spike_count'] = 5
    stats['memory_efficiency'] = 89.4
    stats['cache_hit_ratio'] = 0.88
    stats['concurrent_users'] = 1200
    stats['idle_cycles'] = 427
    return stats

def analyze_stability(log_entries):
    # Irrelevant function - never called in execution path
    critical_events = 0
    for entry in log_entries:
        if 'ERROR' in entry:
            critical_events += 1
    return critical_events

def calculate_baseline(ref_data):
    # Dead code path - not used in main logic
    base = 0
    for x in ref_data:
        base += x ** 0.5
    return base / len(ref_data)

def filter_outliers(values, threshold=1.5):
    # Unused helper - distraction
    q1 = sorted(values)[len(values)//4]
    q3 = sorted(values)[3*len(values)//4]
    iqr = q3 - q1
    lower, upper = q1 - threshold * iqr, q3 + threshold * iqr
    return [v for v in values if lower <= v <= upper]

def compute_ranking(elements):
    # Misleading intermediate calculation
    ranked = sorted(elements, reverse=True)
    position_map = {val: idx+1 for idx, val in enumerate(ranked)}
    return position_map

# Core logic with distractors
def evaluate_component(reading, weight, adjustment_factor=1.0):
    normalized = (reading / 100.0) * weight
    adjusted = normalized * (1.0 + adjustment_factor * 0.1)
    return adjusted

def evaluate_performance(metrics, weights):
    # Key computation embedded in noise
    score_components = defaultdict(float)
    
    # Relevant calculations
    score_components['response_time'] = evaluate_component(metrics['mean_response'], weights['timing'], 0.2)
    score_components['throughput'] = evaluate_component(metrics['peak_throughput'], weights['throughput'], -0.1)
    score_components['reliability'] = evaluate_component((1 - metrics['error_rate']) * 100, weights['reliability'], 0.5)
    score_components['efficiency'] = evaluate_component(metrics['memory_efficiency'], weights['efficiency'], 0.0)
    
    # Distractor assignments (look important but unused)
    score_components['latency_penalty'] = metrics['latency_spike_count'] * 2.5
    score_components['user_load_factor'] = math.log(metrics['concurrent_users']) * 0.3
    score_components['idle_waste'] = metrics['idle_cycles'] / 100
    
    # Composite score using only select components
    essential_parts = ['response_time', 'throughput', 'reliability', 'efficiency']
    partial_sum = sum(score_components[comp] for comp in essential_parts)
    
    # Final transformation
    final_score = int(partial_sum * 10 + 0.5)  # Round to nearest integer
    
    # Dead branch - unreachable due to prior assignment
    if final_score < 0:
        final_score = 0
    
    return final_score

# Unused data structures - red herrings
test_logs = [
    "INFO: System boot",
    "WARN: High latency detected",
    "ERROR: Connection timeout",
    "DEBUG: Retrying request"
]

reference_benchmarks = [88, 76, 91, 83, 79]

# Main execution flow
metrics = generate_metrics()

# Weight configuration (only this matters)
benchmark_weights = {
    'timing': 0.25,
    'throughput': 0.30,
    'reliability': 0.20,
    'efficiency': 0.25
}

# Additional irrelevant processing
frequency_map = Counter([int(x) for x in metrics.values() if isinstance(x, float)])
dynamic_adjusters = [math.sin(math.pi * i / 4) for i in range(8)]

# Critical statement
final_score = evaluate_performance(metrics, benchmark_weights)

# Output result
print(f"Result: {final_score}")