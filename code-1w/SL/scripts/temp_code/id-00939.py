from collections import defaultdict
import math

# Simulate agricultural yield optimization with environmental constraints
def preprocess_soil_metrics(raw_readings):
    processed = defaultdict(float)
    adjustment_factor = 1.08
    
    for key, value in raw_readings.items():
        if 'ph' in key:
            processed['acidity'] += (7.0 - value) * adjustment_factor
        elif 'moisture' in key:
            processed['hydration'] += max(value, 0.1)
        elif 'nutrient' in key:
            processed['fertility'] += math.log(value + 1)
    
    # Irrelevant transformation (distractor)
    temp_score = sum(processed.values()) * 0.92
    normalized = {k: v / (temp_score + 1e-5) for k, v in processed.items()}
    return normalized

def evaluate_stress_conditions(climate_log):
    stress_index = 0
    extreme_events = 0
    
    for record in climate_log:
        temp_anomaly = abs(record['temp'] - 22.5)
        wind_impact = record.get('wind', 0) * 0.3
        
        if temp_anomaly > 10:
            stress_index += temp_anomaly * 0.6
            extreme_events += 1
        
        if record.get('precip', 0) > 30:
            stress_index += 2  # Heavy rain stress
        
        # Distractor computation - not used later
        hypothetical_risk = (wind_impact + temp_anomaly) / (extreme_events + 1)
    
    # Additional unused path
    if extreme_events == 0:
        stress_index *= 0.85
    
    return stress_index

# Main calculation with conditional logic and lambda filtering
def calculate_harvest_efficiency(fields, settings):
    base_efficiency = settings.get('base_yield', 5.0)
    technology_boost = settings.get('tech_level', 1) * 0.15
    total_yield = 0
    
    # Real processing starts here
    for field_id, data in fields.items():
        soil_health = preprocess_soil_metrics(data['readings'])
        environment_stress = evaluate_stress_conditions(data['climate'])
        
        # Core formula components
        fertility_score = soil_health.get('fertility', 0) * 1.2
        hydration_balance = max(soil_health.get('hydration', 0), 0.5)
        
        # Conditional efficiency boost
        efficiency_modifier = (lambda x: x * 1.25 if x > 2 else x * 0.9)(fertility_score)
        
        # Primary yield calculation
        field_potential = base_efficiency\
            * (1 + technology_boost)\
            * efficiency_modifier\
            * (0.85 + hydration_balance * 0.1)
        
        # Stress reduction (real impact)
        field_potential *= max(0.4, (1 - environment_stress * 0.05))
        
        # Dead code branch - misleading control flow
        if False and field_potential > 10:
            field_potential = 10  # Never reached
        
        total_yield += field_potential
    
    # Final aggregation
    average_field_yield = total_yield / len(fields)
    
    # Secondary adjustment using conditional expression (relevant)
    final_adjustment = 1.1 if average_field_yield < 8 else 0.95
    final_yield = average_field_yield * final_adjustment
    
    # Unused diagnostic print (simulates debugging artifact)
    debug_snapshot = f"Yield snapshot: {final_yield:.3f}"
    
    return final_yield

# Configuration setup
config = {
    'base_yield': 5.2,
    'tech_level': 3,
    'optimization_mode': 'high_yield'
}

# Field data input
field_data = {
    'field_01': {
        'readings': {
            'ph_soil': 6.8,
            'moisture_a': 0.45,
            'nutrient_n': 8.2,
            'nutrient_p': 6.1
        },
        'climate': [
            {'temp': 25.1, 'precip': 12, 'wind': 8},
            {'temp': 19.3, 'precip': 5, 'wind': 6},
            {'temp': 33.7, 'precip': 35, 'wind': 12}
        ]
    },
    'field_02': {
        'readings': {
            'ph_soil': 7.1,
            'moisture_a': 0.62,
            'nutrient_n': 10.5,
            'nutrient_p': 7.3
        },
        'climate': [
            {'temp': 21.0, 'precip': 8, 'wind': 4},
            {'temp': 23.4, 'precip': 6, 'wind': 5},
            {'temp': 20.1, 'precip': 15, 'wind': 3}
        ]
    }
}

# Execution point of interest
final_yield = calculate_harvest_efficiency(field_data, config)
print(f"Result: {final_yield}")