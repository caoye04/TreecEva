from collections import defaultdict, Counter
import math

# Simulated environmental sensor data (irrelevant in part)
temperature_readings = [23.4, 24.1, 22.9, 25.3, 26.0, 24.8, 23.9]
humidity_readings = [61, 58, 65, 54, 50, 60, 63]

# Core agricultural model inputs
soil_profiles = [
    {'ph': 6.2, 'nitrogen': 18, 'organic_matter': 3.1, 'depth': 45},
    {'ph': 5.8, 'nitrogen': 12, 'organic_matter': 2.3, 'depth': 38},
    {'ph': 6.5, 'nitrogen': 22, 'organic_matter': 4.0, 'depth': 50}
]

class CropModel:
    def __init__(self, base_yield):
        self.base_yield = base_yield
        self.adjustment_log = defaultdict(int)

    def _ph_factor(self, ph):
        # Optimal pH range: 6.0-6.8
        if 6.0 <= ph <= 6.8:
            return 1.0
        return 0.7 if ph < 6.0 else 0.6

    def _nutrient_score(self, nitrogen, organic_matter):
        score = (nitrogen * 0.3) + (organic_matter * 2.5)
        return min(score / 20.0, 1.2)

    def _depth_penalty(self, depth):
        return 0.8 if depth < 40 else 1.0

    def calculate_yield(self, soil):
        ph_adj = self._ph_factor(soil['ph'])
        self.adjustment_log['ph'] += 1

        nutrient_adj = self._nutrient_score(soil['nitrogen'], soil['organic_matter'])
        depth_adj = self._depth_penalty(soil['depth'])

        # Irrelevant calculation - simulates evapotranspiration (unused)
        try:
            _et = sum(temperature_readings) / len(temperature_readings)
            _vapor_pressure = _et * 0.61 + 2.1
        except:
            _vapor_pressure = 15.0

        yield_potential = self.base_yield * ph_adj * nutrient_adj * depth_adj

        # Dead code path - never executed due to logic
        if False and yield_potential > 100:
            yield_potential *= 1.15  # bonus for high yield (never reached)

        return round(yield_potential, 2)

# Climate data with red herring variables
climate_data = {
    'season': 'summer',
    'rainfall_mm': 120,
    'sunlight_hours': 8.5,
    'wind_speed_avg': 12.4,
    'frost_days': 0
}

# Unused function - decoy for weather impact
def assess_weather_risk(data):
    risk = 0
    if data['rainfall_mm'] < 100:
        risk += 30
    if data['frost_days'] > 5:
        risk += 50
    return risk  # Never called

# Secondary analysis - irrelevant to final result
texture_analysis = ['loam', 'clay', 'sandy_loam']
composition_stats = Counter(texture_analysis * 2)  # Distractor computation

# Recursive helper (over-engineered for simple task)
def binary_search_crop(crops, target_nitrogen=15):
    if len(crops) == 1:
        return crops[0]
    mid = len(crops) // 2
    if crops[mid]['nitrogen'] >= target_nitrogen:
        return binary_search_crop(crops[:mid], target_nitrogen)
    else:
        return binary_search_crop(crops[mid:], target_nitrogen)

# Main optimization function with multiple distractions
def optimize_harvest(climate, soils):
    model = CropModel(base_yield=85)
    yields = []

    # Real processing
    for soil in soils:
        raw_yield = model.calculate_yield(soil)
        # Apply climate factor (only one used from climate_data)
        if climate['rainfall_mm'] > 100:
            raw_yield *= 1.1
        yields.append(raw_yield)

    # Distraction: complex aggregation with unused features
    avg = sum(yields) / len(yields)
    std_dev = (sum((x - avg) ** 2 for x in yields) / len(yields)) ** 0.5
    cv = std_dev / avg if avg != 0 else 0

    # Over-complicated normalization (not actually affecting result)
    normalized = [round((y - avg) / std_dev * 10 + 50, 1) for y in yields]

    # Final adjustment based on recursive selection (uses only one soil)
    best_soil = binary_search_crop(soils)
    final_single = model.calculate_yield(best_soil)

    # Key decision point - what matters is this line below
    final_yield = int(round(avg * 1.05))  # Final output based on average with small boost

    # Dead assignment - misleading overwrite attempt
    final_yield = final_yield  # No-op, but looks like modification

    # Print for traceability
    print(f"Target result: {final_yield}")
    return final_yield

# Execution entry point
final_yield = optimize_harvest(climate_data, soil_profiles)