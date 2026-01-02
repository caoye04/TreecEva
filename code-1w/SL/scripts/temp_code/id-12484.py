import math

# Simulated environmental data (distractor: some fields are unused)
def generate_environmental_metrics():
    return {
        'temperature': [23, 25, 27, 30, 28],
        'humidity': [65, 70, 72, 60, 55],
        'co2_levels': [410, 415, 420, 425, 430],
        'wind_speed': [12, 14, 10, 11, 13],
        'solar_radiation': [800, 850, 900, 870, 830]
    }

# Irrelevant function - dead code path (distractor)
def calculate_wind_efficiency(data):
    efficiency = 0
    for speed in data['wind_speed']:
        if speed > 12:
            efficiency += 0.8
        else:
            efficiency += 0.3
    return round(efficiency * 100) / 100

# Unused complex transformation (red herring)
def transform_co2_logarithmic(levels):
    return [math.log(l + 1) * 1.2 for l in levels if l > 400]

# Simulated soil composition profiles (mix of relevant and irrelevant fields)
soil_profiles = [
    {'ph': 6.5, 'nitrogen': 18, 'organic_matter': 3.2, 'texture': 'loam'},
    {'ph': 5.8, 'nitrogen': 14, 'organic_matter': 2.1, 'texture': 'clay'},
    {'ph': 7.0, 'nitrogen': 22, 'organic_matter': 4.0, 'texture': 'silt'}
]

# Climate data with extra dimensions (only temperature matters)
climate_data = {
    'daily_temp': [23, 25, 27, 30, 28, 26, 24],
    'precipitation': [15, 0, 10, 20, 5, 0, 18],
    'pressure': [1013, 1015, 1012, 1010, 1014, 1016, 1011]
}

# Secondary crop model with misleading intermediate output (decoy)
def simulate_crop_growth_v1(temps, soils):
    base_yield = 0
    peak_days = 0
    for t in temps:
        if 25 <= t <= 28:
            base_yield += 3.5
            peak_days += 1
        elif t > 28:
            base_yield += 2.0
        else:
            base_yield += 1.8
    # This function is never used in final calculation
    print(f'Decoy growth model estimate: {base_yield:.2f} tons/ha')
    return base_yield * 0.7

# Unused nutrient scoring system (complex distractor)
def evaluate_nutrient_balance(soils):
    scores = []
    for s in soils:
        ph_score = 10 - abs(s['ph'] - 6.5)
        n_score = min(s['nitrogen'] / 3, 10)
        om_score = s['organic_matter'] * 2
        total = (ph_score + n_score + om_score) / 3
        scores.append(round(total, 2))
    return scores

# Core algorithm buried within distractions
def compute_thermal_time(temperatures, threshold=20):
    return sum([max(t - threshold, 0) for t in temperatures])

# Destructuring and multiple assignments (relevant concept)
def analyze_ph_nitrogen(soils):
    avg_ph = sum([s['ph'] for s in soils]) / len(soils)
    avg_n = sum([s['nitrogen'] for s in soils]) / len(soils)
    return avg_ph, avg_n

# Complex conditional logic with short-circuiting and bit manipulation (relevance: filtering)
def is_optimal_soil_condition(ph, nitrogen):
    condition_1 = 5.5 <= ph <= 7.5
    condition_2 = nitrogen > 16
    flag = (int(condition_1) << 1) | int(condition_2)
    return (flag & 2) and (flag & 1), flag  # Only first part matters

# Main optimization function with embedded logic chain
def optimize_harvest(climate, soils):
    # Step 1: Extract key thermal accumulation
    thermal_units = compute_thermal_time(climate['daily_temp'])
    
    # Step 2: Unpack average soil properties
    mean_ph, mean_n = analyze_ph_nitrogen(soils)
    
    # Step 3: Evaluate binary condition using bitwise logic
    is_suitable, _ = is_optimal_soil_condition(mean_ph, mean_n)
    
    # Step 4: Apply nonlinear yield response curve
    if thermal_units > 80:
        base_yield = 8.5
    elif thermal_units > 60:
        base_yield = 6.2
    else:
        base_yield = 4.0
    
    # Step 5: Adjust for soil suitability (only this branch affects result)
    adjustment_factor = 1.3 if is_suitable else 0.8
    
    # Step 6: Incorporate subtle integer division rounding effect
    bonus = (mean_n // 5) * 0.1  # Adds 0.4 when mean_n=22
    
    # Step 7: Final composition using conditional expression
    final_yield = base_yield * adjustment_factor + (bonus if bonus > 0 else 0.05)
    
    # Step 8: Clamp to realistic maximum (not triggered here)
    final_yield = min(final_yield, 12.0)
    
    # Step 9: Round to two decimals deterministically
    return round(final_yield * 100) / 100

# Irrelevant preprocessing (distractor block)
environment_metrics = generate_environmental_metrics()
w_eff = calculate_wind_efficiency(environment_metrics)
co2_transformed = transform_co2_logarithmic(environment_metrics['co2_levels'])

# Decoy model call (misleading execution path)
decoy_yield = simulate_crop_growth_v1(
    environment_metrics['temperature'],
    [{'ph': 6.0, 'nitrogen': 15}] * 3
)

# Actual target computation buried among distractions
final_yield = optimize_harvest(climate_data, soil_profiles)

# Print required result
print(f"Result: {final_yield}")