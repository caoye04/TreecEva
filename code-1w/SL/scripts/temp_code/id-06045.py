from collections import defaultdict

# Simulate agricultural yield modeling with environmental factors

def preprocess_soil_data(raw_data):
    soil_quality = defaultdict(int)
    modifiers = {"clay": 1.2, "loam": 1.5, "sand": 0.8}
    for region, soil_type in raw_data.items():
        soil_quality[region] = modifiers.get(soil_type, 1.0)
    return soil_quality

# Irrelevant helper: simulates rainfall prediction (not used in final calculation)
def predict_rainfall(season):
    base = {"spring": 120, "summer": 80, "autumn": 60, "winter": 40}
    adjusted = {k: v * 1.1 for k, v in base.items()}
    return adjusted.get(season, 50)

# Distraction function: calculates theoretical maximum (never called)
def theoretical_max_capacity(area, efficiency=0.95):
    max_units = area * 1000 * efficiency
    bonus = 50 if max_units > 50000 else 20
    return max_units + bonus

# Core logic: computes actual harvest based on dynamic growth cycles
def calculate_harvest_potential(plots, cycles):
    cumulative_yield = 0
    penalty_factor = 0.0
    
    # Track intermediate stats (some unused)
    cycle_stats = defaultdict(lambda: 0)
    degradation_alerts = []
    
    for i in range(cycles):
        cycle_modifier = 1.0
        
        # Environmental degradation over time
        if i > 0 and i % 4 == 0:
            penalty_factor += 0.05
        
        for plot_id, config in plots.items():
            base_area = config['area']
            crop_type = config['crop']
            health = config['health']
            
            # Crop-specific yield coefficients
            coef_map = {'wheat': 2.1, 'corn': 3.4, 'barley': 1.8, 'oats': 1.5}
            base_coeff = coef_map.get(crop_type, 2.0)
            
            # Simulated pest outbreak every 7 cycles (mitigated)
            pest_penalty = 0.1 if (i + 1) % 7 == 0 and crop_type != 'barley' else 0.0
            
            # Actual yield formula
            raw_yield = base_area * base_coeff * health * (1 - penalty_factor) * (1 - pest_penalty)
            
            # Update internal tracking (semi-relevant)
            cycle_stats[i] += raw_yield
            
            # Unused conditional branch (dead code path)
            if raw_yield < 50:
                status = "low"
            elif raw_yield < 200:
                status = "moderate"
            else:
                status = "high"
                # This block does nothing meaningful
                temp_buffer = [status for _ in range(2)]
                del temp_buffer
            
            cumulative_yield += raw_yield
    
    # Final adjustment based on average cycle performance
    avg_cycle_yield = sum(cycle_stats.values()) / len(cycle_stats) if cycle_stats else 0
    final_adjustment = 1.0 if avg_cycle_yield > 150 else 0.9
    final_yield = int(cumulative_yield * final_adjustment)
    
    # Dead computation: unused transformation
    normalized = [round(v / final_yield, 3) for v in cycle_stats.values()] if final_yield != 0 else []
    
    return final_yield

# Main execution
if __name__ == "__main__":
    # Input data: land plots with attributes
    land_plots = {
        'plot_A1': {'area': 40, 'crop': 'wheat', 'health': 0.95},
        'plot_A2': {'area': 35, 'crop': 'corn', 'health': 0.88},
        'plot_A3': {'area': 50, 'crop': 'barley', 'health': 0.92},
        'plot_A4': {'area': 30, 'crop': 'oats', 'health': 0.85}
    }
    
    # Preprocess unrelated data (distraction)
    soil_input = {p: 'loam' for p in land_plots.keys()}
    soil_factors = preprocess_soil_data(soil_input)
    
    # Unused weather forecast
    forecast = predict_rainfall('summer')
    
    # Key statement
    growth_cycles = 12
    final_yield = calculate_harvest_potential(land_plots, growth_cycles)
    
    # Output result
    print(f"Result: {final_yield}")