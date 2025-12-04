import itertools

def calculate_chemical_purity(compounds, threshold):
    # Process chemical compounds data
    base_compounds = [c for c in compounds if c > 0]
    impurities = [abs(c) for c in compounds if c < 0]
    
    # Calculate purity metrics
    purity_index = sum(base_compounds) - sum(impurities)
    normalized_purity = min(100, max(0, purity_index))
    
    # Track reactive elements (not used in final calculation)
    reactive_elements = [c % 5 for c in compounds]
    reaction_factor = sum(reactive_elements) / len(compounds) if compounds else 0
    
    # Perform permutation analysis (distraction)
    permutations = list(itertools.permutations(range(3)))
    permutation_count = len(permutations)
    
    # Calculate product yield based on threshold
    potential_yield = [c for c in base_compounds if c > threshold]
    discarded = [c for c in base_compounds if c <= threshold]
    
    # Apply catalyst effect (relevant calculation)
    catalyst_effect = 2 if normalized_purity > 75 else 1
    
    # Generate product sequence
    product = [p * catalyst_effect for p in potential_yield]
    
    # Apply secondary processing (distraction)
    secondary_process = [(p + reaction_factor) for p in product]
    
    # Calculate final yield
    filtered_sum = sum(product)
    
    return filtered_sum

# Test with sample data
compound_samples = [10, 15, -3, 20, -2, 8, 12, -1]
threshold_value = 9

# Some additional variables for logging (distraction)
lab_temperature = 22.5
process_id = "CP-" + str(len(compound_samples))
log_entry = f"Process {process_id} at {lab_temperature}°C"

# Calculate and print result
result = calculate_chemical_purity(compound_samples, threshold_value)
print(f"Result: {result}")