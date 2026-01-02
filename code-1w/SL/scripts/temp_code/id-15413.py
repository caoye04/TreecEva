def analyze_soil_composition(data):
    # Irrelevant function: analyzes soil but not used in final calculation
    ph_levels = [d['ph'] for d in data]
    nutrient_score = sum(ph_levels) / len(ph_levels)
    return nutrient_score


def simulate_rainfall_pattern(days):
    # Misleading simulation with no impact on result
    import random
    random.seed(42)
    rain_events = [random.randint(0, 20) for _ in range(days)]
    total_rain = sum(rain_events)
    avg_rain = total_rain / len(rain_events)
    return avg_rain  # Dead end


def preprocess_growth_data(raw):
    # Distractor: processes unused data
    filtered = [x for x in raw if x > 0]
    normalized = [round(x * 0.95, 2) for x in filtered]
    return normalized


def decode_genetic_marker(marker_str):
    # Bit manipulation red herring
    binary_rep = ''.join(format(ord(c), '08b') for c in marker_str)
    ones_count = binary_rep.count('1')
    shifted = ones_count << 2
    masked = shifted & 0xFF
n    return masked  # Unused


def calculate_harvest_efficiency(areas, cycles):
    # Core logic hidden among noise
    efficiency_scores = []
    
    for i, area in enumerate(areas):
        cycle = cycles[i]
        base_yield = area * 3.7
        
        # Conditional adjustment based on cycle length
        if cycle > 120:
            adjustment_factor = 1.15
        elif cycle < 60:
            adjustment_factor = 0.85
        else:
            adjustment_factor = 1.0
        
        adjusted_yield = base_yield * adjustment_factor
        
        # Apply diminishing returns using exponentiation
        diminishing_coeff = 1 - (0.05 ** (i + 1)) if i % 3 == 0 else 1.0
        net_yield = adjusted_yield * diminishing_coeff
        
        efficiency_scores.append(net_yield)
    
    # Aggregate using advanced reduction
    total_efficiency = sum(efficiency_scores)
    
    # Final transformation with logarithmic scaling
    import math
    if total_efficiency > 0:
        final_scale = math.log(total_efficiency) * 100
    else:
        final_scale = 0
    
    return int(final_scale)

# Main execution block
if __name__ == '__main__':
    # Real input data
    area_metrics = [12.5, 8.2, 15.7, 6.3]
    growth_cycles = [135, 45, 98, 167]
    
    # Irrelevant data processing
    soil_data = [{'ph': 6.2, 'N': 12}, {'ph': 5.8, 'N': 10}, {'ph': 6.5, 'N': 14}]
    raw_growth = [-1, 45, 67, 0, 89]
    genetic_code = "GATTACA"
    
    # Useless intermediate variables
    avg_ph = analyze_soil_composition(soil_data)
    processed_growth = preprocess_growth_data(raw_growth)
    simulated_rain = simulate_rainfall_pattern(365)
    marker_value = decode_genetic_marker(genetic_code)
    
    # Linear search for no reason
    threshold_index = -1
    for idx, val in enumerate(growth_cycles):
        if val > 100:
            threshold_index = idx
            break
    
    # Key statement
    final_yield = calculate_harvest_efficiency(area_metrics, growth_cycles)
    
    # Print required output
    print(f"Target result: {final_yield}")