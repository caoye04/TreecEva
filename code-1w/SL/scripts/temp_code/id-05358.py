def calculate_performance(base, data):
    adjustment_factor = 0.85
    threshold = base * 0.75
    temp_offset = 0
    cumulative = 0
    peak_count = 0
    smoothed_values = []

    for val in data:
        if val > threshold:
            temp_offset += 1
            peak_count += 1
            adjusted_val = (val - base) * adjustment_factor
        else:
            adjusted_val = (val - base) * 0.5
        
        if adjusted_val < 0:
            adjusted_val = abs(adjusted_val) ** 0.5  # dampen negative deviations
        
        smoothed_values.append(round(adjusted_val, 2))

    # Irrelevant accumulation (distractor)
    total_chars = sum(len(str(int(x))) for x in smoothed_values)
    info_density = total_chars / len(smoothed_values) if smoothed_values else 0

    # Actual computation path
    raw_sum = sum(smoothed_values)
    penalty = peak_count * 0.25
    cumulative = raw_sum - penalty

    extra_buffer = 0
    for i in range(len(smoothed_values)):
        if i % 3 == 0:
            extra_buffer += 0.1  # minor red herring

    # Final calculation
    final_score = int(cumulative + 0.5)  # rounding to nearest integer
    return final_score

# Simulated sensor readings
baseline = 98
readings = [102, 95, 110, 90, 115, 120, 85]

# Misleading preprocessing
normalized = [round((x - baseline) / baseline * 100, 1) for x in readings]
drift_estimate = sum(normalized) / len(normalized)

# Key execution point
final_score = calculate_performance(baseline, readings)
print(f"Result: {final_score}")