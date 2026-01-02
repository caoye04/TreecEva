def calculate_agricultural_yield():
    # Real parameters
    base_area = 250
    growth_rate = 1.08
    season_factor = 0.95
    pest_loss = 0.03
    rainfall_bonus = 0.07

    # Distractor variables - irrelevant to final result
    market_price = 4.15
    labor_cost = 120
    fuel_consumption = 18.3
    dummy_metric_1 = market_price * labor_cost
    dummy_metric_2 = fuel_consumption ** 2

    # Simulated monthly growth with environmental factors
    monthly_values = []
    current_growth = base_area
    for month in range(1, 13):
        current_growth *= growth_rate
        if month == 5:
            current_growth *= season_factor  # Spring peak adjustment
        if month == 8:
            current_growth *= (1 - pest_loss)  # Summer pest impact
        if month == 10:
            current_growth *= (1 + rainfall_bonus)  # Autumn rain benefit
        monthly_values.append(current_growth)

    # Distractor: unused transformation
    inverted_values = [base_area / max(v, 1) for v in monthly_values]
    smoothed_data = [sum(monthly_values[i:i+3]) / 3 for i in range(10)]

    # Key intermediate computation
    total_accumulated = sum(monthly_values)
    peak_month_index = monthly_values.index(max(monthly_values))

    # Distractor: dead code path
    if peak_month_index < 0:
        fallback_value = base_area * (growth_rate ** 12)
        total_accumulated = fallback_value

    # Efficiency model based on variance
    mean_val = total_accumulated / 12
    variance = sum((x - mean_val) ** 2 for x in monthly_values) / 12
    stability_score = (1 - (variance / (mean_val ** 2))) * 100

    # Unused diagnostic metrics
    risk_level = 'high' if variance > 5000 else 'moderate'
    dummy_diagnostic = f'Stability: {stability_score:.1f}, Risk: {risk_level}'

    # Core logic chain
    normalized_peak = max(monthly_values) / base_area
    adjustment_curve = [normalized_peak ** (1/12) for _ in range(12)][0]
    adjusted_production = total_accumulated * adjustment_curve * 0.88

    # Conditional efficiency factor
    if stability_score > 85:
        efficiency_factor = 1.12
    elif stability_score > 75:
        efficiency_factor = 1.05
    else:
        efficiency_factor = 0.93  # This will be overridden below

    # Final override based on logical condition (will evaluate to True)
    efficiency_factor = 1.05 if (pest_loss < 0.05 and rainfall_bonus > 0.05) else 0.98

    # Critical assignment - target of question
    final_yield = adjusted_production * efficiency_factor

    # Distractor: redundant print statements
    debug_info = {"peak": max(monthly_values), "months": len(monthly_values)}
    _ = [print(f'DEBUG: {k}={v}') for k, v in debug_info.items() if False]  # No output

    # Output required result
    print(f"Target result: {final_yield}")
    return final_yield

# Execute function
result = calculate_agricultural_yield()