def calculate_performance(base, delta, limit):
    adjustment = 0
    penalty = 0
    
    # Irrelevant pre-computations (distractors)
    temp_offset = base * 0.1
    auxiliary_flag = (delta + temp_offset) > 50
    
    if delta < 0:
        adjustment = -delta * 2
    else:
        adjustment = delta * 1.5

    # Secondary logic path that may not execute (dead code hint)
    if limit <= 0:
        return -1  # Invalid case, not triggered here

    # Core scoring logic
    raw_score = base + adjustment
    
    # Conditional expression (required Python feature)
    volatility_factor = 1.2 if abs(delta) > limit else 0.8
    
    refined_score = raw_score * volatility_factor
    
    # Additional distraction: unused accumulation
    cumulative_history = []
    for i in range(3):
        cumulative_history.append(refined_score / (i + 1) if i != 0 else refined_score)

    # Final threshold-based correction
    final_correction = 10 if refined_score >= 100 and delta > 0 else 0
    final_score = refined_score + final_correction
    
    # Unused state tracking (intermediate distractor)
    last_updated = 'processed'
    debug_trace = [base, delta, limit, adjustment]
    
    return final_score

# Main execution
baseline = 60
variance = 15
deviation = variance * 1.2  # Real input transformation
threshold = 20

# Key call point
final_score = calculate_performance(baseline, deviation, threshold)
print(f"Target result: {final_score}")