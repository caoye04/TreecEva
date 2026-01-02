def analyze_soil(ph, nitrogen, carbon):
    # Irrelevant soil analysis with decoy logic
    if ph < 5.0:
        return 'acidic'
    elif ph > 7.0:
        return 'alkaline'
    else:
        return 'neutral'

# Unused nutrient scoring (distractor)
def score_nutrient(value):
    return int(value * 1.5) if value > 10 else int(value * 0.8)

# Decoy weather simulation
class WeatherSim:
    def __init__(self, temp, humidity):
        self.temp = temp
        self.humidity = humidity
    
    def get_stress_index(self):
        return (self.temp - 25) * (self.humidity / 100)

# Misleading crop yield estimator (never used)
def estimate_yield(base, rain, temp):
    adjustment = 1 + (rain - 100) / 500
    return base * adjustment

# Core logic buried in distractions
def evaluate_growth_potential(soil_data, climate_risk, pests_present):
    base_score = 0
    ph = soil_data.get('ph', 6.5)
    moisture = soil_data.get('moisture', 30)
    
    # Real but obfuscated logic
    if ph >= 6.0 and ph <= 7.0:
        base_score += 40
    
    if moisture > 25:
        base_score += 30
    
    # Conditional expression used as required
    penalty = 20 if climate_risk == 'high' or pests_present else 0
    
    return base_score - penalty

# Complex data transformation chain
def transform_readings(raw_sensors):
    processed = []
    for val in raw_sensors:
        if val < 0: continue
        processed.append((val ** 0.5) * 2.1)
    return [round(p, 1) for p in processed]

# Recursive filtering function (some paths unused)
def filter_outliers(data, threshold=2.0, depth=0):
    if depth >= 2 or len(data) < 3:
        return data
    avg = sum(data) / len(data)
    dev = [(x - avg)**2 for x in data]
    std_dev = sum(dev) / len(dev)
    new_data = [x for x in data if abs(x - avg) <= threshold * std_dev]
    return filter_outliers(new_data, threshold, depth + 1)

# Main calculation buried under abstractions
def calculate_harvest(environmental_conditions):
    # Extract relevant fields
    soil = environmental_conditions['soil']
    temp_seq = environmental_conditions['temperature_log']
    pest_level = environmental_conditions['pest_activity']

    # Real path starts here — everything above was distraction
    growth_score = evaluate_growth_potential(
        soil, 
        environmental_conditions['climate_risk'], 
        pest_level > 0.7
    )

    # Process sensor data (some steps are red herrings)
    cleaned = filter_outliers(transform_readings(temp_seq))
    effective_temp = sum(cleaned) / len(cleaned) if cleaned else 25

    # Actual accumulation logic
    accumulation = 0
    for t in cleaned:
        if t > 20 and t < 35:
            accumulation += 1.5
    
    # Final composition
    normalized_accumulation = accumulation * 10
    final_modifier = 1.2 if effective_temp > 22 else 0.9
    
    # Key statement
    final_yield = int((growth_score + normalized_accumulation) * final_modifier)
    
    # Print required result
    print(f"Result: {final_yield}")
    return final_yield

# Setup realistic input with noise
conditions = {
    'soil': {'ph': 6.8, 'moisture': 32},
    'temperature_log': [24, -1, 26, 28, 30, 33, 29],  # Note: -1 will be filtered
    'pest_activity': 0.75,
    'climate_risk': 'moderate',
    'elevation': 147,
    'sunlight_hours': 7.2,
    'unused_flag': True
}

# Dead code path (never executed)
def legacy_calculate():
    pass

# Irrelevant global constants
crop_types = ['wheat', 'barley', 'oats']
base_water_requirement = 250
max_tolerance_index = 9.8

# Trigger execution
final_yield = calculate_harvest(conditions)