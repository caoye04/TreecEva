def analyze_soil_composition(elements):
    # Irrelevant computation: calculates unused soil score
    nitrogen_weight = elements.get('N', 0) * 3.1
    phosphorus_weight = elements.get('P', 0) * 2.5
    potassium_weight = elements.get('K', 0) * 1.8
    ph_balance = abs(7.0 - elements.get('pH', 7.0))
    soil_score = (nitrogen_weight + phosphorus_weight + potassium_weight) / max(ph_balance, 0.1)
    return soil_score

# Simulate crop yield under varying conditions
def simulate_growth_stages(base_rate, stress_factors):
    peak_growth = 0
    for day in range(1, 8):  # 7-day cycle
        temp_effect = 1 + 0.1 * (25 - stress_factors['temp'][day % len(stress_factors['temp'])])
        water_effect = stress_factors['water'][day % len(stress_factors['water'])]
        daily_growth = base_rate * temp_effect * water_effect
        if daily_growth > peak_growth:
            peak_growth = daily_growth
    return peak_growth

# Core logic for harvest efficiency
def calculate_harvest_efficiency(metrics, cycles):
    total_efficiency = 0.0
    adjustment_factor = 1.0
    
    # Distractor: unused decomposition tracking
    organic_breakdown = {'cellulose': 0, 'lignin': 0}
    for i in range(len(cycles)):
        cycle_data = cycles[i]
        duration = cycle_data['duration']
        sunlight_avg = sum(cycle_data['sunlight']) / len(cycle_data['sunlight'])
        
        # Real contribution: photosynthetic efficiency
        photo_eff = (sunlight_avg * 0.02) * (duration / 30)
        
        # Misleading intermediate: respiration loss (not actually used)
        respiration_loss = 0
        for hour in range(24):
            if hour < 6 or hour > 18:
                respiration_loss += 0.001 * (24 - hour)
        normalized_loss = respiration_loss / 24
        
        # Actual efficiency update
        total_efficiency += photo_eff
        
        # Bitwise manipulation as red herring
        encoded_metric = metrics['base_productivity'] << 2
        decoded_value = encoded_metric >> 2
        if decoded_value != metrics['base_productivity']:
            adjustment_factor *= 0.9
    
    # String processing distraction
    status_log = "Cycle completed successfully with optimal output"
    if status_log.find("optimal") != -1 and status_log.endswith("output"):
        adjustment_factor *= 1.05
    
    # Final calculation using correct path
    baseline_yield = metrics['base_productivity'] * total_efficiency
    final_yield = int(baseline_yield * adjustment_factor)
    
    # Dead code branch - never reached due to prior logic
    if final_yield < 0:
        final_yield = 0
    elif final_yield > 10000:
        overflow_flag = True
        buffer_copy = final_yield >> 4
        final_yield = 10000  # Capped, but cap not triggered in this case

    return final_yield

# Main execution
if __name__ == '__main__':
    # Input data
    area_metrics = {
        'base_productivity': 42,
        'soil_quality': 'loam',
        'elevation': 150
    }
    
    # Soil analysis (unused result)
    soil_elements = {'N': 12, 'P': 8, 'K': 10, 'pH': 6.8}
    quality_index = analyze_soil_composition(soil_elements)
    
    # Growth cycles with environmental data
    growth_cycles = [
        {
            'duration': 30,
            'sunlight': [6.5, 7.0, 6.8, 7.2, 6.9, 7.1, 6.7],
            'temp': [22, 24, 26, 23, 25],
            'water': [0.95, 0.88, 0.92, 0.85]
        },
        {
            'duration': 30,
            'sunlight': [7.0, 7.3, 7.1, 6.9, 7.2, 7.4, 7.0],
            'temp': [24, 25, 27, 26, 24],
            'water': [0.90, 0.93, 0.89, 0.91]
        }
    ]
    
    # Simulate growth (result not used in final calculation)
    simulated_peak = simulate_growth_stages(1.2, {
        'temp': [22, 24, 26],
        'water': [0.85, 0.90, 0.88, 0.92]
    })
    
    # Key statement
    final_yield = calculate_harvest_efficiency(area_metrics, growth_cycles)
    
    # Output result
    print(f"Target result: {final_yield}")