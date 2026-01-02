def calculate_rating(temps, humidity):
    base_score = 0
    adjustment_factor = 0.5
    outlier_count = 0
    temp_sum = sum(temps)
    avg_temp = temp_sum / len(temps)
    
    # Irrelevant smoothing calculation (distractor)
    smoothed_values = [temps[i] * 0.8 + temps[min(i+1, len(temps)-1)] * 0.2 for i in range(len(temps))]
    smoothed_avg = sum(smoothed_values) / len(smoothed_values)

    # Real logic: count how many temperatures are above average and humidities below threshold
    high_temp_days = 0
    stable_humidity_days = 0
    
    for i, (t, h) in enumerate(zip(temps, humidity)):
        if t > avg_temp:
            high_temp_days += 1
        if h < 60:
            stable_humidity_days += 1
        # Early exit if extreme condition found (not triggered in this data)
        if t > 45:
            return -1
    
    # Secondary distractor: unused correlation estimate
    temp_humidity_pairs = list(zip(temps, humidity))
    correlation_estimate = sum(t * h for t, h in temp_humidity_pairs) / len(temp_humidity_pairs)

    # Core scoring logic
    base_score += high_temp_days * 3
    base_score += stable_humidity_days * 2
    
    # Adjustment based on variance (real impact)
    variance = sum((t - avg_temp) ** 2 for t in temps) / len(temps)
    if variance > 50:
        adjustment_factor = 1.2
    else:
        adjustment_factor = 0.7

    final_score = int(base_score * adjustment_factor)
    
    # Dead code branch (never executed with current inputs)
    if outlier_count > 5:
        final_score = -999

    return final_score

# Input data
temperature_readings = [22, 25, 31, 19, 33, 28, 35]
humidity_data = [65, 58, 45, 70, 52, 61, 40]

# Call function
final_score = calculate_rating(temperature_readings, humidity_data)
print(f"Result: {final_score}")