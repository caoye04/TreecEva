from collections import defaultdict, Counter
import math

# Simulated system performance metrics
def collect_metrics():
    raw_data = [
        ('cpu_load', [0.65, 0.72, 0.58, 0.83]),
        ('memory_usage', [0.81, 0.77, 0.89, 0.64]),
        ('disk_io', [0.45, 0.53, 0.33, 0.61]),
        ('network_latency', [120, 95, 140, 110])
    ]
    
    metrics = defaultdict(float)
    for key, values in raw_data:
        if key == 'network_latency':
            metrics[key] = sum(values) / len(values)
        else:
            metrics[key] = sum([v**2 for v in values]) / len(values)
    
    # Irrelevant transformation (distractor)
    temp_snapshot = {k: v * 100 for k, v in metrics.items() if 'usage' in k}
    normalization_factor = math.log(1 + sum(temp_snapshot.values()))
    
    return metrics

# Weighting scheme for evaluation
def get_weights():
    base_weights = {
        'cpu_load': 0.3,
        'memory_usage': 0.25,
        'disk_io': 0.2,
        'network_latency': 0.25
    }
    
    # Dead code path - never used (red herring)
    def adjust_for_temperature(temp_offset):
        return {k: w * (1 + temp_offset * 0.01) for k, w in base_weights.items()}
    
    # Unused alternative weighting (distractor)
    alt_weights = Counter({'cpu_load': 30, 'memory': 25, 'io': 20, 'latency': 25})
    scaling_constant = 0.01
    
    return base_weights

# Auxiliary function with misleading intermediate result
def calculate_efficiency_ratio(metrics):
    cpu = metrics['cpu_load']
    mem = metrics['memory_usage']
    io = metrics['disk_io']
    latency = metrics['network_latency']
    
    # Complex but irrelevant efficiency score (decoy)
    raw_ratio = (cpu * mem) / (io + 1e-8)
    adjusted = raw_ratio * (100 / (latency + 1))
    normalized = math.tanh(adjusted)
    
    # This value is calculated but never used in final result
    diagnostic_flag = normalized > 0.5
    
    return normalized  # Red herring

# Core evaluation logic
def evaluate_performance(metrics, weights):
    weighted_sum = 0.0
    total_weight = 0.0
    
    for metric_name, value in metrics.items():
        if metric_name == 'network_latency':
            # Invert latency to make it a "higher is better" metric
            value = 200 - min(value, 200)
            value = max(value, 0) / 200  # Normalize to 0-1
        else:
            # Squared values already represent intensity; invert for "lower is better"
            value = (1 - value)
        
        weight = weights[metric_name]
        weighted_sum += value * weight
        total_weight += weight
    
    # Final aggregation
    score = weighted_sum / total_weight if total_weight > 0 else 0
    
    # Transform to percentage scale
    final_normalized_score = score * 100
    
    # Additional distraction: unused conditional adjustment
    if final_normalized_score > 70:
        bonus = math.sin(math.pi * final_normalized_score / 180)
        # Bonus is calculated but not applied
    
    return final_normalized_score

# Misleading preprocessing chain
def preprocess_for_report(data_dict):
    flattened = []
    for k, v in data_dict.items():
        if isinstance(v, list):
            flattened.extend(v)
        else:
            flattened.append(v)
    
    # Statistical decoy computations
    mean_val = sum(flattened) / len(flattened)
    variance = sum((x - mean_val) ** 2 for x in flattened) / len(flattened)
    peak_to_avg = max(flattened) / mean_val
    
    # These are never used
    summary_stats = {
        'mean': mean_val,
        'variance': variance,
        'ratio': peak_to_avg
    }
    
    return summary_stats

# Orchestration with hidden logic path
if __name__ == '__main__':
    # Step 1: Collect metrics
    collected = collect_metrics()
    
    # Step 2: Retrieve weighting scheme
    weights = get_weights()
    
    # Step 3: Calculate irrelevant efficiency ratio (distraction)
    efficiency = calculate_efficiency_ratio(collected)
    
    # Step 4: Preprocess for non-existent report (dead path)
    stats = preprocess_for_report(collected)
    
    # Step 5: Evaluate actual performance (this determines the answer)
    final_score = evaluate_performance(collected, weights)
    
    # Step 6: Print result (required output format)
    print(f"Target result: {final_score}")