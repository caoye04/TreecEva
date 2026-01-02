import math

# Simulated agricultural yield analysis with noise and distractors
def analyze_soil_ph(readings):
    # Irrelevant helper function (dead code path)
    return sum(readings) / len(readings)

def estimate_rainfall_influence(levels):
    # Distractor function with misleading intermediate computation
    adjusted = [lvl * 0.7 for lvl in levels if lvl > 2]
    return sum(adjusted) // 2 if adjusted else 0

def compute_root_depth(soil_type, moisture):
    # Unused complex logic to mislead
    depth_map = {'clay': 30, 'loam': 60, 'sand': 45}
    base = depth_map.get(soil_type, 40)
    return base + (moisture * 0.5)

def transform_data_sequence(raw_seq):
    # Red herring: performs slicing and transformation but not used in final result
    processed = [x ** 0.5 for x in raw_seq if x % 2 == 0]
    shifted = processed[1:] + [processed[0]]
    normalized = [round(x / sum(shifted), 3) for x in shifted]
    return normalized

def calculate_harvest_efficiency(areas, cycles):
    # Core logic embedded within distractions
    efficiency_grid = []
    
    for i in range(len(areas)):
        area = areas[i]
        cycle_data = cycles[i]
        
        # Real calculation begins
        base_yield = area * 120  # Base yield per hectare
        
        # Apply growth modifiers from cycle data
        modifier = 1.0
        for entry in cycle_data:
            temp_mod = 1.0
            if entry['temp'] > 30:
                temp_mod = 0.85
            elif entry['temp'] < 20:
                temp_mod = 0.9
            
            precip_mod = 1.0
            if entry['rain'] < 50:
                precip_mod = 0.93
            elif entry['rain'] > 120:
                precip_mod = 0.88
            
            # Actual cumulative effect
            modifier *= (temp_mod * precip_mod)
        
        adjusted_yield = base_yield * modifier
        efficiency_grid.append(adjusted_yield)
    
    # Aggregate using weighted contribution (based on area size)
    total_area = sum(areas)
    weighted_sum = sum((efficiency_grid[i] * areas[i]) for i in range(len(areas)))
    overall_efficiency = weighted_sum / total_area if total_area else 0
    
    # Final transformation using slicing of intermediate state
    history_log = efficiency_grid + [overall_efficiency]
    recent_trend = history_log[-3:]  # Last three entries
    trend_adjustment = sum(recent_trend) / len(recent_trend)
    
    # Key assignment point
    final_yield = round(trend_adjustment * 0.97, 4)
    return final_yield

# Main execution block
if __name__ == '__main__':
    # Input data setup
    area_metrics = [25.5, 30.0, 20.2, 18.8]
    growth_cycles = [
        [{'temp': 28, 'rain': 85}, {'temp': 32, 'rain': 45}, {'temp': 25, 'rain': 95}],
        [{'temp': 26, 'rain': 110}, {'temp': 19, 'rain': 40}, {'temp': 27, 'rain': 90}],
        [{'temp': 31, 'rain': 130}, {'temp': 24, 'rain': 70}, {'temp': 22, 'rain': 60}],
        [{'temp': 20, 'rain': 55}, {'temp': 29, 'rain': 105}, {'temp': 27, 'rain': 80}]
    ]

    # Irrelevant preprocessing (distractor)
    soil_samples = [6.2, 6.4, 6.8, 7.1, 6.5]
    avg_ph = analyze_soil_ph(soil_samples)
    rainfall_levels = [40, 120, 80, 200, 60]
    rain_impact = estimate_rainfall_influence(rainfall_levels)

    # Noise variables with plausible names
    canopy_cover = [0.7, 0.82, 0.65, 0.78]
    pest_incidence = {'aphids': 12, 'mites': 8, 'scale': 5}
    elevation_data = [120, 145, 130, 160]
    slope_gradient = [3.2, 4.1, 2.8, 5.0]

    # Unused complex list comprehension (red herring)
    microclimate_zones = [
        f"Zone-{i+1}_{soil[:2].upper()}" 
        for i, soil in enumerate(['clay', 'loam', 'sand', 'silt'])
        if elevation_data[i] > 125
    ]

    # Transform unused sequence (more distraction)
    sensor_readings = [16, 25, 36, 49, 64]
    transformed = transform_data_sequence(sensor_readings)

    # Real computation path
    final_yield = calculate_harvest_efficiency(area_metrics, growth_cycles)
    
    # Output target result
    print(f"Result: {final_yield}")