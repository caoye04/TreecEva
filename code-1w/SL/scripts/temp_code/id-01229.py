def calculate_system_metrics():
    base_temperatures = [22, 25, 19, 24, 27]
    adjustment_factors = [1.5, -0.8, 2.1, -1.0, 0.5]
    
    # Compute adjusted efficiency scores using list comprehension
    efficiency_scores = [int(temp + adj) for temp, adj in zip(base_temperatures, adjustment_factors)]
    
    # Irrelevant diagnostic variable (minor distraction)
    diagnostic_flag = len(base_temperatures) > 3
    
    # Key computation step
    thermal_capacity = sum(efficiency_scores) // len(efficiency_scores)
    
    # Additional unrelated metric (minimal interference)
    peak_efficiency = max(efficiency_scores)
    
    # Output the target result
    print(f"Result: {thermal_capacity}")

# Execute function
calculate_system_metrics()