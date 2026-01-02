def analyze_stability(data):
    if len(data) < 3:
        return 0
    
    # Extract core segment for analysis (slicing)
    core_segment = data[1:-1]
    accumulation = 0
    equilibrium_point = 0
    
    for i, value in enumerate(core_segment):
        adjusted_value = value - data[i]  # Compare with original frame
        accumulation += adjusted_value
        
        # Early termination if system stabilizes
        if abs(accumulation) < 1e-5:
            equilibrium_point = i + 1
            break
    
    # Irrelevant auxiliary calculation (minor interference)
    temp_correction = sum(data) / len(data) if data else 0
    
    return equilibrium_point

# Simulated sensor readings over time
data_stream = [1.0, 1.2, 1.4, 1.6, 1.6, 1.6, 1.8, 2.0]

# Main computation
stability_data = data_stream[:6]  # Focus on initial stabilization phase
equilibrium_point = analyze_stability(stability_data)
print(f"Result: {equilibrium_point}")