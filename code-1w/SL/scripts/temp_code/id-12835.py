from itertools import combinations

# Simulate ecological yield prediction in a pollination network

def generate_synergy_pairs(species_list):
    # Distractor: generates irrelevant species pair combos
    return list(combinations(species_list, 2))

def compute_stress_index(environmental_data):
    # Red herring function: computes unrelated stress metric
    base_stress = sum([env['temp'] - 25 for env in environmental_data])
    humidity_penalty = sum([1 if env['humidity'] < 40 else 0 for env in environmental_data])
    return base_stress + humidity_penalty * 2

def normalize_readings(sensor_log):
    # Dead code path: not used in final calculation
    normalized = {}
    for key, values in sensor_log.items():
        avg = sum(values) / len(values)
        normalized[key] = round(avg, 2)
    return normalized

def evaluate_resilience(plant_health, threshold=0.6):
    # Misleading intermediate: looks important but unused
    resilient_count = sum(1 for health in plant_health if health > threshold)
    return resilient_count / len(plant_health) if plant_health else 0

def calculate_harvest(flowers, pollinators, stress_factors):
    # Core logic: actual answer computation
    base_yield = flowers * pollinators
    
    # Apply nonlinear stress decay
    stress_multiplier = 1.0
    for factor in stress_factors:
        if factor == 'drought':
            stress_multiplier *= 0.85
        elif factor == 'pests':
            stress_multiplier *= 0.90
        elif factor == 'heat':
            stress_multiplier *= 0.80
    
    # Secondary adjustment based on pollinator diversity
    diversity_bonus = 0
    if len(pollinators) >= 3:
        diversity_bonus = 15
    elif len(pollinators) == 2:
        diversity_bonus = 7
    
    adjusted_yield = base_yield * stress_multiplier + diversity_bonus
    
    # Final correction using hidden rule: odd flower counts reduce efficiency
    if flowers % 2 == 1:
        adjusted_yield *= 0.95
    
    return int(round(adjusted_yield))

# Irrelevant data structures (distractors)
species_interactions = {
    'bee': ['clover', 'sunflower', 'lavender'],
    'butterfly': ['milkweed', 'aster'],
    'hummingbird': ['fuchsia', 'penstemon']
}

sensor_readings = {
    'light': [800, 850, 780, 900],
    'co2': [410, 415, 405, 420],
    'moisture': [35, 30, 40, 33]
}

environment_log = [
    {'temp': 28, 'humidity': 35},
    {'temp': 31, 'humidity': 30},
    {'temp': 29, 'humidity': 45}
]

# Unused intermediate calculations (red herrings)
stress_index = compute_stress_index(environment_log)
synergy_pairs = generate_synergy_pairs(['A', 'B', 'C', 'D'])
normalized_sensors = normalize_readings(sensor_readings)

# Key input variables
flowers = 124
pollinators = ['honeybee', 'bumblebee', 'solitary', 'moth']  # length = 4
stress_factors = ['drought', 'heat']

# Evaluate resilience (misleading call - result unused)
resilience_ratio = evaluate_resilience([0.8, 0.7, 0.9, 0.65, 0.55])

# Critical execution point
final_yield = calculate_harvest(flowers, pollinators, stress_factors)

print(f"Result: {final_yield}")