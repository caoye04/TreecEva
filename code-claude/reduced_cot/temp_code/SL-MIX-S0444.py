from collections import Counter
import itertools

def analyze_crop_data(rainfall_data, soil_types, crop_yields):
    # Calculate some statistics on rainfall (not directly used for final result)
    rain_stats = Counter(rainfall_data)
    most_common_rain = rain_stats.most_common(1)[0][0]
    
    # Generate combinations of soil types (distraction)
    soil_combinations = list(itertools.combinations(soil_types, 2))
    soil_pairs = len(soil_combinations)
    
    # Process crop yields based on conditions
    threshold = sum(rainfall_data) / len(rainfall_data) * 0.8
    adjustment_factor = 1.5 if most_common_rain > 75 else 0.9
    
    # Apply various transformations to yields
    adjusted_yields = []
    filtered_yields = []
    
    for i, yield_value in enumerate(crop_yields):
        # Apply soil type modifier (distraction calculation)
        soil_modifier = (i % 3) * 0.1
        
        # Complex adjustment based on rainfall
        rain_effect = rainfall_data[i % len(rainfall_data)] / 100
        
        # These calculations don't affect final answer
        theoretical_yield = yield_value * (1 + soil_modifier) * rain_effect
        adjusted_yield = yield_value * adjustment_factor
        
        adjusted_yields.append(adjusted_yield)
        
        # Only keep yields above threshold
        if rainfall_data[i % len(rainfall_data)] > threshold:
            filtered_yields.append(yield_value)
    
    # Calculate highest yield from filtered list
    highest_yield = max(filtered_yields)
    
    # Calculate average yield (distraction)
    avg_yield = sum(adjusted_yields) / len(adjusted_yields)
    
    return highest_yield, avg_yield

# Input data
rainfall_data = [65, 82, 73, 91, 68]
soil_types = ['clay', 'loam', 'sandy']
crop_yields = [120, 145, 135, 160, 125]

# Run analysis
highest, average = analyze_crop_data(rainfall_data, soil_types, crop_yields)
print(f"Result: {highest}")