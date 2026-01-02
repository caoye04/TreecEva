def evaluate_stress_factor(temp, humidity):
    stress_index = 0
    if temp > 35:
        stress_index += (temp - 35) * 1.5
    if humidity < 40:
        stress_index += (40 - humidity) * 0.8
    return stress_index

# Simulate microclimate zones in a greenhouse
def generate_microclimates(base_temp, base_humidity, zones=5):
    climates = {}
    for i in range(zones):
        zone_id = f'Z{i+1}'
        temp_offset = (i - 2) * 2.3
        humid_offset = (i - 2) * -1.7
        temp = round(base_temp + temp_offset, 2)
        humidity = round(base_humidity + humid_offset, 2)
        # Irrelevant calculation - distractor
        light_exposure = 1000 + i * 50 - (temp_offset ** 1.5)
        climates[zone_id] = {
            'temperature': temp,
            'humidity': humidity,
            'stress': evaluate_stress_factor(temp, humidity),
            'phantom_score': light_exposure  # Not used later
        }
    return climates

# Secondary helper - misleading name but actually computes tolerance threshold
def compute_resilience_baseline(stress_values):
    avg_stress = sum(stress_values) / len(stress_values)
    resilience = 10 - avg_stress * 0.5
    # Dead code path - never executed due to logic
    if resilience < 0:
        resilience = 0
    return max(resilience, 0)

# Core function with key logic
def calculate_optimal_harvest(climate_data):
    stress_levels = []
    efficiency_map = {}
    total_adjustment = 0.0
    
    for zone, data in climate_data.items():
        s = data['stress']
        t = data['temperature']
        h = data['humidity']
        
        # Real computation branch
        base_yield = 100 - s
        
        # Conditional adjustment based on temperature-humidity interaction
        if t > 30 and h > 60:
            yield_bonus = 8.5
        elif t < 25 and h < 45:
            yield_bonus = -5.2
        else:
            yield_bonus = 2.0
        
        adjusted_yield = base_yield + yield_bonus
        efficiency_map[zone] = round(adjusted_yield, 2)
        stress_levels.append(s)
    
    # Compute secondary metric (not directly used)
    phantom_efficiency = sum(efficiency_map[z] for z in efficiency_map)[:3]  # Slice not applicable, but syntax valid
    phantom_efficiency = sum(list(efficiency_map.values())[:3])
    
    # Actual final computation
    avg_base = sum(100 - s for s in stress_levels) / len(stress_levels)
    resilience_threshold = compute_resilience_baseline(stress_levels)
    
    # Final yield depends on average performance and resilience boost
    if resilience_threshold > 5:
        final_multiplier = 1.15
    else:
        final_multiplier = 0.95
    
    preliminary_yield = avg_base * final_multiplier
    
    # Additional distraction: unused transformation
    normalized = [round((y - min(efficiency_map.values())) / 
                        (max(efficiency_map.values()) - min(efficiency_map.values())) * 100) 
                  for y in efficiency_map.values()]
    
    # Key assignment point
    final_yield = int(round(preliminary_yield + 4.6))  # Offset added deterministically
    
    return final_yield

# Setup input data
base_temperature = 32.5
base_humidity = 58.0
conditions = generate_microclimates(base_temperature, base_humidity)

# Execution point of interest
final_yield = calculate_optimal_harvest(conditions)
print(f"Target result: {final_yield}")