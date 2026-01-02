from collections import defaultdict, Counter
import math

def analyze_component_health(temps, thresholds):
    # Irrelevant function: analyzes hardware temps but not used in final result
    health = defaultdict(int)
    for sensor, temp in temps.items():
        if temp > thresholds[sensor]:
            health[sensor] = 1
    return health

def compute_redundant_stats(values):
    # Distractor function: computes unused statistical metrics
    mean_val = sum(values) / len(values)
    variance = sum((x - mean_val) ** 2 for x in values) / len(values)
    return {'mean': mean_val, 'variance': variance, 'peak': max(values)}

def preprocess_signal(raw_signal):
    # Dead code path: signal processing not connected to main logic
    filtered = [x for x in raw_signal if abs(x) > 0.1]
    windowed = [sum(filtered[i:i+3]) / min(3, len(filtered)-i) for i in range(0, len(filtered), 3)]
    normalized = [x / max(windowed) for x in windowed]
    return normalized

def evaluate_performance(metrics, benchmark_data):
    # Core logic begins
    base_weights = {'latency': 0.4, 'throughput': 0.35, 'jitter': 0.25}
    adjusted = {}
    for key in metrics:
        if key in base_weights:
            # Apply non-linear scaling based on benchmark reference
            ref = benchmark_data.get(key, 1.0)
            score = (1.0 / metrics[key]) * ref * 100
            adjusted[key] = score * base_weights[key]
    
    # Composite calculation with conditional boost
    raw_total = sum(adjusted.values())
    
    # Conditional bonus based on jitter threshold (critical branching)
    jitter_value = metrics.get('jitter', float('inf'))
    bonus = 0.0
    if jitter_value < 0.05:
        bonus = raw_total * 0.1
    
    # Bit manipulation red herring
    encoded_bonus = int(bonus) ^ 0xCAFEBABE
    decoded_bonus = encoded_bonus ^ 0xCAFEBABE  # Reversible, looks complex but neutral
    
    # Use of slicing and set operations as distractors
    history_log = [raw_total] * 5
    recent_slice = history_log[-3:]  # Unused slice
    unique_totals = list(set(recent_slice))  # Redundant uniqueness check
    
    # Key data transformation using defaultdict (relevant)
    summary = defaultdict(float)
    summary['base'] = raw_total
    summary['bonus'] = decoded_bonus
    
    # Final aggregation
    final_raw = summary['base'] + summary['bonus']
    
    # Secondary adjustment based on throughput tier
    throughput = metrics.get('throughput', 0)
    tier_mod = 0
    if throughput > 90:
        tier_mod = 5
    elif throughput > 75:
        tier_mod = 3
    else:
        tier_mod = 1
    
    # Final score computation
    result = final_raw + tier_mod

    # Unused counter operation (distractor)
    event_counter = Counter(['update', 'refresh', 'update', 'commit'])
    
    return int(result)

# Main execution block
if __name__ == '__main__':
    # Input data
    system_metrics = {
        'latency': 0.025,
        'throughput': 82,
        'jitter': 0.04
    }
    
    reference_benchmark = {
        'latency': 0.03,
        'throughput': 80,
        'jitter': 0.06
    }
    
    # Dead variable assignments (irrelevant)
    calibration_offset = 0.003
    tolerance_window = [0.01, 0.02, 0.03]
    debug_trace = {(x, x**2): x*0.1 for x in range(1, 5)}
    
    # Signal data (unused)
    raw_sensor_data = [-0.5, 0.0, 0.15, -0.05, 0.3, 0.8, -0.2]
    processed = preprocess_signal(raw_sensor_data)
    
    # Hardware monitoring (unrelated)
    temperatures = {'cpu': 68, 'gpu': 72, 'fpga': 58}
    limits = {'cpu': 75, 'gpu': 80, 'fpga': 60}
    status = analyze_component_health(temperatures, limits)
    
    # Statistical shadow variables
    sample_loads = [76, 81, 79, 85, 74]
    stats = compute_redundant_stats(sample_loads)
    
    # Critical assignment
    final_score = evaluate_performance(system_metrics, reference_benchmark)
    
    # Output result
    print(f"Result: {final_score}")