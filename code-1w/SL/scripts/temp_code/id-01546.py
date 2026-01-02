import itertools

# Simulated agricultural dataset with red herrings
def generate_dummy_metrics():
    return [i ** 2 for i in range(10) if i % 3 != 0]

def calculate_shadow_index(data):
    # Irrelevant calculation on unused data
    return sum(x % 7 for x in data if x > 10)

def deprecated_soil_analysis(profiles):
    # Dead function: never called in execution path
    return {k: v * 0.85 for k, v in profiles.items() if 'depth' in k}

def filter_microclimates(climate_list):
    # Distractor transformation: looks important but unused later
    return list(filter(lambda x: x['humidity'] > 60, climate_list))

def assess_drought_risk(temp_seq):
    # Misleading intermediate model
    risk = 0
    for t in temp_seq:
        if t > 35:
            risk += (t - 35) * 1.5
    return risk / len(temp_seq) if temp_seq else 0

def compute_canopy_resilience(*args):
    # Unused complex logic with multiple parameters
    return tuple((a % 11) * 0.3 for a in args)

def evaluate_irrigation_potential(water_table, evap_rate):
    # Another decoy function with plausible naming
    return water_table * (1 - evap_rate / 100)

# Core relevant data
climate_data = [
    {'temp': 28, 'humidity': 65, 'radiation': 820},
    {'temp': 31, 'humidity': 58, 'radiation': 910},
    {'temp': 33, 'humidity': 54, 'radiation': 940},
    {'temp': 29, 'humidity': 68, 'radiation': 790}
]

soil_profiles = {
    'plot_A': {'ph': 6.2, 'nitrogen': 18, 'depth': 120},
    'plot_B': {'ph': 5.8, 'nitrogen': 14, 'depth': 95},
    'plot_C': {'ph': 6.5, 'nitrogen': 21, 'depth': 135}
}

# Irrelevant precomputed constants
BASE_YIELD_FACTOR = 42
MAX_WATER_RETENTION = 87.5
NORMALIZED_INDEX_TABLE = list(itertools.accumulate([1, -1] * 5, lambda a, b: a + b))

# Preliminary dummy processing (distractors)
dummy_metrics = generate_dummy_metrics()
shadow_index = calculate_shadow_index(dummy_metrics)
microclimates_filtered = filter_microclimates(climate_data)
drought_risk_score = assess_drought_risk([entry['temp'] for entry in climate_data])

# Key function with embedded logic and distractors
def optimize_harvest(weather, soils):
    radiation_levels = [day['radiation'] for day in weather]
    avg_radiation = sum(radiation_levels) / len(radiation_levels)
    
    temperature_sequence = [day['temp'] for day in weather]
    high_temp_stress = len([t for t in temperature_sequence if t > 30])
    
    # Real computation begins here
    base_yield = avg_radiation * 0.7
    
    # Apply temperature penalty
    if high_temp_stress > 2:
        base_yield *= (0.9 ** high_temp_stress)
    
    # Extract nitrogen levels using meaningful unpacking
    n_levels = [info['nitrogen'] for info in soils.values()]
    avg_nitrogen = sum(n_levels) / len(n_levels)
    
    # Yield boost from soil fertility
    fertility_factor = 1 + (avg_nitrogen / 100)
    boosted_yield = base_yield * fertility_factor
    
    # Phantom adjustment based on unused index
    phantom_correction = NORMALIZED_INDEX_TABLE[-1] * 0.1  # This equals 0 due to alternating sum
    boosted_yield += phantom_correction
    
    # Final non-linear scaling
    final_value = round(boosted_yield * 0.85, 4)
    
    # Critical distraction: assign to misleading variable name that looks final
    projected_output = final_value * 1.2  # Never used
    
    # Actual target output
    return final_value

# Execution point of interest
final_yield = optimize_harvest(climate_data, soil_profiles)

# Print result as required
print(f"Target result: {final_yield}")