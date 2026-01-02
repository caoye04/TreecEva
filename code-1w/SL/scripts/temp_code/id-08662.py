def analyze_data(samples):
    temp_results = []
    outlier_count = 0
    for sample in samples:
        if sample < -100 or sample > 100:
            outlier_count += 1
            continue
        adjusted = abs(sample) ** 0.5 * 2.5
        if adjusted > 20:
            temp_results.append(18.7)
        else:
            temp_results.append(adjusted)
    return temp_results

# Irrelevant preprocessing block (distractor)
def normalize_signal(signal):
    max_val = max(signal)
    return [s / max_val for s in signal]

# Unused function - red herring
def compute_entropy(data):
    from math import log
    freq = {}
    for d in data:
        freq[d] = freq.get(d, 0) + 1
    total = len(data)
    entropy = 0
    for count in freq.values():
        p = count / total
        entropy -= p * log(p)
    return entropy

# Core metric computation with hidden logic chain
def generate_metrics(base_values):
    raw_metrics = []
    temp_cache = {}
    
    for i, val in enumerate(base_values):
        if i % 3 == 0:
            computed = (val * 1.1) % 25
        elif i % 5 == 0:
            computed = (val + 7) // 3
        else:
            computed = val // 2 + 3
        
        # Store in cache but only some are used later
        temp_cache[f'idx_{i}'] = computed * 0.9
        raw_metrics.append(computed)
    
    # Misleading transformation
    transformed = [x * 1.05 for x in raw_metrics if x > 4]
    
    # Decoy aggregation
    decoy_sum = sum(transformed) / len(transformed) if transformed else 0
    
    # Actual relevant result subset
    return raw_metrics[:8]  # Only first 8 matter

# Set-based filtering and scoring
def filter_relevant(metrics, threshold_set):
    all_vals = set(metrics)
    high_perf = {m for m in all_vals if m > 12}
    medium_perf = {m for m in all_vals if 6 <= m <= 12}
    low_perf = {m for m in all_vals if m < 6}
    
    # Complex inter-set operations (only one matters)
    valid_group = high_perf & threshold_set
    backup_group = medium_perf | low_perf
    redundant_check = high_perf ^ backup_group
    
    # Critical dependency: score based on intersection size
    primary_score = len(valid_group) * 15
    secondary_score = sum(backup_group) * 0.5
    
    # Dead code path - never executed due to prior logic
    if len(redundant_check) > 100:
        fallback = sum(redundant_check) // 10
        return fallback

    return primary_score + secondary_score

# Final evaluation with conditional override
def evaluate_performance(metric_set):
    base_input = [23, 45, 12, 67, 89, 34, 56, 18, 91, 73]
    analysis_result = analyze_data(base_input)
    
    # Distracting noise: normalization call with unused result
    normalized = normalize_signal([x * 100 for x in analysis_result])
    
    metrics = generate_metrics(base_input)
    
    # Key set operation determining final behavior
    threshold_reference = {11, 12, 22, 23, 24, 25, 26, 27}
    intermediate_value = filter_relevant(metrics, threshold_reference)
    
    # Conditional accumulation with early return red herring
    final_score = 0
    for val in metrics:
        if val > 25:
            final_score += val // 4
        elif val > 15:
            final_score += val // 5
        else:
            final_score += val // 6
        
        # Early break that never triggers - misleading control flow
        if final_score < 0:
            break

    # Final override condition — this is the real answer path
    if len(threshold_reference & set(metrics)) >= 3:
        final_score = intermediate_value  # This assignment happens

    return final_score

# Execution entry point
if __name__ == '__main__':
    test_samples = [-200, 150, 45, 60, 75, 30, 90, 105]
    dummy_analysis = analyze_data(test_samples)  # Unused result
    
    metric_set = {12, 23, 24, 25, 34, 56}
    final_score = evaluate_performance(metric_set)
    print(f"Target result: {final_score}")