def calculate_performance(base, data):
    adjustment_factor = 1.0
    cumulative = 0
    peak_detected = False
    temp_offset = 0

    # Simulate environmental interference filtering
    filtered_data = [x for x in data if x > base * 0.8 and x < base * 1.3]

    if len(filtered_data) == 0:
        return base

    for val in filtered_data:
        if val > base * 1.2:
            adjustment_factor *= 1.05
        elif val < base * 0.9:
            adjustment_factor *= 0.97

        # Track cumulative deviation (distraction)
        deviation = abs(val - base)
        cumulative += deviation

        # Simulated hysteresis logic (semi-relevant)
        if val > base * 1.15 and not peak_detected:
            temp_offset += 5
            peak_detected = True

    # Secondary adjustment based on string-encoded condition (use of string method)
    mode_flag = 'NORM-AL'  # Deliberate typo
    normalized_flag = mode_flag.replace('-', '')
    
    if 'AL' in normalized_flag and len(data) % 2 == 0:
        adjustment_factor *= 1.02

    # Core calculation path
    average_deviation = cumulative / len(filtered_data)
    stability_index = (base - average_deviation) / base

    # Final performance score influenced by multiple factors
    raw_score = base * adjustment_factor * (1 + stability_index * 0.1)

    # Irrelevant transformation (dead computation)
    diagnostic_trace = [raw_score * 0.1 for _ in range(3)]
    trace_sum = sum(diagnostic_trace)

    final_score = int(raw_score + 0.5)  # Round to nearest integer

    # Additional red herring: unused conditional expression
    status_msg = 'Optimal' if trace_sum > 10 else 'Suboptimal'

    return final_score

# Input values
baseline = 42
readings = [45, 38, 41, 60, 43, 35, 44]  # Note: 60 and 35 will be filtered out

# Execution point of interest
final_score = calculate_performance(baseline, readings)
print(f"Result: {final_score}")