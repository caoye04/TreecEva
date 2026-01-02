from itertools import compress

# Simulated agricultural sensor data over 7 days
temperature_readings = [22, 24, 19, 25, 23, 20, 21]
soil_moisture_levels = [30, 35, 25, 40, 33, 28, 31]
sunlight_exposure_hours = [6.5, 7.2, 5.8, 8.0, 7.0, 6.0, 6.8]  # Irrelevant distractor

# Distractor variables: unused growth factors
growth_factor_light = 0.85
growth_factor_nutrients = 0.92

# Helper function to filter high-stress days
def is_stress_day(temp, moisture):
    return temp < 20 or temp > 24 or moisture < 26 or moisture > 34

# Secondary helper for irrelevant nutrient calculation
def estimate_nutrient_depletion(days):
    total = 0
    for d in range(days):
        total += (d + 1) * 0.3  # Fake accumulation
    return round(total, 2)

# Main yield calculation combining multiple conditions and filters
def calculate_optimal_yield(temps, moistures):
    stress_flags = [is_stress_day(t, m) for t, m in zip(temps, moistures)]
    
    # Compute baseline yield from favorable days
    favorable_temps = list(compress(temps, [not x for x in stress_flags]))
    favorable_moistures = list(compress(moistures, [not x for x in stress_flags]))
    
    # Base yield per favorable day: harmonic interaction of temp and moisture
    base_yield = 0
    for t, m in zip(favorable_temps, favorable_moistures):
        base_yield += (t * 0.6) + (m * 0.4)
    
    # Penalty for consecutive stress days (state tracking)
    consecutive_stress = 0
    max_consecutive = 0
    for flag in stress_flags:
        if flag:
            consecutive_stress += 1
            max_consecutive = max(max_consecutive, consecutive_stress)
        else:
            consecutive_stress = 0
    
    penalty = max_consecutive * 2.5 if max_consecutive > 1 else 0
    
    # Irrelevant intermediate: simulate fake evaporation effect
    evap_loss = 0
    for hour in sunlight_exposure_hours:
        evap_loss += hour * 0.1  # Computed but not used
    
    # Final yield adjusted by penalty
    final_yield = base_yield - penalty
    
    # Additional red herring: nutrient impact (never applied)
    estimated_loss = estimate_nutrient_depletion(len(temps))
    
    return round(final_yield, 2)

# Execute main logic
baseline_performance = sum(temperature_readings) / len(temperature_readings)  # Distractor calc
auxiliary_score = max(soil_moisture_levels) - min(soil_moisture_levels)  # Unused metric

final_yield = calculate_optimal_yield(temperature_readings, soil_moisture_levels)

print(f"Result: {final_yield}")