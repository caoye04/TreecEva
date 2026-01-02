from collections import defaultdict

# Simulated system performance metrics
def collect_metrics():
    raw_data = [85, 90, 78, 92, 88, 76, 95, 87, 83, 91]
    processed = defaultdict(int)
    temp_log = []

    for val in raw_data:
        if val >= 90:
            processed['high'] += 1
        elif val >= 80:
            processed['medium'] += 1
        else:
            processed['low'] += 1
        
        # Distractor: irrelevant transformation
        adjusted = (val * 1.05) - 5
        temp_log.append(round(adjusted))

    # Irrelevant computation chain
    avg_temp = sum(temp_log) / len(temp_log) if temp_log else 0
    deviation_sum = sum(abs(t - avg_temp) for t in temp_log)
    noise_level = deviation_sum / len(temp_log) if temp_log else 0

    return dict(processed), noise_level

# Auxiliary function with misleading relevance
def calculate_efficiency(data):
    total = sum(data.values())
    efficiency_ratio = (data.get('high', 0) + data.get('medium', 0) * 0.5) / total if total > 0 else 0
    
    # Dead code path - never used
    if efficiency_ratio > 0.8:
        status_flag = "OPTIMAL"
    else:
        status_flag = "SUBOPTIMAL"
    
    # More distraction
    normalized = {k: v / total for k, v in data.items()} if total > 0 else data
    return efficiency_ratio  # Only this is returned

# Core evaluation logic
def evaluate_performance(metrics, threshold):
    high_count = metrics.get('high', 0)
    medium_count = metrics.get('medium', 0)
    low_count = metrics.get('low', 0)

    # Weighted scoring with conditional expression
    score = (high_count * 10) + (medium_count * 5) + (low_count * -3)
    
    # Conditional adjustment based on threshold
    penalty = 15 if high_count < threshold else 0
    bonus = 10 if (high_count >= 3 and medium_count >= 4) else 0
    
    # Intermediate irrelevant calculation
    completeness = (high_count + medium_count + low_count) / 10.0
    scaling_factor = completeness ** 0.5 if completeness > 0 else 0
    
    # Final score computation
    final_raw = score - penalty + bonus
    
    # Another red herring: unused derived metric
    quality_index = (final_raw / 100.0) * scaling_factor if scaling_factor else 0
    
    # Final adjustment using string-based logic (simulating config)
    mode_flag = 'strict' if threshold > 2 else 'relaxed'
    multiplier = 1.1 if mode_flag == 'strict' else 0.9
    
    return int(final_raw * multiplier)

# Main execution flow
if __name__ == "__main__":
    metric_data, noise = collect_metrics()
    base_threshold = 3
    
    # Irrelevant preprocessing step
    sorted_keys = sorted(metric_data.keys(), key=lambda x: metric_data[x], reverse=True)
    summary_stats = {k: metric_data[k] for k in sorted_keys}
    
    # Efficiency computed but not directly used in final score
    efficiency = calculate_efficiency(metric_data)
    
    # Key statement
    final_score = evaluate_performance(metric_data, base_threshold)
    
    # Print result as required
    print(f"Result: {final_score}")