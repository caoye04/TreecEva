def evaluate_performance(output, risk):
    base_efficiency = 85
    adjustment_factor = 0.9
    
    # Irrelevant health metrics (distractor)
    heart_rate = 72
    stress_level = "moderate"
    calories_burned = 230

    # Real computation begins
    normalized_output = output / 100.0
    scaled_risk = risk * 1.5 if risk > 0.5 else risk * 0.7
    
    # Lambda for dynamic threshold (useful)
    threshold_func = lambda x: 0.8 if x > 1.0 else 0.6
    performance_boost = 1.2 if normalized_output > threshold_func(scaled_risk) else 1.0
    
    # Intermediate score with adjustment
    intermediate_score = (base_efficiency + (normalized_output * 10)) * performance_boost
    
    # Misleading bonus path (dead code - never taken due to logic)
    bonus_applied = False
    if output > 200 and risk < 0.3:
        intermediate_score += 10
        bonus_applied = True  # This is never reached in current input
    
    # Final adjustment using slicing on a generated sequence (semi-relevant)
    history_data = [intermediate_score - i*2 for i in range(5)]
    recent_trend = history_data[-3:]  # Last three values
    trend_correction = sum(recent_trend) / len(recent_trend) * 0.05
    
    final_value = intermediate_score + trend_correction
    return int(final_value)

# Simulated inputs
productivity = 120
risk_factor = 0.6

# Key execution point
final_score = evaluate_performance(productivity, risk_factor)
print(f"Result: {final_score}")