def analyze_growth_cycle(temperature_data, rainfall_data):
    # Irrelevant transformation (distractor)
    normalized_temps = [(t - 20) ** 2 for t in temperature_data]
    total_rainfall = sum(rainfall_data)
    
    # Semi-relevant preprocessing
    adjusted_rainfall = [r * 1.2 for r in rainfall_data if r > 5]
    avg_adjusted_rain = sum(adjusted_rainfall) / len(adjusted_rainfall) if adjusted_rainfall else 0
    
    # Core logic masked by noise
    peak_temp_count = len([t for t in temperature_data if t >= 30])
    stress_days = len([t for t in temperature_data if t < 15 or t > 35])
    
    # Misleading efficiency calculation (dead-end)
    false_efficiency = (avg_adjusted_rain + peak_temp_count) / (stress_days + 1) * 0.8
    
    # Actual yield factors
    base_yield = 0
    for i, temp in enumerate(temperature_data):
        if 20 <= temp <= 30:
            contribution = 5 if i < len(rainfall_data) and rainfall_data[i] > 10 else 3
            base_yield += contribution
    
    # Secondary factor: consecutive optimal days
    optimal_streak = 0
    max_streak = 0
    for temp in temperature_data:
        if 22 <= temp <= 28:
            optimal_streak += 1
            max_streak = max(max_streak, optimal_streak)
        else:
            optimal_streak = 0
    
    # Final computation buried in distractions
    bonus_multiplier = 1.5 if max_streak >= 3 else 1.0
    penalty = 0.9 if stress_days > 4 else 1.0
    
    final_yield = int(base_yield * bonus_multiplier * penalty)
    
    # Print required output
    print(f"Result: {final_yield}")
    return final_yield

# Simulated sensor data from agricultural field
temps = [25, 27, 23, 31, 28, 26, 24, 33, 22, 20]
rains = [12, 15, 8, 0, 18, 20, 5, 3, 10, 14]

# Invoke function
result = analyze_growth_cycle(temps, rains)