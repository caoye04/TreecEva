def calculate_solution_concentration():
    # Chemical solution analysis
    initial_mixture = "75% ethanol, 15% water, 10% impurities"
    components = initial_mixture.split(", ")
    
    # Extract ethanol percentage (distractor: processing all components)
    ethanol_data = components[0].replace("%", "").split(" ")
    water_data = components[1].replace("%", "").split(" ")
    impurity_data = components[2].replace("%", "").split(" ")
    
    ethanol_percentage = int(ethanol_data[0])
    water_percentage = int(water_data[0])
    impurity_percentage = int(impurity_data[0])
    
    # Purification process calculations
    total_volume = 200
    purification_factor = 1.25
    
    # Calculate active substance after purification
    active_substance = (ethanol_percentage / 100) * total_volume * purification_factor
    
    # Additional calculations (distractors)
    total_solvent = water_percentage + ethanol_percentage
    waste_volume = (impurity_percentage / 100) * total_volume
    efficiency_ratio = ethanol_percentage / (ethanol_percentage + water_percentage)
    
    # Purification quality check
    purity_threshold = 0.8
    actual_purity = ethanol_percentage / 100
    purity_check = actual_purity > purity_threshold
    
    # Final concentration calculation
    total_solution = total_volume - waste_volume
    final_concentration = active_substance / total_solution if purity_check else 0
    
    print(f"Target result: {final_concentration}")

calculate_solution_concentration()