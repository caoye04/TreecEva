def analyze_signal_integrity(raw_samples, baseline_offset=0.0314):
    sample_size = len(raw_samples)
    filtered_data = [x for x in raw_samples if x > baseline_offset]
    
    # Irrelevant preprocessing (distractor)
    normalized = list(map(lambda x: (x - min(filtered_data)) / (max(filtered_data) - min(filtered_data) + 1e-9), filtered_data))
    noise_floor = sum([abs(a - b) for a, b in zip(normalized, normalized[1:])]) / len(normalized) if normalized else 0
    
    # Real computation begins
    windowed_sums = []
    for i in range(0, len(filtered_data) - 2, 3):
        windowed_sums.append(sum(filtered_data[i:i+3]))
    
    avg_window = sum(windowed_sums) / len(windowed_sums) if windowed_sums else 0
    
    # Destructuring and multiple assignments (relevant)
    peak, valley = max(filtered_data), min(filtered_data)
    dynamic_range = peak - valley
    
    # Dictionary operations and conditional logic
    diagnostics = {
        "count": len(filtered_data),
        "range": dynamic_range,
        "stability": avg_window / (dynamic_range + 1e-5)
    }
    
    if diagnostics["stability"] > 0.5:
        diagnostics["class"] = "high"
        adjustment = 1.2
    elif diagnostics["stability"] > 0.2:
        diagnostics["class"] = "medium"
        adjustment = 0.85
    else:
        diagnostics["class"] = "low"
        adjustment = 0.5
    
    # Key branching with distractors
    temp_cache = {i: val ** 2 for i, val in enumerate(filtered_data)}  # unused cache
    decay_rate = 0.91
    cumulative_decay = 0
    for _ in range(5):
        cumulative_decay += decay_rate
        decay_rate *= 0.99  # misleading iterative update
    
    # Core logic embedded among distractions
    reference_index = int(diagnostics["count"] * 0.75) % len(filtered_data) if filtered_data else 0
    base_metric = filtered_data[reference_index] if filtered_data else 0
    
    sensitivity_factor = adjustment * (1 + noise_floor * 0.1)
    
    # Slicing used meaningfully
    trend_slice = normalized[-3:] if len(normalized) >= 3 else normalized
    trend_bias = sum(trend_slice) / len(trend_slice) if trend_slice else 0
    
    final_diagnostic = dict(diagnostics)
    final_diagnostic["metric"] = base_metric + trend_bias * 0.3
    
    # Critical statement
    threshold_score = final_diagnostic["metric"] * sensitivity_factor
    
    # Print required result
    print(f"Result: {threshold_score}")
    return threshold_score

# Input data
signal_input = [0.05, 0.09, 0.032, 0.12, 0.088, 0.073, 0.105, 0.094, 0.062, 0.111]
analyze_signal_integrity(signal_input)