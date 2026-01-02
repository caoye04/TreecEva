def analyze_sensor_readings(readings):
    valid_ranges = set(range(10, 91))
    normalized = [min(max(r, 0), 100) for r in readings]
    
    # Irrelevant transformation (distractor)
    squared_devs = [(x - 50)**2 for x in normalized]
    avg_sq_dev = sum(squared_devs) / len(squared_devs) if squared_devs else 0
    
    # Core logic: count how many readings are within optimal range
    within_optimal = sum(1 for val in normalized if val in valid_ranges)
    outlier_count = sum(1 for val in normalized if val < 10 or val > 90)
    
    # Distractor: unused complex structure
    stats_summary = {
        'mean': sum(normalized) / len(normalized),
        'peak': max(normalized),
        'truncated': [val // 10 * 10 for val in normalized],
        'entropy_proxy': len(set(normalized))
    }
    
    return within_optimal, outlier_count


def calculate_compliance_index(data):
    # Unused helper function (dead code path - distractor)
    compliance = 0
    for i, val in enumerate(data):
        if i % 2 == 0 and val > 25:
            compliance += 1
    return compliance


def calculate_final_score(data):
    score = 0
    adjustment_factor = 0.75
    
    # Real processing
    in_range, outliers = analyze_sensor_readings(data)
    
    # Secondary distractor computation
    paired_shifts = [a ^ b for a, b in zip(data[:-1], data[1:])]  # XOR of adjacent
    shift_sum = sum(p for p in paired_shifts if p > 0)
    
    # Main scoring logic (dependent on in_range)
    if in_range > 3:
        score += 40
        if in_range >= len(data) * 0.75:  # At least 75% in range
            score += 35
        elif in_range >= len(data) * 0.5:
            score += 20
    else:
        score += 10
    
    # Outlier penalty
    if outliers == 0:
        score += 15
    elif outliers <= 2:
        score += 5
    
    # Final irrelevant rounding operation (distractor)
    temp_result = round(score * adjustment_factor, 3)
    final_correction = int(temp_result + 0.5)
    
    # Actual answer depends only on control flow above
    return int(score * adjustment_factor)  # Note: uses adjustment but not corrected

# Simulated sensor input
sensor_input = [85, 92, 15, 67, 43, 8, 77, 52]

# Key processing steps
filtered_data = [val for val in sensor_input if val >= 5]  # Remove extreme low
processed_data = [min(val, 100) for val in filtered_data]  # Clamp high

# Critical execution point
final_score = calculate_final_score(processed_data)

print(f"Result: {final_score}")