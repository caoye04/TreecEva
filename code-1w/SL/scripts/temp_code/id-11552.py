from collections import defaultdict, Counter
import itertools

# Simulate agricultural yield prediction with noise and distractions
def generate_noise_sequence(length):
    return [i % 7 for i in range(length)]

def deprecated_calc_v1(data):
    # Irrelevant legacy function (dead code path)
    return sum(x ** 0.5 for x in data if x > 3)

def auxiliary_transform(seq):
    # Distractor: used only in decoy branch
    return [x * 1.5 for x in seq if x < 5]

def compute_entropy(vector):
    # Red herring: calculates something unused later
    freqs = Counter(vector)
    total = len(vector)
    entropy = 0
    for count in freqs.values():
        p = count / total
        entropy -= p * (p ** 0.5)  # Not real entropy, but looks plausible
    return round(entropy, 4)

def simulate_pest_migration(zones, severity):
    # Misleading intermediate model
    migration_map = defaultdict(lambda: 'low')
    for i, z in enumerate(zones):
        if i % 3 == 0:
            migration_map[z] = 'high'
        elif i % 5 == 0:
            migration_map[z] = 'medium'
    return dict(migration_map)

def calculate_harvest_efficiency(fields, infestation):
    base_multiplier = 0.95
    adjustment_factor = 1.0
    
    # Real logic begins here — nested conditional with distractors
    if len(fields) > 3:
        temp_store = []
        for k, v in fields.items():
            if 'soil_quality' in v:
                if v['soil_quality'] == 'clay':
                    adjustment_factor *= 0.88
                elif v['soil_quality'] == 'sandy':
                    adjustment_factor *= 1.05
            if 'crop_age' in v:
                age_mod = (100 - v['crop_age']) / 100
                temp_store.append(age_mod)
        
        avg_age_mod = sum(temp_store) / len(temp_store) if temp_store else 1.0
        adjustment_factor *= avg_age_mod
    
    # Bit manipulation decoy (irrelevant)
    encoded_mask = 0
    for i in range(len(fields)):
        encoded_mask ^= (i << 2)
    
    # Critical calculation buried in noise
    baseline_yield = 0
    for attrs in fields.values():
        if 'yield_potential' in attrs:
            baseline_yield += attrs['yield_potential']
    
    # Real dependency on infestation
    stress_penalty = max(0, 1 - (infestation * 0.1))
    adjustment_factor *= stress_penalty
    
    # Final computation
    final_yield = baseline_yield * adjustment_factor * base_multiplier
    
    # Decoy output to mislead tracing
    debug_info = {"mask": encoded_mask, "entropy": compute_entropy(generate_noise_sequence(10))}
    
    return round(final_yield, 6)

# Orchestration with irrelevant setup
terrain_zones = ['north', 'east', 'south', 'west']
zone_rainfall = {z: (i+1)*120 for i, z in enumerate(terrain_zones)}

# Unused transformation chain
transformed_rain = list(map(lambda x: x * 0.8 + 10, zone_rainfall.values()))
expanded_grid = list(itertools.product(terrain_zones, ['A', 'B']))

# Core data structure — meaningful input
area_data = {
    'field_01': {
        'soil_quality': 'clay',
        'crop_age': 65,
        'yield_potential': 230
    },
    'field_02': {
        'soil_quality': 'loam',
        'crop_age': 45,
        'yield_potential': 190
    },
    'field_03': {
        'soil_quality': 'sandy',
        'crop_age': 70,
        'yield_potential': 210
    },
    'field_04': {
        'soil_quality': 'clay',
        'crop_age': 50,
        'yield_potential': 180
    }
}

# Misdirection: pest simulation not directly used but seems important
pest_threat_levels = [0.2, 0.5, 0.8]
active_pests = {f'pest_{i}': level for i, level in enumerate(pest_threat_levels)}
pest_index = sum(active_pests.values()) / len(active_pests)  # 0.5 average

# Key statement
final_yield = calculate_harvest_efficiency(area_data, pest_index)

# Output result as required
print(f"Result: {final_yield}")