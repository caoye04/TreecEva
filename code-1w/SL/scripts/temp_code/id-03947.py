def analyze_component(metrics, threshold=0.5):
    high_perf = [m for m in metrics if m > threshold]
    low_perf = [m for m in metrics if m <= threshold]
    return len(high_perf) - len(low_perf)


def normalize_values(data):
    total = sum(data)
    return [x / total for x in data] if total != 0 else data


def calculate_performance(raw_data):
    processed = {}
    temp_results = []
    
    for key, values in raw_data.items():
        if key.startswith('sensor_'):
            norm_vals = normalize_values(values)
            score = sum([v**2 for v in norm_vals])
            processed[key] = round(score, 4)
            temp_results.append(score)
    
    # Misleading computation - not used in final result
    dummy_aggregate = sum(temp_results) * 0.1 if temp_results else 0
    adjustment_factor = len(temp_results) % 3

    # Real logic path
    benchmark_data = [processed[k] for k in processed.keys() if '7' in k]  # only sensor_7
    if not benchmark_data:
        return 0
    
    base_score = benchmark_data[0] * 100
    
    extra_metrics = [0.1, 0.3, 0.6, 0.8]
    bonus = sum(1 for x in extra_metrics if x < base_score / 50)  # irrelevant check
    
    # Conditional expression (Python feature)
    penalty = 10 if any(x < 0.1 for x in benchmark_data) else 5
    
    # Distractor: unused list comprehension
    [x * 2 for x in range(len(raw_data))]  

    final_score = int(base_score - penalty)
    
    # Use of enumerate and zip (Python features)
    indexed = list(enumerate(zip(temp_results, [x*0.9 for x in temp_results])))
    
    # Dead code - never executed but adds noise
    if False:
        fallback = sum(processed.values())
        final_score = fallback

    return final_score

# Simulated input data
raw_system_data = {
    'sensor_1': [0.2, 0.3, 0.5],
    'sensor_2': [0.1, 0.1, 0.1, 0.7],
    'sensor_3': [0.4, 0.4],
    'sensor_4': [0.6, 0.3, 0.1],
    'sensor_5': [0.9],
    'sensor_6': [0.2, 0.2, 0.2, 0.2, 0.2],
    'sensor_7': [0.5, 0.5]  # This will be used
}

# Key execution point
final_score = calculate_performance(raw_system_data)
print(f"Target result: {final_score}")