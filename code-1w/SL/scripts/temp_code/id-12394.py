import math

# Simulate agricultural yield prediction with noise and irrelevant computations
def preprocess_sensor_readings(data):
    # Irrelevant preprocessing - distractor
    normalized = [math.sin(x / 10) * 1.5 for x in data if x > 5]
    filtered = [x for x in normalized if x < 1.0]
    return filtered

# Decoy function - never called in correct path
def legacy_calculate_yield(area, index):
    adjustment = 0.87
    base = area * index * adjustment
    penalty = base * 0.15 if base > 100 else 0
    return base - penalty

# Unused transformation - dead code path
def transform_coordinates(latitudes, longitudes):
    rad = lambda deg: deg * math.pi / 180
    return [(rad(lat), rad(lon)) for lat, lon in zip(latitudes, longitudes)]

# Core calculation buried in distractions
def compute_stress_factor(temperature, moisture):
    # Relevant logic: calculates plant stress from climate
    temp_stress = abs(temperature - 25) * 0.3
    moisture_stress = (100 - moisture) * 0.05
    total_stress = temp_stress + moisture_stress
    return max(0.5, min(2.0, total_stress))  # Clamp factor

def evaluate_nutrient_score(profile):
    # Relevant: nutrient availability impacts yield
    nutrients = profile.get('nutrients', {})
    score = 0
    for key, val in nutrients.items():
        if key == 'nitrogen':
            score += val * 0.4
        elif key == 'phosphorus':
            score += val * 0.3
        elif key == 'potassium':
            score += val * 0.2
    return score * 0.1

def calculate_harvest_efficiency(climate, soils):
    # Main function - contains key logic
    efficiency_list = []
    
    # Misleading loop 1: processes but doesn't contribute to final result
    dummy_aggregates = []
    for day in climate:
        avg_temp = sum(day['temps']) / len(day['temps'])
        peak = max(day['temps'])
        if peak > 35:
            dummy_aggregates.append(avg_temp * 0.9)
    
    # Relevant processing
    total_weighted_yield = 0
    total_area = 0
    
    for i, entry in enumerate(climate):
        # Extract relevant climate features
        daily_temps = entry['temps']
        precipitation = entry['rain']
        sunlight = entry['sun_hours']
        
        # Compute average temperature stress
        stress_factors = [compute_stress_factor(t, precipitation) for t in daily_temps]
        avg_stress = sum(stress_factors) / len(stress_factors)
        
        # Link soil profile
        soil = soils[i % len(soils)]
        base_fertility = soil['base_fertility']
        nutrient_bonus = evaluate_nutrient_score(soil)
        fertility_index = base_fertility + nutrient_bonus
        
        # Area matters
        area = soil['area_hectares']
        
        # Efficiency formula
        raw_yield = (fertility_index * 80) / avg_stress
        adjusted_yield = raw_yield * (sunlight / 12)  # normalize sunlight
        
        # Weight by area
        total_weighted_yield += adjusted_yield * area
        total_area += area
        
        # Red herring: store intermediate that looks important
        efficiency_list.append({'day': i, 'yield': adjusted_yield, 'stress': avg_stress})
    
    # Final aggregate - this is the answer
    final_yield = total_weighted_yield / total_area if total_area > 0 else 0
    
    # More distractions below
    outlier_count = 0
    for item in efficiency_list:
        if item['stress'] > 1.8:
            outlier_count += 1
    # Unused statistic
    avg_yield_across_days = sum(item['yield'] for item in efficiency_list) / len(efficiency_list)
    
    return final_yield

# Simulated input data
climate_data = [
    {'temps': [22, 24, 26, 28, 23], 'rain': 60, 'sun_hours': 10},
    {'temps': [20, 21, 25, 27, 29], 'rain': 45, 'sun_hours': 11},
    {'temps': [18, 20, 24, 26, 28], 'rain': 70, 'sun_hours': 9},
    {'temps': [25, 26, 27, 29, 31], 'rain': 40, 'sun_hours': 12}
]

soil_profiles = [
    {
        'base_fertility': 7.2,
        'nutrients': {'nitrogen': 35, 'phosphorus': 25, 'potassium': 30},
        'area_hectares': 50
    },
    {
        'base_fertility': 6.8,
        'nutrients': {'nitrogen': 30, 'phosphorus': 20, 'potassium': 25},
        'area_hectares': 75
    },
    {
        'base_fertility': 8.0,
        'nutrients': {'nitrogen': 40, 'phosphorus': 30, 'potassium': 35},
        'area_hectares': 25
    }
]

# Irrelevant coordinate data - decoy
latitudes = [34.5, 35.1, 34.8]
longitudes = [-118.0, -118.5, -117.9]
coords = transform_coordinates(latitudes, longitudes)

# Noise variables
system_version = "AGRI-ML/v2.3"
data_quality_score = 0.97
normalization_factor = 1.05

# Preprocessing call - irrelevant to final result
sensor_noise = [23, 15, 8, 31, 44, 52, 6, 19]
filtered_noise = preprocess_sensor_readings(sensor_noise)

# Key execution point
final_yield = calculate_harvest_efficiency(climate_data, soil_profiles)

# Output result as required
print(f"Result: {final_yield}")