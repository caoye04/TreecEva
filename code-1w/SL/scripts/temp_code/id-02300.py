def analyze_growth_factors(conditions):
    growth_score = 0
    stress_penalty = 0
    for factor, value in conditions.items():
        if factor == 'temperature':
            growth_score += max(0, 30 - abs(value - 25))
            stress_penalty += abs(value - 25) * 0.1
        elif factor == 'humidity':
            growth_score += min(value / 2, 15)
        elif factor == 'light_exposure':
            growth_score += value * 0.3
    return growth_score, stress_penalty

soil_quality = {
    'ph': 6.5,
    'nitrogen': 80,
    'moisture': 45
}

# Simulate seasonal climate fluctuations
climate_data = [
    {'temperature': 22, 'humidity': 60, 'light_exposure': 8},
    {'temperature': 26, 'humidity': 55, 'light_exposure': 9},
    {'temperature': 24, 'humidity': 70, 'light_exposure': 7},
    {'temperature': 28, 'humidity': 50, 'light_exposure': 10}
]

baseline_adjustment = sum([abs(soil_quality[k] - v) 
                            for k, v in {'ph': 6.0, 'nitrogen': 100, 'moisture': 50}.items()])

irrelevant_trend_projection = [round((i + 1) * 1.5 + 0.7 * i**2, 2) for i in range(12)]
dummy_counter = 0
for x in irrelevant_trend_projection:
    if x > 50 and dummy_counter < 5:
        dummy_counter += 1

aggregate_stress = 0
normalized_gains = []

for entry in climate_data:
    score, penalty = analyze_growth_factors(entry)
    normalized_gains.append(max(0, score - baseline_adjustment * 0.3))
    aggregate_stress += penalty

# Misleading intermediate transformation
transformed_gains = [g * 1.2 for g in normalized_gains if g > 10]
temp_deviation_index = sum([abs(entry['temperature'] - 25) for entry in climate_data])

# Dummy tracking variables
tracking_log = []
for i, gain in enumerate(normalized_gains):
    status = 'OPTIMAL' if gain >= 12 else 'SUBOPTIMAL'
    tracking_log.append({'day': i+1, 'status': status})

# Core calculation disguised among distractors
def calculate_harvest_potential(climate_inputs, soil_profile):
    base_yield = 0
    efficiency_factor = (soil_profile['nitrogen'] * 0.01) * (soil_profile['moisture'] * 0.02)
    
    # Hidden critical logic using list comprehension and conditional expression
    daily_potentials = [
        (entry['humidity'] * 0.1) + (entry['light_exposure'] * 0.4)
        if entry['temperature'] >= 24 else 
        (entry['humidity'] * 0.05) + (entry['light_exposure'] * 0.2)
        for entry in climate_inputs
    ]
    
    adjusted_potential = sum(daily_potentials) * efficiency_factor
    
    # Use of conditional expression with misleading fallback
    final_estimate = adjusted_potential if adjusted_potential > 0 else 0.0
    
    # Dead code branch (never executed due to data)
    if temp_deviation_index < 0:
        final_estimate *= 0.8  # This line is unreachable
    
    return final_estimate

# Key assignment statement
final_yield = calculate_harvest_potential(climate_data, soil_quality)

# Print result as required
print(f"Result: {final_yield}")