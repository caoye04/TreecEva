def calculate_energy_profile():
    base_load = [120, 135, 150, 160, 180, 200, 190, 175, 160, 140]
    peak_threshold = 170
    
    # Identify peak usage period
    peak_periods = [i for i, load in enumerate(base_load) if load > peak_threshold]
    peak_index = peak_periods[0] if peak_periods else len(base_load)//2
    
    # Adjust loads with efficiency factor
    efficiency_factor = 0.9
    adjusted_loads = [load * efficiency_factor for load in base_load]
    
    # Calculate residual energy after peak
    residual_loads = [load - 50 for load in adjusted_loads]
    
    # Key computation point
    energy_capacity = residual_loads[peak_index:] and sum(residual_loads[peak_index:])
    
    # Irrelevant auxiliary variable (minor distraction)
    avg_load = sum(base_load) / len(base_load)
    
    print(f"Result: {energy_capacity}")

calculate_energy_profile()