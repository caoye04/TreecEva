def analyze_system_stability(readings):
    stability_scores = []
    temp_buffer = []
    cumulative_drift = 0.0
    correction_factor = 1.05
    baseline_adjustment = 0.98
    
    for i, reading in enumerate(readings):
        raw_value = reading * correction_factor
        adjusted_value = raw_value * baseline_adjustment
        
        # Simulate noise filtering
        if len(temp_buffer) >= 3:
            temp_buffer.pop(0)
        temp_buffer.append(adjusted_value)
        
        # Compute moving variance as stability proxy
        mean_temp = sum(temp_buffer) / len(temp_buffer)
        variance = sum((x - mean_temp) ** 2 for x in temp_buffer) / len(temp_buffer)
        stability_score = 100 - (variance * 10)
        
        # Irrelevant debug computation (distractor)
        theoretical_max = (i + 1) * 10 + 5
        placeholder_metric = theoretical_max * 0.75 if i % 2 == 0 else theoretical_max * 0.25
        
        stability_scores.append(round(stability_score, 3))
        
        # Cumulative drift tracking (semi-relevant but not used in final result)
        cumulative_drift += abs(adjusted_value - mean_temp)

    # Secondary loop: cross-compare readings using zip (irrelevant to final answer)
    consistency_checks = 0
    for curr, nxt in zip(stability_scores, stability_scores[1:]):
        if abs(curr - nxt) < 5:
            consistency_checks += 1

    # Final processing step with key statement
    peak_stability = max(stability_scores)
    return peak_stability

# Input data
sensor_readings = [9.1, 9.3, 9.2, 9.5, 9.4, 9.6, 9.3, 9.2]
result = analyze_system_stability(sensor_readings)
print(f"Target result: {result}")