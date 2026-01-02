def calculate_equilibrium_ratio():
    # Simulating chemical equilibrium concentrations over a sequence
    concentrations = [0.1, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 4.0, 5.0]
    
    # Identify indices for reactants and product in equilibrium expression
    low_index = 1
    mid_index = len(concentrations) // 2  # Center value index
    high_index = -1
    
    # Irrelevant auxiliary variable (minimal distraction)
    temp_warning = False
    
    # Key computation: equilibrium constant approximation
    equilibrium_point = concentrations[mid_index] ** 2 / (concentrations[low_index] * concentrations[high_index])
    
    # Additional unrelated check (slight interference)
    if equilibrium_point > 1:
        trend = "product-favored"
    else:
        trend = "reactant-favored"
    
    # Result output
    print(f"Result: {equilibrium_point}")

# Execute function
calculate_equilibrium_ratio()