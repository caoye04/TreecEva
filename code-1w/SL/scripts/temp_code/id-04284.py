def analyze_growth_factor(temp, rainfall):
    # Auxiliary calculation with partial relevance
    base_factor = temp * 0.8 if temp > 20 else temp * 0.5
    bonus = 1.2 if rainfall > 80 else 1.0
    penalty = 0.7 if rainfall < 40 else 1.0
    return base_factor * bonus * penalty

# Simulate agricultural yield across regions
temperature_readings = [22, 19, 25, 18]
rainfall_stats = [85, 35, 95, 45]
soil_quality_index = [7, 6, 8, 5]  # Not used in final computation (distractor)
unused_buffer = [0] * 10  # Dead code element for interference

region_data = {}
for i in range(4):
    key = f'region_{i}'
    region_data[key] = {
        'temp': temperature_readings[i],
        'rain': rainfall_stats[i],
        'soil': soil_quality_index[i]
    }

# Secondary tracking variables (some irrelevant)
total_assessments = 0
irrelevant_sum = 0
for record in region_data.values():
    if record['temp'] > 20:
        irrelevant_sum += record['soil']  # Distractor: accumulates unused data
    total_assessments += 1

# Core logic hidden among auxiliary operations
def calculate_harvest_potential(data):
    cumulative_score = 0
    adjustment_factor = 0
    
    for k, v in data.items():
        # Relevant conditional expression
        growth_multiplier = 1.5 if v['rain'] > 70 else 0.9
        
        # Actual contribution to result
        raw_yield = v['temp'] * growth_multiplier
        
        # Intermediate distraction
        hypothetical_max = v['temp'] * 1.8  # Unused in final path
        deviation = hypothetical_max - raw_yield  # Computed but irrelevant
        
        # Only this contributes to final result
        if v['temp'] >= 20:
            adjustment_factor += 2
        else:
            adjustment_factor -= 1
        
        cumulative_score += raw_yield
    
    # Final computation uses only cumulative_score and adjustment_factor
    final_component = cumulative_score + adjustment_factor * 3.5
    return int(final_component)  # Deterministic integer result

# Execution point of interest
final_yield = calculate_harvest_potential(region_data)

# Print result as required
print(f"Target result: {final_yield}")