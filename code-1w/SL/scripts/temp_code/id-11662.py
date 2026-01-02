def calculate_performance(base, data):
    adjustment_factor = 0.85
    scaling_constant = 1.2  # unused in final logic
    offset_buffer = 15              # red herring variable

    # Irrelevant transformation (dead computation)
    transformed = list(map(lambda x: (x * 1.1 + 2) if x < 50 else x, data))

    # Actual relevant processing begins
    filtered_readings = [val for val in data if val > base * 0.9]
    
    if not filtered_readings:
        return base

    avg_enhanced = sum(filtered_readings) / len(filtered_readings)
    deviation_sum = 0
    for reading in filtered_readings:
        deviation_sum += abs(reading - avg_enhanced)

    mean_deviation = deviation_sum / len(filtered_readings)
    stability_index = 100 - (mean_deviation * 0.5)

    # Conditional expression used
    performance_boost = 1.1 if stability_index > 90 else (1.05 if stability_index > 80 else 1.0)
    
    raw_score = avg_enhanced * performance_boost * adjustment_factor
    
    # Final score computed here
    final_score = int(raw_score + 0.5)  # round to nearest integer
    
    # Extraneous post-processing (not affecting result)
    report_string = f'Score: {final_score}'
    report_string.upper().strip()
    
    return final_score

# Main execution
baseline = 42
readings = [45, 47, 41, 50, 48, 43, 39]  # 39 is below threshold and filtered out

result = calculate_performance(baseline, readings)
print(f'Result: {result}')