from collections import defaultdict
import math

# Simulate agricultural yield optimization with noise and distractors
def analyze_growth_potential(temp, rainfall, ph):
    base_score = (temp - 20) * 0.8 + (rainfall - 100) * 0.5
    if ph < 5.5 or ph > 7.5:
        base_score *= 0.6
    return max(base_score, 0)

def calculate_erosion_risk(slope, veg_density):
    # Irrelevant function - red herring
    return slope * (1 - veg_density / 100) * 10

def assess_pest_outbreak(temperature, humidity):
    # Dead code path - never used in final calculation
    risk = 0.3 * temperature + 0.2 * humidity
    return min(risk, 100)

def compute_fertilizer_need(nitrogen_level, crop_type='corn'):
    # Distractor computation
    needs = {'corn': 150, 'wheat': 100, 'soy': 80}
    return needs.get(crop_type, 120) - nitrogen_level

def optimize_harvest(weather, soils):
    # Core logic buried among distractions
    cumulative_yield = 0
    erosion_map = defaultdict(lambda: 0)
    pest_projection = []
    
    # Real processing begins here
    for region_id, readings in weather.items():
        temp_avg = sum(readings['temps']) / len(readings['temps'])
        total_rain = sum(readings['rain_mm'])
        
        # Process corresponding soil data
        soil_ph = soils[region_id]['ph']
        nitrogen = soils[region_id]['nitrogen']
        slope_grade = soils[region_id]['slope']
        vegetation = soils[region_id]['vegetation_cover']
        
        # Actual yield contribution
        raw_potential = analyze_growth_potential(temp_avg, total_rain, soil_ph)
        efficiency_factor = (1 - 0.01 * slope_grade) * (0.7 + vegetation * 0.005)
        adjusted_yield = raw_potential * efficiency_factor
        
        # Store in map but only cumulative matters
        erosion_map[region_id] = calculate_erosion_risk(slope_grade, vegetation)
        pest_projection.append(assess_pest_outbreak(temp_avg, total_rain / 10))
        
        # Critical accumulation
        cumulative_yield += adjusted_yield * 10  # Scale to field level
    
    # Secondary transformation
    modifier_chain = lambda x: math.log(x + 10) if x > 50 else math.sqrt(x * 2)
    transformed = modifier_chain(cumulative_yield)
    
    # Final adjustment using distractor variables (but they don't affect outcome)
    fake_dependency = len(erosion_map) * 0  # Always zero
    projection_bias = sum(p for p in pest_projection if p > 50) * 0  # Also zero
    
    result = int(transformed * 17 + 3) + fake_dependency + projection_bias
    return result

# Generate synthetic input data
climate_data = {
    'field_A1': {
        'temps': [22, 24, 19, 25, 23],
        'rain_mm': [95, 120, 80, 110, 90]
    },
    'field_B2': {
        'temps': [26, 28, 25, 27, 24],
        'rain_mm': [130, 115, 105, 140, 125]
    },
    'field_C3': {
        'temps': [18, 20, 21, 19, 22],
        'rain_mm': [85, 95, 100, 88, 92]
    }
}

soil_profiles = {
    'field_A1': {'ph': 6.2, 'nitrogen': 110, 'slope': 8, 'vegetation_cover': 65},
    'field_B2': {'ph': 5.8, 'nitrogen': 95, 'slope': 12, 'vegetation_cover': 45},
    'field_C3': {'ph': 7.1, 'nitrogen': 130, 'slope': 5, 'vegetation_cover': 80}
}

# Unused test cases - dead code paths
sample_fields = [
    {'coords': (45.1, -75.3), 'crop': 'corn'},
    {'coords': (45.2, -75.4), 'crop': 'wheat'}
]

# Key execution point
final_yield = optimize_harvest(climate_data, soil_profiles)
print(f"Result: {final_yield}")