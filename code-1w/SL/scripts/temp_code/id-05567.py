def compute_efficiency():
    components = ['valve', 'pump', 'filter', 'compressor', 'regulator']
    readings = [104, 203, 156, 98, 215]
    
    # Irrelevant transformation: frequency mapping (not used in final calculation)
    freq_map = {k: v % 50 for k, v in zip(components, readings)}
    adjusted_readings = [r * 0.95 if r > 150 else r * 1.05 for r in readings]
    
    # Distractor: unused smoothing function
    def smooth(x):
        return [0.8 * x[i] + 0.2 * x[i-1] if i > 0 else x[0] for i in range(len(x))]
    smoothed = smooth(adjusted_readings)
    
    # Actual relevant logic starts here
    valid_indices = [i for i, r in enumerate(readings) if r >= 100]
    filtered_components = [components[i] for i in valid_indices]
    total_output = sum(readings[i] for i in valid_indices)
    
    # Simulated cycle time based on component count
    base_cycle = len(filtered_components)
    overhead = 0
    for i in range(base_cycle):
        if i % 2 == 0:
            overhead += 1.5
    cycle_time = base_cycle + overhead
    
    # Key computation
    efficiency_score = total_output / (cycle_time * 2.5)
    
    # Print result as required
    print(f"Result: {efficiency_score}")
    
    # Additional red herring: entropy-like calculation not affecting result
    import math
    if total_output > 0:
        entropy = -sum((r / total_output) * math.log(r / total_output) for r in readings if r > 0)
    
    return efficiency_score

compute_efficiency()