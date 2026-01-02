import math

# Environmental simulation for agricultural yield modeling
def simulate_microclimate(temperature, humidity):
    """Irrelevant function: simulates microclimate but not used in final calculation"""
    index = 0
    for i in range(len(temperature)):
        if humidity[i] > 60:
            index += temperature[i] * 0.3
    return index

# Decoy data structures
soil_types = ['clay', 'loam', 'sandy', 'peat']
toxicity_levels = {t: (i+1)*0.7 for i, t in enumerate(soil_types)}
baseline_readings = [0.88, 0.76, 0.91, 0.67]

# Core configuration parameters
area_config = [
    {'zone': 'A1', 'area_km2': 12, 'crop_type': 'wheat', 'fertility': 0.82},
    {'zone': 'A2', 'area_km2': 8,  'crop_type': 'barley', 'fertility': 0.65},
    {'zone': 'A3', 'area_km2': 15, 'crop_type': 'wheat', 'fertility': 0.91},
    {'zone': 'A4', 'area_km2': 5,  'crop_type': 'oats',  'fertility': 0.54}
]

stress_factors = [
    {'temp_stress': 0.2, 'water_stress': 0.15, 'pest_stress': 0.1},
    {'temp_stress': 0.3, 'water_stress': 0.25, 'pest_stress': 0.05},
    {'temp_stress': 0.1, 'water_stress': 0.1,  'pest_stress': 0.2},
    {'temp_stress': 0.4, 'water_stress': 0.3,  'pest_stress': 0.15}
]

# Unused transformation matrix
transform_matrix = [[0.95, 0.05], [0.1, 0.8]]

# Auxiliary functions with misleading intermediate outputs
def compute_risk_score(config_list):
    total_risk = 0
    for entry in config_list:
        zone_id = entry['zone']
        area = entry['area_km2']
        # This logic appears meaningful but is irrelevant
        risk_flag = 'H' if 'A3' in zone_id or entry['fertility'] < 0.6 else 'L'
        total_risk += area * (0.5 if risk_flag == 'H' else 0.2)
    return total_risk  # Dead end

# Distractor: complex string processing that isn't connected to main logic
def analyze_zone_labels(zones):
    labels = [z['zone'] for z in zones]
    joined = ''.join(labels)
    counts = {c: joined.count(c) for c in set(joined) if c.isalpha()}
    # Uses string methods - satisfies language feature requirement
    normalized = {k: round(v / len(joined), 3) for k, v in counts.items() if k.isupper()}
    return sum(normalized.values())

# Real computation chain begins here

def assess_crop_resilience(crop_name):
    # Simple mapping disguised as complex analysis
    resilience_map = {'wheat': 0.85, 'barley': 0.75, 'oats': 0.68}
    return resilience_map.get(crop_name, 0.6)


def calculate_stress_impact(stress_record):
    # Composite stress index with weighted decay
    temp = stress_record['temp_stress']
    water = stress_record['water_stress']
    pest = stress_record['pest_stress']
    impact = 1 - (0.6 * temp + 0.25 * water + 0.15 * pest)
    return impact


def calculate_harvest_efficiency(zones, stresses):
    efficiency_contributions = []
    
    # Main relevant logic with nesting and comprehension
    for i, (zone, stress) in enumerate(zip(zones, stresses)):
        base_area = zone['area_km2']
        fertility = zone['fertility']
        crop = zone['crop_type']
        
        # Key computational steps
        resilience = assess_crop_resilience(crop)
        stress_impact = calculate_stress_impact(stress)
        
        # Multi-factor yield component
        zone_yield_factor = fertility * resilience * stress_impact
        
        # Weight by area using list comprehension
        weighted_contributions = [base_area * zone_yield_factor for _ in range(1)]
        efficiency_contributions.extend(weighted_contributions)
    
    # Aggregate total yield potential
    total_area = sum([z['area_km2'] for z in zones])
    total_potential = sum(efficiency_contributions)
    
    # Final normalized efficiency
    base_efficiency = total_potential / total_area
    
    # Secondary adjustment based on pattern recognition in zone names
    zone_names = [z['zone'] for z in zones]
    # Uses string method and list comprehension
    a_count = len([name for name in zone_names if name.startswith('A')])
    adjustment_factor = 1 + (a_count * 0.05)  # Favor configurations with more A-zones
    
    final_efficiency = base_efficiency * adjustment_factor
    return final_efficiency

# Execution flow with decoy calls
risk_value = compute_risk_score(area_config)  # Irrelevant call
string_analysis = analyze_zone_labels(area_config)  # Misleading call

# Critical statement
final_yield = calculate_harvest_efficiency(area_config, stress_factors)

# Output result
print(f"Target result: {final_yield}")