import itertools

# Weather data analysis for crop yield optimization
def analyze_rainfall_patterns(measurements):
    # Historical thresholds (not all used)
    historical_min = 15.75
    historical_max = 120.25
    default_threshold = 45.5
    
    # Process measurements
    valid_measurements = [(day, amount) for day, amount in measurements if amount > 0]
    
    # Calculate some statistics that aren't directly used
    total_rainfall = sum(amount for _, amount in valid_measurements)
    average_rainfall = total_rainfall / len(valid_measurements) if valid_measurements else 0
    
    # Generate some auxiliary data
    seasonal_factors = [(i, 0.8 + 0.05 * i) for i in range(1, 5)]
    adjustment_values = list(itertools.accumulate([2.5, 1.5, 3.0, 2.0]))
    
    # Apply filters to find optimal rainfall threshold
    preliminary_data = [(day, amount) for day, amount in valid_measurements 
                       if historical_min <= amount <= historical_max]
    
    # This sorting is important for the final result
    sorted_data = sorted(preliminary_data, key=lambda x: x[1])
    
    # Calculate a weighting factor (not used in final result)
    weight_factor = adjustment_values[-1] / len(seasonal_factors) if seasonal_factors else 1.0
    
    # Apply additional processing
    filtered_data = [(day, amount) for day, amount in sorted_data 
                    if day % 2 == 0 and amount >= default_threshold]
    
    # Determine optimal threshold
    optimal_threshold = filtered_data[-1][1] if filtered_data else default_threshold
    
    # Some additional calculations that don't affect the result
    potential_yield = optimal_threshold * weight_factor / 2
    risk_factor = (historical_max - optimal_threshold) / historical_max
    
    print(f"Result: {optimal_threshold}")
    return optimal_threshold

# Sample data: (day, rainfall_amount)
measurements = [(1, 30.5), (2, 62.5), (3, 10.2), (4, 45.5), 
                (5, 85.0), (6, 70.0), (7, 5.5), (8, 55.5)]

result = analyze_rainfall_patterns(measurements)