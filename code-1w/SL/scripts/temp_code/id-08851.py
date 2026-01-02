from itertools import cycle

def simulate_growth_cycle(base, factors):
    accumulator = 0
    temp_shift = 0
    for i, factor in enumerate(factors):
        if i % 2 == 0:
            accumulator += (base + i) * factor
        else:
            temp_shift += base ** (i % 3)
    return accumulator

def assess_stress_levels(readings):
    stress_score = 0
    for r in readings:
        if r > 75:
            stress_score += 1
    return stress_score if stress_score > 0 else 1

def calculate_harvest_efficiency(soil_data, weather_pattern, thresholds):
    # Primary computation path
    growth_cycles = [simulate_growth_cycle(val, [2, 3, 4]) for val in soil_data]
    total_growth = sum(growth_cycles)
    
    # Distractor: complex but irrelevant temperature drift analysis
    temp_drift = 0
    for w in weather_pattern:
        temp_drift += abs(w - 20) * 0.5
        if temp_drift > 50:
            temp_drift = 50
    
    # Real logic continues
    stress_readings = [assess_stress_levels(thresholds), assess_stress_levels([t*2 for t in thresholds])]
    avg_stress = sum(stress_readings) / len(stress_readings)
    
    # Key efficiency formula
    baseline_efficiency = total_growth / (avg_stress + 1)
    
    # Distractor: unused nutrient tracking
    nutrient_map = {i: val * 1.5 for i, val in enumerate(soil_data)}
    total_nutrients = sum(nutrient_map.values())
    nutrient_cycle = cycle([1, -1, 0])
    balance_shift = 0
    for _ in range(5):
        balance_shift += next(nutrient_cycle)
    
    # Conditional adjustment using dictionary operation
    modifiers = {'low': 0.8, 'high': 1.2}
    adjustment = modifiers['high'] if baseline_efficiency >= 100 else modifiers['low']
    
    # Final yield calculation
    final_yield = int(baseline_efficiency * adjustment)
    
    # Irrelevant sorting of unrelated synthetic data
    dummy_data = [abs((i * 3) % 7 - 4) for i in range(10)]
    dummy_data.sort(reverse=True)
    
    # Output target variable
    print(f"Result: {final_yield}")
    return final_yield

# Inputs
soil_input = [12, 15, 10, 18]
weather_input = [22, 25, 19, 24, 21, 20, 23]
temp_thresholds = [60, 80, 70, 90, 65]

# Execution entry point
final_yield = calculate_harvest_efficiency(soil_input, weather_input, temp_thresholds)