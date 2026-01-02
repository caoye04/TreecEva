from itertools import combinations
from functools import reduce

# Simulate system performance evaluation with multiple metrics
def analyze_response_times(raw_logs):
    clean_data = [x for x in raw_logs if 0 < x < 5000]
    avg_time = sum(clean_data) / len(clean_data)
    outlier_count = len([x for x in clean_data if x > 3 * avg_time])
    return {'avg': avg_time, 'outliers': outlier_count}

def compute_throughput(events_log, window_size=100):
    sorted_events = sorted(events_log)
    max_count = 0
    for i in range(len(sorted_events)):
        count = 0
        window_start = sorted_events[i]
        for j in range(i, len(sorted_events)):
            if sorted_events[j] - window_start <= window_size:
                count += 1
            else:
                break
        if count > max_count:
            max_count = count
    return max_count

def evaluate_consistency(latency_samples):
    if len(latency_samples) < 2:
        return 0.0
    mean_val = sum(latency_samples) / len(latency_samples)
    variance = sum((x - mean_val) ** 2 for x in latency_samples) / len(latency_samples)
    std_dev = variance ** 0.5
    consistency_ratio = (std_dev / mean_val) * 100 if mean_val != 0 else 0
    return round(consistency_ratio, 3)

def char_frequency_analysis(text_stream):
    # Distractor function: counts character frequency but not used in final score
    freq_map = {}
    for char in text_stream:
        freq_map[char] = freq_map.get(char, 0) + 1
    return freq_map

def generate_combinations_analysis(items):
    # Another distractor: generates combinations but unused
    combo_keys = []
    for r in range(2, min(4, len(items)+1)):
        for combo in combinations(items, r):
            combo_keys.append(reduce(lambda a, b: a + b, map(str, combo)))
    return len(combo_keys)

def main():
    # Raw input data
    response_logs = [120, 150, 90, 85, 2000, 110, 95, 100, 130, 105]
    event_timestamps = [10, 25, 30, 35, 60, 70, 80, 100, 105, 110, 115, 140]
    latencies = [50, 60, 55, 58, 62, 59, 57, 61, 56, 63]
    dummy_text = "performanceevaluationmetrics"
    irrelevant_items = [1, 2, 3, 4]

    # Step 1: Analyze response times
    perf_metrics = analyze_response_times(response_logs)
    
    # Step 2: Compute peak throughput
    peak_load = compute_throughput(event_timestamps)
    
    # Step 3: Evaluate timing consistency
    stability_index = evaluate_consistency(latencies)
    
    # Distractor computations (irrelevant to final result)
    _ = char_frequency_analysis(dummy_text)
    _ = generate_combinations_analysis(irrelevant_items)
    temp_offset = sum([i**2 for i in range(5)])  # 0+1+4+9+16 = 30
    scaling_factor = 1.0 + (temp_offset / 1000)  # 1.03, not actually used
    
    # Build core metrics dictionary
    metrics = {
        'avg_response': perf_metrics['avg'],
        'peak_throughput': peak_load,
        'stability': stability_index
    }
    
    # Weight configuration for scoring
    benchmark_weights = {
        'avg_response': 0.4,
        'peak_throughput': 0.35,
        'stability': 0.25
    }
    
    # Core evaluation logic
    normalized_response = 100 * (1 - min(metrics['avg_response'] / 200, 1))
    normalized_throughput = 100 * (metrics['peak_throughput'] / 50)
    normalized_stability = 100 * (1 - min(metrics['stability'] / 20, 1))
    
    weighted_components = {
        'response': normalized_response * benchmark_weights['avg_response'],
        'throughput': normalized_throughput * benchmark_weights['peak_throughput'],
        'reliability': normalized_stability * benchmark_weights['stability']
    }
    
    # Final score calculation
    final_score = sum(weighted_components.values())
    
    # Print result as required
    print(f"Result: {final_score}")
    
    return final_score

# Execute and capture result
def evaluate_performance(met, weights):
    # This function call is the key execution point
    return sum(
        [
            100 * (1 - min(met['avg_response'] / 200, 1)) * weights['avg_response'],
            100 * (met['peak_throughput'] / 50) * weights['peak_throughput'],
            100 * (1 - min(met['stability'] / 20, 1)) * weights['stability']
        ]
    )

final_score = evaluate_performance(
    {
        'avg_response': 110.0,
        'peak_throughput': 5,
        'stability': 8.367
    },
    {
        'avg_response': 0.4,
        'peak_throughput': 0.35,
        'stability': 0.25
    }
)
print(f"Result: {final_score}")