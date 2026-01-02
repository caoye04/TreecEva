def analyze_growth_patterns(temperatures, rainfall, soil_ph):
    # Irrelevant analysis: pH trend (not used in final result)
    ph_trend = 'stable' if all(6.0 <= ph <= 7.0 for ph in soil_ph) else 'variable'
    
    # Distractor: unused growth prediction model
    predicted_growth = sum(t * 0.5 + r * 0.3 for t, r in zip(temperatures, rainfall))
    
    # Relevant: count optimal growing days
    optimal_days = [
        i for i in range(len(temperatures))
        if temperatures[i] >= 20 and rainfall[i] >= 30 and 6.5 <= soil_ph[i] <= 6.8
    ]
    
    # Early return red herring (never triggered in this input)
    if len(optimal_days) == 0:
        return 0.0
    
    # Compute average temp during optimal days
    avg_temp_during_optimal = sum(temperatures[i] for i in optimal_days) / len(optimal_days)
    
    # Compute cumulative rainfall in first half of season
    mid_point = len(rainfall) // 2
    cumulative_rain_first_half = sum(rainfall[:mid_point])  # Not used later
    
    # Helper function for efficiency calculation
    def calculate_harvest_efficiency(days, base_yield=100):
        scaling_factor = 1.0
        if len(days) > 5:
            scaling_factor += 0.2
        elif len(days) > 3:
            scaling_factor += 0.1
        
        # Efficiency depends on length of optimal period
        base = base_yield * scaling_factor
        penalty = 0.05 * (len(temperatures) - len(days))  # artificial penalty
        return base - penalty
    
    # Additional distractor: simulate pest risk based on temperature spikes
    spike_days = [t for t in temperatures if t > 35]
    pest_risk_score = len(spike_days) * 1.5  # Computed but not used
    
    # Key computation
    intermediate_yield = calculate_harvest_efficiency(optimal_days)
    adjustment = avg_temp_during_optimal * 0.1
    final_yield = int(intermediate_yield + adjustment)
    
    # Print result as required
    print(f"Result: {final_yield}")
    
    # Return unused metrics to increase cognitive load
    return {
        'final_yield': final_yield,
        'pest_risk': pest_risk_score,
        'ph_status': ph_trend
    }

# Input data
temps = [22, 25, 19, 36, 24, 26, 28, 37, 21, 23]
rains = [45, 50, 10, 5, 40, 60, 55, 0, 30, 35]
ph_levels = [6.7, 6.6, 7.1, 6.9, 6.5, 6.7, 6.8, 7.0, 6.4, 6.6]

# Execute function
def main():
    result = analyze_growth_patterns(temps, rains, ph_levels)

main()