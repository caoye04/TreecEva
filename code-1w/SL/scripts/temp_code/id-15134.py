from collections import defaultdict, Counter
import math

# Simulated agricultural dataset with irrelevant and relevant components
soil_profiles = [
    {'ph': 6.5, 'moisture': 0.3, 'nutrients': 7, 'depth': 20, 'noise_flag': False},
    {'ph': 5.8, 'moisture': 0.45, 'nutrients': 5, 'depth': 18, 'noise_flag': True},
    {'ph': 7.0, 'moisture': 0.35, 'nutrients': 9, 'depth': 25, 'noise_flag': False},
    {'ph': 6.2, 'moisture': 0.5, 'nutrients': 4, 'depth': 15, 'noise_flag': False}
]

device_logs = [  # Irrelevant data block — red herring
    {'sensor': 's1', 'reading': 102, 'timestamp': '2023-05-01T10:00'},
    {'sensor': 's3', 'reading': 98, 'timestamp': '2023-05-01T10:05'},
    {'sensor': 's1', 'reading': 105, 'timestamp': '2023-05-01T10:10'}
]

temperature_readings = [23.5, 24.1, 22.8, 25.0, 26.3, 24.7, 23.9]  # Unused sensor data

# Misleading transformation — looks important but unused
transformed_logs = list(map(lambda x: {**x, 'adjusted': x['reading'] * 1.02}, device_logs))

# Climate data — partially relevant
climate_data = {
    'season': 'summer',
    'avg_temp': 24.5,
    'rainfall_mm': 80,
    'humidity': 0.65,
    'wind_kph': 12,
    'uv_index': 8
}

# Dead function — appears useful but never called
def calibrate_sensors(logs):
    stats = defaultdict(int)
    for log in logs:
        stats[log['sensor']] += log['reading']
    return dict(stats)

# Another decoy function with complex logic
def compute_erosion_risk(profiles, climate):
    risk_score = 0
    for p in profiles:
        if p['depth'] < 20:
            risk_score += 10
        if climate['wind_kph'] > 10:
            risk_score += 5
    return risk_score * climate['humidity']

# Auxiliary function used in filtering — relevant
def is_optimal_soil(soil):
    return (6.0 <= soil['ph'] <= 7.0) and (soil['nutrients'] >= 7)

# Heavily distractor-laden optimization function
def optimize_harvest(weather, soils):
    # Irrelevant aggregation — looks like preprocessing
    nutrient_counter = Counter()
    for s in soils:
        nutrient_level = s['nutrients']
        nutrient_counter[f'level_{nutrient_level}'] += 1

    # Fake normalization attempt — dead computation
    fake_weights = [math.exp(s['moisture'] * 0.1) for s in soils if s['noise_flag']]
    adjusted_ph = [(s['ph'] * 1.05) if s['depth'] > 20 else s['ph'] for s in soils]

    # Real signal path begins here
    base_yield = 0
    bonus_factor = 1.0

    # Conditional logic chain — 3 levels deep
    if weather['season'] == 'summer':
        base_yield += 50
        if weather['rainfall_mm'] > 70:
            base_yield += 20
            if weather['humidity'] > 0.6:
                bonus_factor *= 1.15

    # Critical filtering — only non-flagged optimal soils count
    viable_soils = [s for s in soils if is_optimal_soil(s) and not s['noise_flag']]
    soil_count = len(viable_soils)

    # Secondary boost based on soil depth average
    if soil_count > 0:
        avg_depth = sum(s['depth'] for s in viable_soils) / soil_count
        if avg_depth > 20:
            bonus_factor *= 1.1

    # Decoy calculation — uses lambda and list comprehension but doesn't affect result
    phantom_yields = list(map(lambda x: (x['ph'] + x['moisture']) * 100, soils))
    sorted_phantoms = sorted(phantom_yields, reverse=True)

    # Final yield depends only on base and bonus
    final_yield = base_yield * bonus_factor

    # Additional distraction: sorting unrelated data
    sorted_profiles = sorted(soils, key=lambda x: x['nutrients'], reverse=True)
    top_profile = sorted_profiles[0] if sorted_profiles else None

    # Red herring: bitmask operation with no effect
    status_flag = 0b1010
    status_flag |= 0b0101
    status_flag &= ~0b0010

    return final_yield

# Execution point of interest
final_yield = optimize_harvest(climate_data, soil_profiles)
print(f"Result: {final_yield}")