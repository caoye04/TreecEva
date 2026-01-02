def calculate_performance(base, data):
    adjustment_factor = 0.85
    penalty_rate = 0.12
    
    # Irrelevant transformation (distractor)
    transformed = list(map(lambda x: (x ** 0.5) * 1.5, data))
    
    # Real processing path
    filtered = [x for x in data if x > base * 0.75]
    
    # Secondary distractor: unused smoothing logic
    smooth_op = lambda val: val * 0.9 if val > base else val * 1.1
    smoothed_values = [smooth_op(v) for v in data]  # Computed but not used
    
    # Accumulate valid deviations
    deviation_sum = 0
    count = 0
    for reading in filtered:
        if reading > base:
            deviation_sum += (reading - base) * adjustment_factor
        elif reading < base:
            deviation_sum -= (base - reading) * penalty_rate
        count += 1
        
        # Early termination red herring (never triggers under this input)
        if deviation_sum < -1000:
            return -1
    
    # Auxiliary metric (not used in final result)
    avg_deviation = deviation_sum / count if count > 0 else 0
    volatility_index = sum(1 for x in data if abs(x - base) > base * 0.2)
    
    # Final score computation
    stability_bonus = 10 if volatility_index < 5 else 0
    final_score = int(deviation_sum + stability_bonus)
    
    return final_score

# Initial setup
baseline = 42
readings = [38, 45, 40, 50, 35, 48, 41, 44, 39, 52]

# Key execution point
final_score = calculate_performance(baseline, readings)
print(f"Result: {final_score}")