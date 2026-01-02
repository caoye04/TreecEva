def analyze_pattern_sequence():
    # Simulate analysis of a pattern in signal data
    raw_signals = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    filtered = raw_signals[2:8]  # Slice to focus on central pattern
    peak = max(filtered)
    avg = sum(filtered) / len(filtered)
    deviation_sum = sum((x - avg) ** 2 for x in filtered)
    variance_estimate = deviation_sum / len(filtered) if len(filtered) > 1 else 0

    # Irrelevant statistical distraction
    redundant_calc = (peak * avg) / (variance_estimate + 1e-5)
    noise_floor = 0.5 * peak

    # Actual relevant metric extraction
    pattern_strength = len([x for x in filtered if x > avg])

    return pattern_strength, variance_estimate, redundant_calc


def evaluate_consistency(metrics):
    # Assess temporal consistency from prior results
    strength, var, redun = metrics
    time_weights = [0.8, 0.9, 1.0, 1.1, 1.2]  # Hypothetical weights over time

    # Fake propagation of time-based adjustment (only one value used later)
    adjusted_strength = strength * time_weights[2]
    decay_factor = 0.95 ** 3
    inflated_estimate = redun * 1.5  # Unused but plausible

    # Dummy loop with side-effect-free operations
    temp = 0
    for i in range(3):
        temp += i * 0.1

    consistency_score = adjusted_strength if strength >= 4 else adjusted_strength * 0.7

    return consistency_score, decay_factor

def calculate_performance_rating():
    # Core function that integrates multiple reasoning steps
    
    # Step 1: Extract pattern information
    pattern_metrics = analyze_pattern_sequence()
    
    # Step 2: Evaluate temporal consistency
    score, decay = evaluate_consistency(pattern_metrics)
    
    # Step 3: Apply conditional adjustment based on combinatorics-like logic
    base_cases = [1, 2, 3, 4]
    combinations_possible = 0
    for i in range(len(base_cases)):
        for j in range(i + 1, len(base_cases)):
            if base_cases[j] - base_cases[i] <= 2:
                combinations_possible += 1
    
    # Step 4: Conditional override logic (simulates decision policy)
    threshold = 6
    if combinations_possible >= threshold:
        multiplier = 1.25
    else:
        multiplier = 0.85
    
    # Step 5: Final integration
    intermediate_result = score * multiplier
    
    # Distractor: complex-looking but unused calculation
    phantom_score = (pattern_metrics[1] + pattern_metrics[0]) * 10
    shadow_buffer = [phantom_score * k for k in range(4)]
    
    # Final computation
    final_score = int(intermediate_result + 0.5)  # Round to nearest integer
    
    # Output requirement
    print(f"Result: {final_score}")
    
    return final_score

# Execute main logic
calculate_performance_rating()