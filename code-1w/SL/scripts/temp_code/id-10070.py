import math

# Irrelevant utility function (dead code path)
def calculate_wind_speed(elevation):
    return (elevation * 0.3) + 5.7

# Another decoy function with misleading intermediate result
def assess_solar_exposure(lat, lon):
    base = lat * 1.2 + lon * 0.8
    adjustment = math.sin(base / 10)
    return base + adjustment  # Never used in final computation

# Unused but plausible-looking data structure
topography_map = {
    'ridges': [(3, 4), (7, 8), (12, 11)],
    'valleys': [(1, 2), (5, 6)]
}

# Real input data for agriculture model
climate_data = [
    {'temp': 22, 'rainfall': 85, 'humidity': 60},
    {'temp': 25, 'rainfall': 90, 'humidity': 55},
    {'temp': 19, 'rainfall': 110, 'humidity': 70}
]

soil_profiles = [
    {'ph': 6.4, 'nitrogen': 120, 'organic_matter': 3.2},
    {'ph': 5.8, 'nitrogen': 95, 'organic_matter': 2.1},
    {'ph': 6.9, 'nitrogen': 145, 'organic_matter': 4.0}
]

# Distractor variables with realistic agricultural names
baseline_irrigation = 75
max_crop_height = 1.8
pest_pressure_index = 0.43

# Hidden key parameters buried in noise
cultivation_factor = 0.87
rotation_bonus = 1.1

# Lambda used for filtering suitable zones (relevant)
suitable_ph = lambda x: 5.5 <= x['ph'] <= 7.0

# List comprehension with distractors and real logic
viable_soils = [s for s in soil_profiles if suitable_ph(s)]

# Bitwise red herring - looks important but unused
event_flag = 0b101010
status_mask = 0b110011
masked_event = event_flag & status_mask

# Set operations as required - some relevant, some not
evaluated_zones = {0, 1, 2}
disputed_zones = {1}
active_zones = evaluated_zones - disputed_zones  # Partially relevant

# Decoy transformation using trigonometric functions
temp_amplitude = sum(math.cos(d['temp'] * math.pi / 180) for d in climate_data)

# Core calculation chain begins here — only now reaching relevance
rainfall_avg = sum(cd['rainfall'] for cd in climate_data) / len(climate_data)
humidity_weighted_temp = sum(
    cd['temp'] * (cd['humidity'] / 100) for cd in climate_data
) / len(climate_data)

# Nitrogen efficiency curve (non-linear transform)
nitrogen_levels = [s['nitrogen'] for s in viable_soils]
mean_nitrogen = sum(nitrogen_levels) / len(nitrogen_levels)
nitrogen_efficiency = math.sqrt(mean_nitrogen / 100)

# Organic matter threshold logic with conditional expression
organic_matter_total = sum(s['organic_matter'] for s in viable_soils)
base_yield = organic_matter_total > 6.0 ? 420 : 380  # Ternary simulation via lambda due to Python syntax
ternary_sim = lambda a, b, c: a if b else c
base_yield = ternary_sim(420, organic_matter_total > 6.0, 380)

# Complex multi-factor yield optimizer (key function)
def optimize_harvest(climate, soils):
    # Nested comprehensions and filters
    good_rainfall_days = len([c for c in climate if c['rainfall'] >= 85])
    temp_score = sum(1 for c in climate if 20 <= c['temp'] <= 26)
    
    # Bit manipulation distraction inside function
    control_word = 0b111000
    shift_factor = (control_word >> 3) & 0b111  # equals 7
    
    # Real logic masked by abstraction
    ph_balance = len([s for s in soils if 6.0 <= s['ph'] <= 7.0])
    nitrogen_boost = math.log(mean_nitrogen + 1) * 0.5
    
    # Multi-step accumulation
    yield_potential = base_yield
    yield_potential += (good_rainfall_days * 12.5)
    yield_potential += (temp_score * 8.3)
    yield_potential *= nitrogen_efficiency
    yield_potential *= cultivation_factor
    
    # Conditional bonus (only if exactly two climate entries qualify)
    if good_rainfall_days == 2:
        yield_potential *= rotation_bonus
    
    # Final adjustment using set-derived count
    zone_multiplier = len(active_zones) / 2.0  # evaluates to 1.5
    yield_potential *= zone_multiplier
    
    return yield_potential

# Execution point of interest
final_yield = optimize_harvest(climate_data, soil_profiles)

# Print result as required
print(f"Result: {final_yield}")