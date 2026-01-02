def calculate_efficiency(data):
    base_efficiency = 85.0
    adjustment_factor = 0.9
    
    # Extract performance metrics using enumerate and apply dynamic corrections
    corrected_metrics = [
        metric * (adjustment_factor + index * 0.05) 
        for index, metric in enumerate(data)
    ]
    
    # Secondary filter: only consider values above threshold using lambda
    valid_metrics = list(filter(lambda x: x > 75, corrected_metrics))
    
    # Final efficiency calculation
    if valid_metrics:
        energy_output = sum(valid_metrics) / len(valid_metrics)
    else:
        energy_output = base_efficiency
    
    return energy_output

# Simulated sensor readings from turbine array
turbine_readings = [80, 70, 90, 60]

# Irrelevant variable (minor distraction, intervention level 5)
status_flags = [True, False, True]

energy_output = calculate_efficiency(turbine_readings)
print(f"Result: {energy_output}")