import itertools

def calculate_fluid_dynamics():
    flow_rates = [12, 8, 15, 6, 10]
    container_heights = [3, 5, 2, 7, 4]
    
    # Relevant calculation: volume = flow_rate * height
    volumes = [rate * height for rate, height in zip(flow_rates, container_heights)]
    
    # Distractor: Processing that doesn't affect final result
    pressure_factors = [v * 0.1 for v in volumes]
    temperature_adjustments = [p + 2.5 for p in pressure_factors]
    
    # Relevant: Process volumes using itertools
    volume_combinations = itertools.combinations(volumes, 2)
    processed_data = []
    
    for combo in volume_combinations:
        # Distractor calculation that gets discarded
        thermal_effect = sum(combo) * 0.15
        
        # Relevant calculation: average of combination
        avg_volume = sum(combo) / 2
        processed_data.append(avg_volume)
        
        # Distractor: Additional processing not used
        density_variation = avg_volume * 1.2
    
    # Final relevant operation
    final_volume = processed_data[-1]
    print(f"Result: {final_volume}")
    return final_volume

calculate_fluid_dynamics()