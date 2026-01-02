def calculate_optimal_yield(temps, humids):
    # Simulate agricultural yield prediction based on environmental factors
    baseline_yield = 50
    adjustment_factor = 0.0
    cumulative_stress = 0.0
    peak_stress = -float('inf')
    temp_hum_ratio_series = []
    stress_flags = []

    for i, (t, h) in enumerate(zip(temps, humids)):
        temp_deviation = abs(t - 25)  # Ideal temp: 25C
        humidity_deviation = abs(h - 60)  # Ideal humidity: 60%

        # Compute individual stress scores
        temp_stress = max(0, temp_deviation * 0.8)
        humid_stress = max(0, humidity_deviation * 0.3)
        combined_stress = temp_stress + humid_stress

        # Track rolling stress metrics (some are distractions)
        cumulative_stress += combined_stress
        if combined_stress > peak_stress:
            peak_stress = combined_stress

        # This ratio is not actually used in final calculation
        if h != 0:
            temp_hum_ratio = t / h
        else:
            temp_hum_ratio = 0
        temp_hum_ratio_series.append(temp_hum_ratio)

        # Only significant stress triggers flag (semi-relevant)
        stress_flags.append(combined_stress > 10)

        # Actual adjustment uses only average stress influence
        adjustment_factor += (temp_stress * 0.5) - (humid_stress * 0.2)

    # Distraction: analyze ratio trends (never used)
    ratio_changes = []
    for j in range(1, len(temp_hum_ratio_series)):
        ratio_changes.append(temp_hum_ratio_series[j] - temp_hum_ratio_series[j-1])

    avg_ratio_change = sum(ratio_changes) / len(ratio_changes) if ratio_changes else 0
    flagged_intervals = [i for i, flag in enumerate(stress_flags) if flag]

    # Another distraction: unused smoothing logic
    smoothed_yield = baseline_yield
    for _ in range(2):
        smoothed_yield = (smoothed_yield + baseline_yield) / 2

    # Real computation: yield impacted by net adjustment
    net_adjustment = adjustment_factor * 0.9
    preliminary_yield = baseline_yield - net_adjustment

    # Final nonlinear response to cumulative stress (key effect)
    stress_penalty = cumulative_stress * 0.4
    final_yield = preliminary_yield - stress_penalty

    # Dead code path - never executed due to data
    if avg_ratio_change < -5 and len(flagged_intervals) > 20:
        final_yield *= 0.7

    return final_yield

# Environmental sensor readings over 10 days
temperature_data = [22, 24, 26, 28, 23, 27, 25, 24, 26, 25]
humidity_data = [58, 62, 55, 65, 59, 61, 60, 57, 63, 58]

# Core execution point
final_yield = calculate_optimal_yield(temperature_data, humidity_data)

print(f"Result: {final_yield}")