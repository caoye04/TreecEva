import itertools

# Simulate agricultural yield optimization with environmental constraints
def analyze_soil_ph(readings):
    avg_ph = sum(readings) / len(readings)
    deviation = max(readings) - min(readings)
    # Irrelevant computation for nutrient balance
    nutrient_score = (avg_ph * 1.7) + (deviation * 0.3)
    return avg_ph if 6.0 <= avg_ph <= 7.0 else 6.5

def normalize_humidity(values):
    min_val, max_val = min(values), max(values)
    range_val = max_val - min_val
    if range_val == 0:
        return [1.0] * len(values)
    # Distractor: unused transformation
    inverted = [(max_val - v) / range_val for v in values]
    normalized = [(v - min_val) / range_val for v in values]
    return normalized

def compute_wind_resistance(structures):
    # Complex but irrelevant to final result
    base_ratings = {'A': 8, 'B': 6, 'C': 4, 'D': 2}
    total_rating = 0
    for s in structures:
        if s in base_ratings:
            total_rating += base_ratings[s] * 1.2
    adjusted = total_rating * 0.95
    return adjusted  # Not used later

def calculate_growth_potential(temp_data, light_exposure):
    # Relevant calculation: integrates temperature stability and light
    temp_stability = 1 - (sum(abs(temp_data[i] - temp_data[i-1]) for i in range(1, len(temp_data))) / len(temp_data)) * 0.05
    ideal_temp_ratio = sum(1 for t in temp_data if 22 <= t <= 28) / len(temp_data)
    
    # Distractor block: pest resistance modeling (unused)
    pest_factor = 0.8
    if ideal_temp_ratio > 0.7:
        pest_factor += 0.15
    elif any(t > 35 for t in temp_data):
        pest_factor -= 0.2
    
    # Actual relevant logic
    light_efficiency = sum(light_exposure) / (len(light_exposure) * 12.0)
    potential = (ideal_temp_ratio * 0.6) + (light_efficiency * 0.4)
    return round(potential * 100, 2)

def calculate_harvest_efficiency(metrics, cycles):
    # Extract key components from metrics
    base_area = metrics['core_area']
    efficiency_factor = metrics['efficiency_index']
    
    # Historical data - distractor
    historical_yields = [420, 435, 410, 445, 450]
    trend = sum(historical_yields[i] - historical_yields[i-1] for i in range(1, len(historical_yields)))
    projected_baseline = historical_yields[-1] + (trend / len(historical_yields))
    
    # Core logic: use cycle data to adjust efficiency
    peak_cycle_index = cycles.index(max(cycles))
    cycle_stability = len([c for c in cycles if c >= 0.8 * max(cycles)])
    stability_bonus = 1 + (cycle_stability / len(cycles)) * 0.1
    
    # Use itertools to generate efficiency combinations (only one used)
    combinations = list(itertools.product([base_area], [efficiency_factor], [stability_bonus]))
    candidate_results = []
    for area, factor, bonus in combinations:
        raw_yield = area * factor * bonus
        if raw_yield > 500:
            raw_yield *= 0.92  # Adjustment for overcapacity
        candidate_results.append(raw_yield)
    
    # Final adjustment based on peak timing
    if peak_cycle_index < len(cycles) // 2:
        final_adjustment = 0.95
    else:
        final_adjustment = 1.05
    
    # THE KEY COMPUTATION
    final_yield = candidate_results[0] * final_adjustment
    return round(final_yield)

# Main execution
if __name__ == "__main__":
    # Input data
    soil_readings = [6.8, 6.5, 7.1, 6.3, 6.9]
    humidity_levels = [65, 70, 68, 72, 66]
    wind_structures = ['A', 'B', 'A', 'C']
    temperature_readings = [24, 26, 23, 28, 27, 25, 24, 26]
    light_hours = [10, 12, 11, 12, 10, 13, 12, 11]
    growth_cycles = [0.88, 0.92, 0.95, 0.87, 0.93, 0.96, 0.94, 0.91]
    
    # Irrelevant preprocessing
    ph_balance = analyze_soil_ph(soil_readings)
    humidity_norm = normalize_humidity(humidity_levels)
    wind_rating = compute_wind_resistance(wind_structures)
    
    # Relevant data preparation
    growth_potential = calculate_growth_potential(temperature_readings, light_hours)
    
    # Key metric structure
    area_metrics = {
        'core_area': 42,
        'efficiency_index': 23.5,
        'auxiliary_factor': 1.8  # Unused
    }
    
    # Execution point of interest
    final_yield = calculate_harvest_efficiency(area_metrics, growth_cycles)
    
    # Output result
    print(f"Result: {final_yield}")