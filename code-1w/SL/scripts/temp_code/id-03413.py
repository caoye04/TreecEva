def analyze_performance(temperatures, humidity_levels):
    # Irrelevant baseline metrics
    base_metric_a = sum(temperatures) / len(temperatures)
    base_metric_b = max(humidity_levels) - min(humidity_levels)

    # Distractor: complex but unused transformation
    transformed_humidity = [abs(h - 50) * 0.8 for h in humidity_levels if h != 0]
    adjustment_factor = len(transformed_humidity) % 7 if transformed_humidity else 1

    # Relevant data processing with enumerate and zip
    temp_with_idx = list(enumerate(temperatures))
    combined_data = list(zip(temp_with_idx, humidity_levels))

    high_temp_events = 0
    stress_sum = 0.0

    for (idx, temp), hum in combined_data:
        if temp > 30:
            high_temp_events += 1
            stress_value = temp * (hum / 100.0)
            stress_sum += stress_value

            # Early break: rare condition
            if stress_value > 45.0:
                break

    # Secondary distractor computation (unused)
    avg_stress_without_break = stress_sum / len(combined_data) if combined_data else 0
    outlier_count = sum(1 for t in temperatures if abs(t - base_metric_a) > 15)

    # Core logic for final score
    duration_impact = len(temperatures) * 0.5
    event_penalty = high_temp_events * 2.3
    aggregate_stress = stress_sum * 1.15

    final_score = int((aggregate_stress - event_penalty + duration_impact) * adjustment_factor)

    # Print result as required
    print(f"Result: {final_score}")
    return final_score

# Input data
temps = [25, 32, 35, 29, 40, 27]
humids = [45, 60, 70, 50, 80, 40]

# Execute
result = analyze_performance(temps, humids)