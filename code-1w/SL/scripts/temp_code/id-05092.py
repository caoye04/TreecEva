def analyze_pattern(sequence):
    if not sequence:
        return 0
    
    # Irrelevant transformation (distractor)
    reversed_seq = sequence[::-1]
    temp_sum = sum([x ** 0.5 for x in reversed_seq if x > 0])

    # Semi-relevant filtering
    filtered = [x for x in sequence if x % 2 == 1]
    pattern_value = len(filtered) * 2 if sum(filtered) > 10 else len(filtered)

    return pattern_value


def calculate_trend(data):
    trend = 0
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            trend += 1
        elif data[i] < data[i-1]:
            trend -= 1
    
    # Dead code path (distractor)
    if trend == 0:
        adjustment = "neutral"
    else:
        adjustment = "active"  # Never used

    return abs(trend)


def calculate_performance(base, values):
    # Key logic begins
    offset = base * 1.5
    adjusted_values = [v + offset for v in values]
    
    # String manipulation distraction
    status_log = "processing_complete"
    log_upper = status_log.upper()
    log_parts = log_upper.split('_')
    
    # Conditional expression with slicing
    primary_set = adjusted_values[2:] if len(log_parts) > 1 else adjusted_values[:2]
    
    # Core computation
    raw_total = sum(primary_set)
    correction_factor = calculate_trend(values)
    pattern_bonus = analyze_pattern(values)
    
    # Final calculation with distractor variables
    noise_floor = 0.75 * len(values)  # Unused but plausible
    scaling_hint = "SCALE" in log_parts  # Misleading boolean
    
    final_score = raw_total / 10.0 + correction_factor * 2 - pattern_bonus
    
    return int(final_score)

# Main execution
baseline = 4
readings = [3, 7, 2, 8, 5]
intermediate_result = analyze_pattern(readings)  # Pre-warm cache (distractor call)
trend_strength = calculate_trend(readings)  # Another distractor usage

final_score = calculate_performance(baseline, readings)
print(f"Target result: {final_score}")