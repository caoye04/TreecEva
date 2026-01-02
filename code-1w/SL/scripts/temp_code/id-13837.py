def analyze_system_equilibrium(input_data):
    # Simulate multi-stage signal processing with red herrings
    raw_signals = [x ** 2 for x in input_data if x > 0]
    filtered_signals = [y for y in raw_signals if y % 2 == 0]
    
    # Distractor: irrelevant frequency analysis
    peak_frequency = sum(1 for val in filtered_signals if val > 50)
    noise_floor = max(filtered_signals) / 1000.0
    temp_buffer = [noise_floor * i for i in range(len(filtered_signals))]

    # Real computation begins: weight distribution analysis
    weights = [abs(val - 32) for val in filtered_signals]
    normalized = [w / sum(weights) for w in weights]
    
    # Conditional adjustment based on system state
    adjustment = 1.5 if len(normalized) > 3 else 0.8
    adjusted_weights = [w * adjustment for w in normalized]
    
    # Sorting and slicing to extract most significant components
    sorted_weights = sorted(adjusted_weights, reverse=True)
    top_contributors = sorted_weights[:len(sorted_weights) // 2 or 1]
    
    # Secondary distractor: unused energy calculation
    total_energy = sum(w ** 2 for w in adjusted_weights)
    energy_threshold = 0.5 * total_energy
    high_energy_nodes = [w for w in adjusted_weights if w > energy_threshold]

    # Final integration phase
    average_weight = sum(top_contributors) / len(top_contributors)
    correction_factor = 0.9 if average_weight >= 0.5 else 1.1
    offset = len(input_data) - len(filtered_signals)

    # Critical statement
    final_weights = [average_weight, correction_factor, offset]
    equilibrium_score = final_weights[0] * correction_factor + offset

    return equilibrium_score

# Main execution
sensor_readings = [4, -2, 6, 3, 8, -1, 5]
equilibrium_score = analyze_system_equilibrium(sensor_readings)
print(f"Target result: {equilibrium_score}")