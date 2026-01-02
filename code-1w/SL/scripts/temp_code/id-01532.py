def calculate_system_efficiency():
    temperatures = [22, 24, 28, 30, 26, 23]
    base_output = 150
    efficiency_scores = []
    
    for temp in temperatures:
        if temp < 25:
            efficiency = base_output * 0.9
        elif temp >= 30:
            efficiency = base_output * 0.75
        else:
            efficiency = base_output * 0.85
        efficiency_scores.append(round(efficiency, 2))
    
    # Additional computation to derive final metric
    average_efficiency = sum(efficiency_scores) / len(efficiency_scores)
    peak_efficiency = max(efficiency_scores)
    min_efficiency = min(efficiency_scores)
    efficiency_variance = peak_efficiency - min_efficiency
    
    # Output result
    print(f"Result: {peak_efficiency}")
    
    return peak_efficiency

# Execute function
calculate_system_efficiency()