import math

def analyze_rainfall(patterns):
    # Irrelevant analysis function (dead code path)
    total = 0
    for p in patterns:
        if p > 50:
            total += p * 0.3
    return total // 2 if total > 100 else 0

def calculate_ph_balance(soil_list):
    # Distractor: computes something unused later
    balanced = 0
    for s in soil_list:
        if 6.0 <= s['ph'] <= 7.0:
            balanced += 1
    return balanced

def simulate_growth(stress_index):
    # Misleading intermediate model
    if stress_index < 20:
        return 1.8
    elif stress_index < 50:
        return 1.2
    else:
        return 0.4  # Severe stress

def compute_resilience_factor(data):
    # Complex but irrelevant resilience metric
    factor = 1.0
    for entry in data:
        temp = entry['temp']
        humidity = entry['humidity']
        if temp > 35 and humidity < 40:
            factor *= 0.92
        elif temp < 10 and humidity > 70:
            factor *= 0.88
    return round(factor, 4)

def optimize_harvest(weather, soils):
    # Core logic starts here — this is the key function
    base_yield = 0
    stress_accumulator = 0
    peak_temp_count = 0
    low_rain_days = 0

    # Process climate data
    for day in weather:
        temp = day['temp']
        rain = day['rainfall']
        radiation = day['radiation']

        # Accumulate base yield from solar radiation (main contributor)
        base_yield += radiation * 0.7

        # Track heat stress events
        if temp > 38:
            stress_accumulator += (temp - 38) * 1.5
            peak_temp_count += 1

        # Count drought-like conditions
        if rain < 5:
            low_rain_days += 1

    # Apply temperature stress penalty
    stress_penalty = stress_accumulator * 0.3

    # Calculate water scarcity adjustment
    water_factor = 1.0 - (low_rain_days * 0.02)

    # Soil nutrient boost from first three optimal layers
    nutrient_boost = sum(
        [s['nitrogen'] * 0.1 + s['phosphorus'] * 0.05
         for i, s in enumerate(soils) if i < 3 and s['depth_cm'] <= 30]
    )

    # Phantom calculation using distractor functions (misleading)
    _ = calculate_ph_balance(soils)
    _ = compute_resilience_factor(weather)

    # Final yield computed via multi-step reasoning
    preliminary = base_yield - stress_penalty
    adjusted = preliminary * water_factor
    final_yield = int(adjusted + nutrient_boost)

    # Early exit red herring (never triggered in this input)
    if final_yield < 0:
        return 0

    return final_yield

# Simulated environmental dataset (real inputs)
climate_data = [
    {'temp': 32, 'humidity': 60, 'rainfall': 12, 'radiation': 85},
    {'temp': 36, 'humidity': 55, 'rainfall': 3, 'radiation': 90},
    {'temp': 39, 'humidity': 45, 'rainfall': 0, 'radiation': 95},
    {'temp': 41, 'humidity': 40, 'rainfall': 2, 'radiation': 93},
    {'temp': 34, 'humidity': 65, 'rainfall': 15, 'radiation': 80},
    {'temp': 28, 'humidity': 75, 'rainfall': 20, 'radiation': 70},
    {'temp': 37, 'humidity': 50, 'rainfall': 4, 'radiation': 88},
    {'temp': 33, 'humidity': 62, 'rainfall': 8, 'radiation': 82}
]

soil_profiles = [
    {'depth_cm': 15, 'ph': 6.4, 'nitrogen': 22, 'phosphorus': 18},
    {'depth_cm': 25, 'ph': 6.8, 'nitrogen': 19, 'phosphorus': 20},
    {'depth_cm': 35, 'ph': 7.1, 'nitrogen': 16, 'phosphorus': 15},
    {'depth_cm': 45, 'ph': 7.3, 'nitrogen': 14, 'phosphorus': 12}
]

# Triggering computation
final_yield = optimize_harvest(climate_data, soil_profiles)
print(f"Result: {final_yield}")