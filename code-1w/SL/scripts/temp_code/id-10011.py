def analyze_text_patterns(text):
    char_count = {}
    for c in text:
        char_count[c] = char_count.get(c, 0) + 1
    uppercase_count = sum(1 for c in text if c.isupper())
    reversed_text = text[::-1]
    normalized = text.lower().replace(' ', '')
    return char_count, len(normalized)


def transform_metrics(raw_values, scaling_factor=1.5):
    adjusted = [x * scaling_factor for x in raw_values if x > 0]
    squared = [x**2 for x in adjusted]
    filtered = [x for x in squared if x < 1000]
    return filtered if len(filtered) > 3 else [0]


def compute_hash_chain(seed_value, iterations=5):
    result = seed_value
    history = []
    for i in range(iterations):
        result = (result * 7 + 13) % 1009
        history.append(result)
    return history[-1]


def dummy_validation_check(data):
    if isinstance(data, list) and len(data) > 0:
        temp_sum = sum(data)
        avg = temp_sum / len(data)
        outlier_detected = any(abs(x - avg) > 2 * avg for x in data)
        return True if not outlier_detected else False
    return False


def evaluate_performance(metrics, baselines):
    # Core relevant logic starts here
    base_score = 0
    for k, v in metrics.items():
        if k in baselines:
            deviation = abs(v - baselines[k])
            penalty = deviation * 0.1 if deviation > 5 else 0
            base_score += baselines[k] - penalty
    
    secondary_adjustment = 0
    values = list(metrics.values())
    if len(values) >= 3:
        sorted_vals = sorted(values)
        median_val = sorted_vals[len(sorted_vals) // 2]
        secondary_adjustment = median_val * 0.25
    
    # Irrelevant hash computation (distractor)
    _ = compute_hash_chain(123, 7)
    
    # Dummy call with no effect (red herring)
    _ = dummy_validation_check([10, 20, 30, 40])
    
    # Conditional expression - required python feature
    multiplier = 1.75 if base_score >= 40 else 0.85
    
    # Final calculation
    final_score = (base_score + secondary_adjustment) * multiplier
    
    # Unused variables and computations (distractions)
    unused_list = [i**3 for i in range(10)]
    unused_dict = {f'key_{i}': i * 2 for i in range(5)}
    shadow_copy = metrics.copy()
    for key in shadow_copy:
        shadow_copy[key] += 100  # Dead operation
    
    return final_score

# Main execution block
input_text = "DynamicAnalysisEngineV2"
text_analysis_result, norm_length = analyze_text_patterns(input_text)

# Build metric data with meaningful and irrelevant components
metric_data = {
    'throughput': 45.0,
    'latency': 30.0,
    'accuracy': 55.0,
    'stability': 40.0,
    'bandwidth': 20.0  # Not in baselines -> will be ignored
}

benchmarks = {
    'throughput': 50,
    'latency': 35,
    'accuracy': 60,
    'stability': 45
}

raw_telemetry = [-5, 10, 15, 20, 25, 0, 30]
processed_telemetry = transform_metrics(raw_telemetry)

# Another distraction: unused transformation
hash_signature = compute_hash_chain(norm_length + sum(processed_telemetry))

# Key statement
final_score = evaluate_performance(metric_data, benchmarks)

# Print result as required
print(f"Target result: {final_score}")