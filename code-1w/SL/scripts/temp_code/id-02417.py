import math

def simulate_growth(base_rate, inhibitors, enhancers):
    # Simulate plant growth with environmental factors
    raw_growth = base_rate * (1 + sum(enhancers) - sum(inhibitors))
    adjusted_growth = max(raw_growth, 0.1)
    return adjusted_growth

def compute_stress_index(values):
    # Compute a red-herring stress metric (not used in final result)
    mean_val = sum(values) / len(values)
    variance = sum((x - mean_val) ** 2 for x in values) / len(values)
    return math.sqrt(variance) if variance > 0 else 0

def normalize_vector(vec):
    # Normalize for numerical stability (semi-relevant)
    norm = math.sqrt(sum(x ** 2 for x in vec))
    return [x / norm for x in vec] if norm != 0 else vec

def calculate_potential(conditions):
    # Calculate growth potential using list comprehension
    multipliers = [1.2 if c > 25 else 0.8 for c in conditions]
    base_potential = 100
    for m in multipliers:
        base_potential *= m
    return base_potential

def harvest_results(exposures, stresses):
    # Core logic: combine exposure and stress effects
    filtered_exposures = [e for e in exposures if e > 10]
    total_exposure = sum(filtered_exposures)
    
    # Irrelevant transformation
    inverted_stresses = [1 / s if s != 0 else 0 for s in stresses]
    avg_inverted = sum(inverted_stresses) / len(inverted_stresses)
    
    # Key computation chain
    scaling_factor = 0.5 if avg_inverted > 0.3 else 0.7
    intermediate_yield = total_exposure * scaling_factor
    
    # Apply diminishing returns
    if intermediate_yield > 200:
        intermediate_yield = 200 + (intermediate_yield - 200) * 0.3
    
    # Final adjustment based on count of high-stress events
    high_stress_count = sum(1 for s in stresses if s > 0.6)
    penalty = high_stress_count * 8
    final_yield = int(intermediate_yield - penalty)
    
    return final_yield

# Main execution block
if __name__ == "__main__":
    # Environmental sensor readings (hypothetical)
    light_exposure = [8, 15, 22, 30, 40, 5]
    temperature_readings = [22, 28, 35, 19, 27]
    soil_moisture = [0.4, 0.6, 0.3, 0.7]
    
    # Control variables
    baseline_rate = 0.9
    blockers = [0.1, 0.05]
    promoters = [0.08, 0.12]
    
    # Distractor computations
    growth_prediction = simulate_growth(baseline_rate, blockers, promoters)
    stress_metric = compute_stress_index(soil_moisture)
    normalized_light = normalize_vector(light_exposure)
    potential_score = calculate_potential(temperature_readings)
    
    # Critical data for answer
    exposure_levels = [x * 2 for x in light_exposure]  # Amplified exposure
    stress_factors = [0.5, 0.7, 0.8, 0.4]  # Measured stress levels
    
    # Execute key statement
    final_yield = harvest_results(exposure_levels, stress_factors)
    
    # Output result
    print(f"Result: {final_yield}")