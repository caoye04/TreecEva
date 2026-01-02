def compute_overlap_and_differences():
    # Domain: sensor data analysis
    morning_readings = {105, 110, 115, 120, 125, 130, 135}
    evening_readings = {115, 120, 125, 140, 145, 150}
    
    # Find common readings (overlap)
    stable_readings = morning_readings & evening_readings
    
    # Identify unique fluctuations
    fluctuating_morning = morning_readings - stable_readings
    fluctuating_evening = evening_readings - stable_readings
    
    # Combine all fluctuating values into a single set
    all_fluctuations = fluctuating_morning | fluctuating_evening
    
    # Apply correction factor: increment each fluctuation by 5
    corrected_fluctuations = {x + 5 for x in all_fluctuations}
    
    # Final result set: union of stable readings and corrected fluctuations
    result_set = stable_readings | corrected_fluctuations
    
    # Compute sum of final result set
    result_set_sum = sum(result_set)
    
    # Print result for verification
    print(f"Result: {result_set_sum}")
    
    return result_set_sum

# Execute function
evaluate_result = compute_overlap_and_differences()