def calculate_energy_output():
    base_loads = [120, 85, 95, 76, 134, 67]
    peak_threshold = 90
    processed_loads = [load * 1.1 for load in base_loads if load > peak_threshold]
    
    # Irrelevant auxiliary calculation (minor distraction)
    avg_load = sum(base_loads) / len(base_loads)
    normalized_values = [round(x / avg_load, 2) for x in base_loads]
    
    efficiency_factor = 0.93
    total_energy = sum(processed_loads[1:4]) * efficiency_factor
    
    # Print result as required
    print(f"Result: {total_energy}")
    
    return total_energy

# Execute function
calculate_energy_output()