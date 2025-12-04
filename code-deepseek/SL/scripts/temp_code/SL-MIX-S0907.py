def calculate_efficiency(sensor_readings):
    # Process sensor data for efficiency analysis
    initial_readings = [reading * 2.5 for reading in sensor_readings]
    processed_data = [(idx, val * 0.8 + 15) for idx, val in enumerate(initial_readings)]
    
    # Calculate base efficiencies (distractor - not used in final result)
    base_efficiencies = [data[1] * 0.9 for data in processed_data]
    
    # Filter and rank valid efficiencies
    efficiency_threshold = 25.0
    valid_efficiencies = [data for data in processed_data if data[1] > efficiency_threshold]
    
    # Create efficiency tuples with adjustment factors
    adjustment_factors = [0.85, 1.2, 0.95, 1.1, 1.05]
    efficiency_tuples = []
    
    for i, data in enumerate(valid_efficiencies):
        if i < len(adjustment_factors):
            adjusted_value = data[1] * adjustment_factors[i]
            efficiency_tuples.append((data[0], adjusted_value))
    
    # Intermediate calculation that doesn't affect final result
    avg_efficiency = sum([eff[1] for eff in efficiency_tuples]) / len(efficiency_tuples) if efficiency_tuples else 0
    
    # Select final efficiency based on highest adjusted value
    filtered_efficiencies = [eff for eff in efficiency_tuples if eff[1] > 28]
    final_efficiency = max(filtered_efficiencies, key=lambda x: x[1])[0]
    
    print(f"Result: {final_efficiency}")

# Main execution
sensor_data = [12, 8, 15, 6, 20]
calculate_efficiency(sensor_data)