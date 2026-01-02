def preprocess_sensor_noise(readings):
    # Irrelevant signal processing function (dead code path)
    filtered = [x * 0.98 + 1.5 for x in readings if x > -50]
    return [f for f in filtered if f < 100]


def validate_soil_ph(ph_levels):
    # Distractor validation logic with no impact on result
    status = []
    for i, ph in enumerate(ph_levels):
        if ph < 6.0:
            status.append((i, 'acidic'))
        elif ph > 7.5:
            status.append((i, 'alkaline'))
        else:
            status.append((i, 'optimal'))
    return status


def calculate_growth_modifier(temp, humidity):
    # Relevant calculation used later
    base = temp * 0.1
    if humidity > 60:
        base *= 1.2
    elif humidity < 40:
        base *= 0.85
    return round(base, 3)


def simulate_root_spread(layers, compaction):
    # Complex but irrelevant simulation (decoy function)
    spread = 0
    for idx, layer in enumerate(layers):
        resistance = compaction[idx] * 0.3
        spread += (layer / (resistance + 0.1)) * (idx + 1)
    return min(spread, 15.0)


def calculate_optimal_harvest(weather_seq, cycles):
    # Core logic with multiple steps and distractors
    
    # Irrelevant preprocessing (distractor)
    smoothed = [sum(weather_seq[max(0,i-1):i+1])/(min(i+1,2)) for i in range(len(weather_seq))]
    anomalies = [i for i, x in enumerate(smoothed) if abs(x - 25) > 10]
    
    # Key data structures
    growth_track = []
    stress_factors = {"heat": 0, "drought": 0, "excess": 0}
    
    peak_biomass = 0
    cumulative_light = 0
    
    for cycle in cycles:
        # Nesting Level 1: Cycle loop
        daily_yield = 0
        
        for temp, humidity, light in zip(cycle['temps'], cycle['humidity'], cycle['light']):
            # Nesting Level 2: Daily conditions
            
            # Red herring: sensor adjustment
            adjusted_temp = temp + (0.5 if humidity > 70 else -0.3)
            
            # Relevant modifier calculation
            modifier = calculate_growth_modifier(temp, humidity)
            
            # Accumulate light (used later)
            cumulative_light += light
            
            if temp > 35:
                stress_factors['heat'] += 1
            if humidity < 30:
                stress_factors['drought'] += 1
            if humidity > 80:
                stress_factors['excess'] += 1

            # Core yield contribution
            daily_yield += (temp * 0.5 + humidity * 0.3) * modifier * (light / 1000)
        
        # Track per-cycle biomass
        cycle_biomass = daily_yield * len(cycle['temps'])
        growth_track.append(cycle_biomass)
        
        if cycle_biomass > peak_biomass:
            peak_biomass = cycle_biomass
    
    # Summation and final adjustment
    total_potential = sum(growth_track)
    
    # Apply stress penalties
    stress_ratio = 1 - (stress_factors['heat'] * 0.02 + \
                       stress_factors['drought'] * 0.03 + \
                       stress_factors['excess'] * 0.015)
    
    # Final yield computation (key answer point)
    final_yield = int(total_potential * stress_ratio * (cumulative_light / 5000))
    
    # Dead code: post-harvest analysis (never executed due to return above)
    efficiency_score = 0
    if final_yield > 200:
        for i, g in enumerate(growth_track):
            efficiency_score += g / (i + 1)
    
    return final_yield

# Main execution block
if __name__ == "__main__":
    
    # Irrelevant sensor array (distractor)
    soil_moisture = [33, 45, 50, 60, 70, 75, 80]
    ph_values = [5.8, 6.2, 6.0, 6.5, 7.0, 7.6, 5.9]
    
    # Unused matrix transformation (red herring)
    transposed = [[row[i] for row in [[1,2],[3,4],[5,6]]] for i in range(2)]
    
    # Validate soil (no effect on output)
    ph_status = validate_soil_ph(ph_values)
    
    # Simulate root spread (unused result)
    soil_layers = [10, 15, 20, 25]
    compaction_index = [0.8, 1.2, 1.5, 1.1]
    root_extent = simulate_root_spread(soil_layers, compaction_index)
    
    # Climate data (input)
    climate_data = [25, 27, 30, 33, 36, 34, 32]
    
    # Growth cycles (main input)
    growth_cycles = [
        {
            'temps': [22, 24, 25, 27, 26],
            'humidity': [50, 55, 60, 65, 58],
            'light': [800, 900, 1000, 950, 870]
        },
        {
            'temps': [28, 30, 32, 35, 33, 31],
            'humidity': [40, 38, 35, 33, 45, 50],
            'light': [1000, 1100, 1200, 1150, 1050, 980]
        },
        {
            'temps': [26, 25, 24, 23],
            'humidity': [60, 65, 70, 72],
            'light': [850, 900, 920, 880]
        }
    ]
    
    # Preprocess climate (irrelevant)
    noise_data = [x + 2.5 for x in climate_data]
    cleaned = preprocess_sensor_noise(noise_data)
    
    # Critical statement
    final_yield = calculate_optimal_harvest(climate_data, growth_cycles)
    
    print(f"Result: {final_yield}")