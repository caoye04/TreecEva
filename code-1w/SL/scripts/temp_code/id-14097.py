from collections import defaultdict
import math

def analyze_efficiency(metrics):
    efficiency = 1.0
    penalty = 0.0
    for key, value in metrics.items():
        if 'latency' in key:
            penalty += 0.1 * math.log(value + 1)
        elif 'throughput' in key:
            efficiency *= (1 + value / 1000)
    return efficiency - penalty

def validate_stability(readings):
    avg = sum(readings) / len(readings)
    variance = sum((x - avg) ** 2 for x in readings) / len(readings)
    return variance < 25

def compute_performance(data):
    scores = defaultdict(float)
    temp_results = []
    
    for entry in data:
        raw_score = entry['base'] * 1.5
        adjustment = 0.0
        
        if entry['mode'] == 'high_load':
            adjustment = -20 if entry['errors'] > 2 else -10
        elif entry['mode'] == 'low_latency':
            adjustment = 15 if validate_stability(entry['response_times']) else 5
        
        # Irrelevant aggregation
        outlier_count = 0
        for rt in entry['response_times']:
            if rt > 200:
                outlier_count += 1
        dummy_weight = outlier_count * 0.01  # Not used later
        
        processed_value = raw_score + adjustment
        scores[entry['mode']] += processed_value
        temp_results.append(processed_value)
    
    # Secondary processing with distractor variables
    total_modes = len(scores)
    aggregate_sum = sum(temp_results)
    mean_performance = aggregate_sum / len(temp_results)
    fluctuation_index = max(temp_results) - min(temp_results)
    
    # Red herring computation
    hypothetical_gain = 0
    for i in range(len(temp_results)):
        if i % 3 == 0:
            hypothetical_gain += math.sqrt(temp_results[i])

    # Actual final score calculation
    base_final = mean_performance * (1 + 0.01 * fluctuation_index)
    if total_modes > 1:
        base_final += 10
    
    # Final adjustment based on efficiency analysis
    meta_metrics = {
        'latency_spike_count': 3,
        'throughput_peak': 850,
        'latency_avg': 45
    }
    efficiency_bonus = analyze_efficiency(meta_metrics)
    final_adjustment = efficiency_bonus * 5
    
    final_score = int(base_final + final_adjustment)
    
    # Print required result
    print(f"Result: {final_score}")
    return final_score

# Benchmark data
benchmark_data = [
    {
        'base': 80,
        'mode': 'high_load',
        'errors': 3,
        'response_times': [120, 130, 125, 210, 190]
    },
    {
        'base': 70,
        'mode': 'low_latency',
        'errors': 0,
        'response_times': [45, 50, 40, 60, 55]
    },
    {
        'base': 90,
        'mode': 'low_latency',
        'errors': 0,
        'response_times': [50, 55, 45, 40, 65]
    }
]

# Execute
final_score = compute_performance(benchmark_data)