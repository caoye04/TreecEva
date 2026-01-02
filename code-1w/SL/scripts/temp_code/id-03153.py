from itertools import combinations

# Simulated system performance metrics across different workloads
def analyze_workload_efficiency(base_metrics, stress_factors):
    adjusted = []
    temp_buffer = []
    for i, metric in enumerate(base_metrics):
        adjustment = stress_factors[i % len(stress_factors)]
        enhanced = metric * (1 + adjustment / 100)
        if enhanced > 90:
            temp_buffer.append(enhanced * 0.95)  # throttling effect
        else:
            temp_buffer.append(enhanced)
    
    # Irrelevant smoothing pass (distractor)
    smoothed = [temp_buffer[0]]
    for i in range(1, len(temp_buffer)):
        smoothed.append((temp_buffer[i] + temp_buffer[i-1]) / 2)
    
    return [round(v, 2) for v in temp_buffer]

# Legacy function for backward compatibility (dead code path)
def legacy_normalization(data):
    max_val = max(data)
    return [x / max_val for x in data] if max_val != 0 else data

# Core evaluation logic
def evaluate_performance(weights, benchmarks):
    weighted_sum = 0.0
    weight_total = 0.0
    
    # Simulate multi-criteria decision making with conditional weighting
    for key in weights:
        if key in benchmarks:
            impact = weights[key]
            raw_value = benchmarks[key]
            
            # Conditional scaling based on threshold
            scaled = raw_value * 1.1 if raw_value >= 85 else raw_value * 0.95
            weighted_sum += scaled * impact
            weight_total += impact
    
    final = weighted_sum / weight_total if weight_total != 0 else 0
    
    # Secondary adjustment using set intersection size (semi-relevant distractor)
    high_performers = {k: v for k, v in benchmarks.items() if v > 88}
    critical_dimensions = {'latency', 'throughput', 'consistency', 'fault_tolerance'}
    overlap_count = len(high_performers.keys() & critical_dimensions)
    bonus = overlap_count * 2.5
    
    return final + bonus

# Main execution
if __name__ == "__main__":
    # Raw benchmark scores from testing suite
    raw_data = [76, 88, 92, 79, 85]
    stress_profile = [5, -3, 8, 0, 12]
    
    # Normalize raw data through analysis pipeline
    processed = analyze_workload_efficiency(raw_data, stress_profile)
    
    # Create benchmark dictionary
    dimensions = ['latency', 'throughput', 'consistency', 'scalability', 'fault_tolerance']
    benchmark_dict = {dim: val for dim, val in zip(dimensions, processed)}
    
    # Weight assignment based on importance
    metric_weights = {
        'latency': 0.2,
        'throughput': 0.25,
        'consistency': 0.15,
        'scalability': 0.1,
        'fault_tolerance': 0.3
    }
    
    # Irrelevant combination generator (distractor)
    all_pairs = list(combinations(dimensions, 2))
    pair_count = len(all_pairs)
    dummy_aggregate = sum(len(pair) for pair in all_pairs)  # unused computation
    
    # Critical execution point
    final_score = evaluate_performance(metric_weights, benchmark_dict)
    
    # Print result
    print(f"Result: {final_score}")