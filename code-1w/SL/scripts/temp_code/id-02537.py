def analyze_signal_strength(signal, threshold, weight_factor):
    adjusted = [s * weight_factor for s in signal]
    above_threshold = [a for a in adjusted if a > threshold]
    below_threshold = [a for a in adjusted if a <= threshold]
    
    # Distractor: irrelevant noise calculation
    noise_floor = sum([abs(a - threshold) for a in adjusted]) / len(adjusted) if adjusted else 0
    noise_ratio = len(below_threshold) / len(adjusted) if adjusted else 0

    # Semi-relevant transformation
    normalized = [max(0, min(100, (a / (threshold * 1.5)) * 100)) for a in above_threshold]
    
    # Conditional expression used meaningfully
    bonus = 10 if len(above_threshold) > len(below_threshold) else 5
    
    # Core logic chain
    base_score = sum(normalized)
    penalty = 0
    if len(below_threshold) > 0:
        penalty = int(noise_ratio * 10) * 3
    
    intermediate_result = base_score - penalty + bonus

    # Additional distractor: unused path
    if noise_ratio < 0.3:
        adjustment = 0.9
    else:
        adjustment = 1.1  # never used

    return int(intermediate_result)


def evaluate_performance(data_stream, mode='aggressive'):
    # Simulate preprocessing
    filtered = [x for x in data_stream if x > 0]  # remove negatives
    inverted = [100 - x for x in filtered]  # transform scale

    # Bitwise masking as part of obfuscation
    masked = [i ^ 7 for i in inverted]

    # Two evaluation paths — only one is taken
    if mode == 'aggressive':
        level = 40
        factor = 1.8
    else:
        level = 60  # dead code path
        factor = 1.2  # dead code path

    # Critical call with side-effect-free computation
    score = analyze_signal_strength(masked, threshold=level, weight_factor=factor)
    
    # Final adjustment using logical and comparison operations
    multiplier = 1.5 if score > 100 and (score % 2 == 0) else 1.2
    final_score = int(score * multiplier)
    
    # Print required for traceability
    print(f"Result: {final_score}")
    return final_score

# Execution entry point
raw_data = [23, 45, 12, 67, 89, 34, 56]
evaluate_performance(raw_data, mode='aggressive')