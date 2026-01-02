import math

# Irrelevant utility function (dead code path)
def calculate_wavelength(freq):
    return 3e8 / freq if freq > 0 else 0

# Misleading agricultural metrics (distractor variables)
baseline_yield = 1200
projected_rainfall = [110, 130, 95, 80, 140]
elevation_zones = {1: 'low', 2: 'mid', 3: 'high'}

# Core data structures with mixed relevance
climate_data = {
    'temperature': [23, 25, 27, 26, 24],
    'humidity': [65, 70, 75, 72, 68],
    'wind_speed': [10, 15, 12, 18, 20]
}

soil_profiles = [
    {'ph': 6.2, 'nitrogen': 45, 'organic': 3.1},
    {'ph': 5.8, 'nitrogen': 38, 'organic': 2.7},
    {'ph': 6.5, 'nitrogen': 50, 'organic': 3.4}
]

# Decoy optimization model (unused but plausible)
class YieldPredictor:
    def __init__(self):
        self.factor = 1.0

    def predict(self, data):
        return sum(data) * self.factor

# Auxiliary transformation (partially relevant)
transform_readings = lambda x: [val * 0.9 + 5 for val in x if val > 0]

# Secondary processing chain with red herring computations
temperature_adj = transform_readings(climate_data['temperature'])
humidity_efficiency = [math.log(h + 1) for h in climate_data['humidity']]

# Fake correlation matrix (irrelevant computation)
corr_matrix = [[0 for _ in range(3)] for _ in range(3)]
for i in range(3):
    for j in range(3):
        corr_matrix[i][j] = abs(i - j) * 0.1

# Key algorithm: crop yield optimizer with embedded logic
def assess_ph_compatibility(ph):
    return 0.8 if 5.5 <= ph <= 6.5 else 0.6

def compute_nutrient_score(n_val, org):
    return (n_val * 0.7) + (org * 10)

# Central optimization function with multiple steps
def optimize_harvest(weather, soils):
    base = 0
    adjustment_factor = 0
    
    # Step 1: temperature integration
    avg_temp = sum(weather['temperature']) / len(weather['temperature'])
    if avg_temp > 25:
        adjustment_factor += 0.1
    elif avg_temp < 24:
        adjustment_factor -= 0.05
    
    # Step 2: wind stress penalty
    high_wind_days = len([w for w in weather['wind_speed'] if w > 15])
    stress_penalty = high_wind_days * 0.02
    
    # Step 3: process each soil profile
    for idx, soil in enumerate(soils):
        # Substep A: pH effect
        ph_mod = assess_ph_compatibility(soil['ph'])
        
        # Substep B: nutrient contribution
        nut_score = compute_nutrient_score(soil['nitrogen'], soil['organic'])
        
        # Substep C: micro-climate interaction (simulated)
        temp_impact = abs(climate_data['temperature'][idx % 5] - 25) * -0.5
        
        # Accumulate base yield
        plot_yield = 800 * ph_mod + nut_score * 12 + temp_impact
        
        # Add conditional bonus using ternary-like expression
        plot_yield += 50 if soil['nitrogen'] > 40 and ph_mod == 0.8 else 0
        
        base += plot_yield
    
    # Step 4: aggregate weather effects
    humidity_weight = sum(humidity_efficiency) / len(humidity_efficiency)
    
    # Step 5: final composition
    final_base = base / len(soils)
    total_factor = 1 + adjustment_factor - stress_penalty + (humidity_weight * 0.01)
    
    # Final calculation (target result)
    result = final_base * total_factor
    
    # Dead assignment (distractor)
    dummy = math.sin(math.pi / 4) * 1000
    
    return int(result)

# Unused but plausible alternative method
def legacy_optimization(data):
    return sum(data['temperature']) * 20

# Critical execution point
final_yield = optimize_harvest(climate_data, soil_profiles)

# Print required output
print(f"Result: {final_yield}")