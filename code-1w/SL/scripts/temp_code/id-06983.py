def calculate_optimal_yield(temps, humids):
    # Simulate agricultural yield prediction based on environmental factors
    base_yield = 100.0
    adjustment_factor = 0.0
    cumulative_stress = 0.0
    peak_stress = 0.0
    temp_deviation_sum = 0.0
    valid_days = 0

    # Irrelevant tracking variables (distractors)
    outlier_count = 0
    total_readings = len(temps)
    dummy_metric = sum([t ** 0.5 for t in temps if t > 0]) / len(temps)

    # Lambda to determine if a day is within optimal growth range
    is_optimal = lambda t, h: 20 <= t <= 30 and 40 <= h <= 70

    # Secondary lambda for stress penalty calculation
    stress_penalty = lambda t, h: max(0, abs(t - 25) * 0.5 + abs(h - 55) * 0.2)

    for i in range(len(temps)):
        temp = temps[i]
        humid = humids[i]

        # Track deviation from ideal temperature (semi-relevant)
        temp_deviation_sum += abs(temp - 25)

        if temp < 10 or temp > 40:
            outlier_count += 1
            continue  # Skip extreme temperature days

        if humid < 20 or humid > 90:
            continue  # Skip extreme humidity days

        # Only consider valid days for yield calculation
        valid_days += 1
        if is_optimal(temp, humid):
            adjustment_factor += 1.2
        else:
            penalty = stress_penalty(temp, humid)
            adjustment_factor -= min(penalty * 0.1, 0.8)

        daily_stress = stress_penalty(temp, humid)
        cumulative_stress += daily_stress
        if daily_stress > peak_stress:
            peak_stress = daily_stress

    # Dummy transformation (irrelevant to final yield)
    avg_temp_deviation = temp_deviation_sum / len(temps) if temps else 0
    stress_efficiency = (cumulative_stress / valid_days * 0.95) if valid_days > 0 else 0

    # Core yield computation (only this affects final answer)
    if valid_days == 0:
        net_yield = base_yield * 0.3
    else:
        net_adjustment = adjustment_factor / valid_days
        net_yield = base_yield * (0.7 + net_adjustment * 0.3)

    # Final yield adjusted by number of valid days
    final_yield = net_yield * (valid_days / len(temps)) if temps else 0

    return final_yield

# Environmental sensor data over 10-day period
temperature_data = [22, 25, 35, 28, 18, 24, 31, 26, 20, 33]
humidity_data = [50, 58, 85, 60, 30, 52, 75, 45, 38, 88]

# Execute main computation
final_yield = calculate_optimal_yield(temperature_data, humidity_data)
print(f"Result: {final_yield}")