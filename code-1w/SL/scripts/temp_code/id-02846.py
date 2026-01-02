def analyze_system_load():
    # Simulate time-series power load data (in kW) over a day in 2-hour intervals
    base_loads = [12.5, 14.0, 18.2, 25.6, 30.1, 28.4, 22.7, 16.3]
    
    # Distractor: Temperature readings (not used in final calculation)
    temperatures = [22, 23, 25, 29, 32, 30, 27, 24]
    temp_factor = sum(t // 5 for t in temperatures if t > 25)  # Unused computation
    
    # Apply efficiency decay over time due to system wear
    efficiency_decay = [1.0 - (i * 0.03) for i in range(len(base_loads))]
    adjusted_loads = [base_loads[i] / efficiency_decay[i] for i in range(len(base_loads))]
    
    # Distractor: Redundant safety margin (computed but not critical)
    safety_margin = 1.15
    protected_loads = [load * safety_margin for load in adjusted_loads]  # Not used
    
    # Compute rolling 3-period average to smooth out transient spikes
    rolling_loads = []
    for i in range(2, len(adjusted_loads)):
        window_avg = sum(adjusted_loads[i-2:i+1]) / 3
        rolling_loads.append(round(window_avg, 3))
    
    # Introduce auxiliary index tracking for debugging (semi-relevant)
    index_map = {i: idx for i, idx in enumerate(range(len(rolling_loads)))}
    reverse_indices = [index_map[i] for i in sorted(index_map, reverse=True)]  # Unused
    
    # Key statement
    peak_capacity = max(rolling_loads)
    
    # Additional distractor: Attempt to normalize with unused reference
    normalization_base = adjusted_loads[0]
    normalized_peak = peak_capacity / normalization_base  # Irrelevant
    
    # Print result as required
    print(f"Result: {peak_capacity}")
    
    return peak_capacity

analyze_system_load()